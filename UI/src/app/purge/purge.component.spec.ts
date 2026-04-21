import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PurgeComponent } from './purge.component';

describe('PurgeComponent', () => {
  let component: PurgeComponent;
  let fixture: ComponentFixture<PurgeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PurgeComponent]
    });
    fixture = TestBed.createComponent(PurgeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
