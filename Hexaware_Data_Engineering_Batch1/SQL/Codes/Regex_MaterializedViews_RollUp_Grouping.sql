create database assignment_6;
use assignment_6;

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

--Total Aggregations using SQL Queries.
select
    Region,
    Product,
    SalesAmount,
    AVG(salesamount) OVER () grand_average,
	SUM(salesamount) OVER () grand_sum
from
    Sales;



--Over() and Partition by 

select Region, Product, SalesAmount,
Rank() over(partition by Region order by SalesAmount) Rank
from sales;


--Total Aggregation using OVER and PARTITION BY in SQL Queries

select
    Region,
    Product,
    SalesAmount,
    AVG(salesamount) OVER (partition by region) avg_by_region,
	SUM(salesamount) OVER (partition by product) total_by_product
from
    Sales;


--creation subtotals

select Region, Product,
		sum(SalesAmount) as total	
from sales
Group by 
	Rollup(Region, Product);


--RegExp
--regex are not directly supported in ms server
--that's why we need to use Like or Pathindex


--Gives product starting with E
select distinct Product from sales where Product like'E%';

--Gives Region ending with h
select distinct Region from sales where Region like'%h';



--Materialized view

CREATE VIEW [dbo].myindex4
WITH SCHEMABINDING
AS
SELECT Region, Product
FROM [dbo].[Sales]
GROUP BY Region, Product;

CREATE UNIQUE CLUSTERED INDEX myindex ON [dbo].myindex4 (Region, Product);

