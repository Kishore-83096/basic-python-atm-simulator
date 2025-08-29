create database ATM;
use ATM;
CREATE TABLE ATMHOLDERS (
    CARD_NUMBER BIGINT PRIMARY KEY ,
    CARD_HOLDER_NAME VARCHAR(100) NOT NULL,
    USER_ID VARCHAR(100) NOT NULL,
    PASS_WORD VARCHAR(100) NOT NULL UNIQUE  KEY,
    BALANCE BIGINT
    );

SELECT * FROM ATMHOLDERS;
INSERT INTO ATMHOLDERS(CARD_NUMBER,CARD_HOLDER_NAME,USER_ID,PASS_WORD,BALANCE) VALUES(080812001234,"Hemanth KUMAR","hemant1484@ATM.COM","089098",0);
commit;

DELETE FROM ATMHOLDERS where CARD_NUMBER = 888800005509;
Select CARD_NUMBER ,CARD_HOLDER_NAME, USER_ID , BALANCE from ATMHOLDERS where USER_ID = "Allu Arjun@atm.com";
DELETE FROM ATMHOLDERS WHERE card_number = 1234567890;
ALTER TABLE ATMHOLDERS modify Card_Number  VARCHAR(12) unique not null;
describe AtmHolders;
SELECT CARD_NUMBER FROM  ATMHOLDERS WHERE CARD_NUMBER = 11112222333;
CREATE TABLE ADMINSTRATOR (
    Admin_id varchar(100) PRIMARY KEY ,
    Admin_name varchar(20) not null,
    Pin int NOT NULL UNIQUE  KEY
);
select * from Adminstrator;
INSERT INTO Adminstrator(Admin_id,Admin_name,Pin) VALUES("Kishore@Admim.bank","Kishore",0000);
ALTER TABLE Adminstrator modify Pin VARCHAR(4) unique not null;
describe Adminstrator;
update Adminstrator set Admin_id = "Kishore@Admin.bank" where Admin_name = "Kishore";
SELECT Card_Number,NAME,USER_ID  FROM ATMHOLDERS WHERE CARD_NUMBER = "656412378908";

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each transaction
    transaction_datetime DATETIME NOT NULL,          -- Date and time of the transaction
    transaction_type VARCHAR(50) NOT NULL,          -- Type of transaction (e.g., 'credit', 'debit')
    amount DECIMAL(10, 2) NOT NULL                   -- Amount of the transaction, with two decimal places
);

select * from Transactions;
describe transactions;
SELECT * FROM (SELECT * FROM transactions WHERE Card_Number = 778907890654 ORDER BY transaction_datetime DESC LIMIT 5) AS last_transactions ORDER BY transaction_datetime ASC;
SELECT Transaction_datetime ,transaction_type, Amount FROM (SELECT * FROM transactions WHERE Card_Number = 778907890654 ORDER BY transaction_datetime DESC LIMIT 5) AS last_transactions ORDER BY transaction_datetime ASC;
