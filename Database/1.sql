








use sqldb;

select * from usertbl;
select * from buytbl;

select userid from buytbl group by userid;
select userid, sum(amount) from buytbl group by userid;
select userid, sum(amount) as total_amount from buytbl group by userid order by total_amount;

-- 평균 구매량
select userid, avg(amount) as '평균구매량' from buytbl group by userid order by avg(amount);

-- 구매횟수
select userid, count(amount) as '구매횟수' from buytbl group by userid

-- 사용자별 총구매액이 1000 이상인 고객 데이터를 출력
-- group by 에서 조건을 지정하는 경우 : having (o), where(x)
-- select userid, sum(price * amount) as '총구매금액' from buytbl group by userid where '총구매금액' >= 1000; error
select userid, sum(price * amount) as '총구매금액' from buytbl group by userid having sum(price * amount) >= 1000; 

-- 구매횟수가 2회 이상인 구매정보를 출력
select * from buytbl group by userid having count(amount) >= 2;

-- usertbl에서 가장 키가 큰 사람과 작은 사람을 출력하시오
select max(height) from usertbl;
select min(height) from usertbl;
select name, height from usertbl where height in (((select max(height) from usertbl), (select min(height) from usertbl)));
select name, min(height) from usertbl;
select name, max(height) from usertbl;

use employees;
select * from employees;

create table testtbl1(id int, fname varchar(50), lname varchar(50));
use sqlab;
use employees;
insert into testtbl1 select emp_no, first_name, last_name from employees.employees;  -- 데이터 테이브에 접근
select * from testtbl1;

-- 데이터 수정 : update
select * from testtbl1 where fname='Aamer';
update testtbl1 set lname ='없음' where fname='Aamer';

use sqldb;
-- buytbl
update buytbl set price = price*1.5;
select * from buytbl;

## Join
select * from usertbl;
select * from buytbl;

-- inner join
select * from buytbl inner join usertbl
	on buytbl.userID = usertbl.userID;

select * from buytbl b inner join usertbl u
	on b.userID = u.userID;
    
select * from buytbl, usertbl
	where buytbl.userID = usertbl.userID;

select * from buytbl b, usertbl u
	where b.userID = u.userID;
    
-- 조용필이 구매한 제품의 이름과 조용필의 주소를 출력하시오
select prodName, addr from buytbl inner join usertbl
	on buytbl.userID = usertbl.userID;
    where name = '조용필';

-- 모니터를 구매한 사람들의 이름을 출력
select name from buytbl b inner join usertbl u
	on b.userID = u.userID
    where prodName = '모니터';
    
-- 전화번호가 없는 고객의 이름, 주소, 구매제품 출력
select name, addr, prodName from buytbl b inner join usertbl u
	on b.userID = u.userID
    where mobile1 is null;

-- 총구매금액이 가장 큰 고객정보를 출력
select name, amount, price, sum(amount*price) '총구매금액 '
	from buytbl b inner join usertbl u
	on b.userID = u.userID
    group by b.userid
    order by (sumamount*price) desc
    limit 1; 
    
-- left join
select * from buytbl b left join usertbl u
	on b.userID = u.userID;
    
-- right join
select * from buytbl b right join usertbl u
	on b.userID = u.userID
    
-- table 3개 join

create table stdtbl (
	stdname varchar(10) not null primary key,
    addr char(4) not null);
insert into stdtbl values('김범수', '경남'),('성시경','서울'),('조용필', '경기'),('은지원', '경북'),('바비킴', '서울');
select * from stdtbl;

create table clubtbl (
	clubname varchar(10) not null primary key,
    roomno char(4) not null);
insert into clubtbl values ('수명', '101호'), ('바둑','102호'),('축구', '103호'), ('봉사', '104호');
select * from clubtbl;

create table stdclubtbl(
	num int auto_increment not null primary key,
    stdname varchar(10) not null,
    clubname varchar(10) not null);
insert into stdclubtbl values(null, '김범수', '바둑'), (null, '김범수', '축구'), (null, '조용필', '축구'),
select * from stdclubtbl;

select * from stdtbl;
select * from clubtbl;
select * from stdclubtbl;

select * from stdtbl inner join stdclubtbl on stdtbl.stdname = stdclubtbl.stdname
					 inner join clubtbl on clubtbl.clubname = stdclubtbl.clubname;

select * from stdtbl s inner join stdclubtbl sc on s.stdname = sc.stdname
					 inner join clubtbl c on c.clubname = sc.clubname;
                     
select * from stdtbl, stdclubtbl, clubtbl
	where stdtbl.stdname = stdclubtbl.stdname
	and clubtbl.clubname = stdclubtbl.clubname;

select * from stdtbl s, stdclubtbl sc, clubtbl c
	where s.stdname = sc.stdname
	and c.clubname = sc.clubname;

-- 축구부에 가입한 학생의 주소를 출력
select * from stdtbl s, stdclubtbl sc, clubtbl c
	where s.stdname = sc.stdname
	and c.clubname = sc.clubname
    and c.clubname ='축구';


### if 구문/ case when 구문
### procedure() : 함수

drop procedure if exists ifproc3;
delimiter $$

create procedure ifproc3()

begin
	declare point int;
    declare credit char(1);
    set point = 77;
    
    if point >= 90 then
		set credit = 'A';
	elseif point >= 80 then
		set credit = 'B';
	elseif point >= 70 then
		set credit = 'C';
	else
		set credit = 'D';
	end if;
    
    select concat('취득학점 : ', point), concat('학점 : ', credit);
end $$

delimiter ;

call ifproc3();

-- case when
drop procedure if exists ifproc2;
delimiter $$

create procedure ifproc2()

begin
	declare point int;
    declare credit char(1);
    set point = 77;
    
    case
		when point >=90 then
			set credit = 'A';
		when point >=80 then
			set credit = 'B';
		when point >=70 then
			set credit = 'C';
		else
			set credit = 'D';
	end case;
    
    select concat('취득학점 : ', point), concat('학점 : ', credit);
end $$    

delimiter ;

call ifproc2();

select userid, usernmae, sum(price*amount) as 'total_amount'
	from buytbl b right join usertbl u
    on b.userID = u.userID
    group by u.userID
    order by total_amount desc;

-- 기본함수

-- cast : 데이터타임을 변환
select cast('2020-10-16 12:25:29:123' as date) as 'date';
select cast('2020-10-16 12:25:29:123' as time) as 'Time';
select cast('2020-10-16 12:25:29:123' as datetime) as 'DateTime';

-- concat : 이어주는 함수
use sqldb;
show tables;
select num, 
	concat(cast(price as char(10)), 'x', cast(amount as char(10)), '=') as '가격*구매량',
	price*amount as '총 구매금액'
    from buytbl;

select concat('100', '200');
select concat_ws('/','2020','01','01') as '날짜';

-- ifnull(요소1, 요소2) : 요소1이 null이면 요소2를 리턴, 요소1이 null이 아니면 요소1을 리턴
select ifnull(null, 100); 
select ifnull(100, 200);

-- insert('문자열1', index, length, '문자열2') : 문자열1의 index 위치에 length 길이 인덱스에 문자열2를 입력
select insert('abcdefghijk', 3, 4, '@@@@');
select insert('abcdefghijk', 3, 2, '@@@@');

-- left ('문자열', num) : 문자열 왼쪽으로부터 num갯수 만큼 요소출력
-- right ('문자열', num) : 문자열 오른쪼으로부터 num갯수 만큼 요소출력
select left('abcdefghi', 3);
select right('abcdefghi', 3);

-- repeat('문자열', n) : 문자열을 n회 반복
select repeat('abc', 10);

-- lower()
select lower('abcdEFG');
select upper('abcdEFG');

-- lpad('문자열1', num, '@') : 문자열 1을 num 크기만큼 자리수를 늘리고 빈자리를 '@'로 채운다
select lpad('abc', 7, '@');
select rpad('abc', 7, '@');

-- lstrim, retrim : 좌우 공백제거
select ltrim('       abc       ');
select rtrim('       abc       ');

-- replace('문자열1'.'문자열2', '문자열3') : 문자열1에서 문자열2를 찾아서 문자열3으로 변경
select replace('hello mysql', 'mysql', 'python');

-- abs
select abs(-3);

-- ceiling, floor(), round()
select ceiling(4.7);
select floor(4.7);
select round(4.7);
select round(4.3);

-- 나머지 계산
select mod(11,2);
select mod(15,3);

-- sqrt : 제곱근
select sqrt(9);

-- pow : 승
select pow(2,3);

-- length : byte
select length('abd')





























