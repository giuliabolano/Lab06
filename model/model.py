from database import DB_connect
from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        #codice per connettersi al database, eseguire la query ed estrarre la lista degli oggetti
        cnx= DB_connect.get_connection()  #richiama la classe di connessione per aprire il canale di comunicazione con il database SQL del progetto
        elenco_strumenti= [] #dizionario vuoto per riempirlo poi degli oggetti strumento
        if cnx is not None: #controllo sicurezza per verificare che la connessione sia andata a buon fine e non sia None
            cursore = cnx.cursor(dictionary=True) #crea un cursore che esegue la query, impostando dictionary=True per fare in modo
            #che ogni riga del database venga letta come un dizionario chiave-valore
            query= """ SELECT * FROM strumento """
            cursore.execute(query) #prende tutte le colonne dalla tabella strumento
            for row in cursore:
                elenco_strumenti.append(Strumento(codice=row['codice'],
                                        tipo=row['tipo'],
                                        marca=row['marca'],
                                        anno_acquisto= row['anno_acquisto'],
                                        valore= row['valore'],
                                        disponibile= row['disponibile'])) #oppure mettevo Strumwnto(**row)
            cursore.close()
            cnx.close() #si chiude il cursore e la connessione con il database
            return elenco_strumenti
        return None



    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        tutti_gli_strumenti = self.get_strumenti()

        if tutti_gli_strumenti is None:
            return []

        risultati_filtrati = []
        for strumento in tutti_gli_strumenti:
                # Controlliamo se la stringa cercata è contenuta nel tipo dello strumento
            if tipo.lower() in strumento.tipo.lower():
                risultati_filtrati.append(strumento)

        return risultati_filtrati



