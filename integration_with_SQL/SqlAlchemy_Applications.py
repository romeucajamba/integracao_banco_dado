from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()
"""A declarative_base é a minha estrutura pré_definida e nela contém o orm 
#base_declarativa ou declarative_base é o modelo que vou usar para criar as classes da minha aplicação
 de maneira que eu consiga fazer mapeamento para o banco de dados e consequentemente a integração
 
 Eu preciso da declarative_base porque eu estou criando minhas tabelas aqui no python por meio das
  classes e depois que eu conectar ao banco eu vou usa-las para que elas executem as sqlstatmants e criem
  a minha estrutura lá dentro do meu banco de dados
 """

#Estendeno ou herdadno a  as características da classe Base
class User(Base):
    #Minha tabela
    __tablename__ = "user_account"

    #Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    #Criando relacionamento entre as tabelas
    address = relationship("Address", back_populates="User", cascade="all, delete-orphan")#Referenciado o relacionameto entre a tabela user e address

    # Defindo uma representação para a class Address
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullName={self.fullname})"

#Recuperar as informações
print(User.__tablename__)


class Address(Base):
    __tablename__ = "Address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    # Criando relacionamento entre as tabelas
    user = relationship("User", back_populates="Address", cascade="all, delete-orphan")#Referenciado o relacionameto entre a tabela user e address


    #Defindo uma representação para a class Address
    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(Address.__tablename__)

#Conexão com banco de dados
#Minha engine para a conexão com o banco
engine = create_engine("sqlite://")#Estou dizendo que vou usar o sqlite que já vem com o python

#mapear os objectos ou classes User e Address que criamos e persitir(Inserir) no banco de dados, definir a estrutura deles lá dentro

#Criando as classes como tabelas no banco

#Estamos usando a base e dentro da base tem o método associado que é o metadata com o método create_all() para criar tabelas
Base.metadata.create_all(engine)


#Inspecionando a minha engine
#Ele vai buscar as informações da minha engine que está conmetado ao banco(Ele vai mostrar informações do banco)
#Investiga o schema do banco de dados
inspetor_engine = inspect(engine)

#Constactar se tem tabela user_account

print(inspetor_engine.has_table("user_account"))

#Mostrar as tabelas que tem no banco

print(inspetor_engine.get_table_names())

#Me retorne a informação ou nome do banco de dados, e não atribuimos nome então retornará o nome main
print(inspetor_engine.default_schema_name)


########################    Criando a minha sessão para manter os dados no meu banco    ################################

with Session(engine) as session:
    romeu=User(
        name='Romeu',
        fullname='Romeu Cajamba',
        email_address = [Address(email_address='romuecajamba@gmail.com')]
    )
    tomas=User(
        name='Tomás',
        fullname='Tomás Cajamba',
        email_address=[Address(email_address='tomascajamba@outlook.pt')]
      
    )
    #Meu usário sem enderesso de email
    patrick=User(
        name='Patrick',
        fullname='Parick Cardoso'
    )

    #Enviando os meus dados para o banco(Persistência de dados)
    session.add_all([romeu, tomas, patrick])
    session.commit()


########################################  Executando consultas ao banco  #####################################
stm = select(User).where(User.name.in_(['romeu']))

print(stm)


print("Recuperar usuário a partir de condição de filtragem")
for user in session.scalar([stm]):
    print(user)


stm = select(Address).where(Address.user_id.in_([2]))
for address in session.scalar([stm]):
    print(address)