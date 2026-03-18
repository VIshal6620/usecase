import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Event
from ..service.EventService import EventService
from ..utility.DataValidator import DataValidator


class EventCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['participantName'] = requestForm.get('participantName')
        self.form['eventName'] = requestForm.get('eventName')
        self.form['email'] = requestForm.get('email')
        self.form['registrationDate'] = requestForm.get('registrationDate')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.participantName = self.form['participantName']
        obj.eventName = self.form['eventName']
        obj.email = self.form['email']
        obj.registrationDate = self.form['registrationDate']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['participantName'] = obj.participantName
        self.form['eventName'] = obj.eventName
        self.form['email'] = obj.email
        self.form['registrationDate'] = obj.registrationDate

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['participantName'])):
            inputError['participantName'] = "participantName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['participantName'])):
                inputError['participantName'] = "participantName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['eventName'])):
            inputError['eventName'] = "eventName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['eventName'])):
                inputError['eventName'] = "eventName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['email'])):
            inputError['email'] = "email can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isemail(self.form['email'])):
                inputError['email'] = "email contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['registrationDate'])):
            inputError['registrationDate'] = "endDate can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['registrationDate'])):
                inputError['registrationDate'] = "Incorrect date format, should be YYYY-MM-DD"
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
            uniqueAttrib = {"participantName": self.form['participantName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the EVENT
            event = self.form_to_model(Event())
            self.get_service().save(event)
            res["success"] = True
            res["result"]["data"] = event.id
            res["result"]["message"] = "Event added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["participantName"] = json_request.get("participantName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Event.objects.last().id
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
            event_list = EventService().preload()
            preloadList = []
            for x in event_list:
                preloadList.append(x.to_json())
            res["result"]["event_list"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return EventService()