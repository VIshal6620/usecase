from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.UserCtl import UserCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.ChangePasswordCtl import ChangePasswordCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl
from .ctl.ErrorCtl import ErrorCtl
from .ctl.LoanCtl import LoanCtl
from .ctl.GymCtl import GymCtl
from .ctl.TravelCtl import TravelCtl
from .ctl.HolidayCtl import HolidayCtl
from .ctl.SpeakerCtl import SpeakerCtl
from .ctl.PlantNurseryCtl import PlantNurseryCtl
from .ctl.EventCtl import EventCtl
from .ctl.RewardCtl import RewardCtl


@csrf_exempt
def action(request, page, action="get", id=0, pageNo=1):
    methodCall = page + "Ctl()." + action + "(request,{'id':id, 'pageNo':pageNo})"
    response = eval(methodCall)
    return response