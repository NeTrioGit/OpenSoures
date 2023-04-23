이것은 MySQL 데이터베이스의 데이터를 사용하여 원형 차트를 생성하고 사용자가 HTML 형식을 사용하여 데이터를 업데이트할 수 있는 PHP 스크립트입니다.

// PIZZA 데이터베이스와 PIE 테이블을 만드는 코드입니다.

₩₩₩CREATE DATABASE PIZZA;

USE PIZZA;

CREATE DATABASE pizza;

USE pizza;

CREATE TABLE pie (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  source1 VARCHAR(255) NOT NULL,
  source1_i FLOAT(11) NOT NULL,
  source2 VARCHAR(255) NOT NULL,
  source2_i FLOAT(11) NOT NULL,
  source3 VARCHAR(255) NOT NULL,
  source3_i FLOAT(11) NOT NULL,
  source4 VARCHAR(255) NOT NULL,
  source4_i FLOAT(11) NOT NULL,
  source5 VARCHAR(255) NOT NULL,
  source5_i FLOAT(11) NOT NULL
);
₩₩₩
