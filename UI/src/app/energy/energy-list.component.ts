import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-energy-list',
  templateUrl: './energy-list.component.html',
  styleUrls: ['./energy-list.component.css']
})
export class EnergyListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.ENERGY, locator, route);
      }

}
