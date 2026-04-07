import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Security
from ..service.SecurityService import SecurityService
from ..utility.DataValidator import DataValidator


class SecurityCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['StaffName'] = requestForm.get('StaffName')
        self.form['shift'] = requestForm.get('shift')
        self.form['salary'] = requestForm.get('salary')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.StaffName = self.form['StaffName']
        obj.shift = self.form['shift']
        obj.salary = self.form['salary']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['StaffName'] = obj.StaffName
        self.form['shift'] = obj.shift
        self.form['salary'] = obj.salary

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['StaffName'])):
            inputError['StaffName'] = "StaffName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['StaffName'])):
                inputError['StaffName'] = "StaffName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['shift'])):
            inputError['shift'] = "shift can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isRewardCode(self.form['shift'])):
                inputError['shift'] = "contains only shift"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['salary'])):
            inputError['salary'] = "salary can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isinteger(self.form['salary'])):
                inputError['salary'] = "salary contains only number"
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
            uniqueAttrib = {"StaffName": self.form['StaffName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Security
            security = self.form_to_model(Security())
            self.get_service().save(security)
            res["success"] = True
            res["result"]["data"] = security.id
            res["result"]["message"] = "security added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["StaffName"] = json_request.get("StaffName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Security.objects.last().id
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
            security_list = SecurityService().preload()
            preloadList = []
            for x in security_list:
                preloadList.append(x.to_json())
            res["result"]["securityList"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return SecurityService()