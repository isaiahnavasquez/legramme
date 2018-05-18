export class Blog {
  id: number;
  title: string;
  content: string;
  pub_date: string;
  category: number;
  author: number;
  cover_photo: string;
  user: string;
}

export class User {
  id: number;
  username: string;
  first_name: string;
  blogs: number[];
}

export class Profile {
  user_id: number;
  default_pic: string;
  about: string;
}
