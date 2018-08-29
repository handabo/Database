-- 创建school数据库并指定默认的字符集
drop database if exists school; 
create database school default charset utf8;

-- 切换到school数据库
use school;

-- 创建学生表
-- 学生的学号是主键(primary key)
create table tb_student
(
stuid int not null,
stuname varchar(20) not null,
stusex bit default 1,
stubirth date,
primary key (stuid)
);

-- 删除学生表
-- drop table tb_student;

-- 修改学生表
alter table tb_student add column stuaddr varchar(100);
alter table tb_student drop column stubirth;

-- 插入学生记录
insert into tb_student values (1001, '骆昊', 1, '四川成都');
insert into tb_student (stuid, stuname) values (1002, '王大锤');
insert into tb_student values 
(1003, '白元芳', default, null),
(1004, '白洁', 0, '湖北武汉'),
(1005, '狄仁杰', 1, '山西大同'),
(1006, '武则天', 0, '四川广元'),
(1007, '冷面', 1, '广东东莞');

-- 删除学生记录
delete from tb_student where stuid=1007;
delete from tb_student where stuid=1007 or stuid=1009;
delete from tb_student where stuid in (1007, 1008, 1009);

-- 更新学生记录
update tb_student set stuaddr='四川成都' where stuname='白元芳';
update tb_student set stuname='王小锤', stusex=0 where stuid=1002;

-- 查询所有行所有列
select * from tb_student;

-- 投影(查询指定的列)
select stuname, stusex from tb_student;

-- 别名
select stuname as 姓名, stusex as 性别 from tb_student;
select stuname as 姓名, if(stusex, '男', '女') as 性别 from tb_student;

-- 筛选(查询指定的行)
-- 查询男学生的姓名
select stuname as 姓名 from tb_student where stusex=1;
-- 查询女学生的姓名
select stuname as 姓名 from tb_student where stusex=0;
-- 查询学号是奇数的学生的学号和姓名
select stuid 学号, stuname 姓名 from tb_student where stuid%2<>0;
-- 查询学号是1003或1005或1006的学生(集合运算)
select stuid 学号, stuname 姓名 from tb_student where stuid in (1003, 1005, 1006);
select stuid 学号, stuname 姓名 from tb_student where stuid=1003 or stuid=1005 or stuid=1006;
-- 查询学号是1003或1005或1006的女学生(and-而且)
select stuid 学号, stuname 姓名 from tb_student where stuid in (1003, 1005, 1006) and stusex=0;
-- 查询学号是在1003/1005/1006中或者是女学生(or-或者)
select stuid 学号, stuname 姓名 from tb_student where stuid in (1003, 1005, 1006) or stusex=0;
-- 查询家庭住址不是null的学生学号和姓名(处理空值)
select stuid 学号, stuname 姓名 
from tb_student 
where stuaddr is null;

SELECT
	stuid AS 学号,
	stuname AS 姓名 
FROM
	tb_student 
WHERE
	stuaddr IS NOT NULL;


select stuid, stuname 
from tb_student 
where stuid between 1003 and 1005;
-- where stubirth between '1980-1-1' and '1989-12-31';

-- 模糊查询
select stuid, stuname 
from tb_student 
where stuname like '王%';

select stuid, stuname 
from tb_student 
where stuname like '王_';

select stuid, stuname 
from tb_student 
where stuname like '王__';

select stuid, stuname 
from tb_student 
where stuname like '%王%';

select stuid, stuname 
from tb_student 
where stuname regexp '^王|白.*';

select stuid, stuname 
from tb_student 
where stuname regexp '^王|白.*'
order by stuid desc;

select stuid, stuname 
from tb_student 
where stuname regexp '^王|白.*'
order by stusex asc, stuid desc;