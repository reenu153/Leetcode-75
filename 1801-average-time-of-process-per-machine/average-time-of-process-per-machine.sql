# Write your MySQL query statement below

select A1.machine_id,ROUND(AVG(ABS(A2.timestamp-A1.timestamp)),3)as processing_time from Activity A1, Activity A2 
where A1.activity_type='start' and A2.activity_type='end'
and A1.process_id = A2.process_id and A1.machine_id=A2.machine_id
group by A1.machine_id 