import { Component } from '@angular/core';
import { BaseCtl } from '../base.component';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-security',
  templateUrl: './security.component.html',
  styleUrls: ['./security.component.css']
})
export class SecurityComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.SECURITY, locator, route);
    }


}
