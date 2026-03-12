import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-plantnursery-list',
  templateUrl: './plantnursery-list.component.html',
  styleUrls: ['./plantnursery-list.component.css']
})
export class PlantNurseryListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.PLANTNURSERY, locator, route);
      }

}
