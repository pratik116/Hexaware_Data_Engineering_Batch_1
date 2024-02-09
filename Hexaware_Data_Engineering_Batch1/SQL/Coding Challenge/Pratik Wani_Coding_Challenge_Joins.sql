create database SQL_coding_challange;
use SQL_coding_challange;

create table Student (
    student_id int PRIMARY KEY,
    student_name varchar(50),
    age int,
    course_id int,
	city varchar(50),
    constraint fk_course foreign key (course_id) references Course(course_id)
);
create table Course (
    course_id int PRIMARY KEY,
    course_name varchar(50)
);

insert into Course(course_id,course_name)
values
    (1,'Mathematics'),
    (2,'History'),
    (3,'Science'),
    (4,'English'),
    (5,'Computer Science'),
    (6,'Physics'),
    (7,'Chemistry'),
    (8,'Biology'),
    (9,'Geography'),
    (10,'Economics'),
	(11,'Information Technology');

insert into Student (student_id,student_name,age,course_id,city)
values
    (1,'Pratik',20,1,'Nashik'),
    (2,'Aditya',22,2,'Pune'),
    (3,'Neha',21,3,'Mumbai'),
    (4,'Riya',19,4,'Kolkata'),
    (5,'Aarav',23,5,'Chennai'),
    (6,'Ishaan',20,6,'Nagpur'),
    (7,'Kavya',22,7,'Banglor'),
    (8,'Arjun',21,8,'Bhopal'),
    (9,'Pooja',19,9,'Surat'),
    (10,'Aanya',23,10,'Ayodya'),
    (11,'Rahul',22,1,'jhanshi'),
    (12,'Ananya',20,2,'Varanasi'),
    (13,'Vivek',21,3,'Kashi'),
    (14,'Sanya',19,4,'Mathura'),
    (15,'Yashika',23,5,'Dhule'),
    (16,'Rohit',20,6,'Jalgaon'),
    (17,'Meera',22,7,'Vizapur'),
    (18,'Aryan',21,8,'Latur'),
    (19,'Priya',19,9,'Sambhajinagar'),
    (20,'Varun',23,10,'Thane'),
	(21,'Shyam',20,1,'Jabalpur');

	
--Inner Join 
select student.*,course.* 
from student inner join course
on student.course_id=course.course_id;








--Left Join

select student.*,course.*
from  student right join  course
on student.course_id=course.course_id;




--full join
select student.*,course.* 
from student full join course
on student.course_id=course.course_id;



--cross
select student.*,course.* 
from student cross join course ;



--Equi join

select student.*,course.* 
from student,course
where student.course_id=course.course_id;




--Non-equi join

select student.*,course.* 
from student,course
where student.course_id>course.course_id;