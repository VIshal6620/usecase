import { Component } from '@angular/core';
import { BaseCtl } from '../base.component';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-plantnursery',
  templateUrl: './plantnursery.component.html',
  styleUrls: ['./plantnursery.component.css']
})
export class PlantNurseryComponent extends BaseCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.PLANTNURSERY, locator, route);
      }

}
