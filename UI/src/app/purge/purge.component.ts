import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseCtl } from '../base.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-purge',
  templateUrl: './purge.component.html',
  styleUrls: ['./purge.component.css']
})
export class PurgeComponent extends BaseCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.PURGE, locator, route);
      }

}
