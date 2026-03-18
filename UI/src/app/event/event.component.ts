import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseCtl } from '../base.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css']
})
export class EventComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.EVENT, locator, route);
    }


}
