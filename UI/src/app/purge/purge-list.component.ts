import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-purge-list',
  templateUrl: './purge-list.component.html',
  styleUrls: ['./purge-list.component.css']
})
export class PurgeListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.PURGE, locator, route);
      }

}
