import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import DonationCamp
from ..service.DonationCampService import DonationCampService
from ..utility.DataValidator import DataValidator


class DonationCampCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['campName'] = requestForm.get('campName')
        self.form['campDate'] = requestForm.get('campDate')
        self.form['organizer'] = requestForm.get('organizer')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.campName = self.form['campName']
        obj.campDate = self.form['campDate']
        obj.organizer = self.form['organizer']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['campName'] = obj.campName
        self.form['campDate'] = obj.campDate
        self.form['organizer'] = obj.organizer

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['campName'])):
            inputError['campName'] = "campName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['campName'])):
                inputError['campName'] = "campName contains only "
                self.form['error'] = True

        if (DataValidator.isNull(self.form['campDate'])):
            inputError['campDate'] = "campDate can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['campDate'])):
                inputError['campDate'] = "Incorrect date format, should be YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['organizer'])):
            inputError['organizer'] = "organizer can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['organizer'])):
                inputError['organizer'] = "organizer contains only "
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
            uniqueAttrib = {"campName": self.form['campName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the DonationCamp
            donationcamp = self.form_to_model(DonationCamp())
            self.get_service().save(donationcamp)
            res["success"] = True
            res["result"]["data"] = donationcamp.id
            res["result"]["message"] = "DonationCamp added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["campName"] = json_request.get("campName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = DonationCamp.objects.last().id
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

    def preload(self, request, params={}, donationcamp_list=None):
        try:
            res = {"result": {}, "success": True}
            donationcamp_list = DonationCampService().preload()
            preloadList = []
            for x in donationcamp_list:
                preloadList.append(x.to_json())
            res["result"]["donationcamp_list"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return DonationCampService()