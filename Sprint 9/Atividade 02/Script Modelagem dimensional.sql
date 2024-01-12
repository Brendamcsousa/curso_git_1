--Tabela Fato (FatoLocacao):

CREATE TABLE FatoLocacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idCombustivel INT,
    idVendedor INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel),
    FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor)
)

--Tabela de Dimensão Cliente (DimCliente):

CREATE TABLE DimCliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(255),
    cidadeCliente VARCHAR(255),
    estadoCliente VARCHAR(255),
    paisCliente VARCHAR(255)
)

--Tabela de Dimensão Carro (DimCarro):

CREATE TABLE DimCarro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    chassiCarro VARCHAR(255),
    marcaCarro VARCHAR(255),
    modeloCarro VARCHAR(255),
    anoCarro INT
)

--Tabela de Dimensão Combustível (DimCombustivel):

CREATE TABLE DimCombustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(255)
)

--Tabela de Dimensão Vendedor (DimVendedor):

CREATE TABLE DimVendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(255),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(255)
)