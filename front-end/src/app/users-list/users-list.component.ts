import { Component, OnInit } from '@angular/core';
import { User, Profile } from '../data-classes';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-users-list',
  templateUrl: './users-list.component.html',
  styleUrls: ['./users-list.component.css']
})

export class UsersListComponent implements OnInit {

  users: User[] = [];

  constructor(
    private authService: AuthService,
  ) { }

  ngOnInit() {
    this.getUsers();
  }

  getUsers() {
    this.authService.getUsers().subscribe(data => {
      this.users = data.slice(0,6)
    });
  }

}
