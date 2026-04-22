import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DonationcampComponent } from './donationcamp.component';

describe('DonationcampComponent', () => {
  let component: DonationcampComponent;
  let fixture: ComponentFixture<DonationcampComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DonationcampComponent]
    });
    fixture = TestBed.createComponent(DonationcampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
