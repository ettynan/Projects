import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class LocationService {
    constructor(public http: HttpClient) {

    }
    getCity(callback) {
        navigator.geolocation.getCurrentPosition((result) => {
            console.log(result)
            this.http.get(`http://open.mapquestapi.com/geocoding/v1/reverse?key=uLPGp8KKQGSE72r1TmUMx6irYRAAp4fc&location=${result.coords.latitude},${result.coords.longitude}&includeRoadMetadata=true&includeNearestIntersection=true`).subscribe(val => {
                callback(val);
                console.log(val)
            });
        })
    }
}