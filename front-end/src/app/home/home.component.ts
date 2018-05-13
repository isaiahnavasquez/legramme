import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(
    private blogService: BlogService,
    private authService: AuthService,
  ) { }

  ngOnInit() {
    this.blogService.getBlogs().subscribe(data => {
      console.log(data)
    })
  }

}
