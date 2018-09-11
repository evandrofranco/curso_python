
class Pessoa():
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return 'nome: %s' % (self.nome)

    def __repr__(self):
        return 'Pessoa <%s>' % str(self)


def read():
    f = open('dados.csv', 'r')
    pessoas = []
    for i in f:
        p = i.split(',')
        pessoa = Pessoa(p[0], p[1], p[2])
        pessoas.append(pessoa)
        print(pessoa)
    print(pessoas)
    return pessoas


def write():
    pessoas = read()
    f = open('pessoas.txt', 'w')
    for i in pessoas:
        f.write(str(i) + '\n')
    f.close()


write()
