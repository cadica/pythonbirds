class Pessoa:
    def __init__(self, nome=None, idade=50):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Ricardo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Arruda'
    print(p.nome)
    print(p.idade)
