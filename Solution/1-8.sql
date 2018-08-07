
# 按照通过率从大到小排序

# 620 有趣的电影
select * from cinema where mod(id, 2) = 1 and description != 'boring' order by rating DESC
# 交换工资有m=男性 和 f=女性的值 。交换所有的 f 和 m 值
update salary set sex=IF(sex='m','f', 'm')


# 181 超过经理收入的员工
select E.name Employee
from Employee E
inner join Employee M
on E.ManagerId = M.Id and E.salary > M.Salary;

#  183. 从不订购的客户 not in
select Name from Customers c
where c.Id not in
(select CustomerId from Orders o);

# 626. 换座位 1和2 换，3和4换座位
select s.id , s.student from
(
select id-1 as id ,student from seat wheremod(id,2)=0
union
select id+1 as id,student from seat wheremod(id,2)=1 and id !=(select count(*) from seat)
union
select id,student from seat where mod(id,2)=1and id = (select count(*) from seat)
) s order by id;

# 178. 分数排名 有相同的分数排名rank
select Score,
(select count(distinct Score) from Scoreswhere Score >=s.Score) Rank
from Scores s order by Score DESC;


# 基础知识
# 选取众数
select sum( if (Salary>0,1,0) ) as num,Salary
from Employee  group by Salary   order by num desc  limit 1

# case when
SELECT country, 
       SUM( CASE WHEN sex = '1' THEN 
                      population ELSE 0 END),  --男性人口 
       SUM( CASE WHEN sex = '2' THEN 
                      population ELSE 0 END)   --女性人口 
FROM  Table_A 
GROUP BY country; 


# 选取中位数
select * 
from (
select t1.salary from Employee t1, Employee t2
group by t1.salary
having sum(case when t2.salary >= t1.salary then 1 else 0 end) >= count(*)/2
and sum(case when t2.salary <= t1.salary then 1 else 0 end) >= count(*)/2
)tmp
