import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-donationcamp-list',
  templateUrl: './donationcamp-list.component.html',
  styleUrls: ['./donationcamp-list.component.css']
})
export class DonationCampListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.DONATIONCAMP, locator, route);
      }

}
