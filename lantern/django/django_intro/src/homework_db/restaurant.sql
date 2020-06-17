CREATE TABLE Restaurant (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone_number VARCHAR(10) NOT NULL UNIQUE,
    opening_time FLOAT NOT NULL,
    closing_time FLOAT NOT NULL,
    city INTEGER REFERENCES City(id) NOT NULL,
    country INTEGER REFERENCES Country(id) NOT NULL,
    menu INTEGER REFERENCES Menu(id) NOT NULL,
    );

CREATE TABLE Country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    );


CREATE TABLE City (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    id_of_country INTEGER REFERENCES Country(id) NOT NULL,
    );

CREATE TABLE Employee (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	middle_name VARCHAR(30),
	last_name VARCHAR(30) NOT NULL,
	phone_number VARCHAR(10) NOT NULL UNIQUE,
	email VARCHAR (70) NOT NULL UNIQUE,
	address VARCHAR(100) NOT NULL,
	career VARCHAR(50) NOT NULL,
	salary FLOAT NOT NULL,
	restaurant INTEGER REFERENCES Restaurant(id) NOT NULL,
	);

CREATE TABLE Dish (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    components VARCHAR NOT NULL,
    cooking_time FLOAT NOT NULL,
    weight INTEGER NOT NULL,
    price FLOAT NOT NULL,
    );

CREATE TABLE Menu (
    id SERIAL PRIMARY KEY,
    id_of_dish INTEGER REFERENCES Dish(id),
    );

CREATE TABLE MenuOfRestaurant (
    id_of_menu INTEGER REFERENCES Menu(id) NOT NULL,
    id_of_dish INTEGER REFERENCES Dish(id) NOT NULL,
    );




