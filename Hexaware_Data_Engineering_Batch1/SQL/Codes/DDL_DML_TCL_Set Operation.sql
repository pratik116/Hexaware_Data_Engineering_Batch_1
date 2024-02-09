--create database
create database DataEngB1;

--use database
use DataEngB1;

--create table
create table students(
name varchar(50) not null,
Id int primary key,
Email varchar(50),
City varchar(30)
);

--show tables
select table_name
from information_schema.tables;


--select 
select * from students;
select Id, name from students;

--insert 
insert into students (name,Id,Email,City) values
('Amit Patel',1,'amit.patel@email.com','Mumbai'),
('Priya Sharma',2,'priyasharma@email.com','Delhi'),
('Raj Singh',3,'raj.singh@email.com','Jaipur'),
('Neha Gupta',4,'neha.gupta@email.com','Bangalore'),
('Aniket Verma',5,'aniket.verma@email.com','Hyderabad');

select * from students;

--select with distinct 
--Here i will add the record having name Amit Patel

insert into students (name,Id,Email,City) values
('Amit Patel',6,'amit.patel2@email.com','Nashik');

select distinct name from students; -- Because of distict we get only one result of Raj Singh

--Alter table
alter table students add salary int;

alter table students drop column salary;

alter table students add salary int;

--rename table name

exec sp_rename 'students','student_info';

--update data
update student_info
set salary=50000;

select * from student_info;

-- delete specific row using where clause
delete from student_info where id=6;

select * from student_info;

--inserting more records
insert into student_info (name,Id,Email,City,salary) values
('Sara Khan',6,'sara.khan@email.com','Mumbai',50000),
('Vikram Sharma',7,'vikram.sharma@email.com','Delhi',50000),
('Preeti Singh',8,'preeti.singh@email.com','Jaipur',50000),
('Amit Joshi',9,'amit.joshi@email.com','Bangalore',50000),
('Divya Verma',10,'divya.verma@email.com','Hyderabad',50000);

insert into student_info (name,Id,Email,City,salary) values
('Samira Khan',11,'samira.khan@email.com','Mumbai',20000),
('Vikram jagtap',12,'vikram.jagtap@email.com','Nashik',80000);

select * from student_info;

--group by having and order by clause

select city, sum(salary) as citywise_total_salary from student_info 
group by city having sum(salary)>90000 order by citywise_total_salary;

--begin transaction and commit 
begin transaction;

insert into student_info (name,Id,Email,City,salary) values
('Pratik Wani',13,'pratik.wani@gmail.com','Nashik',50000);

commit;

--rollback
begin transaction;
delete from student_info where id=13;

rollback;
commit;

select * from student_info;

--savepoint 

begin transaction;

delete from student_info where id=13;
save transaction sp1;

delete from student_info where id=12;
save transaction sp2;

delete from student_info where id=11;
save transaction sp3;

rollback transaction sp1;--here now the changes occured after sp1 will undo back

select * from student_info;

-- Set Operations
--union

select * from student_info where id between 1 and 5 -- gives record for id's 1 to 5
union
select * from student_info where id between 3 and 7-- gives record for id's 3 to 7

--because of using union it will add both results and it will add the repeated rows ONLY ONCE

--intersection

select * from student_info where id between 1 and 5 -- gives record for id's 1 to 5
intersect
select * from student_info where id between 3 and 7-- gives record for id's 3 to 7

--because of using intersect it will select only the repeated rows


--union all

select * from student_info where id between 1 and 5 -- gives record for id's 1 to 5
union all
select * from student_info where id between 3 and 7-- gives record for id's 3 to 7

--because of using union all it will add both results and it will not remove the repeated rows 

--except (minus)

select * from student_info where id between 1 and 5 -- gives record for id's 1 to 5
except
select * from student_info where id between 3 and 7-- gives record for id's 3 to 7

--It displays the rows which are present in the first query but 
--absent in the second query with no duplicates.


-- Logical Operators in SQL

--1) operator
select * from student_info where id in(1,2,11,78);

--between operator
select * from student_info where salary between 45000 and 60000;

--like
select name from student_info where name like '%A';--ends with A

--not like
select name from student_info where name not like '%A%';--not contains A 

--or 
select * from student_info where id=10 or id=1;

--all
select * from student_info where name=all
(select name from student_info)

--any
select * from student_info where name=any
(select name from student_info)

--exists
select * from student_info where exists
(select name from student_info where id=100);--return nothing as subquery return none

select * from student_info where exists
(select name from student_info where id=11)--return whole table as subquery result is not empty

--some
select * from student_info where id<some(select id from student_info where city='Delhi');


--Here will add another table having cid, coursename 
--will add another column in student table as c_id which will be fk

create table course_info(
c_id int primary key,
c_name varchar(50) not null
);

--inserting dummy values
insert into course_info (c_id,c_name) VALUES
(1,'Mathematics'),
(2,'Physics'),
(3,'Computer Science'),
(4,'History'),
(5,'English');

--adding new column to student_info
alter table student_info
add course_id int references course_info(c_id);

--adding values 
update student_info 
set course_id=5 where id in (11,12);

--Joins
select * from student_info 
inner join course_info on
student_info.course_id=course_info.c_id;

--join with group by and having
select student_info.city,sum(salary) as total_sal_by_city from student_info 
inner join course_info on
student_info.course_id=course_info.c_id
group by student_info.city 
having sum(salary)>45000;

--Index
create index course_name ON student_info(name);

