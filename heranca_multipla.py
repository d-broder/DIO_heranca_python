class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

            
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo
    def __str__ (self):
        return self.__class__.__name__

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
    def __str__ (self):
        return "Ave"


class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "Oi, estou falando!"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
        #print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro())


#gato = Gato(nro_patas=4, cor_pelo="preto")
#print(gato)
 

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)

print(ornitorrinco.falar())
