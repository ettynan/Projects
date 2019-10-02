import { Component, OnInit } from '@angular/core';
import { LocationService } from '../location.service';

@Component({
  selector: 'app-location',
  templateUrl: './location.component.html',
  styleUrls: ['./location.component.css']
})
export class LocationComponent implements OnInit {
loc;
  constructor(public ls:LocationService) { }

  ngOnInit() {
    this.ls.getCity((res)=>{
    this.loc = res
    })
  }

}
