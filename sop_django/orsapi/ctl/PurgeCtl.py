import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Purge
from ..service.PurgeCtl import PurgeService
from ..utility.DataValidator import DataValidator


class PurgeCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['purgeCode'] = requestForm.get('purgeCode')
        self.form['dataType'] = requestForm.get('dataType')
        self.form['lastRunDate'] = requestForm.get('lastRunDate')
        self.form['status'] = requestForm.get('status')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.purgeCode = self.form['purgeCode']
        obj.dataType = self.form['dataType']
        obj.lastRunDate = self.form['lastRunDate']
        obj.status = self.form['status']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['purgeCode'] = obj.purgeCode
        self.form['dataType'] = obj.dataType
        self.form['lastRunDate'] = obj.lastRunDate
        self.form['status'] = obj.status

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['purgeCode'])):
            inputError['purgeCode'] = "purgeCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isAllCharAllowed(self.form['purgeCode'])):
                inputError['purgeCode'] = "purgeCode contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['dataType'])):
            inputError['dataType'] = "dataType can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['dataType'])):
                inputError['dataType'] = "dataType contains only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['lastRunDate'])):
            inputError['lastRunDate'] = "lastRunDate can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['lastRunDate'])):
                inputError['lastRunDate'] = "Incorrect date format, should be YYYY-MM-DD"
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
            uniqueAttrib = {"purgeCode": self.form['purgeCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Purge
            purge = self.form_to_model(Purge())
            self.get_service().save(purge)
            res["success"] = True
            res["result"]["data"] = purge.id
            res["result"]["message"] = "Purge added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["purgeCode"] = json_request.get("purgeCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Purge.objects.last().id
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
            purge_list = PurgeService().preload()
            preloadList = []
            for x in purge_list:
                preloadList.append(x.to_json())
            res["result"]["purgelist"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return PurgeService()