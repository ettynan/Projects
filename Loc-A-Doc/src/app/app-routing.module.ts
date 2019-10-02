import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingComponent } from './landing/landing.component';
import { InsuranceComponent } from './insurance/insurance.component';
import { DoctorPickComponent } from './doctor-pick/doctor-pick.component';
import { DoctorResultComponent } from './doctor-result/doctor-result.component';
import { LocationComponent } from './location/location.component';


const routes: Routes = [{
  path: "home", 
  component: LandingComponent
},
{ path: "location",
  component: LocationComponent
},
{
  path: "insurance",
  component: InsuranceComponent
},
{
  path: "doctor-pick",
  component: DoctorPickComponent
},
{
  path: "doctor-result",
  component: DoctorResultComponent
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
