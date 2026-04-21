import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PurgeListComponent } from './purge-list.component';

describe('PurgeListComponent', () => {
  let component: PurgeListComponent;
  let fixture: ComponentFixture<PurgeListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PurgeListComponent]
    });
    fixture = TestBed.createComponent(PurgeListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
