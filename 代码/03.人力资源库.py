DROP DATABASE IF EXISTS HRS;
CREATE DATABASE HRS DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

USE HRS;

CREATE TABLE TbDept 
( 
dno INT NOT NULL COMMENT '部门编号', 
dname VARCHAR ( 10 ) NOT NULL COMMENT '部门名称', 
dloc VARCHAR ( 20 ) NOT NULL COMMENT '部门所在地'
);

ALTER TABLE TbDept ADD CONSTRAINT Pk_Dept PRIMARY KEY ( dno );

INSERT INTO TbDept ( dno, dname, dloc )
VALUES
	( 10, '会计部', '北京' ),
	( 20, '研发部', '成都' ),
	( 30, '销售部', '重庆' ),
	( 40, '运维部', '深圳' );

CREATE TABLE TbEmp 
(
eno INT NOT NULL COMMENT '员工编号',
ename VARCHAR ( 20 ) NOT NULL COMMENT '员工姓名',
job VARCHAR ( 10 ) NOT NULL COMMENT '职位',
mgr INT COMMENT '直接主管编号',
sal INT NOT NULL COMMENT '月薪',
comm INT COMMENT '月补贴',
dno INT NOT NULL COMMENT '所属部门编号' 
);

ALTER TABLE TbEmp ADD CONSTRAINT Pk_Emp_Eno PRIMARY KEY ( eno );
ALTER TABLE TbEmp ADD CONSTRAINT Fk_Emp_Dno FOREIGN KEY ( dno ) REFERENCES TbDept ( dno );

INSERT INTO TbEmp ( eno, ename, job, mgr, sal, comm, dno )
VALUES
	( 7800, '张三丰', '总裁', NULL, 9000, 1800, 20 ),
	( 2056, '乔峰', '分析师', 7800, 5000, 2000, 20 ),
	( 3088, '李莫愁', '设计师', 2056, 3500, NULL, 20 ),
	( 3211, '张无忌', '程序员', 2056, 3200, NULL, 20 ),
	( 3233, '丘处机', '程序员', 2056, 3400, 800, 20 ),
	( 3251, '张翠山', '程序员', 2056, 4000, NULL, 20 ),
	( 5566, '宋远桥', '会计师', 7800, 4000, 1500, 10 ),
	( 5234, '郭靖', '出纳', 5566, 2000, 200, 10 ),
	( 3344, '黄蓉', '销售主管', 7800, 3000, 2500, 30 ),
	( 1359, '胡一刀', '销售员', 3344, 1800, NULL, 30 ),
	( 4466, '苗人凤', '销售员', 3344, 2500, NULL, 30 ),
	( 3244, '欧阳锋', '程序员', 3088, 3200, NULL, 20 ),
	( 3577, '杨过', '会计', 5566, 2200, NULL, 10 ),
	( 3588, '朱九真', '会计', 5566, 2500, NULL, 10 );
	
	
-- (1)查询月薪最高的员工姓名和工资
select ename, sal from TbEmp
where sal=(select max(sal) from TbEmp);


-- (2)查询员工的姓名和年薪((月薪+补贴)*13)
select ename as 姓名, (sal+ifnull(comm,0))*13 as 年薪
from TbEmp;


-- (3)查询有员工的部门编号和人数
select dno, count(dno) from TbEmp
group by dno;


-- (4)查询所有部门的名称和人数
select dname, ifnull(total, 0) from TbEmp t1
left outer join (select dno, count(dno) as total
from TbEmp group by dno) t2
on t1.dno=t2.dno;


-- (5)查询薪资最高的员工(Boss除外)的姓名和工资
select ename, sal from TbEmp
where sal=(select max(sal) from TbEmp where mgr is not null);


-- (6)查询薪水超过平均薪水的员工的姓名和工资
select ename, sal from TbEmp
where sal>(select avg(sal) from TbEmp);


-- (7)查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
select ename, t1.dno, sal, avgsal, sal-avgsal from TbEmp t1
inner join (select dno, avg(sal) as avgsal
from TbEmp group by dno) t2
on t1.dno=t2.dno and sal>avgsal;


-- (8)查询部门中薪水最高的人姓名、工资和所在部门名称
select ename, sal, dname from tbemp t1
(select dno, max(sal) as maxsal
from tbemp group by dno) temp


-- (9)查询主管的姓名和职位



-- 尽量避免使用distinct和in运算
-- 我们可以通过exists或者not exists来取代去重和集合运算

-- (10)查询薪资排名4~6名的员工姓名和工资
-- 分页查询
select ename, sal from TbEmp
order by sal desc limit 3;
select ename, sal from TbEmp
order by sal desc limit 3 offset 3;
select ename, sal from TbEmp
order by sal desc limit 10,10;



drop user 'hanbo'@'%'  删除用户
create user 'hanbo'@'%' identified by '123123';   创建用户
grant all privileges on *.* to 'hanbo'@'%';   授予所有权限
-- grant all privileges on HRS.* to 'hanbo'@'%';   仅授予HRS数据库权限
revoke insert, delete on HRS.* from 'hanbo'@'%';  除了insert, delete权限