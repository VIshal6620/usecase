import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Limit
from ..service.LimitService import LimitService
from ..utility.DataValidator import DataValidator


class LimitCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['limitCode'] = requestForm.get('limitCode')
        self.form['limitName'] = requestForm.get('limitName')
        self.form['maxValue'] = requestForm.get('maxValue')
        self.form['status'] = requestForm.get('status')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.limitCode = self.form['limitCode']
        obj.limitName = self.form['limitName']
        obj.maxValue = self.form['maxValue']
        obj.status = self.form['status']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['limitCode'] = obj.limitCode
        self.form['limitName'] = obj.limitName
        self.form['maxValue'] = obj.maxValue
        self.form['status'] = obj.status

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['limitCode'])):
            inputError['limitCode'] = "limitCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isAllCharAllowed(self.form['limitCode'])):
                inputError['limitCode'] = "limitCode contains only "
                self.form['error'] = True

        if (DataValidator.isNull(self.form['limitName'])):
            inputError['limitName'] = "limitName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['limitName'])):
                inputError['limitName'] = "limitName contains only "
                self.form['error'] = True

        if (DataValidator.isNull(self.form['maxValue'])):
            inputError['maxValue'] = "maxValue can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isinteger(self.form['maxValue'])):
                inputError['maxValue'] = "maxValue contains only "
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
            uniqueAttrib = {"limitCode": self.form['limitCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Limit
            limit = self.form_to_model(Limit())
            self.get_service().save(limit)
            res["success"] = True
            res["result"]["data"] = limit.id
            res["result"]["message"] = "Limit added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["limitCode"] = json_request.get("limitCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Limit.objects.last().id
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
            limit_list = LimitService().preload()
            preloadList = []
            for x in limit_list:
                preloadList.append(x.to_json())
            res["result"]["limitList"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return LimitService()