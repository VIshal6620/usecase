import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlantnurseryComponent } from './plantnursery.component';

describe('PlantnurseryComponent', () => {
  let component: PlantnurseryComponent;
  let fixture: ComponentFixture<PlantnurseryComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PlantnurseryComponent]
    });
    fixture = TestBed.createComponent(PlantnurseryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
