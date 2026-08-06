# Most Asked SQL Interview Questions

30 questions across the 6 topics that come up most often. 5 per topic.

## Joins

1. What's the difference between INNER JOIN and LEFT JOIN, and what happens to unmatched rows on the right table in a LEFT JOIN?
2. Write a query to find duplicate rows in a table using a self-join.
3. What's the difference between UNION and UNION ALL?
4. Can you join on a condition that isn't equality? Give an example.
5. How would you find rows in Table A that don't exist in Table B?

## Window Functions

1. What's the difference between RANK, DENSE_RANK, and ROW_NUMBER?
2. Write a query to find the top 3 highest-paid employees in each department.
3. What does PARTITION BY do, and how is it different from GROUP BY?
4. How would you calculate a running total using a window function?
5. What's LAG and LEAD used for? Give a real use case.

## GROUP BY and HAVING

1. Why can't you filter on an aggregate function using WHERE?
2. Write a query to find departments with more than 10 employees.
3. Can you use HAVING without GROUP BY? What happens?
4. What's the execution order of SELECT, WHERE, GROUP BY, HAVING?
5. How do you count distinct values within a group?

## Subqueries vs CTEs

1. When would you use a CTE instead of a subquery?
2. What's a correlated subquery? Give an example.
3. Can a CTE reference itself? What's that called?
4. Write a query using a CTE to find the second-highest salary.
5. What's the difference between a subquery in WHERE vs a subquery in FROM?

## Indexing

1. Why would a query be slow without an index, and how does an index fix it?
2. What's the difference between a clustered and non-clustered index?
3. Can too many indexes hurt performance? How?
4. What is a composite index, and when should you use one?
5. How would you check if a query is actually using an index?

## Normalization

1. What's the difference between 1NF, 2NF, and 3NF?
2. Given a messy table with repeating columns, how would you normalize it to 1NF?
3. What's a transitive dependency, and how does 3NF eliminate it?
4. When would you deliberately denormalize a table?
5. What's the difference between normalization and indexing? (People often mix these up.)
