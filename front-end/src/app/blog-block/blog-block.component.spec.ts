import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogBlockComponent } from './blog-block.component';

describe('BlogBlockComponent', () => {
  let component: BlogBlockComponent;
  let fixture: ComponentFixture<BlogBlockComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BlogBlockComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BlogBlockComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
