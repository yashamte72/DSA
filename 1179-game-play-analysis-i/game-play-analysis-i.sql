# Write your MySQL query statement below
SELECT 
    player_id, 
    min(event_date) as first_login
From Activity
GROUP BY player_id