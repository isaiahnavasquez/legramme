import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

<<<<<<< HEAD
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
=======
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
import { UsersListComponent } from './users-list/users-list.component';
import { UserBlockComponent } from './user-block/user-block.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ProfileComponent,
    CreateBlogComponent,
    LoginComponent,
    BlogBlockComponent,
    BlogListComponent,
    UsersListComponent,
    UserBlockComponent
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
>>>>>>> f96c0430a0d70442f2a3069dd59bced23b3716b5
  bootstrap: [AppComponent]
})
export class AppModule { }
