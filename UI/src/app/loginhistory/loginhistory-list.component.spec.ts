import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginhistoryListComponent } from './loginhistory-list.component';

describe('LoginhistoryListComponent', () => {
  let component: LoginhistoryListComponent;
  let fixture: ComponentFixture<LoginhistoryListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LoginhistoryListComponent]
    });
    fixture = TestBed.createComponent(LoginhistoryListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
