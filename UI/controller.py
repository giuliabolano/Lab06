import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # metodo che serve come gestore di eventi che riceve l'oggetto evento (e) generato quando l'utente compie un'azione grafica es cliccare pulsante
    def handle_cerca(self,e):
        #gestisce l'evento di ricerca degli strumenti in base al tipo inserito
        tipo= self._view.input_tipo_strumento.value #legge il testo che l'utente ha scritto dentro la casella di input

        if not tipo: #se la casella è vuota
            self._view.show_alert("Inserisci un tipo di strumento valido!!")
            return

        strumenti= self._model.cerca_strumenti_per_tipo(tipo) #passa il metodo scritto in model.py

        self._view.lista_strumenti.controls.clear() #pulisce la lista visiva precedente
        if not strumenti:
            self._view.show_alert("Nessuno strumento trovato per questo tipo.")
        else:
            for s in strumenti:
                #trasforma i dati ottenuti dalla ricerca in elementi grafici testuali visibili all'utente
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        self._view.update() #aggiorna pagina flet



    def handle_mostra(self, e):
        #gestisce la visualizzazione di tutti gli strumenti presenti nel database
        #metodo che scatta quando si schiacca bottone mostra
        strumenti = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()
        if not strumenti:
            self._view.show_alert("Il database è vuoto o non ci sono strumenti")
        else:
            for s in strumenti:
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        self._view.update()
