### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is an open source object relational database management system (ORDBMS)that holds data in tables and manages relationships between those tables.

- What is the difference between SQL and PostgreSQL?
  SQL is the programming language used for managing data in a relational database 
  management system (RDBMS). 

- In `psql`, how do you connect to a database?
  In the command line type the following command:
  psql database_name

- What is the difference between `HAVING` and `WHERE`?
  `WHERE` filters the records of a table based on a specific condition.`HAVING` is 
  used to filter the records in a group based on a specific condition.  

- What is the difference between an `INNER` and `OUTER` join?
  `INNER` join only keeps information that is common to both tables. `OUTER` join
  also keeps information that's not common based on the specific type of `OUTER`
  join. 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
`LEFT OUTER` combines all of the rows from left table and matching rows from the right table. `RIGHT OUTER` combines the matching rows from the first table and all of the rows from the right table. 

- What is an ORM? What do they do?
ORM or Object relational mapping lets you query and manipulate a database using object oriented techniques. SQLAlchemy is an example of an ORM library. 

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
Making server side requests can help avoid CORS issues in the browser. Also if the API we use requires a password, people will know what the password is by reading the JS. It is also easier for the server to store/process the data. However, client side requests can be faster. 

- What is CSRF? What is the purpose of the CSRF token?
CSRF is a security vulnerability in which unauthorized commands are submitted by a user that the browser trusts. CSRF is a secure random token used to prevent CSRF attacks.  

- What is the purpose of `form.hidden_tag()`?
It is used to create the hidden field that includes the CSRF token and protects the forms from CSRF attacks. 