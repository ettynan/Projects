import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorResultComponent } from './doctor-result.component';

describe('DoctorResultComponent', () => {
  let component: DoctorResultComponent;
  let fixture: ComponentFixture<DoctorResultComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DoctorResultComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DoctorResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
