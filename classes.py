
class Veiculo():

    def __init__(self, ano):
        self.ano = ano

    def obter_ano(self):
        return 'O ano de frabricação é: %s' % (self.ano)


class Carro(Veiculo):

    def __init__(self, modelo, preco, ano):
        Veiculo.__init__(self, ano)
        self.modelo = modelo
        self.preco = preco

    def obter_tudo(self):
        return 'O carro %s, custa R$ %.2f e foi fabricado em: %s' %\
            (self.modelo, self.preco, Veiculo.obter_ano(self))

    def __str__(self):
        return '<%s (%s)>:%s' % (self.modelo, self.ano, self.preco)

    def __repr__(self):
        return 'Carro[%s]' % str(self)


def main():
    uno = Carro('uno', 14000.4, 2000)
    gol = Carro('gol', 15000, 2006)
    fusca = Carro('fusca', 35000, 1975)
    carros = [uno, gol, fusca]
    print(carros)
    print(uno)
    print(uno.obter_ano())
    print(uno.obter_tudo())


if __name__ == '__main__':
    main()
