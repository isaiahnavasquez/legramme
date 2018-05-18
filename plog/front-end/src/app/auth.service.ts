import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { User, Profile } from './data-classes';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient,
    private cookieService: CookieService,
    private router: Router,
  ) { }

  loginUser(username, password) {
    
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }

    const auth = {
        'username': username,
        'password': password
    }

    return this.http.post('http://127.0.0.1:8000/api/auth-token/', auth, httpOptions);
  }
  
  getAuthToken(): string {
    return this.cookieService.get('auth-token');
  }
  
  isLoggedIn(): boolean {
    const isLoggedIn = this.cookieService.check('auth-token');
    if (isLoggedIn) {
      this.router.navigate(['/home']);
    } else {
      this.router.navigate(['/login']);
    }
    return isLoggedIn
  }

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('http://127.0.0.1:8000/api/users');
  }
  
  // NOTE: additional useful information related to user (profile)
  getProfiles(): Observable<Profile[]> {
    return this.http.get<Profile[]>('http://127.0.0.1:8000/api/profiles');
  }
  
  // NOTE: returns profile, user id
  getProfile(id: number): Observable<Profile> {
    return this.http.get<Profile>('http://127.0.0.1:8000/api/profile/' + id);
  }
  
  // NOTE: returns username and name of user
  getUser(id: number): Observable<User> {
    return this.http.get<User>('http://127.0.0.1:8000/api/users/' + id);
  }
  
  getUserID(): number {
    return +this.cookieService.get('user-id');
  }

}
