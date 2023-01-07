# ORM
**ORM** stands for Object Relational Mapper. The main goal of ORM is to send data between a database and models in an application. 
It maps a relation between the database and a model. So, ORM maps object attributes to fields of a table.
The main advantage of using ORM is that it makes the entire development process fast and error-free. Essentially, it eliminates the need to write SQL code.

# Advantages of ORM
ORMs have some benefits over the traditional approach. The main advantage is that it is easier to change the database if needed when ORMs are used. Some of the other advantages are that it provides rapid development and makes project more portable.

SQL differs significantly in different databases which created a problem for developers. Since SQL is used to create classes and objects needed for data interpretation, working with huge amounts of data with varied SQL for various databases proved to be difficult for developers. To overcome the problem of hard-coding database entries, the concept of ORM was developed.

ORMs automatically create a database from defined models or scheme which meant that the developer need not have knowledge of the SQL used in the database.

# Django ORM
Django is equipped with an ORM which is one of the best ORMs available in the industry today. It is tightly coupled with the Django framework and is very efficient. Django’s ORM is best known for its ability to handle medium to low complexity queries and medium to huge datasets. Migrations are another useful feature of Django ORM.

Another famous database toolkit that is popularly used in place of Django’s ORM is SQLAlchemy. It is preferred to Django ORM for many problem statements. Although, it is the developer’s choice to choose SQLAlchemy or Django ORM. Django ORM tends to produce larger and complex queries when unnecessary at times which can cause the performance to decrease.

The main usage of a database is to store and retrieve data whenever necessary. Django ORM uses Querysets to achieve this functionality. Queryset is a list of objects present in a model. We can use Querysets to filter, arrange and manage our data. The main purpose of these is to make query retrieval faster and easier.

# Relationship between fields of tables
Abstraction is a major concern when working with data, Django ORM provides a level of abstraction that is easy to work with. ORM will relate the object’s attributes to the corresponding table fields automatically. The relationship between the fields of different models in the database are as follows.

There are 3 kinds of relationships between fields of tables.

     **One to one** − here, there exists a one-to-one relationship between two tables. For each row in table1, there exists a row in table2.

     **One to many** − here, there exists a one-to-many relationship between two tables. For each row in table1, there could be many rows in table2.

     **Many to many** − In this relationship, for one id, there could be multiple rows in two tables.

These relationships represent the ways in which fields of different tables can be linked to each other.
