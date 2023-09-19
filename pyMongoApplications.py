import datetime

import pymongo as pyM
#Conexão com mongoDB
cliente = pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster1.yoczfda.mongodb.net/?retryWrites=true&w=majority")
db.cliente.test

collections = db.test_collections
#Mostrando a coleção
print(db.test_collections)

#Definição de informações para compor o Documento
post = {
    "author": "Romeu_Cajamba",
    "text":"My first mongoDB  appliation!",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

#Preparando para submeter as infos
post = db.posts

post_id = posts.insert_one(post).iserted_id
print(post_id)

print(db.posts)