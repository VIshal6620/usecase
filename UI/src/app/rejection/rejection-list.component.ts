import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';

@Component({
  selector: 'app-rejection-list',
  templateUrl: './rejection-list.component.html',
  styleUrls: ['./rejection-list.component.css']
})
export class RejectionListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.REJECTION, locator, route);
      }

}
