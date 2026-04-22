from django.views.decorators.csrf import csrf_exempt

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
from .ctl.RejectionCtl import RejectionCtl
from .ctl.BloodDonationCtl import BloodDonationCtl
from .ctl.SecurityCtl import SecurityCtl
from .ctl.NotificationTemplateCtl import NotificationTemplateCtl
from .ctl.LimitCtl import LimitCtl
from .ctl.PurgeCtl import PurgeCtl
from .ctl.DonationCampCtl import DonationCampCtl


@csrf_exempt
def action(request, page, action="get", id=0, pageNo=1):
    methodCall = page + "Ctl()." + action + "(request,{'id':id, 'pageNo':pageNo})"
    response = eval(methodCall)
    return response