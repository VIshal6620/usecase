import { RouterModule, Routes } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { LoginComponent } from "./login/login.component";
import { SignupComponent } from "./login/signup.component";
import { UserComponent } from "./user/user.component";
import { RoleComponent } from "./role/role.component";
import { UserListComponent } from "./user/user-list.component";
import { RoleListComponent } from "./role/role-list.component";
import { LoanComponent } from "./loan/loan.component";
import { LoanListComponent } from "./loan/loan-list.component";
import { GymComponent } from "./gym/gym.component";
import { GymListComponent } from "./gym/gym-list.component";
import { TravelComponent } from "./travel/travel.component";
import { TravelListComponent } from "./travel/travel-list.component";
import { HolidayComponent } from "./holiday/holiday.component";
import { HolidayListComponent } from "./holiday/holiday-list.component";
import { SpeakerComponent } from "./speaker/speaker.component";
import { SpeakerListComponent } from "./speaker/speaker-list.component";
import { PlantNurseryComponent } from "./plantnursery/plantnursery.component";
import { PlantNurseryListComponent } from "./plantnursery/plantnursery-list.component";
import { ChangepasswordComponent } from "./user/changepassword.component";
import { NgModule } from "@angular/core";
import { ForgetpasswordComponent } from "./login/forgetpassword.component";
import { EventListComponent } from "./event/event-list.component";
import { EventComponent } from "./event/event.component";
import { RewardComponent } from "./reward/reward.component";
import { RewardListComponent } from "./reward/reward-list.component";
import { RejectionComponent } from "./rejection/rejection.component";
import { RejectionListComponent } from "./rejection/rejection-list.component";
import { BloodDonationComponent } from "./blood-donation/blood-donation.component";
import { BloodDonationListComponent } from "./blood-donation/blood-donation-list.component";
import { SecurityComponent } from "./security/security.component";
import { SecurityListComponent } from "./security/security-list.component";
import { NotificationTemplateComponent } from "./notification-template/notification-template.component";
import { NotificationTemplateListComponent } from "./notification-template/notification-template-list.component";
import { LimitComponent } from "./limit/limit.component";
import { LimitListComponent } from "./limit/limit-list.component";
import { PurgeListComponent } from "./purge/purge-list.component";
import { PurgeComponent } from "./purge/purge.component";
import { DonationCampListComponent } from "./donationcamp/donationcamp-list.component";
import { DonationCampComponent } from "./donationcamp/donationcamp.component";
import { AccountComponent } from "./account/account.component";
import { AccountListComponent } from "./account/account-list.component";
import { EnergyListComponent } from "./energy/energy-list.component";
import { EnergyComponent } from "./energy/energy.component";
import { LoginHistoryListComponent } from "./loginhistory/loginhistory-list.component";
import { LoginHistoryComponent } from "./loginhistory/loginhistory.component";






const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'dashboard'
  },
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'signup',
    component: SignupComponent
  },
  {
    path: 'user',
    component: UserComponent
  },
  {
    path: 'role',
    component: RoleComponent
  },

  {
    path: 'userlist',
    component: UserListComponent
  },
  {
    path: 'user/:id',
    component: UserComponent
  },
  {
    path: 'rolelist',
    component: RoleListComponent
  },
  {
    path: 'role/:id',
    component: RoleComponent
  },

  {
    path: 'loan',
    component: LoanComponent
  },
  {
    path: 'loanlist',
    component: LoanListComponent
  },
  {
    path: 'loan/:id',
    component: LoanComponent
  },
  {
    path: 'gym',
    component: GymComponent
  },
  {
    path: 'gymlist',
    component: GymListComponent
  },
  {
    path: 'gym/:id',
    component: GymComponent
  },
  {
    path: 'travel',
    component: TravelComponent
  },
  {
    path: 'travellist',
    component: TravelListComponent
  },
  {
    path: 'travel/:id',
    component: TravelComponent
  },
  {
    path: 'holiday',
    component: HolidayComponent
  },
  {
    path: 'holidaylist',
    component: HolidayListComponent
  },
  {
    path: 'holiday/:id',
    component: HolidayComponent
  },
  {
    path: 'speaker',
    component: SpeakerComponent
  },
  {
    path: 'speakerlist',
    component: SpeakerListComponent
  },
  {
    path: 'speaker/:id',
    component: SpeakerComponent
  },
  {
    path: 'PlantNursery',
    component: PlantNurseryComponent
  },
  {
    path: 'PlantNurserylist',
    component: PlantNurseryListComponent
  },
  {
    path: 'PlantNursery/:id',
    component: PlantNurseryComponent
  },
  {
    path: 'Event',
    component: EventComponent
  },
  {
    path: 'Eventlist',
    component: EventListComponent
  },
  {
    path: 'event/:id',
    component: EventComponent
  },
  { path: 'reward', 
    component: RewardComponent },
  {
     path: 'rewardlist',
   component: RewardListComponent
   },
  { 
  path: 'reward/:id',
   component: RewardComponent 
  },
  { path: 'rejection', 
    component: RejectionComponent },
  {
     path: 'rejectionlist',
   component: RejectionListComponent
   },
  { 
  path: 'rejection/:id',
   component: RejectionComponent 
  },
  { path: 'BloodDonation', 
    component: BloodDonationComponent },
  {
     path: 'BloodDonationlist',
   component: BloodDonationListComponent
   },
  { 
  path: 'BloodDonation/:id',
   component: BloodDonationComponent 
  },
  { path: 'Security', 
    component: SecurityComponent },
  {
     path: 'Securitylist',
   component: SecurityListComponent
   },
  { 
  path: 'Security/:id',
   component: SecurityComponent 
  },
    { path: 'NotificationTemplate', 
    component: NotificationTemplateComponent },
  {
     path: 'NotificationTemplatelist',
   component: NotificationTemplateListComponent
   },
  { 
  path: 'NotificationTemplate/:id',
   component: NotificationTemplateComponent 
  },
  { path: 'limit', 
    component: LimitComponent },
  {
     path: 'limitlist',
   component: LimitListComponent
   },
  { 
  path: 'limit/:id',
   component: LimitComponent 
  },
  { path: 'purge', 
    component: PurgeComponent },
  {
     path: 'purgelist',
   component: PurgeListComponent
   },
  { 
  path: 'purge/:id',
   component: PurgeComponent 
  },
  { path: 'DonationCamp', 
    component: DonationCampComponent },
  {
     path: 'DonationCamplist',
   component: DonationCampListComponent
   },
  { 
  path: 'DonationCamp/:id',
   component: DonationCampComponent 
  },
  { path: 'account', 
    component: AccountComponent },
  {
     path: 'accountlist',
   component: AccountListComponent
   },
  { 
  path: 'account/:id',
   component: AccountComponent 
  },
  { path: 'energy', 
    component: EnergyComponent },
  {
     path: 'energylist',
   component: EnergyListComponent
   },
  { 
  path: 'energy/:id',
   component: EnergyComponent 
  },
  { path: 'loginhistory', 
    component: LoginHistoryComponent },
  {
     path: 'loginhistorylist',
   component: LoginHistoryListComponent
   },
  { 
  path: 'loginhistory/:id',
   component: LoginHistoryComponent 
  },
  {
    path: 'changepassword',
    component: ChangepasswordComponent
  },
  {
    path: 'forgetpassword',
    component: ForgetpasswordComponent
  }

  
];

@NgModule({

  // imports: [RouterModule.forRoot(routes)],

  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }