-- Kullanıcılar tablosu
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username NVARCHAR(100) NOT NULL,
    Password NVARCHAR(255) NOT NULL,
    Email NVARCHAR(255) NOT NULL,
    IsAdmin BIT DEFAULT 0,
    CreatedAt DATETIME DEFAULT GETDATE()
);

-- Çalışanlar tablosu
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(100) NOT NULL,
    LastName NVARCHAR(100) NOT NULL,
    PhoneNumber NVARCHAR(20) NOT NULL,
    IMEI NVARCHAR(50) NOT NULL,
    ProgramSerialNo NVARCHAR(100) NOT NULL,
    IsActive BIT DEFAULT 1,
    ContractDate DATETIME NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    CONSTRAINT UQ_IMEI UNIQUE (IMEI),
    CONSTRAINT UQ_PhoneNumber UNIQUE (PhoneNumber),
    CONSTRAINT UQ_ProgramSerialNo UNIQUE (ProgramSerialNo)
);

-- Konum geçmişi tablosu
CREATE TABLE LocationHistory (
    LocationID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeID INT NOT NULL,
    Latitude DECIMAL(10, 8) NOT NULL,
    Longitude DECIMAL(11, 8) NOT NULL,
    Accuracy FLOAT,
    Speed FLOAT,
    Timestamp DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Çalışan sözleşmeleri tablosu
CREATE TABLE EmployeeContracts (
    ContractID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeID INT NOT NULL,
    ContractText NVARCHAR(MAX) NOT NULL,
    SignedDate DATETIME NOT NULL,
    ExpiryDate DATETIME,
    IsActive BIT DEFAULT 1,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
); 