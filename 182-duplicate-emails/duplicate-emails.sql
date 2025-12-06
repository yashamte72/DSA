# Write your MySQL query statement below
select email
From Person
group by email
having count(*) > 1;