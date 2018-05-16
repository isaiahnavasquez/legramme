import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service';
import { Blog } from '../data-classes'

@Component({
  selector: 'app-blog-block',
  templateUrl: './blog-block.component.html',
  styleUrls: ['./blog-block.component.css']
})
export class BlogBlockComponent implements OnInit {

  blog: Blog = new Blog()

  constructor(
    private blogService: BlogService,
  ) { }

  ngOnInit() {
    
  }

}
