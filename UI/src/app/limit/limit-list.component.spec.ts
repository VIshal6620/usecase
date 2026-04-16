import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LimitListComponent } from './limit-list.component';

describe('LimitListComponent', () => {
  let component: LimitListComponent;
  let fixture: ComponentFixture<LimitListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LimitListComponent]
    });
    fixture = TestBed.createComponent(LimitListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
