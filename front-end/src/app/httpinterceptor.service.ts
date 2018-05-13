import { Injectable, Injector } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import 'rxjs/add/observable/throw';
import 'rxjs/add/observable/catch';

@Injectable()
export class HttpinterceptorService {

  constructor() { }
  
  // intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
  //   {
  //     headers: req.headers.set('Authorization')
  //   }
  // }
  // 
}
