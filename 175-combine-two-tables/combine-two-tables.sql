# Write your MySQL query statement below
select 
    firstName,
    lastName,
    Address.city,
    Address.state
FROM Person 
LEFT JOIN Address
ON Person.personId = Address.personId;