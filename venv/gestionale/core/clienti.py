from dataclasses import dataclass

categoria_valide = {"Gold", "Silver", "Bronze"}

class Cliente:
    def __init__(self, name, mail, categoria):
        self.name = name
        self.mail = mail
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
       # categoria_valide = {"Gold", "Silver", "Bronze"}
        if categoria not in categoria_valide:
            raise ValueError("Categoria non valida.Scegliere fra Gold, Silver e Bronze")
        self._categoria = categoria

    def descrizione(self):  # to_String
        # "Cliente Fulvio Binachi (Gold)-fulvio@google.com
        return f"Cliente{self.name}{self.categoria}- {self.mail}"

@dataclass
class ClienteRecord:
    name:str
    mail:str
    categoria:str

def _test_modulo():
    c1 = Cliente(name="Mario Bianchi", mail="mario.bianchi@polito.it", categoria="Gold")
    #c2 = Cliente(name="Carlo Maone", mail="carlo.masone@polito.it", categoria="Silver")
    print(c1.descrizione())
    #print(c2.descrizione())

 #SEMPRE PER ESEGUIRE SOLO IL CODICE NECESSARIO E NON ALTRO DAGLI IMPORT
if (__name__=="__main__"):
    _test_modulo()