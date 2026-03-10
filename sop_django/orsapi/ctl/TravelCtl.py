import json

from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Travel
from ..service.LoanService import LoanService
from ..service.TravelService import TravelService
from ..utility.DataValidator import DataValidator


class TravelCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['travelerName'] = requestForm.get('travelerName')
        self.form['destination'] = requestForm.get('destination')
        self.form['startDate'] = requestForm.get('startDate')
        self.form['endDate'] = requestForm.get('endDate')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.travelerName = self.form['travelerName']
        obj.destination = self.form['destination']
        obj.startDate = self.form['startDate']
        obj.endDate = self.form['endDate']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['travelerName'] = obj.travelerName
        self.form['destination'] = obj.destination
        self.form['startDate'] = obj.startDate
        self.form['endDate'] = obj.endDate

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['travelerName'])):
            inputError['travelerName'] = "travelerName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['travelerName'])):
                inputError['travelerName'] = "travelerName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['destination'])):
            inputError['destination'] = "destination can not be null"
            self.form['error'] = True


        if (DataValidator.isNull(self.form['startDate'])):
            inputError['startDate'] = "DOB can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['startDate'])):
                inputError['startDate'] = "Incorrect date format, should be YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['endDate'])):
            inputError['endDate'] = "DOB can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['endDate'])):
                inputError['endDate'] = "Incorrect date format, should be YYYY-MM-DD"
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
            uniqueAttrib = {"travelerName": self.form['travelerName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the user
            travel = self.form_to_model(Travel())
            self.get_service().save(travel)
            res["success"] = True
            res["result"]["data"] = travel.id
            res["result"]["message"] = " Travel added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["travelerName"] = json_request.get("travelerName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Travel.objects.last().id
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
            travel_list = TravelService().preload()
            preloadList = []
            for x in travel_list:
                preloadList.append(x.to_json())
            res["result"]["travellist"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return TravelService()