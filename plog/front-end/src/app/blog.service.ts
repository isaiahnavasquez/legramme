import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';
import { Blog } from './data-classes';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Location } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class BlogService {

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) { }

  getBlogs(): Observable<Blog[]> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': this.authService.getAuthToken()
      })
    }

    return this.http.get<Blog[]>('http://127.0.0.1:8000/api/blogs/', httpOptions);
  };

  getBlog(id): Observable<Blog> {
    return this.http.get<Blog>('http://127.0.0.1:8000/api/blogs/' + id);
  }

}
