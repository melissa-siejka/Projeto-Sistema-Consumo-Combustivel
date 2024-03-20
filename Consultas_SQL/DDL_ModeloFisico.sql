-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-03-20 16:00:55 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE abastecimento (
    nr_reqastecimento  NUMBER(9) NOT NULL,
    id_veiculo         NUMBER(7) NOT NULL,
    dt_abastecimento   DATE NOT NULL,
    cd_motorista       NUMBER(6) NOT NULL,
    cd_tipocombustivel NUMBER(3) NOT NULL,
    cd_posto           NUMBER(4) NOT NULL,
    nr_hodometro       NUMBER(7) NOT NULL,
    qt_litros          NUMBER(5, 2) NOT NULL,
    vl_combustivel     NUMBER(5, 2) NOT NULL
);

ALTER TABLE abastecimento ADD CONSTRAINT abastecimento_pk PRIMARY KEY ( nr_reqastecimento );

CREATE TABLE cargo_motorista (
    cd_cargo NUMBER(3) NOT NULL,
    ds_cargo VARCHAR2(50) NOT NULL
);

ALTER TABLE cargo_motorista ADD CONSTRAINT cargo_motorista_pk PRIMARY KEY ( cd_cargo );

CREATE TABLE motorista (
    nr_matricula    NUMBER(6) NOT NULL,
    nr_cnh          NUMBER(9) NOT NULL,
    tp_categoria    VARCHAR2(2) NOT NULL,
    cd_cargo        NUMBER(3) NOT NULL,
    dt_admissao     DATE NOT NULL,
    dt_desligamento DATE,
    in_ativo        CHAR(1) NOT NULL,
    id_pessoa       NUMBER(7) NOT NULL
);

ALTER TABLE motorista ADD CONSTRAINT motorista_pk PRIMARY KEY ( nr_matricula );

CREATE TABLE pessoa (
    id_pessoa   NUMBER(7) NOT NULL,
    nm_pessoa   VARCHAR2(100) NOT NULL,
    nr_cpfcnpj  CHAR(14) NOT NULL,
    nr_cep      CHAR(8) NOT NULL,
    ds_endereco VARCHAR2(200) NOT NULL
);

ALTER TABLE pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( id_pessoa );

CREATE TABLE posto_conveniado (
    cd_posto       NUMBER(4) NOT NULL,
    dt_convenio    DATE NOT NULL,
    dt_desconvenio DATE,
    in_ativo       CHAR(1) NOT NULL,
    id_pessoa      NUMBER(7) NOT NULL
);

ALTER TABLE posto_conveniado ADD CONSTRAINT posto_conveniado_pk PRIMARY KEY ( cd_posto );

CREATE TABLE tipo_combustivel (
    cd_tipocombustivel NUMBER(3) NOT NULL,
    ds_tipocombustivel VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_combustivel ADD CONSTRAINT tipo_combustivel_pk PRIMARY KEY ( cd_tipocombustivel );

CREATE TABLE tipo_veiculo (
    cd_tipoveiculo NUMBER(3) NOT NULL,
    ds_tipoveiculo VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_veiculo ADD CONSTRAINT tipo_veiculo_pk PRIMARY KEY ( cd_tipoveiculo );

CREATE TABLE unidade (
    cd_unidade   NUMBER(6) NOT NULL,
    in_ativa     CHAR(1) NOT NULL,
    nm_municipio VARCHAR2(50) NOT NULL,
    id_pessoa    NUMBER(7) NOT NULL
);

ALTER TABLE unidade ADD CONSTRAINT unidade_pk PRIMARY KEY ( cd_unidade );

CREATE TABLE unidade_veiculo (
    id_veiculo    NUMBER(7) NOT NULL,
    cd_unidade    NUMBER(6) NOT NULL,
    dt_vinculo    DATE NOT NULL,
    dt_desvinculo DATE
);

ALTER TABLE unidade_veiculo
    ADD CONSTRAINT unidade_veiculo_pk PRIMARY KEY ( id_veiculo,
                                                    cd_unidade,
                                                    dt_vinculo );

CREATE TABLE veiculo (
    id_veiculo          NUMBER(7) NOT NULL,
    nr_placa            CHAR(7) NOT NULL,
    dt_aquisicao        DATE NOT NULL,
    dt_baixa            DATE,
    qt_capacidadetanque INTEGER NOT NULL,
    in_ativo            CHAR(1) NOT NULL,
    cd_tipoveiculo      NUMBER(3) NOT NULL,
    cd_tipocombustivel  NUMBER(3) NOT NULL
);

ALTER TABLE veiculo ADD CONSTRAINT veiculo_pk PRIMARY KEY ( id_veiculo );

CREATE TABLE veiculo_motorista (
    id_veiculo    NUMBER(7) NOT NULL,
    cd_motorista  NUMBER(6) NOT NULL,
    dt_vinculo    DATE NOT NULL,
    dt_desvinculo DATE
);

ALTER TABLE veiculo_motorista
    ADD CONSTRAINT veiculo_motorista_pk PRIMARY KEY ( id_veiculo,
                                                      cd_motorista,
                                                      dt_vinculo );

ALTER TABLE abastecimento
    ADD CONSTRAINT abast_motorista_fk FOREIGN KEY ( cd_motorista )
        REFERENCES motorista ( nr_matricula );

ALTER TABLE abastecimento
    ADD CONSTRAINT abast_posto_fk FOREIGN KEY ( cd_posto )
        REFERENCES posto_conveniado ( cd_posto );

ALTER TABLE abastecimento
    ADD CONSTRAINT abast_tipo_combustivel_fk FOREIGN KEY ( cd_tipocombustivel )
        REFERENCES tipo_combustivel ( cd_tipocombustivel );

ALTER TABLE abastecimento
    ADD CONSTRAINT abast_veiculo_fk FOREIGN KEY ( id_veiculo )
        REFERENCES veiculo ( id_veiculo );

ALTER TABLE motorista
    ADD CONSTRAINT motorista_cargo_motorista_fk FOREIGN KEY ( cd_cargo )
        REFERENCES cargo_motorista ( cd_cargo );

ALTER TABLE motorista
    ADD CONSTRAINT motorista_pessoa_fk FOREIGN KEY ( id_pessoa )
        REFERENCES pessoa ( id_pessoa );

ALTER TABLE posto_conveniado
    ADD CONSTRAINT posto_conveniado_pessoa_fk FOREIGN KEY ( id_pessoa )
        REFERENCES pessoa ( id_pessoa );

ALTER TABLE unidade_veiculo
    ADD CONSTRAINT und_unidade_fk FOREIGN KEY ( cd_unidade )
        REFERENCES unidade ( cd_unidade );

ALTER TABLE unidade_veiculo
    ADD CONSTRAINT und_veiculo_fk FOREIGN KEY ( id_veiculo )
        REFERENCES veiculo ( id_veiculo );

ALTER TABLE unidade
    ADD CONSTRAINT unidade_pessoa_fk FOREIGN KEY ( id_pessoa )
        REFERENCES pessoa ( id_pessoa );

ALTER TABLE veiculo_motorista
    ADD CONSTRAINT veic_motorista_fk FOREIGN KEY ( cd_motorista )
        REFERENCES motorista ( nr_matricula );

ALTER TABLE veiculo_motorista
    ADD CONSTRAINT veic_veiculo_fk FOREIGN KEY ( id_veiculo )
        REFERENCES veiculo ( id_veiculo );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo_tipo_combustivel_fk FOREIGN KEY ( cd_tipocombustivel )
        REFERENCES tipo_combustivel ( cd_tipocombustivel );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo_tipo_veiculo_fk FOREIGN KEY ( cd_tipoveiculo )
        REFERENCES tipo_veiculo ( cd_tipoveiculo );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            11
-- CREATE INDEX                             0
-- ALTER TABLE                             25
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
