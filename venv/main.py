class Prodotto:
    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)