

drop database if exists sqldb;
create database sqldb;




use sqldb;

CREATE TABLE usertbl -- 회원 테이블
( userID   CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  name     VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr    CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1 CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2 CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height     SMALLINT,  -- 키
  mDate     DATE  -- 회원 가입일
);
CREATE TABLE buytbl -- 회원 구매 테이블
(  num  INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID   CHAR(8) NOT NULL, -- 아이디(FK)
   prodName  CHAR(6) NOT NULL, --  물품명
   groupName  CHAR(4)  , -- 분류
   price      INT  NOT NULL, -- 단가
   amount     SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (userID) REFERENCES userTbl(userID)
);

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);

select * from usertbl;
select * from buytbl;

-- 김경호라는 가수의 데이터를 출력
select * from usertbl where name = '김경호';

-- 출생연도가 1970년 이후이고, 키가 182 이상인 회원의 userid를 출력
select userID, name from usertbl where birthYear > 1970 and height >= 182;

-- 출생연도가 1970년 이후이거나, 키가 182 이상인 회원의 userid를 출력
select userID, name from usertbl where birthYear > 1970 or height >= 182;

-- 키가 180 이상이고 183 이하인 회원의 이름을 출력
select name from usertbl where height >= 180 and height <= 183;
select name from usertbl where height  between 180 and 183;

-- 출생지가 '경남', '전남' 또는 '경북'인 회원의 이름과 아이디를 출력
select userID, name, addr from usertbl where addr = '경남' or addr='전남' or addr = '경북';
select userID, name, addr from usertbl where addr in ('경남','전남','경북');

-- 텍스트 검색
-- 성이 '김'인 사람의 데이터를 출력
select name from usertbl where name like '김%';

-- 이름이 '종신'인 사람의 데이터를 출력
select name from usertbl where name like '%종신';

-- 이름이 '종신'인 성이 한 글자만 사람의 데이터를 출력
select name from usertbl where name like '_종신';

-- 키가 178 이상인 사람의 데이터를 출력
select name, height from usertbl where height >= 178;

-- 임재범 보다 키가 큰 사람의 데이터를 출력
select height from usertbl where name = '임재범';
select * from usertbl where height = 182;

select * from usertbl where height > (select height from usertbl where name = '임재범');


-- 임재범 보다 나이가 많은 사람의 이름을 출력하시오
select name from usertbl where birthYear < (select birthYear from usertbl where name = '임재범');


-- 김범수와 출생지역이 동일한 사람의 데이터ㅡㄹ 출력
select * from usertbl where addr = (select addr from usertbl where name = '김범수');
select * from usertbl where addr in (select addr from usertbl where name = '김범수');

-- subquery에서 값이 복수인 경우 비교연산 할 수 없다
-- all() - 전체데이터에 True. any() - 어느하나만 True
-- 경남에 사는 사람 보다 키가 큰 사람의 데이터를 출력
select * from usertbl where height > (select height from usertbl where addr = '경남');        -- 왜또 나만 안돼  에러 맞대

select * from usertbl where height > all(select height from usertbl where addr = '경남');   -- 최대값
select * from usertbl where height > any(select height from usertbl where addr = '경남');   -- 최소값

-- 경남에 사는 사람 보다 키가 동일한 사람의 데이터를 출력
select * from usertbl where height = (select height from usertbl where addr = '경남');      -- 에러
select * from usertbl where height in (select height from usertbl where addr = '경남');      -- in 키워드를 써줌

-- 정렬(sort) : order by  == sort_values()
-- 출생 기준으로 오름차순 정렬해서 출력
select * from usertbl order by birthYear;
-- 출생 기준으로 내림차순 정렬해서 출력
select * from usertbl order by birthYear desc;

-- 키 순으로 오름차순 정렬하시오
select * from usertbl order by height;

-- 키 순으로 내림차순 정렬하시오
select * from usertbl order by height desc;

-- 출생지의 종류를 중복값없이 출력하시오
select distinct(addr) from usertbl;           -- 중복값 없이

-- 출생지 종류수를 출력
select count(addr) from usertbl;           -- 중복값을 갖는다
select count(distinct(addr)) from usertbl;     -- 중복값없이

-- head()같은 출력
-- n개만 출력
select * from usertbl limit 3;

-- 키가 가장 큰 사람의 이름을 출력하시오
select name from usertbl order by height desc limit 1;

-- subquery를 이용해서 기존 table을 복사해서 새로운 table을 생성
create table buytbl1 (select * from buytbl);
select * from buytbl1;

create table buytbl2 (select userID, prodName from buytbl);
select * from buytbl2

create table usertbl2 (select userid, name from usertbl);
select * from usertbl2













