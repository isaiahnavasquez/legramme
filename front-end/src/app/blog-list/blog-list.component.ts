import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service';
import { Blog } from '../data-classes'

@Component({
  selector: 'app-blog-list',
  templateUrl: './blog-list.component.html',
  styleUrls: ['./blog-list.component.css']
})
export class BlogListComponent implements OnInit {

  blogs: Blog[] = [];

  constructor(
    private blogService: BlogService,
  ) { }

  ngOnInit() {
    this.getBlogs();
  }
  
  getBlogs() {
    this.blogService.getBlogs().subscribe(data => {
      console.log(data);
      this.blogs = data;
    })
  }

}
