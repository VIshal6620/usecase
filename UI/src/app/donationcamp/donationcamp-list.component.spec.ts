import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DonationcampListComponent } from './donationcamp-list.component';

describe('DonationcampListComponent', () => {
  let component: DonationcampListComponent;
  let fixture: ComponentFixture<DonationcampListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DonationcampListComponent]
    });
    fixture = TestBed.createComponent(DonationcampListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
