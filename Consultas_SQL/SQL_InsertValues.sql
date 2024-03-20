
---- 1 Inserção registro de pessoa

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (1, 'Administração Central','75904383000121','87308445','Rua Fioravante João Ferri, 99');

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (2, 'Campo Mourão','75904383000121','87308445','Rua Fioravante João Ferri, 99');	

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (3, 'Engenheiro Beltrão','75904383000202','87270000','Rodovia da Hortelã, km 01');	

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (4, 'Guarapuava','75904383019817','80400630','Avenida Manoel Ribas, 4850');	

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (5, 'Ivaiporã','75904383010194','86870000','Rodovia PR 466, km 110');

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (6, 'Posto Mahle','50018077000167','84043450','Rodov. BR-376, Km 504 S/N - Distrito Industrial');

INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (7, 'Unidade Transportes','75904383000207','87300970','BR-487, KM 197 - Zona Rural');


INSERT INTO PESSOA(id_pessoa,nm_pessoa, nr_cpfcnpj, nr_cep,ds_endereco)   
VALUES (8, 'João da Silva','01175211115','87300000','Av. Irmãos Pereira, 99');

---- 2 Inserção registro de unidade

INSERT INTO UNIDADE(cd_unidade, in_ativa, nm_municipio,id_pessoa)   
VALUES (1,'T','Campo Mourão',1);

INSERT INTO UNIDADE(cd_unidade, in_ativa, nm_municipio,id_pessoa)   
VALUES (2,'T','Campo Mourão',2);

INSERT INTO UNIDADE(cd_unidade, in_ativa, nm_municipio,id_pessoa)   
VALUES (3,'T','Engenheiro Beltão',3);

INSERT INTO UNIDADE(cd_unidade, in_ativa, nm_municipio,id_pessoa)   
VALUES (4,'T','Unidade Transportes',7);

INSERT INTO UNIDADE(cd_unidade, in_ativa, nm_municipio,id_pessoa)   
VALUES (5,'T','Guarapuava',4);

INSERT INTO UNIDADE(cd_unidade, in_ativa, nm_municipio,id_pessoa)   
VALUES (6,'T','Ivaiporã',5);

---- 3 Inserção registro de posto conveniado

	
INSERT INTO POSTO_CONVENIADO(cd_posto, dt_convenio, dt_desconvenio,in_ativo,id_pessoa)   
VALUES (199,'01/01/2024', null,'T',6);

---- 4 Inserção registro tipo de cargo

INSERT INTO CARGO_MOTORISTA (cd_cargo, ds_cargo)
VALUES (1,'MOTORISTA DE BITREM');

INSERT INTO CARGO_MOTORISTA (cd_cargo, ds_cargo)
VALUES (1,'MOTORISTA DE FURGAO');

INSERT INTO CARGO_MOTORISTA (cd_cargo, ds_cargo)
VALUES (1,'MOTORISTA DE CARRETA');



---- 5 Inserção registro motorista

INSERT INTO MOTORISTA(nr_matricula,nr_cnh, tp_categoria, cd_cargo, dt_admissao,dt_desligamento, in_ativo,id_pessoa)   
VALUES (445553, 123456789, 'E', 1, '01/05/2022', null,'T', 8);


---- 6 Inserção registro tipo de combustível

INSERT INTO TIPO_COMBUSTIVEL (cd_tipocombustivel, ds_tipocombustivel)
VALUES (1,'Gasolina');

INSERT INTO TIPO_COMBUSTIVEL (cd_tipocombustivel, ds_tipocombustivel)
VALUES (2,'Etanol');

INSERT INTO TIPO_COMBUSTIVEL (cd_tipocombustivel, ds_tipocombustivel)
VALUES (3,'Diesel S10');

INSERT INTO TIPO_COMBUSTIVEL (cd_tipocombustivel, ds_tipocombustivel)
VALUES (4,'Diesel S500');

INSERT INTO TIPO_COMBUSTIVEL (cd_tipocombustivel, ds_tipocombustivel)
VALUES (5,'GLP');


---- 7 Inserção registro tipo de veículo

INSERT INTO TIPO_VEICULO (cd_tipoveiculo, ds_tipoveiculo)
VALUES (1, 'Leve');

INSERT INTO TIPO_VEICULO (cd_tipoveiculo, ds_tipoveiculo)
VALUES (2, 'Médio');

INSERT INTO TIPO_VEICULO (cd_tipoveiculo, ds_tipoveiculo)
VALUES (3, 'Pesado');

---- 8 Inserção registro veículo


INSERT INTO VEICULO (id_veiculo, nr_placa, dt_aquisicao, dt_baixa, qt_capacidadetanque, in_ativo, cd_tipoveiculo, cd_tipocombustivel)
VALUES(1001,'ABC9J10', '10/05/2019', null, 360, 'T',3,3);

---- 9 Inserção registro veículo por unidade

INSERT INTO UNIDADE_VEICULO (id_veiculo,cd_unidade,dt_vinculo,dt_desvinculo)
VALUES	(1001,4,'15/06/2023',null);

---- 10 Inserção registro veículo e motorista

INSERT INTO VEICULO_MOTORISTA (id_veiculo,cd_motorista, dt_vinculo, dt_desvinculo)
VALUES (1001,445553, '10/10/2023',null);

---- 11 Inserção registro abastecimento
	
INSERT INTO ABASTECIMENTO (nr_reqastecimento, id_veiculo, dt_abastecimento, cd_motorista, cd_tipocombustivel, cd_posto, nr_hodometro, qt_litros, vl_combustivel)
VALUES (102030,1001,'10/03/2024',445553,3,199,15097, 360,1575);

INSERT INTO ABASTECIMENTO (nr_reqastecimento, id_veiculo, dt_abastecimento, cd_motorista, cd_tipocombustivel, cd_posto, nr_hodometro, qt_litros, vl_combustivel)
VALUES (102030,1001,'12/03/2024',445553,3,199,15452, 150,1575);