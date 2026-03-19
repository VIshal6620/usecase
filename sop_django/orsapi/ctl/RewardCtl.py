import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import Reward
from ..service.RewardService import RewardService
from ..utility.DataValidator import DataValidator


class RewardCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['rewardCode'] = requestForm.get('rewardCode')
        self.form['rewardName'] = requestForm.get('rewardName')
        self.form['rewardAmount'] = requestForm.get('rewardAmount')
        self.form['rewardStatus'] = requestForm.get('rewardStatus')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.rewardCode = self.form['rewardCode']
        obj.rewardName = self.form['rewardName']
        obj.rewardAmount = self.form['rewardAmount']
        obj.rewardStatus = self.form['rewardStatus']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['rewardCode'] = obj.rewardCode
        self.form['rewardName'] = obj.rewardName
        self.form['rewardAmount'] = obj.rewardAmount
        self.form['rewardStatus'] = obj.rewardStatus

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['rewardCode'])):
            inputError['rewardCode'] = "rewardCode can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isRewardCode(self.form['rewardCode'])):
                inputError['rewardCode'] = "rewardCode contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['rewardName'])):
            inputError['rewardName'] = "rewardName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['rewardName'])):
                inputError['rewardName'] = "contains only rewardName"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['rewardAmount'])):
            inputError['rewardAmount'] = "rewardAmount can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isinteger(self.form['rewardAmount'])):
                inputError['rewardAmount'] = "rewardAmount contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['rewardStatus'])):
            inputError['rewardStatus'] = "rewardStatus can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['rewardStatus'])):
                inputError['rewardStatus'] = "rewardStatus contains only numbe"
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
            uniqueAttrib = {"rewardCode": self.form['rewardCode']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the Reward
            reward = self.form_to_model(Reward())
            self.get_service().save(reward)
            res["success"] = True
            res["result"]["data"] = reward.id
            res["result"]["message"] = "Reward added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["rewardCode"] = json_request.get("rewardCode", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = Reward.objects.last().id
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
            reward_list = RewardService().preload()
            preloadList = []
            for x in reward_list:
                preloadList.append(x.to_json())
            res["result"]["rewardList"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return RewardService()