/*
create table books (
  id int not null auto_increment,
  title varchar(255) not null,
  published_date int,
  author_id int,
  genre_id int,
  editorial_id int,
  creation_date datetime default current_timestamp,
  refresh_date datetime default current_timestamp on update current_timestamp,
  primary key (id) 
);

create table genres (
  id int not null auto_increment;
  name varchar(255) not null,
  creation_date datetime default current_timestamp,
  refresh_date datetime default current_timestamp on update current_timestamp,
  primary key (id)
);

create table authors (
    id int not null auto_increment,
    name varchar(255) not null,
    creation_date datetime default current_timestamp,
    refresh_date datetime default current_timestamp on update current_timestamp,
    primary key (id)
);

create table users (
  id int not null auto_increment,
  name varchar(255) not null,
  creation_date datetime default current_timestamp,
  refresh_date datetime default current_timestamp on update current_timestamp,
  primary key (id)
);



create table reviews (
  id int not null auto_increment,
  content text,
  book_id int,
  user_id int,
  creation_date datetime default current_timestamp,
  refresh_date datetime default current_timestamp on update current_timestamp,  
  primary key (id),
  FOREIGN KEY (book_id) references books(id),
  FOREIGN KEY (user_id) references users(id)
);



insert into books (title,published_date,author_id,genre_id,editorial_id) values ("The Lord of the Rings",1954,1,2,3);
insert into authors (name) values ("J.R.R. Tolkien");
insert into genres (name) values ("Fantasy");
insert into genres (name) values ("Science Fiction");
insert into editorials (name) values ("Houghton Mifflin");
insert into editorials (name) values ("Allen & Unwin");
insert into editorials (name) values ("HarperCollins");
insert into users (name) values ("John Doe");
insert into reviews (content,book_id,user_id) values ("A fantastic read!",1,1);

select 
    b.id as 'Book ID',
    b.title as 'Book Name',
    a.name as 'Author Name',
    g.name as 'Genre',
    r.content as 'Review Text',
    u.name as 'Review User'
from
    books b 
join authors a on b.author_id = a.id
join genres g on b.genre_id = g.id
join reviews r on b.id = r.book_id
join users u on r.user_id = u.id;



select 
    b.id as 'Book ID',
    b.title as 'Book Name',
    a.name as 'Author Name',
    g.name as 'Genre',
    r.content as 'Review Text',
    u.name as 'Review User'
from
    books b 
join authors a on b.author_id = a.id
join genres g on b.genre_id = g.id
join reviews r on b.id = r.book_id
join users u on r.user_id = u.id;


SELECT * FROM books WHERE id = 1;
SELECT * FROM authors WHERE id = 1;
SELECT * FROM genres  WHERE id = 1;
SELECT * FROM editorials WHERE id = 1;
SELECT * FROM reviews WHERE id = 1;
SELECT * FROM users WHERE id = 1;
*/



