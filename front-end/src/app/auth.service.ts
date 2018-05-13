import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { CookieService } from 'ngx-cookie-service'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient,
    private cookieService: CookieService,
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

    return this.http.post('http://127.0.0.1:8000/api-token-auth/', auth, httpOptions);
  }
  
  getAuthToken(): string {
    return this.cookieService.get('auth-token');
  }
  
  isLoggedIn(): boolean {
    
    
    return 
  }

}
