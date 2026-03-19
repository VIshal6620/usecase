import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ServiceLocatorService } from '../service-locator.service';
import { BaseListCtl } from '../base-list.component';

@Component({
  selector: 'app-reward-list',
  templateUrl: './reward-list.component.html',
})
export class RewardListComponent extends BaseListCtl{

  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
    super(locator.endpoints.REWARD, locator, route);
  }

}