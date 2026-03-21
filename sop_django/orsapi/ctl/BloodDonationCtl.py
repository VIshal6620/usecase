import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import BloodDonation
from ..service.BloodDonationService import BloodDonationService
from ..utility.DataValidator import DataValidator


class BloodDonationCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['donorName'] = requestForm.get('donorName')
        self.form['bloodGroup'] = requestForm.get('bloodGroup')
        self.form['donationDate'] = requestForm.get('donationDate')
        self.form['contactNumber'] = requestForm.get('contactNumber')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.donorName = self.form['donorName']
        obj.bloodGroup = self.form['bloodGroup']
        obj.donationDate = self.form['donationDate']
        obj.contactNumber = self.form['contactNumber']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['donorName'] = obj.donorName
        self.form['bloodGroup'] = obj.bloodGroup
        self.form['donationDate'] = obj.donationDate
        self.form['contactNumber'] = obj.contactNumber

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['donorName'])):
            inputError['donorName'] = "donorName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['donorName'])):
                inputError['donorName'] = "donorName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['bloodGroup'])):
            inputError['bloodGroup'] = "bloodGroup can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isAllCharAllowed(self.form['bloodGroup'])):
                inputError['bloodGroup'] = "bloodGroup  is required"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['donationDate'])):
            inputError['donationDate'] = "donationDate can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['donationDate'])):
                inputError['donationDate'] = "Incorrect date format, should be YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['contactNumber'])):
            inputError['contactNumber'] = "endDate can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.ismobilecheck(self.form['contactNumber'])):
                inputError['contactNumber'] = "contactNumber  is required"
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
            uniqueAttrib = {"donorName": self.form['donorName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the BloodDonation
            blood_donation = self.form_to_model(BloodDonation())
            self.get_service().save(blood_donation)
            res["success"] = True
            res["result"]["data"] = blood_donation.id
            res["result"]["message"] = "BloodDonation added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["donorName"] = json_request.get("donorName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = BloodDonation.objects.last().id
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
            blood_donation_list = BloodDonationService().preload()
            preloadList = []
            for x in blood_donation_list:
                preloadList.append(x.to_json())
            res["result"]["blood_donationList"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return BloodDonationService()