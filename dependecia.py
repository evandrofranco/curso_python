import classes
from classes import Carro


def main():
    uno = classes.Carro('uno', 14000.4, 2000)
    fusca = Carro('fusca', 30000.3, 1957)
    print(uno.obter_tudo())
    print(fusca.obter_tudo())


if __name__ == '__main__':
    main()
