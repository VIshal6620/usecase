import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import LoginHistory
from ..service.LoginHistoryService import LoginHistoryService
from ..utility.DataValidator import DataValidator


class LoginHistoryCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['historyCode'] = requestForm.get('historyCode')
        self.form['userName'] = requestForm.get('userName')
        self.form['loginTime'] = requestForm.get('loginTime')
        self.form['status'] = requestForm.get('status')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.historyCode = self.form['historyCode']
        obj.userName = self.form['userName']
        obj.loginTime = self.form['loginTime']
        obj.status = self.form['status']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['historyCode'] = obj.historyCode
        self.form['userName'] = obj.userName
        self.form['loginTime'] = obj.loginTime
        self.form['status'] = obj.status

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['historyCode'])):
            inputError['historyCode'] = "historyCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isAlphaNumeric(self.form['historyCode'])):
                inputError['historyCode'] = "historyCode contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['userName'])):
            inputError['userName'] = "userName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['userName'])):
                inputError['userName'] = "userName contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['loginTime'])):
            inputError['loginTime'] = "loginTime can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isTime(self.form['loginTime'])):
                inputError['loginTime'] = "loginTime contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['status'])):
            inputError['status'] = "status can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isAllCharAllowed(self.form['status'])):
                inputError['status'] = "status contains only"
                self.form['error'] = True

        return self.form['error']


    def save(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            self.request_to_form(json_request)
            res = {"result": {}, "success": True}

            # perform input validation
            if (self.input_validation()):
                res["success"] = False
                res["result"]["inputerror"] = self.form["inputError"]
                return JsonResponse(res)
            # Check unique elements
            pk = int(self.form['id'])
            uniqueAttrib = {"historyCode": self.form['historyCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the LoginHistory
            loginhistory = self.form_to_model(LoginHistory())
            self.get_service().save(loginhistory)
            res["success"] = True
            res["result"]["data"] = loginhistory.id
            res["result"]["message"] = "LoginHistory added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["historyCode"] = json_request.get("historyCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = LoginHistory.objects.last().id
            else:
                res["success"] = False
                res["result"]["message"] = "No record found"
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get(self, request, params={}):
        try:
            role = self.get_service().get(params["id"])
            res = {"result": {}, "success": True}
            if (role != None):
                res["success"] = True
                res["result"]["data"] = role.to_json()
            else:
                res["success"] = False
                res["result"]["message"] = "No record found"
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def delete(self, request, params={}):
        try:
            role = self.get_service().get(params["id"])
            res = {"result": {}, "success": True}
            if (role != None):
                self.get_service().delete(params["id"])
                res["success"] = True
                res["result"]["data"] = role.to_json()
                res["result"]["message"] = "Data has been deleted successfully"
            else:
                res["success"] = False
                res["result"]["message"] = "Data was not deleted"
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def preload(self, request, params={}):
        try:
            res = {"result": {}, "success": True}
            loginhistory_list = LoginHistoryService().preload()
            preloadList = []
            for x in loginhistory_list:
                preloadList.append(x.to_json())
            res["result"]["loginhistory_list"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return LoginHistoryService()