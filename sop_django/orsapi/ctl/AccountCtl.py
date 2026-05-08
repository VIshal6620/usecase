import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Account
from ..service.AccountService import AccountService
from ..utility.DataValidator import DataValidator





class AccountCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['accountCode'] = requestForm.get('accountCode')
        self.form['userName'] = requestForm.get('userName')
        self.form['accountType'] = requestForm.get('accountType')
        self.form['status'] = requestForm.get('status')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.accountCode = self.form['accountCode']
        obj.userName = self.form['userName']
        obj.accountType = self.form['accountType']
        obj.status = self.form['status']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['accountCode'] = obj.accountCode
        self.form['userName'] = obj.userName
        self.form['accountType'] = obj.accountType
        self.form['status'] = obj.status

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['accountCode'])):
            inputError['accountCode'] = "accountCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isAllCharAllowed(self.form['accountCode'])):
                inputError['accountCode'] = "accountCode contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['userName'])):
            inputError['userName'] = "userName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['userName'])):
                inputError['userName'] = "userName contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['accountType'])):
            inputError['accountType'] = "accountType can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['accountType'])):
                inputError['accountType'] = "accountType contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['status'])):
            inputError['status'] = "status can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['status'])):
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
            uniqueAttrib = {"accountCode": self.form['accountCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Account
            account = self.form_to_model(Account())
            self.get_service().save(account)
            res["success"] = True
            res["result"]["data"] = account.id
            res["result"]["message"] = "Account added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["accountCode"] = json_request.get("accountCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Account.objects.last().id
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
            account_list = AccountService().preload()
            preloadList = []
            for x in account_list:
                preloadList.append(x.to_json())
            res["result"]["accountlist"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return AccountService()