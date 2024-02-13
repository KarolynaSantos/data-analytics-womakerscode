import sqlite3

conexao = sqlite3.connect('Banco')
cursor = conexao.cursor()


# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('''CREATE TABLE alunos( id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));''')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterio

cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Karolyna", 25, "Data Scienci")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Phillip", 28, "Engenharia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Ygor", 27, "Engenharia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Nina", 19, "Psicologa")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Livia", 20, "Biologia")')

# 3. Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * from alunos')
for alunos in dados:
  print(alunos)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

dados = cursor.execute('SELECT nome, idade from alunos where idade > 20')
for alunos in dados:
  print(alunos)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

dados = cursor.execute('SELECT * from alunos where curso = "Engenharia" ORDER BY nome')
for alunos in dados:
  print(alunos)

# d) Contar o número total de alunos na tabela

dados = cursor.execute('SELECT count(id) from alunos')
for alunos in dados:
   print(alunos)

# 4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
  
cursor.execute('UPDATE alunos SET idade = 20 where nome = "Karolyna"')

#b) Remova um aluno pelo seu ID.

cursor.execute('DELETE from alunos where id = 2')

#5. Criar uma Tabela e Inserir Dados Crie uma tabela chamada "clientes" com os campos: id (chaveprimária), nome (texto), idade (inteiro) e saldo (float). 

cursor.execute('CREATE TABLE clientes( id INT, nome VARCHAR(100), idade INT, saldo float);')

# Insira alguns registros de clientes na tabela.

cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Karolyna", 25, 220)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Phillip", 28, 340)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Gabriel", 27, 5)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Bruna", 52, 2500)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Amanda", 32, 1300)')

# 6. Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefa

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados = cursor.execute('SELECT nome, idade from clientes where idade > 30')
for clientes in dados:
  print(clientes)

# b) Calcule o saldo médio dos clientes.

dados = cursor.execute('SELECT avg(saldo) from clientes')
for clientes in dados:
  print(clientes)

# c) Encontre o cliente com o saldo máximo.

dados = cursor.execute('SELECT * from clientes where saldo = (select max(saldo) from clientes)')
for clientes in dados:
  print(clientes)

# d) Conte quantos clientes têm saldo acima de 1000.

dados = cursor.execute('SELECT count(id) from clientes where saldo > 1000')
for clientes in dados:
  print(clientes)

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo = 10 where id = 3')

# b) Remova um cliente pelo seu ID.

cursor.execute('DELETE from clientes where id = 5')

#8. Junção de Tabelas Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 

cursor.execute('CREATE TABLE compras( id INT, cliente_id INT, produto VACHAR(100), valor float);')

#Insira algumas compras associadas a clientes existentes na tabela "clientes".

cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Caneta", 20)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 2, "Caderno", 28)')

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

dados = cursor.execute('SELECT nome, produto, valor from clientes join compras on clientes.id = compras.id')
for clientes in dados:
  print(clientes)

conexao.commit()
conexao.close
