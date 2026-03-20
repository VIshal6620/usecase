import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';
import { BaseCtl } from '../base.component';

@Component({
  selector: 'app-rejection',
  templateUrl: './rejection.component.html',
  styleUrls: ['./rejection.component.css']
})
export class RejectionComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.REJECTION, locator, route);
    }


}
