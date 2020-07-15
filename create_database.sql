drop database if exists enote;
create database enote;
use enote;

-- Note: I've ommitted Foreign Keys as there is inconsistency for the test data
drop table if exists enote.person;
create table enote.person (
	id_person BIGINT PRIMARY KEY,
    name VARCHAR(256),
    surname VARCHAR(256),
    zip INT,
    city VARCHAR(50),
    country VARCHAR(60),
    email VARCHAR(512),
    phone_number VARCHAR(128),
    birth_date DATE
);

-- Note: I've ommitted Foreign Keys as there is inconsistency for the test data
drop table if exists enote.account;
create table enote.account (
	id_account BIGINT PRIMARY KEY,
    id_person BIGINT NOT NULL,
    account_type VARCHAR(20),
	FOREIGN KEY (id_person) REFERENCES enote.person(id_person)
);

-- Note: I've ommitted the primary key (PK) for the table as there were duplicates for the same id_transaction and id_person
-- Note: I've ommitted Foreign Keys as there is inconsistency for the test data
drop table if exists enote.transaction;
create table transaction (
	id_transaction BIGINT NOT NULL,
    id_account BIGINT NOT NULL,
    transaction_type CHAR(2),
    transaction_date DATE,
    transaction_amount FLOAT,
	PRIMARY KEY (id_transaction, id_account)
	FOREIGN KEY (id_account) REFERENCES enote.account(id_account)
)
