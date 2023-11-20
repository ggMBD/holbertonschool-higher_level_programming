# SQL - Introduction


## Database Fundamentals

### Introduction

Databases are an essential component of modern applications, providing a structured and organized way to store, manage, and retrieve data. This guide provides a brief overview of database concepts and introduces MySQL, a popular open-source relational database management system (RDBMS).

### What is a Database?

A database is a structured collection of data organized to be easily accessed, managed, and updated. It is essentially a repository of information designed to store, retrieve, and manage data efficiently. Databases are commonly used in various applications, including business, finance, healthcare, and education.

### Relational Databases

A relational database is a type of database that organizes data into tables, each with rows and columns. Each row represents a unique record, and each column represents a specific attribute of that record. Tables are linked together through relationships, allowing for efficient data retrieval and manipulation.

### SQL: Structured Query Language

SQL (Structured Query Language) is the standard language used to interact with databases. SQL commands allow users to create, read, update, and delete (CRUD) data within a database.

### MySQL: An Open-Source RDBMS

MySQL is a popular open-source RDBMS widely used for web applications, e-commerce platforms, and data warehousing. It is known for its ease of use, reliability, and scalability.

### Creating a Database in MySQL

To create a database in MySQL, use the following SQL statement:

```sql
CREATE DATABASE database_name;
```

Replace `database_name` with the desired name of your database.

### Data Definition Language (DDL) and Data Manipulation Language (DML)

DDL and DML are two subsets of SQL used for different purposes:

* **DDL (Data Definition Language):** Defines the structure of a database, including creating, modifying, or deleting tables and indexes.

* **DML (Data Manipulation Language):** Manipulates data within a database, including inserting, updating, or deleting records.

### Creating or Altering a Table

To create a table in MySQL, use the following SQL statement:

```sql
CREATE TABLE table_name (
    column1_name data_type,
    column2_name data_type,
    ...
);
```

Replace `table_name` with the desired name of your table, and add columns with their respective data types. To modify an existing table, use the `ALTER TABLE` statement.

### Selecting Data from a Table

To select data from a table in MySQL, use the following SQL statement:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Replace `column1`, `column2`, ... with the columns you want to select, `table_name` with the table name, and `condition` with a filter expression.

### Inserting, Updating, or Deleting Data

To insert data into a table in MySQL, use the `INSERT INTO` statement. To update data in a table, use the `UPDATE` statement. To delete data from a table, use the `DELETE FROM` statement.

### Subqueries

Subqueries are nested SELECT statements that allow you to query data from within another query. They are useful for complex data retrieval and aggregation.

### MySQL Functions

MySQL provides a variety of built-in functions for manipulating data and performing calculations. Some common functions include:

* `AVG()` - Calculates the average of a set of values
* `COUNT()` - Counts the number of rows in a table
* `MAX()` - Retrieves the maximum value in a set of values
* `MIN()` - Retrieves the minimum value in a set of values
* `SUM()` - Calculates the sum of a set of values

This guide provides a basic introduction to database concepts and MySQL. For more in-depth information, refer to the official MySQL documentation and online resources.
