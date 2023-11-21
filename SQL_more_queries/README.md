# MySQL User Management and Data Retrieval Techniques

## Creating a New MySQL User

To create a new MySQL user, utilize the `CREATE USER` statement:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

Replace `username` with the desired username, `localhost` with the host from which the user will connect, and `password` with the desired password.

## Managing User Privileges

To grant privileges to a MySQL user, employ the `GRANT` statement. For instance, to grant all privileges on a database named `mydatabase` to a user named `myuser`, use the following SQL statement:

```sql
GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
```

## Understanding PRIMARY KEY and FOREIGN KEY Constraints

* **PRIMARY KEY:** A PRIMARY KEY is a unique identifier for a table in a relational database. It ensures that each row in the table has a unique value for the specified column(s).

* **FOREIGN KEY:** A FOREIGN KEY is a column or set of columns in one table that references the PRIMARY KEY of another table. It creates a relationship between the two tables, ensuring that the values in the FOREIGN KEY column(s) exist in the referenced table's PRIMARY KEY.

## Utilizing NOT NULL and UNIQUE Constraints

* **NOT NULL:** The NOT NULL constraint ensures that a column cannot contain null values. This constraint guarantees that data in the column is always present.

* **UNIQUE:** The UNIQUE constraint ensures that no two rows in a table have the same value for the specified column(s). This constraint prevents duplicate records from being inserted into the table.

## Retrieving Data from Multiple Tables with JOIN Operations

To retrieve data from multiple tables in a single query, employ JOIN operations. JOINs combine rows from two or more tables based on a related column between them. Common JOIN types include:

* **INNER JOIN:** Returns rows that have matching values in both tables.

* **LEFT JOIN:** Returns all rows from the left table and matching rows from the right table.

* **RIGHT JOIN:** Returns all rows from the right table and matching rows from the left table.

## Understanding Subqueries and Their Applications

Subqueries are nested SELECT statements that allow you to query data from within another query. They can be used to filter, aggregate, or transform data before it is returned by the main query.

## Distinguishing JOIN and UNION Operations

* **JOIN:** JOIN operations combine rows from two or more tables based on a related column between them. They are used to retrieve data from multiple tables in a single query.

* **UNION:** UNION operations combine the results of two or more SELECT statements. They are used to combine data from different sources or to remove duplicates when combining results.