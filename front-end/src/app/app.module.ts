import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

// services
import { AuthService } from './auth.service';
import { BlogService } from './blog.service';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { CreateBlogComponent } from './create-blog/create-blog.component';
import { LoginComponent } from './login/login.component';
import { BlogBlockComponent } from './blog-block/blog-block.component';
import { BlogListComponent } from './blog-list/blog-list.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ProfileComponent,
    CreateBlogComponent,
    LoginComponent,
    BlogBlockComponent,
    BlogListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [
    AuthService,
    CookieService,
    BlogService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
