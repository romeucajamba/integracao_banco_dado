from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import text
from sqlalchemy import Session


engine_conector = create_engine('sqlite://')
metadata = MetaData(schema='Cadastro')

cliente = Table(
        'Cliente',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('nome_cliente', String(40), nullable=False),
)

pedidos = Table(
    'Pedidos',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_cliente', Integer, ForeignKey('Cliente.id')),
)

metadata.create_all(engine_conector)

####### Uma consulta ########
consult_sql = text('select * from Cliente')

######### informar a consulta ao banco para ele retornar as informações requeridas ####################
engine_conector.execute(consult_sql)

######################Inserir dados ###########################
insert_data = text('insert into Cliente values("Romeu Cajamba")')
engine_conector.execute(insert_data)

####################################### Encerrar a minha sessão ##############################################
Session.close()
