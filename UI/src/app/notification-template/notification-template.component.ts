import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseCtl } from '../base.component';

@Component({
  selector: 'app-notification-template',
  templateUrl: './notification-template.component.html',
  styleUrls: ['./notification-template.component.css']
})
export class NotificationTemplateComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.NOTIFICATIONTEMPLATE, locator, route);
    }


}
