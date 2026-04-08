import { Component } from '@angular/core';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';
import { BaseListCtl } from '../base-list.component';

@Component({
  selector: 'app-notification-template-list',
  templateUrl: './notification-template-list.component.html',
  styleUrls: ['./notification-template-list.component.css']
})
export class NotificationTemplateListComponent extends BaseListCtl{
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
        super(locator.endpoints.NOTIFICATIONTEMPLATE, locator, route);
      }

}
