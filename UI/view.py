import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None

        # Non obbligatorio mettere già qui tutti gli elementi UI

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        """ Imposta il controller alla pagina """
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge Elementi di UI alla pagina e la aggiorna. """
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        # TextField per responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView per mostrare la lista di strumenti aggiornata
        self.lista_strumenti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # TextField per ricerca strumento per tipo
        self.input_tipo_strumento = ft.TextField(label="Tipo")

        # ListView per mostrare il risultato della ricerca strumenti per tipo
        self.lista_strumenti_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- PULSANTI e TOGGLE associati a EVENTI ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)

        # Altri Pulsanti da implementare (es. "Mostra" e "Cerca")
        #qua bisogna sapere cosa cercare
        self.input_tipo_strumento = ft.TextField(label="Tipo Strumento (es. Chitarra)", width= 250)

        self._btn_mostra = ft.Button("Mostra", on_click=self.controller.handle_mostra)
        #questo crea un pulsante che visualizza l'intero elenco del tipo di strumenti
        self._btn_cerca = ft.Button("Cerca", on_click=self.controller.handle_cerca)
        #questo crea un pulsante che cerca quel tipo di strumento


        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            #blocco che raggruppa la casella di testo per il tipo e i pulsanti creati prima di cerca e mostra
            #questo crea un'intestazione testuale chiara per dividere visivamente la pagina e far capire all'utente a cosa serve quella sezione
            ft.Row(controls=[ft.Text("Strumenti", size=16, weight=ft.FontWeight.BOLD), self._btn_mostra],
                   alignment=ft.MainAxisAlignment.START),

            ft.Divider(),
            # disegna una linea di separazione per staccare questa parte dai risultati sottostanti


            # Sezione 4
            # inserisco ListView che farà da contenitore per i risultati ottenuti dal database
            ft.Text("Cerca Strumenti per tipo", size=16, weight=ft.FontWeight.BOLD),
            # sistema tutto dentro una riga allineata al centro in modo ordinato
            ft.Row(controls=[self.input_tipo_strumento, self._btn_cerca], alignment=ft.MainAxisAlignment.START),
            # start = sx


            self.lista_strumenti
            #permesso a flet per stampare a schermo l'elenco degli strumenti ogni volta che il controller esegue una ricerca o preme "mostra"
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
