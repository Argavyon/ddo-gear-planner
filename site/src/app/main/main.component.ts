import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { EquippedService } from '../equipped.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  params;

  constructor(
    private readonly route: ActivatedRoute,
    private readonly router: Router,
    private equipped: EquippedService
  ) {
  }

  ngOnInit() {
    this.route.queryParamMap.subscribe(params => {
      this.equipped.updateFromParams(params.params);
    });
  }

}
