class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=70):
        self.filhos = list(filhos)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    del antonio.filhos
    antonio.sobrenome = 'Arruda'
    antonio.olhos = 4
    del antonio.olhos
    print(antonio.__dict__)
    print(ricardo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(antonio.olhos)
    print(ricardo.olhos)
    print(id(Pessoa.olhos), id(antonio.olhos), id(ricardo.olhos))
    print(Pessoa.metodo_statico(), ricardo.metodo_statico(), antonio.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), antonio.nome_e_atributos_de_classe())
