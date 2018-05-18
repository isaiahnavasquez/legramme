import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  errors: string = ''

  constructor(
    private authService: AuthService,
    private cookieService: CookieService,
    private router: Router,
  ) { }

  ngOnInit() {
    
  }

  loginUser(event) {
    event.preventDefault();
    const username = event.target.querySelector('#username').value;
    const password = event.target.querySelector('#password').value;
    this.authService.loginUser(username, password).subscribe(
      response => {
        console.log('saving session')
        this.cookieService.set('auth-token', response['token']);
        this.cookieService.set('user-id', response['id']);
        this.router.navigate(['/home']);
      },
      errors => {
        this.errors = 'Invalid Credentials'
      }
    )
  }

}
