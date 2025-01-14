3.
create table user(
id int comment '编号',
name varchar(50) comment '姓名',
age int comment '年龄',
sex varchar(1) comment '性别',
phone char(13) comment '联系方式'
)comment '用户表';

insert into user (id,name,sex,age,phone)
values (1,'柳岩','女',20,'12345678901'),
       (2,'张无忌','男',18,'12345678123'),
       (3,'韦一笑','男',38,'12345897123'),
       (4,'赵敏','女',18,'12347574573'),
       (5,'小昭','女',16,'12567690123'),
       (6,'杨逍','男',28,'12567893127'),
       (7,'范瑶','男',40,'12367892126');

4.
select * from user
where age between 20 and 30;

5.
delete from user where name like N'%张%';

6.
select avg(age) from user;

7.
select * from user where name like N'%张%' and age between 20 and 30 order by age desc;

8.
create table team(
id int,
teanName char(50)
);

create table score(
id int,
teamid int,
userid int,
score int
);

alter table team
add primary key(id);
alter table score
add foreign key(teamid)
references team(id);

alter table user
add primary key(id);
alter table score
add foreign key(userid)
references user(id);

9.
select user.id
from score st s join team st t on s.teamid = t.teamName 
join user st u on u.id = s.userid 
where t.teamName = N'ECNU' and u.age<20;

10.
select sum(ifnull{score,0}) as sumscore
from score join team on team.teamName = score.teamid
where teamName = N'ECNU';