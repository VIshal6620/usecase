import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NotificationTemplateListComponent } from './notification-template-list.component';

describe('NotificationTemplateListComponent', () => {
  let component: NotificationTemplateListComponent;
  let fixture: ComponentFixture<NotificationTemplateListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NotificationTemplateListComponent]
    });
    fixture = TestBed.createComponent(NotificationTemplateListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
