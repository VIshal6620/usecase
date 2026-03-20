import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Rejection
from ..service.RejectionService import RejectionService
from ..utility.DataValidator import DataValidator


class RejectionCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['rejectionCode'] = requestForm.get('rejectionCode')
        self.form['requestName'] = requestForm.get('requestName')
        self.form['rejectionReason'] = requestForm.get('rejectionReason')
        self.form['rejectionStatus'] = requestForm.get('rejectionStatus')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.rejectionCode = self.form['rejectionCode']
        obj.requestName = self.form['requestName']
        obj.rejectionReason = self.form['rejectionReason']
        obj.rejectionStatus = self.form['rejectionStatus']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['rejectionCode'] = obj.rejectionCode
        self.form['requestName'] = obj.requestName
        self.form['rejectionReason'] = obj.rejectionReason
        self.form['rejectionStatus'] = obj.rejectionStatus

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['rejectionCode'])):
            inputError['rejectionCode'] = "rejectionCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isRewardCode(self.form['rejectionCode'])):
                inputError['rejectionCode'] = "rejectionCode contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['requestName'])):
            inputError['requestName'] = "requestName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['requestName'])):
                inputError['requestName'] = "requestName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['rejectionReason'])):
            inputError['rejectionReason'] = "rejectionReason can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['rejectionReason'])):
                inputError['rejectionReason'] = "rejectionReason contains only name"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['rejectionStatus'])):
            inputError['rejectionStatus'] = "rejectionStatus can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isRewardCode(self.form['rejectionStatus'])):
                inputError['rejectionStatus'] = "rejectionStatus contains only number"
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
            uniqueAttrib = {"rejectionCode": self.form['rejectionCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Rejection
            rejection = self.form_to_model(Rejection())
            self.get_service().save(rejection)
            res["success"] = True
            res["result"]["data"] = rejection.id
            res["result"]["message"] = "Rejection added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["rejectionCode"] = json_request.get("rejectionCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Rejection.objects.last().id
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
            rejection_list = RejectionService().preload()
            preloadList = []
            for x in rejection_list:
                preloadList.append(x.to_json())
            res["result"]["rejectionList"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return RejectionService()