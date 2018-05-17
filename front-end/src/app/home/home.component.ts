import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service';
import { AuthService } from '../auth.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  selected: string = 'users';

  constructor(
    private blogService: BlogService,
    private authService: AuthService,
    private activeRoute: ActivatedRoute,
  ) { }

  ngOnInit() {
    
  }
  
  getBlogs() {
    this.selected = 'blogs';
  }
  
  getUsers() {
    this.selected = 'users';
  }

}
