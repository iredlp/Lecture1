from dataclasses import dataclass


class Prodotto:
    aliquota_iva=0.22 #variabili di classe--pvverp è la stessa per tutte le istanze che verranno create.

    def __init__(self, name: str, price:float, quantity: int, supplier=None):
        self.name = name
        self._price=None #INIZIALIZZO A ZERO
        self.price = price #IL TRATTINO BASSO MI DICE CHE è MEGLIO NON TOCCARE LA VARIABILE
                           #se ne METTO DUE DO ANCORA PIù SICUREZZA DI NON MODIFICA
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price*self.quantity

    def valore_lordo(self):
        netto=self.valore_netto()
        lordo= netto*(1+self.aliquota_iva)
        return lordo

    def prezzo_finale(self) -> float:
        return self.valore_lordo()

    @classmethod
    def costruttore_con_quantita_uno(cls, name:str, price:float, supplier:str):
        return cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)
    @property
    def price(self): #eq.getter di java
        return self._price
    @price.setter #LO POSSO FARE SE HO DEFINITO UN GETTER
    def price(self,valore):
        if(valore<0):
            raise ValueError("Attenzione il prezzo non può essere negativo")
            pass
        self._price=valore

#PER ESSERE STAMPATO
    def __str__(self): #rappresento in stringa
        return f"{self.name}- disponibili {self.quantity} pezzi a {self.price}£"

    #per stampare in modo più leggibile al programmatore
    def __repr__(self):
        return f"Prodotto (name= { self.name}, price= { self.price}, quantity= { self.quantity}, supplier={ self.supplier}) "

    def __eq__(self,other:object):
       if not isinstance(other,Prodotto):
           return NotImplemented
       return (self.name==other.name
                and self.price==other.price
                and self.quantity==other.quantity
                and self.supplier==other.supplier )

    def __lt__(self, other:"Prodotto")-> bool:
        return self.price<other.price

#EREDITARIETA'
class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price:float, quantity: int, supplier:str, sconto_percento:float ):
       # Prodotto.__init__()
        #oppure se non mi ricordo da quale costruttore eredito posso fare
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento=sconto_percento

    def prezzo_finale(self)->float:
        return self.price*(1+self.aliquota_iva)
                #self.valore_lordo()*(1-self.sconto_percento/100))

class Servizio(Prodotto):
    def __init__(self, name:str, tariffa_oraria:float, ore: int):
        super().__init__(name=name, price=tariffa_oraria, quantity=1,supplier=None)
        self.ore=ore

    def prezzo_finale(self)->float:
        return self.price*self.ore


@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario:float

MAX_QUANTITA=1000
def crea_prodotto_standard(nome:str, prezzo:float):
    return Prodotto(nome, prezzo, quantity=1, supplier=None)

def _test_modulo():
    print("Sto testando il modulo del prodotti.py")
    myproduct1= Prodotto(name="Laptop",price=1200.0, quantity=12,supplier="ABC")
    print(f"Nome prodotto: {myproduct1.name}-prezzo:{myproduct1.price}")

    print(f"Il totale loro di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
    p3= Prodotto.costruttore_con_quantita_uno(name="Auricolari", price= 200.0, supplier="ABC") #Modo per chiamare metodo di classe
    #print(f"Prezzo scontato di myproduct1{Prodotto.applica_sconto{ myproduct1.price, percentuale:0.15)}") #Modo per chiamare un metodo statico

    myproduct2 = Prodotto(name="Mouse", price=10.0, quantity=25, supplier="CDE")
    print(f"Nome prodotto: {myproduct2.name}-prezzo:{myproduct2.price}")

    print(f"Valore lordo myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva=0.24
    print(f"Valore lordo myproduct1: {myproduct1.valore_lordo()}")


    #Scrivere una classe Cliente che abbia i campi "nome","email","categoria" ("Gold", "Silver","Broze")
    #vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
    #che deve restituire una stringa formattata as esempio
    #"Cliente Fulvio Bianchi (Gold)-fulvio@google.com"

    #Si modifichi la classe cliente in maniera tale che la proprietà categoria sia protetta e accetti solo
        #GOLD, SILVER E BRONZE


    p_a= Prodotto(name="Laptop",price=1200.0, quantity=12,supplier="ABC")
    p_b=Prodotto(name="Mouse", price=10.0, quantity=14, supplier="CDE")

    print("-----------------------------------------------------------------")

    print("myproduct1==p_a?",myproduct1==p_a) #va a chiamare il metdodo __eq__ appena implementto emi aspetto True
    print("p_a==p_b?",p_a==p_b) #Mi aspetto False

    mylist=[p_a,p_b, myproduct1]
    mylist.sort() #se metto REVERSE==True inverte l'ordinamento
    print("lista di prodotti ordinata")
    for p in mylist:
        print(f"-{p} ")
    print(mylist)

#Questo serve per non far leggere il codice eseguibile quando si chiama l'import e non avere parte di codice inutile
if (__name__=="__main__"):
    _test_modulo()