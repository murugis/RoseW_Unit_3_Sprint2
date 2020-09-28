### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

1. In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

The type of relationship that exists between the `Employee` and `Territory` is * One to many*
This means that an employee can have more than one territory.

2.What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?

It will be suitable when we are retrieving high volumes of data. This because it is flexible, performs better. in addition it is easy to scale.

MongoDB will not be suitable when we want to connect different tables using the primary and foreign key. This is because MongoDb is not ACID compliant as the data is put in one collection and retrival is dificult as it is not structured. 

3.What is "NewSQL", and what is it trying to achieve?
It is a relational database management system.

it is trying to  provide scalbility of NoSQL. additionally, it provides structured language that will help work efficiently and effectively in NoSQL database as in the structured SQL databases while it complies with ACID.