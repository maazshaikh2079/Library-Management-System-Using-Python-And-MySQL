use lmsdb;

-- create table Library(
-- Book_ID numeric(4),
-- Book_Title varchar(30),
-- Author char(40));

-- create table Borrowed(
-- Borrower char(50),
-- Phone_No numeric(10),
-- Book_ID numeric(4),
-- Book_Title varchar(30),
-- Author char(40));

-- desc library;
-- desc borrowed;

-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1111, "The Universe Explained", "Alex Turner");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1112, "Java Programming", "John Smith");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1113, "C++ Primer", "Stanley Lippman");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1114, "Data Science for Beginners", "Amanda Brown");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1115, "Web Development 101", "Sarah Johnson");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1116, "A.I. Fundamentals", "Michael Chen");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1117, "Machine Learning Basics", "Emily Adams");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1118, "Mathematics for Programmers", "David Lee");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1119, "Chemistry Essentials", "Jennifer White");
-- INSERT INTO Library (Book_ID, Book_Title, Author) VALUES (1120, "Physics Fundamentals", "Robert Johnson");

-- insert into Borrowed(Borrower,Phone_No,Book_ID,Book_Title,Author) values("Maaz",7208613298,1121,"JS: The Good Parts","Douglas Crockford");
-- insert into Borrowed(Borrower,Phone_No,Book_ID,Book_Title,Author) values("Wahaj",9321627175,1122,"The Pragmatic Programmer","Andrew Hunt");

select * from Borrowed;
select * from LIBRARY;

-- TRUNCATE TABLE Library;
-- TRUNCATE TABLE Borrowed;
