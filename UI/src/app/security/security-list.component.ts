import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-security-list',
  templateUrl: './security-list.component.html',
  styleUrls: ['./security-list.component.css']
})
export class SecurityListComponent extends BaseListCtl{

  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
    super(locator.endpoints.SECURITY, locator, route);
  }

}
