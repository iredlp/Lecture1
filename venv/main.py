class Prodotto:
    aliquota_iva=0.22 #variabili di classe--pvverp è la stessa per tutte le istanze che verranno create.

    def __init__(self, name: str, price:float, quantity: int, supplier=None):
        self.name = name
        self.price=None #INIZIALIZZO A ZERO
        self.price = price #IL TRATTINO BASSO MI DICE CHE è MEGLIO NON TOCCARE LA VARIABILE
        #se ne METTO __DUE DO ANCORA PIù SICUREZZA DI NON MODIFICA
        self.quantity = quantity
        self.supplier = supplier
    def valore_netto(self):
        return self._price*self.quantity

    def valore_lordo(self):
        netto=self.valore_netto()
        lordo= netto*(1+self.aliquota_iva)
        return lordo
    @classmethod
    def costruttore_con_quantita_uno(cls, name:str, price:float, supplier:str):
        cls(name,price, quantity:1, supplier)

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




myproduct1= Prodotto(name="Laptop",price=1200.0, quantity=12,supplier="ABC")
print(f"Nome prodotto: {myproduct1.name}-prezzo:{myproduct1.price}")

print(f"Il totale loro di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
p3= Prodotto.costruttore_con_quantita_uno(name:"Auricolari", price: 200.0, supplier:"ABC") #Modo per chiamare metodo di classe
print(f"Prezzo scontato di myproduct1{Prodotto.applica_sconto{ myproduct1.price, percentuale:0.15)}") #Modo per chiamare un metodo statico

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
    def __init__(self,nome,mail,categoria):
        self.nome=nome
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
        return f"Cliente{self.nome}{self.categoria}- {self.mail }"

c1= Cliente(nome: "Mario Bianchi", mail="mario.bianchi@polito.it",categoria="Gold")
c2 = Cliente(nome: "Carlo Maone", mail = "carlo.masone@polito.it", categoria = "Platinum")
print(c1.descrzione())
print(c2.descrzione())
