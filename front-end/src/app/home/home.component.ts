import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service';
import { AuthService } from '../auth.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  selectedPage: string = 'blogs';

  constructor(
    private blogService: BlogService,
    private authService: AuthService,
    private activatedRoute: ActivatedRoute,
    private route: Router,
  ) { }

  ngOnInit() {
    
  }
  
  getBlogs() {
    this.route.navigate(['blogs'], { relativeTo: this.activatedRoute });
    this.selectedPage = 'blogs';
  }
  
  getUsers() {
    this.route.navigate(['authors'], { relativeTo: this.activatedRoute })
    this.selectedPage = 'users';
  }

}
