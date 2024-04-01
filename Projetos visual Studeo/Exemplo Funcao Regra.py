# Exemplo Consulta Python


from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Função para verificar e registrar o abastecimento do veículo
def registrar_abastecimento(id_veiculo, dt_abastecimento):
    try:
        # Conectar ao banco de dados
        engine = create_engine('sua_string_de_conexao')
        Session = sessionmaker(bind=engine)
        session = Session()

        # Verificar se o veículo está ativo e a data de abastecimento é válida
        query = text('SELECT IN_ATIVO, DT_BAIXA FROM VEICULO WHERE ID_VEICULO = :id_veiculo')
        result = session.execute(query, {'id_veiculo': id_veiculo}).fetchone()

        if result:
            in_ativo, dt_baixa = result

            if in_ativo == 'T':
                # Veículo está ativo, registrar o abastecimento
                registrar_abastecimento_no_banco(id_veiculo, dt_abastecimento, session)
            elif in_ativo == 'F' and dt_abastecimento <= dt_baixa:
                # Veículo inativo, mas a data de abastecimento é válida, registrar o abastecimento
                registrar_abastecimento_no_banco(id_veiculo, dt_abastecimento, session)
            else:
                # Informar ao usuário que o veículo está inativo
                print("Veículo inativo, favor verificar!")
        else:
            print("Veículo não encontrado.")

        session.commit()
        session.close()
    except SQLAlchemyError as e:
        print(f"Erro ao acessar o banco de dados: {e}")

# Função para gravar o abastecimento do veículo no banco de dados
def registrar_abastecimento_no_banco(id_veiculo, dt_abastecimento, session):
    # Implemente aqui a lógica para gravar o abastecimento no banco de dados
    pass

# Exemplo de uso da função
id_veiculo = 123  # ID do veículo
dt_abastecimento = datetime.now()  # Data de abastecimento (exemplo: data atual)
registrar_abastecimento(id_veiculo, dt_abastecimento)
