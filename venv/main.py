#from datetime import date
from venv.gestionale.core.prodotti import Prodotto, crea_prodotto_standard,ProdottoScontato,ProdottoRecord
from venv.gestionale.core.clienti import Cliente, ClienteRecord
#from venv.vendite.fatture import Fattura
from venv.vendite.ordini import Ordine, OrdineConSconto, RigaOrdine
import networkx as nx

print("==============================================================")

p1=Prodotto("Ebook Reader", price=120.0, quantity=1, supplier="AAA")
p2= crea_prodotto_standard("Tablet", prezzo=750)
print("==============================================================")

print(p1)
print(p2)

#MODI PER IMPORTARE
#1)
from venv.gestionale.core.prodotti import ProdottoScontato
p21=ProdottoScontato(name="Auricolari", price=230, quantity=1, supplier="AAA", sconto_percento=10)

#2)
from venv.gestionale.core.prodotti import ProdottoScontato as ps #così rinomino
p3=ps(name="Auricolari", price=230, quantity=1, supplier="ABC", sconto_percento= 10)

#3)
from venv.gestionale.core import prodotti
from venv.gestionale.core import prodotti as p

#HO IMPORTATO TUTTO IL MODULO

#4)
p4= prodotti.ProdottoScontato(name="Auricolari", price=230, quantity=1, supplier="ABC", sconto_percento= 10)

p5=p.ProdottoScontato(name="Auricolari", price=230, quantity=1, supplier="ABC",sconto_percento= 10)
print("==============================================================")

c1=Cliente(name="Maio Rossi", mail="mail@gmail.com", categoria="Gold")
print(c1.descrizione())


    #NB: la @ accanro ai metodi vuol dire che stiamo scrivendo in override ereditando
    #se ho la freccia in alto indica che è un ovverride di qulcosa prima, se in basso mi indica che il metodo sarà sovrascritto  nel codice sotto

cliente1= ClienteRecord("Mario Rossi","mariorossi@gmail.com","Gold")
p1= prodotti.ProdottoRecord("Laptop", 1200.0)
p2= prodotti.ProdottoRecord("Mouse", 20.0)
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

#fattura = Fattura(ordine, "2026/01", date.today())
#print(fattura.genera_fattura())