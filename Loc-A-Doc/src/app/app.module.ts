import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingComponent } from './landing/landing.component';
import { InsuranceComponent } from './insurance/insurance.component';
import { DoctorPickComponent } from './doctor-pick/doctor-pick.component';
import { DoctorResultComponent } from './doctor-result/doctor-result.component';
import { LocationComponent } from './location/location.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    LandingComponent,
    InsuranceComponent,
    DoctorPickComponent,
    DoctorResultComponent,
    LocationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
