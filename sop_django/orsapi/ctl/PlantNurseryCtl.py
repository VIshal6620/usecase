import json
from django.http import JsonResponse
from ..ctl.BaseCtl import BaseCtl
from ..ctl.ErrorCtl import ErrorCtl
from ..models import PlantNursery
from ..service.PlantNurseryService import PlantNurseryService
from ..utility.DataValidator import DataValidator


class PlantNurseryCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id')
        self.form['plantName'] = requestForm.get('plantName')
        self.form['category'] = requestForm.get('category')
        self.form['quantity'] = requestForm.get('quantity')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.plantName = self.form['plantName']
        obj.category = self.form['category']
        obj.quantity = self.form['quantity']
        return obj

    def model_to_form(self, obj):
        if obj == None:
            return
        self.form['id'] = obj.id
        self.form['plantName'] = obj.plantName
        self.form['category'] = obj.category
        self.form['quantity'] = obj.quantity

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['plantName'])):
            inputError['plantName'] = "plantName can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['plantName'])):
                inputError['plantName'] = "plantName contains only number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['category'])):
            inputError['category'] = "category can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['quantity'])):
            inputError['quantity'] = "quantity can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isinteger(self.form['quantity'])):
                inputError['quantity'] = "quantity contains only number"
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
            uniqueAttrib = {"plantName": self.form['plantName']}
            duplicateErrors = self.get_service().mduplicateFields(uniqueAttrib, pk)
            size = len(duplicateErrors)
            if (size > 0):
                res["success"] = False
                res["result"]["inputerror"] = duplicateErrors
                return JsonResponse(res)

            # Add/ Update the plant_nursery
            plant_nursery = self.form_to_model(PlantNursery())
            self.get_service().save(plant_nursery)
            res["success"] = True
            res["result"]["data"] = plant_nursery.id
            res["result"]["message"] = "PlantNursery added successfully"
            return JsonResponse(res)

        except Exception as ex:
            return ErrorCtl.handle(ex)


    def search(self, request, params={}):
        try:
            json_request = json.loads(request.body)
            res = {"result": {}, "success": True}
            if (json_request):
                params["plantName"] = json_request.get("plantName", None)
                params["pageNo"] = json_request.get("pageNo", None)
            records = self.get_service().search(params)
            if records and records.get("data"):
                res["success"] = True
                res["result"]["data"] = records["data"]
                res["result"]["lastId"] = PlantNursery.objects.last().id
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
            plant_nursery_list = PlantNurseryService().preload()
            preloadList = []
            for x in plant_nursery_list:
                preloadList.append(x.to_json())
            res["result"]["plant_nursery_List"] = preloadList
            return JsonResponse(res)
        except Exception as ex:
            return ErrorCtl.handle(ex)

    def get_service(self):
        return PlantNurseryService()