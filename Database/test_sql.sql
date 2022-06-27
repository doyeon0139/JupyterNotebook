



use shopdb;     -- 데이터베이스 선택

-- select 칼럼명 from 테이블명 where 조건;

select * from membertdl;

-- 실행 ctrl+enter : 한 줄 실행
-- ctrl + shift + enter :  전체실행 또는 선택한 블록 실행

select memberadress from membertdl;

select memberadress from membertdl where membername = '당당';
select * from productbl;

select productname from productbl where amount < 5;