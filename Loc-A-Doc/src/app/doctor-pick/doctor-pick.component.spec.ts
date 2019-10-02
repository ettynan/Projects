import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorPickComponent } from './doctor-pick.component';

describe('DoctorPickComponent', () => {
  let component: DoctorPickComponent;
  let fixture: ComponentFixture<DoctorPickComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DoctorPickComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DoctorPickComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
