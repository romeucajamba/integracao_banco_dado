from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from integration_with_SQL.SqlAlchemy_Applications import session

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData()

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_adress', String(50)),
    Column('mickname', String(40), nullable=False)
)

print(user.primary_key)

user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('prf_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),

)

print(user_prefs.primary_key)

###################################################Conectabndo com o BD ##############################

metadata_obj.create_all(engine)

#vai tornar o nome do banco com as tabelas
for tables in metadata_obj.sorted_tables:
    print(tables)


metada_objt_bk = MetaData(schema="bank")

banco = Table(
    'Banco',
    metada_objt_bk,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)
###################### Informações da tabela Banco ###############
print(banco.primary_key)




sql = text('select * from user')
result = engine.execute(sql)

for row in result:
    print(row)

print(engine.execute(sql))


sql_insert = text("insert into user values('2', 'romeu', 'romeucajamba@gmail.com', 'ro )")

engine.execute(sql_insert)

### Encerrar a sessão ###

session.cloes()