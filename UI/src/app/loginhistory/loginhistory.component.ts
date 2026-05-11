import { Component } from '@angular/core';
import { BaseCtl } from '../base.component';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-loginhistory',
  templateUrl: './loginhistory.component.html',
  styleUrls: ['./loginhistory.component.css']
})
export class LoginHistoryComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.LOGINHISTORY, locator, route);
    }


}
