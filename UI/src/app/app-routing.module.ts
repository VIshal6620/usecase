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
import { ChangepasswordComponent } from "./user/changepassword.component";
import { ForgetpasswordComponent } from "./login/forgetpassword.component";
import { NgModule } from "@angular/core";
import { HolidayComponent } from "./holiday/holiday.component";
import { HolidayListComponent } from "./holiday/holiday-list.component";
import { SpeakerComponent } from "./speaker/speaker.component";
import { SpeakerListComponent } from "./speaker/speaker-list.component";




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
   path:'gymlist',
   component: GymListComponent
  },
  {
   path:'gym/:id',
   component: GymComponent
  },
  {
    path:'travel',
    component: TravelComponent
  },
 {
   path:'travellist',
   component: TravelListComponent
  },
  {
    path:'travel/:id',
    component: TravelComponent
  },
  {
    path:'holiday',
    component: HolidayComponent
  },
 {
   path:'holidaylist',
   component: HolidayListComponent
  },
  {
    path:'holiday/:id',
    component: HolidayComponent
  },
  {
    path:'speaker',
    component: SpeakerComponent
  },
 {
   path:'speakerlist',
   component: SpeakerListComponent
  },
  {
    path:'speaker/:id',
    component: SpeakerComponent
  },
  {
    path: 'changepassword',
    component: ChangepasswordComponent
  },
  {
    path: 'forgetpassword',
    component:ForgetpasswordComponent
  }

];

@NgModule({
  
  // imports: [RouterModule.forRoot(routes)],
  
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }