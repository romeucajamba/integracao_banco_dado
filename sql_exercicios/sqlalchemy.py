from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import  Session


my_engine = create_engine('sqlite://')
my_metadata = MetaData()

produtos = Table(
    'Produtos',
    my_metadata,
    Column('id_produt', Integer, primary_key=True, nullable=False),
    Column('nome_produto', String(100), nullable=False),
    Column('preco_produt', Float, nullable=False),
    Column('Categoria', String(10), nullable=False),
)


cliete = Table(
    'Cliente',
    my_metadata,
    Column('id_cliente', Integer, primary_key=True),
    Column('Nome', String(50), nullable=False),
    Column('BI', String(20, nullable=False)),
    Column('Telf', Integer, nullable=False),
    Column('morada',String(50), nullable=False)
)

fatura = Table(
    'Fatura',
    my_metadata,
    Column('Numero', Integer, primary_key=True, nullable=False ),
    Column('Data', Date, nullable=False),
    Column('Total', Integer, nullable=False),
    Column('id_fatura', Integer, ForeignKey('Produtos.id_produt'), nullable=False)
)

for tables in my_metadata.sorted_tables:   
        print(tables)
############################################# Conectar com o Banco de dados #######################################

my_metadata.create_all(my_engine)

############################################## consultas ao Banco de dados ##########################################
sql = text('Select * from Produtos')
print(my_engine.execute(sql))
sql = text('Select * from Cliente')
print(my_engine.execute(sql))
sql = text('Select * from Fatura')
print(my_engine.execute(sql))

########################################### Inserir dados ###########################################################

insert_data_sql = text('insert into Cliente values("1","Romeu", "0007656237LA087","943558106", "Sambizanga-Lixeira")')

my_engine.execute(insert_data_sql)

############################ Fechar sessão #######################
Session.close()