import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import NotificationTemplate
from ..service.NotificationTemplateService import NotificationTemplateService
from ..utility.DataValidator import DataValidator


class NotificationTemplateCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['templateCode'] = requestForm.get('templateCode')
        self.form['title'] = requestForm.get('title')
        self.form['content'] = requestForm.get('content')
        self.form['status'] = requestForm.get('status')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.templateCode = self.form['templateCode']
        obj.title = self.form['title']
        obj.content = self.form['content']
        obj.status = self.form['status']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['templateCode'] = obj.templateCode
        self.form['title'] = obj.title
        self.form['content'] = obj.content
        self.form['status'] = obj.status

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['templateCode'])):
            inputError['templateCode'] = "templateCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isRewardCode(self.form['templateCode'])):
                inputError['templateCode'] = "templateCode contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['title'])):
            inputError['title'] = "title can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isRewardCode(self.form['title'])):
                inputError['title'] = "contains only title"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['content'])):
            inputError['content'] = "content can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isinteger(self.form['content'])):
                inputError['content'] = "content contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['status'])):
            inputError['status'] = "status can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isinteger(self.form['status'])):
                inputError['status'] = "status contains only number"
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
            uniqueAttrib = {"templateCode": self.form['templateCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the NotificationTemplate
            notification_template = self.form_to_model(NotificationTemplate())
            self.get_service().save(notification_template)
            res["success"] = True
            res["result"]["data"] = notification_template.id
            res["result"]["message"] = "NotificationTemplate added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["templateCode"] = json_request.get("templateCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = NotificationTemplate.objects.last().id
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
            notification_template_list = NotificationTemplateService().preload()
            preloadList = []
            for x in notification_template_list:
                preloadList.append(x.to_json())
            res["result"]["notification_templateList"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return NotificationTemplateService()