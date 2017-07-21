Drop DATABASE IF EXISTS Patents;

CREATE DATABASE Patents;

USE Patents;

CREATE TABLE Patents(
   ID VARCHAR(10) NOT NULL PRIMARY KEY,
   Title VARCHAR(256),
   Brief_Description VARCHAR(256)
);

CREATE TABLE Patents_Description(
   ID VARCHAR(10),
   FOREIGN KEY (ID) REFERENCES Patents(ID),
   Description Text
);

CREATE TABLE Address(
   ID VARCHAR (10),
   FOREIGN KEY (ID) REFERENCES Patents(ID),
   Organization VARCHAR (256),
   City VARCHAR (256),
   State VARCHAR (256)
);

CREATE TABLE Inventors(
   ID VARCHAR (10),
   FOREIGN KEY (ID) REFERENCES Patents(ID),
   First_name VARCHAR (256),
   Last_name VARCHAR (256)
);

CREATE TABLE CPC(
   ID VARCHAR (10),
   FOREIGN KEY (ID) REFERENCES Patents(ID),
   Section VARCHAR (10),
   Class VARCHAR (10),
   Subclass VARCHAR (10),
   Maingroup VARCHAR (10),
   Subgroup VARCHAR (10)
);






