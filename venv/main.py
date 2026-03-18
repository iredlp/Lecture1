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
        return f"{self.name}- disponibili{self.quantity}pezzi a {self.price}£"

    #per stampare in modo più leggibile al programmatore
    def __repr__(self):
        return f"Prodotto(name= { self.name}, price= { self.price}, quantity= { self.quantity}, supplier={ self.supplier}) "

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
class Cliente:
    def __init__(self,name,mail,categoria):
        self.name=name
        self.mail=mail
        self._categoria =None
        self.categoria=categoria
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self,categoria):
        categoria_valide={"Gold","Silver","Bronze"}
        if categoria not in categoria_valide:
            raise ValueError("Categoria non valida.Scegliere fra Gold, Silver e Bronze")
        self._categoria=categoria

    def descrizione(self): #to_String
        #"Cliente Fulvio Binachi (Gold)-fulvio@google.com
        return f"Cliente{self.name}{self.categoria}- {self.mail }"

c1= Cliente(name= "Mario Bianchi", mail="mario.bianchi@polito.it",categoria="Gold")
c2 = Cliente(name= "Carlo Maone", mail = "carlo.masone@polito.it", categoria = "Silver")
print(c1.descrizione())
print(c2.descrizione())

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


my_product_scontato=ProdottoScontato(name="Auricolari",price=320, quantity=1,supplier="ABC", sconto_percento=10)
my_service=Servizio(name="Consulenta",tariffa_oraria=100.0, ore=3)

mylist.append(my_product_scontato)
mylist.append(my_service) #LI INSERISCO NELLA STESSA LISTA ANCHE SE SONO ELEMENTI DIVERSI

mylist.sort(reverse=True)

for elem in mylist:
    print(elem.name, "->", elem.prezzo_finale())

#DEF UNA CLASSE ABBONAMENTO CHE ABBIA COME ATTIRIBUTI -nome, prezzo_mensile, mesi.
#Abbonamento dovrà avere un metodo per calcolare il prezzo finale, ottenuto come prezzo_mensile*mesi
class Abbonamento(Prodotto):
    def __init__(self, name: str, prezzo_mensile: float, mesi:int):
        super().__init__(name=name, price=prezzo_mensile, quantity=1, supplier=None)
        self.name=name
        self.prezzo_mensile=prezzo_mensile
        self.mesi=mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile * self.mesi

abb=Abbonamento(name="Software gestionale", prezzo_mensile=30, mesi=24)

mylist.append(abb)
for elem in mylist:
    print(elem.name, "->", elem.prezzo_finale())

def calcola_totale(elementi):
    tot=0
    for  e in elementi:
        tot+=e.prezzo_finale()
    return tot

print(f"Il totale è: {calcola_totale(mylist)}")

#IMPORTIAMO PROTOCOLLO
from typing import Protocol

#CREO UNA CLASSE SENZA COSTRUTTORE, AVRò SOLO I METODI CHE POI LE CLASSI
# CHE VOGLIO UTILIZZARE DEVO AVERE IN calcola_totale
#serve per definire altre classi
class HaPrezzoFinale(Protocol):
    def prezzo_finale(self) -> float:
        ...
    #...come il PASS, ma nel pass sto indicando che poi ci scrverò qualcosa,
    # con i 3 puntini NON DEVO DAVVERP SCRIVERE CODICE LI, MA LO FARà UN ALTRO /ALTRE CLASSI

def calcola_totale(elementi:list[HaPrezzoFinale])->float:
    return sum(e.prezzo_finale() for e in elementi) #SCRITTURA MOLTO COMPATTA

print(f"Il totale è: {calcola_totale(mylist)} ")

print("-----------------------------------------------------------------")
print("SPERIMENTIAMO CON DATACLASS")
from dataclasses import dataclass

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario:float

@dataclass
class ClienteRecord:
    name:str
    email:str
    categoria:str

@dataclass
class RigaOrdine:
    prodotto:ProdottoRecord
    quantita: int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario*self.quantita

@dataclass
class Ordine:
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self)->float:
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self,aliquota_iva):
        return self.totale_netto()*(1+aliquota_iva)

    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineConSconto(Ordine): #eredita da ordine
    sconto_percentuale:float

    def totale_scontato(self):
        self.totale_lordo()*(1-self.sconto_percentuale)

    def totale_netto(self):
        netto_base=super().totale_netto()
        return netto_base*(1-self.sconto_percentuale)

    #NB: la @ accanro ai metodi vuol dire che stiamo scrivendo in override ereditando
    #se ho la freccia in alto indica che è un ovverride di qulcosa prima, se in basso mi indica che il metodo sarà sovrascritto  nel codice sotto

cliente1= ClienteRecord("Mario Rossi","mariorossi@gmail.com","Gold")
p1= ProdottoRecord("Laptop", 1200.0)
p2= ProdottoRecord("Mouse", 20.0)
ordine= Ordine([RigaOrdine(p1,1), RigaOrdine(p2,10)], cliente1)
ordine_scontato= OrdineConSconto([RigaOrdine(p1,1), RigaOrdine(p2,10)], cliente1, 0.1)


print(ordine)
print("Numero di righe nell'ordine:", ordine.numero_righe())
print("Totale netto:", ordine.totale_netto())
print("Totale lordo(IVA- 22%):", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto:", ordine_scontato.totale_netto())
print("Totale lordo scontato:", ordine_scontato.totale_lordo(0.22))
print("-----------------------------------------------------------------")