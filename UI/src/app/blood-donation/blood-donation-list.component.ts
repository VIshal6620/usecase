import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-blood-donation-list',
  templateUrl: './blood-donation-list.component.html',
  styleUrls: ['./blood-donation-list.component.css']
})
export class BloodDonationListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.BLOODDONATION, locator, route);
      }

}
