import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';
import { BaseCtl } from '../base.component';

@Component({
  selector: 'app-donationcamp',
  templateUrl: './donationcamp.component.html',
  styleUrls: ['./donationcamp.component.css']
})
export class DonationCampComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.DONATIONCAMP, locator, route);
    }


}
