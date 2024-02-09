use SQL_coding_challange;

create table Sales (
    Region varchar(50),
    Product char(50),
    SalesAmount int
);

-- Insert some sample data
insert into Sales values('North','Electrical',400);
insert into Sales values('North','Mechanical',1200);
insert into Sales values('South','Electrical',800);
insert into Sales values('South','Mechanical',1700);
insert into Sales values('East','Electrical',900);
insert into Sales values('East','Mechanical',2000);


--OVER and PARTITION BY Clause in SQL Queries

select Region, Product, SalesAmount,
Rank() over(partition by Region order by SalesAmount) Rank
from sales;




--Creating Subtotals

select Region, Product,
		sum(SalesAmount) as total	
from sales
Group by 
	Rollup(Region,Product);



--Total Aggregations using SQL Queries. 

select
    Region,
    Product,
    SalesAmount,
    sum(salesamount) OVER () grand_sum
from
    Sales;







--2)
select
    Region,
    Product,
    SalesAmount,
    sum(salesamount) OVER (partition by region) as sum_regionwise
from
    Sales;