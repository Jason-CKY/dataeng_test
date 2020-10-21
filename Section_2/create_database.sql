DROP DATABASE IF EXISTS CAR_DEALERSHIP;
CREATE DATABASE CAR_DEALERSHIP;

CREATE TABLE Manufacturer 
(
    ManufacturerID    BIGSERIAL NOT NULL,
    Name  VARCHAR(50) NOT NULL,
    PRIMARY KEY(ManufacturerID)
);

CREATE TABLE SalesPerson 
(
    SalesPersonID    BIGSERIAL NOT NULL,
    Name  VARCHAR(50) NOT NULL,
    PRIMARY KEY(SalesPersonID)
);

CREATE TABLE Customer 
(
    CustomerID      BIGSERIAL NOT NULL,
    Name            VARCHAR(50) NOT NULL,
    PhoneNumber     INT NOT NULL,
    PRIMARY KEY(CustomerID)
);

CREATE TABLE Car 
(
    SerialNumber    BIGSERIAL NOT NULL,
    ModelName       VARCHAR(50) NOT NULL,
    ModelVariant    VARCHAR(50) NOT NULL,
    CarWeight       FLOAT NOT NULL,
    Engine_CC       INT NOT NULL,
    Price           DECIMAL(12, 2) NOT NULL,
    ManufacturerID  BIGSERIAL NOT NULL,
    PRIMARY KEY(SerialNumber),
    FOREIGN KEY(ManufacturerID) REFERENCES Manufacturer(ManufacturerID) ON DELETE CASCADE
);

CREATE TABLE Transaction 
(
    TransactionID           BIGSERIAL NOT NULL,
    TransactionDateTime     DATETIME NOT NULL,
    SerialNumber            BIGSERIAL NOT NULL,
    SalesPersonID           BIGSERIAL NOT NULL,
    CustomerID              BIGSERIAL NOT NULL,
    Primary KEY(TransactionID),
    FOREIGN KEY(SerialNumber) REFERENCES Car(SerialNumber) ON DELETE CASCADE,
    FOREIGN KEY(SalesPersonID) REFERENCES SalesPerson(SalesPersonID) ON DELETE CASCADE,
    FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE
);