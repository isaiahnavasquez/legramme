import { Component, OnInit, Input } from '@angular/core';
import { User } from '../data-classes';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-user-block',
  templateUrl: './user-block.component.html',
  styleUrls: ['./user-block.component.css']
})
export class UserBlockComponent implements OnInit {

  @Input() user: User;
  about: string = ''

  constructor(
    private authService: AuthService,
  ) { }

  ngOnInit() {
    this.initializeData();
  }
  
  initializeData() {
    this.authService.getProfile(this.user.id).subscribe(data => {
      this.about = data['about']
    })
  }

}
