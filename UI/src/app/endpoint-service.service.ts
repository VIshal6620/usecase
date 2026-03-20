import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EndpointServiceService {

  constructor() { }

  public SERVER_URL = "http://localhost:8000/orsapi";
  public USER = this.SERVER_URL + "/User";
  public ROLE = this.SERVER_URL + "/Role";
  public LOAN = this.SERVER_URL + "/Loan";
  public GYM = this.SERVER_URL + "/Gym"
  public TRAVEL = this.SERVER_URL + "/Travel"
  public HOLIDAY = this.SERVER_URL + "/Holiday"
  public SPEAKER = this.SERVER_URL + "/Speaker"
  public PLANTNURSERY = this.SERVER_URL + "/PlantNursery"
  public EVENT = this.SERVER_URL + "/Event"
  public REWARD = this.SERVER_URL + "/Reward"
  public REJECTION = this.SERVER_URL + "/Rejection"
}