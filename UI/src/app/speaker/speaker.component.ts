import { Component } from '@angular/core';
import { BaseCtl } from '../base.component';
import { ServiceLocatorService } from '../service-locator.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-speaker',
  templateUrl: './speaker.component.html',
  styleUrls: ['./speaker.component.css']
})
export class SpeakerComponent extends BaseCtl {
   constructor(public locator: ServiceLocatorService, route: ActivatedRoute) {
      super(locator.endpoints.SPEAKER, locator, route);
    }


}