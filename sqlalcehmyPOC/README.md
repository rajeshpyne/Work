## SQL Alchemy
Sql Alchemy is a Python toolkit and Object Relational Mapper(ORM) that allows 
app developers to use SQL for smooth and fault-tolerant transactional database
operations. The ORM translates Python classes to tables for relational databases
and automatically converts Pythonic SQLAlchemy Expression Language to SQL statements.

This conversion allows developers to write SQL queries with Python Syntax. 
SQLAlchemy also abstracts database connections and provides connection 
maintainence automatically. Together these features make SQLAlchemy a 
fantastic package for loading and querying database.

### What is Flask-SQLAlchemy?
Flask SQLAlchemy is an extension for Flask that aims for simplifying using SQLAlchemy
with Flask by providing defaults and helpers to accomplish common tasks. 
One of the most sought after helpers being handling of a database connection across the app.

However, ensuring your database connection session is available throughout your app 
can be accomplished with base SQLAlchemy and does not require Flask-SQLAlchemy.

Flask-SQLAlchemy's purpose is to handle the return of connections to prevent issues 
with worker threading. These issues arise when an app user switches from one route to another.
Below is a common error that occurs when a threading problem is present in Flask App.

```text
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 12345 and this is thread id 54321.
```

This is often caused by a session or database connection being unavailable to part of your app. 
This error effectively breaks the app and must be resolved to continue the development.