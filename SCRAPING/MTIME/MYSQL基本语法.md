1.通过命令行连接MYSQL
命令行切换到MYSQL安装目录中的bin目录下，输入mysql -hlocalhost -uroot -p password
其中-u后输入用户名，-p后输入密码

2.显示所有数据库：show databases;

3.创建数据库：create database dbname;

4.使用数据库：use dbname;

5.查看当前使用了哪个数据库：select database();

6.删除数据库：drop database dbname;

7.查看数据库中的表：show tables;

8.查看表内所有内容：select * from tbname;

9.创建新表：create table table_name (column_name column_type);
比如 create table mtime(NAME varchar(250) PRIMARY KEY,LINK varchar(250),point int,YEAR varchar(250));

10.更改字段数据类型:alter table tbname modify column column_name new_data_type;

11.查看表内数据类型：show column from tbname;

12.删除表内所有内容：delete from tbname;

 
 
