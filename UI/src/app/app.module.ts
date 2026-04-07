import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';


import { UserComponent } from './user/user.component';
import { UserListComponent } from './user/user-list.component';
import { ChangepasswordComponent } from './user/changepassword.component';
import { RoleComponent } from './role/role.component';
import { NavbarComponent } from './navbar/navbar.component';
import { RoleListComponent } from './role/role-list.component';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './login/login.component';
import { ForgetpasswordComponent } from './login/forgetpassword.component';
import { SignupComponent } from './login/signup.component';
import { GymComponent } from './gym/gym.component';
import { GymListComponent } from './gym/gym-list.component';
import { LoanComponent } from './loan/loan.component';
import { LoanListComponent } from './loan/loan-list.component';
import { TravelComponent } from './travel/travel.component';
import { TravelListComponent } from './travel/travel-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { HttpServiceService } from './http-service.service';
import { EndpointServiceService } from './endpoint-service.service';
import { ServiceLocatorService } from './service-locator.service';
import { AuthServiceService } from './auth-service.service';
import { HolidayComponent } from './holiday/holiday.component';
import { HolidayListComponent } from './holiday/holiday-list.component';
import { SpeakerComponent } from './speaker/speaker.component';
import { SpeakerListComponent } from './speaker/speaker-list.component';
import { PlantNurseryListComponent } from './plantnursery/plantnursery-list.component'
import { PlantNurseryComponent } from './plantnursery/plantnursery.component';
import { EventComponent } from './event/event.component';
import { EventListComponent } from './event/event-list.component';
import { RewardComponent } from './reward/reward.component';
import { RewardListComponent } from './reward/reward-list.component';
import { RejectionComponent } from './rejection/rejection.component';
import { RejectionListComponent } from './rejection/rejection-list.component';
import { BloodDonationComponent } from './blood-donation/blood-donation.component';
import { BloodDonationListComponent } from './blood-donation/blood-donation-list.component';
import { SecurityComponent } from './security/security.component';
import { SecurityListComponent } from './Security/security-list.component';


@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    UserListComponent,
    ChangepasswordComponent,
    RoleComponent,
    NavbarComponent,
    RoleListComponent,
    DashboardComponent,
    FooterComponent,
    LoginComponent,
    ForgetpasswordComponent,
    SignupComponent,
    GymComponent,
    GymListComponent,
    LoanComponent,
    LoanListComponent,
    TravelComponent,
    TravelListComponent,
    HolidayComponent,
    HolidayListComponent,
    SpeakerComponent,
    SpeakerListComponent,
    PlantNurseryComponent,
    PlantNurseryListComponent,
    EventComponent,
    EventListComponent,
    RewardComponent,
    RewardListComponent,
    RejectionComponent,
    RejectionListComponent,
    BloodDonationComponent,
    BloodDonationListComponent,
    SecurityComponent,
    SecurityListComponent,
 ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS, useClass: AuthServiceService, multi: true
    },
    HttpServiceService,
    EndpointServiceService,
    ServiceLocatorService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }