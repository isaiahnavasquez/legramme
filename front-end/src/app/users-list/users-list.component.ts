import { Component, OnInit } from '@angular/core';
import { User } from '../data-classes';
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
      console.log(data);
    });
  }

}
