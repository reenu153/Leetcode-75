# Write your MySQL query statement below

select w1.id from Weather W1, Weather W2 
where  DATEDIFF(W1.recordDate,W2.recordDate)=1 and w1.temperature>w2.temperature