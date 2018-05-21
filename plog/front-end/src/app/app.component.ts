import { Component, OnInit, ViewChild, Input } from '@angular/core';
import { MatSidenav } from '@angular/material/';
import { AuthService } from './auth.service';
import { Router, ActivatedRoute, Event, NavigationEnd } from '@angular/router';
import { User, Profile } from './data-classes';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  
  title = 'app';
  loggedIn: boolean = false;
  activeRoute: string = '';
  user: User = new User();
  profile: Profile = new Profile();
  
  constructor (
    private authService: AuthService,
    private router: Router,
    private activatedRoute: ActivatedRoute,
  ) { }
  
  ngOnInit() {
    // NOTE: check if user is logged in or not
    // and routes the app accordingly
    this.isLoggedIn();
    
    // NOTE: checks the selected tab-page
    this.router.events.subscribe((event: Event) => {
      if (event instanceof NavigationEnd) {
        this.activeRoute = event.url;
      }
    });
  }
  
  isLoggedIn() {
    // NOTE: get information and display in the app accordingly
    this.loggedIn = this.authService.isLoggedIn();
    if (this.loggedIn) {
      const id = +this.authService.getUserID();
      this.authService.getProfile(id).subscribe(data => {
        this.profile = data
      });
      this.authService.getUser(id).subscribe(data => {
        this.user = data;
      });
    }
  }
  
}
