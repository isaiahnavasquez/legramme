import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'
import { HomeComponent } from './home/home.component';
import { CreateBlogComponent } from './create-blog/create-blog.component';
import { ProfileComponent } from './profile/profile.component';
import { LoginComponent } from './login/login.component';
import { BlogListComponent } from './blog-list/blog-list.component';
import { UsersListComponent } from './users-list/users-list.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { 
    path: 'home',
    component: HomeComponent,
    children: [
      { path: 'authors', component: UsersListComponent },
      { path: 'blogs', component: BlogListComponent },
      { path: '', component: BlogListComponent }
    ]
  },
  { path: 'profile', component: ProfileComponent },
  { path: 'create-blog', component: CreateBlogComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AppRoutingModule { }
