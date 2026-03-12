import json

from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Speaker
from ..service.SpeakerService import SpeakerService
from ..utility.DataValidator import DataValidator


class SpeakerCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['speakerName'] = requestForm.get('speakerName')
        self.form['topic'] = requestForm.get('topic')
        self.form['organization'] = requestForm.get('organization')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.speakerName = self.form['speakerName']
        obj.topic = self.form['topic']
        obj.organization = self.form['organization']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['speakerName'] = obj.speakerName
        self.form['topic'] = obj.topic
        self.form['organization'] = obj.organization

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['speakerName'])):
            inputError['speakerName'] = "speakerName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['speakerName'])):
                inputError['speakerName'] = "speakerName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['topic'])):
            inputError['topic'] = "topic can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['organization'])):
            inputError['organization'] = "organization can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['organization'])):
                inputError['organization'] = "organization contains only number"
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
            uniqueAttrib = {"speakerName": self.form['speakerName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the speaker
            speaker = self.form_to_model(Speaker())
            self.get_service().save(speaker)
            res["success"] = True
            res["result"]["data"] = speaker.id
            res["result"]["message"] = "speaker added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["speakerName"] = json_request.get("speakerName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Speaker.objects.last().id
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
            speaker_list = SpeakerService().preload()
            preloadList = []
            for x in speaker_list:
                preloadList.append(x.to_json())
            res["result"]["speakerlist"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return SpeakerService()