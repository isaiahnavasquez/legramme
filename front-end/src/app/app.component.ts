import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/';
import { AuthService } from './auth.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  
  title = 'app';
  loggedIn: boolean = false;
  
  constructor (
    private authService: AuthService,
    private router: Router,
  ) { }
  
  ngOnInit() {
    this.authService.isLoggedIn();
  }
  
}
