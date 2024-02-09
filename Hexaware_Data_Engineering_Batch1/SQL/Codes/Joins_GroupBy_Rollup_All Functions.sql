
----Assignment 4

use practice;
-- Create the Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    Unit NVARCHAR(50),
    Price DECIMAL(10, 2)
);

-- Insert data into the Products table
INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES
(1, 'Chais', 1, 1, '10 boxes x 20 bags', 18),
(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19),
(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10),
(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22),
(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35),
(6, 'Grandma''s Boysenberry Spread', 3, 2, '12 - 8 oz jars', 25),
(7, 'Uncle Bob''s Organic Dried Pears', 3, 7, '12 - 1 lb pkgs.', 30),
(8, 'Northwoods Cranberry Sauce', 3, 2, '12 - 12 oz jars', 40),
(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97);



-- Create the OrderDetails table
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT references products(productid),
    Quantity INT
);


-- Insert data into the OrderDetails table
INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
VALUES
(1, 10248, 1, 12),
(2, 10248, 9, 10),
(3, 10248, 7, 5),
(4, 10249, 6, 9),
(5, 10249, 5, 40),
(6, 10250, 4, 10),
(7, 10250, 5, 35),
(8, 10250, 6, 15),
(9, 10251, 2, 6),
(10, 10251, 7, 15);

select * from Products;
select * from OrderDetails;

--Exists
SELECT ProductName FROM Products
WHERE exists (SELECT ProductID FROM OrderDetails WHERE Quantity=15);

--Any
--1)
SELECT ProductName, productid
FROM Products WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity=15);

 --2)
SELECT ProductName, ProductID
FROM Products
WHERE ProductID=ANY(SELECT ProductID FROM OrderDetails WHERE Quantity>12);

--3)
SELECT ProductName
FROM Products
WHERE ProductID=ANY(SELECT ProductID FROM OrderDetails WHERE Quantity > 1000);

--All
SELECT ProductName
FROM Products
WHERE ProductID=ALL(SELECT ProductID FROM OrderDetails WHERE Quantity>0);

--group by 
select  products.CategoryID,count(*) total_cat from products inner join
orderdetails on products.ProductID=orderdetails.ProductID
group by products.CategoryID 

--group by having
select  products.CategoryID,count(*) total_cat from products inner join
orderdetails on products.ProductID=orderdetails.ProductID
group by products.CategoryID 
having count(*)>1

--joins

--1)Inner Join

select products.*,orderdetails.* from products inner join
orderdetails on products.ProductID=orderdetails.ProductID;


--2)Left join

select products.*,orderdetails.* from products left join
orderdetails on products.ProductID=orderdetails.ProductID;


--3)Right Join

select products.*,orderdetails.* from products right join
orderdetails on products.ProductID=orderdetails.ProductID;


--4)Full Join

select products.*,orderdetails.* from products full join
orderdetails on products.ProductID=orderdetails.ProductID;

--5)Cross Join

select products.*,orderdetails.* from products cross join
orderdetails;

--6) Equi Join

select products.*,orderdetails.* from products,orderdetails where
products.ProductID=orderdetails.ProductID;

--or

select products.*,orderdetails.* from products join orderdetails
on products.ProductID=orderdetails.ProductID;


--7)Non-Equi Join:

select products.*,orderdetails.* from products join orderdetails
on products.ProductID > orderdetails.ProductID;


--  Aggregate function:-

--sum
select sum(quantity) total_ordered_products from OrderDetails

--count
select CategoryID,count(*) as total_product 
from products group by CategoryID;

--average
select avg(price) Avg_Price from products;

--Max and Min
select max(price) max_Price, min(price) min_price from products;

--string functions:-

--Ascii
select ProductName, ascii(ProductName) asciiValue from products;

--char
select char(65) as char;


--len
select productname, len(productname) length from products;

--Lower and Upper

select Productname, Lower(ProductName) as Lowercase, Upper(ProductName) as  Uppercase 
from products;

--reverse
select reverse(productname) ReverseNames from products;

--convert to str
select str(price) as stringvalues from products;



-- Date Functions:
--Getdate
select getdate() as curr_date;

--dateadd
select dateadd(mm,2,getdate()) as After_2_Months;

--datediff
select datediff(year,'2002-03-10',getdate()) Age;


--datepart
select datepart(mm,'2002-03-10') BirthMonth;
select datepart(year,'2002-03-10') BirthYear;

-- day, month, year
select day ('2002-03-10') BirthDay;
select month ('2002-03-10') BirthMonth;
select year ('2002-03-10') BirthYear;


--Mathematical Functions
--ABS
select abs(-101) as Absolute_value;

--sin
select sin(90) angle_in_radian;

--ceiling
select ceiling(price) ceil_price from products;

--floor
select floor(price) floor_price from products;

--round
select round(price,1) round_price from products;

--exp
select exp(Price) Exponential_values from products;

--log
select log(Price) log_values from products;

--nested subquery

select productname, productID from products 
where productID in (select productID from orderdetails where price 
in(select price from orderdetails where OrderID>5));


--Assignment 4 // Hands on exercises

--1) Filter Data based on Aggregated Results using Group By and Having

select  products.CategoryID,count(*) total_cat 
from products inner join orderdetails 
on products.ProductID=orderdetails.ProductID
group by products.CategoryID 
having count(*)>1 
order by products.CategoryID desc;
--Aggregate function used: Count

select  products.CategoryID,sum(products.price) categorywise_total_price 
from products inner join orderdetails 
on products.ProductID=orderdetails.ProductID
group by products.CategoryID 
having count(*)>0
order by categorywise_total_price;


--2) Filtering Data using SQL Queries

select ProductID, Productname from products;

select CategoryId, Price from products;

select OrderID from orderdetails


--3) Total Aggregations using SQL Queries

--sum
select sum(quantity) total_ordered_products from OrderDetails

--count
select CategoryID,count(*) as total_product 
from products group by CategoryID;

--average
select avg(price) Avg_Price from products;

--Max and Min
select max(price) max_Price, min(price) min_price from products;



--4) Order of Execution of SQL Queries

select  products.CategoryID,count(*) total_cat 
from products inner join orderdetails 
on products.ProductID=orderdetails.ProductID
where OrderDetails.Quantity>5
group by products.CategoryID 
having count(*)>1 
order by products.CategoryID desc;





--5) Rules and Restrictions to Group and Filter Data in SQL queries

select  
	products.CategoryID,
	count(*) as count,
	sum(products.price) categorywise_total_price 
from products inner join orderdetails 
on products.ProductID=orderdetails.ProductID
group by products.CategoryID 
having count(*)>0
order by categorywise_total_price;

select 