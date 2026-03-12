import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlantnurseryListComponent } from './plantnursery-list.component';

describe('PlantnurseryListComponent', () => {
  let component: PlantnurseryListComponent;
  let fixture: ComponentFixture<PlantnurseryListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PlantnurseryListComponent]
    });
    fixture = TestBed.createComponent(PlantnurseryListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
