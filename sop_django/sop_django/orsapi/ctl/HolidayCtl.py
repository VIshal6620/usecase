import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Holiday
from ..service.HolidayService import HolidayService
from ..utility.DataValidator import DataValidator


class HolidayCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['holidayCode'] = requestForm.get('holidayCode')
        self.form['holidayName'] = requestForm.get('holidayName')
        self.form['holidayDate'] = requestForm.get('holidayDate')
        self.form['holidayType'] = requestForm.get('holidayType')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.holidayCode = self.form['holidayCode']
        obj.holidayName = self.form['holidayName']
        obj.holidayDate = self.form['holidayDate']
        obj.holidayType = self.form['holidayType']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['holidayCode'] = obj.holidayCode
        self.form['holidayName'] = obj.holidayName
        self.form['holidayDate'] = obj.holidayDate
        self.form['holidayType'] = obj.holidayType

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['holidayCode'])):
            inputError['holidayCode'] = "holidayCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['holidayCode'])):
                inputError['holidayCode'] = "holidayCode contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['holidayName'])):
            inputError['holidayName'] = "holidayName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['holidayName'])):
                inputError['holidayName'] = "holidayName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['holidayDate'])):
            inputError['holidayDate'] = "holidayDate can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['holidayDate'])):
                inputError['holidayDate'] = "Incorrect date format, should be YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['holidayType'])):
            inputError['holidayType'] = "holidayType can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['holidayType'])):
                inputError['holidayType'] = "Incorrect date format, should be YYYY-MM-DD"
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
            uniqueAttrib = {"holidayCode": self.form['holidayCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Holiday
            holiday = self.form_to_model(Holiday())
            self.get_service().save(holiday)
            res["success"] = True
            res["result"]["data"] = holiday.id
            res["result"]["message"] = "Holiday added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["holidayCode"] = json_request.get("holidayCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Holiday.objects.last().id
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
            holiday_list = HolidayService().preload()
            preloadList = []
            for x in holiday_list:
                preloadList.append(x.to_json())
            res["result"]["holidaylist"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return HolidayService()