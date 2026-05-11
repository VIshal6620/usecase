import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';
import { BaseListCtl } from '../base-list.component';

@Component({
  selector: 'app-loginhistory-list',
  templateUrl: './loginhistory-list.component.html',
  styleUrls: ['./loginhistory-list.component.css']
})
export class LoginHistoryListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.LOGINHISTORY, locator, route);
      }

}