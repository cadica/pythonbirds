class Pessoa:
    def __init__(self, *filhos, nome=None, idade=70):
        self.filhos = list(filhos)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    ricardo = Pessoa(nome='Ricardo')
    antonio = Pessoa(ricardo, nome='Antonio')
    print(Pessoa.cumprimentar(antonio))
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:
        print(filho.nome)
