# criando o banco de dados no sqLite

import sqlite3

#criando as variáveis
nome = ('maze')
idade = ('66')
email = ('maze@gmail.com')

# acessando o banco e criando as tabelas

banco = sqlite3.connect("meu primeiro banco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas(nome texte, idade interger, email text)")

# depois de criadas as tabelas, inserindo os valores
#cursor. execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+", '"+email+"')")


banco.commit()

cursor.execute("SELECT *from pessoas")
# printando o que foi adcionado nas tabelas

print(cursor.fetchall())

# código para deletar dados da tabela
try:
        
    banco = sqlite3.connect("meu primeiro banco.db")

    cursor = banco.cursor()



    cursor. execute("DELETE from pessoas WHERE idade = 65")


    banco.commit()

    cursor.execute("SELECT *from pessoas")
    
    #print("os dados foram removidos com sucesso!!")
    
    
except sqlite3.Error as erro :
         print(" erro ao excluir !!", erro)


# substituindo dados da tabela

banco = sqlite3.connect("meu primeiro banco.db")


cursor = banco.cursor()
cursor.execute("UPDATE pessoas SET nome ='' WHERE idade = 30")
banco.commit()