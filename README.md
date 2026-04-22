# ETF Tracker

**ETF Tracker** e un'applicazione web completa per la gestione, analisi e simulazione di portafogli ETF. Costruita con Python Flask e JavaScript vanilla, offre tutto cio che serve per investire consapevolmente.

## Funzionalita

- **Dashboard** - Riepilogo del portafoglio con KPI, grafici di andamento e allocazione per asset class
- **Ricerca ETF** - Cerca e filtra tra centinaia di ETF, confronta fino a 3 titoli contemporaneamente
- **Analisi** - Backtest storico, matrice di correlazione, volatilita, max drawdown e Sharpe ratio
- **Simulazioni** - Confronto PAC vs PIC con calcolo del potere del cost averaging
- **Portafogli Modello** - Strategie classiche (All-Weather, Bogleheads, Permanent Portfolio, ecc.)
- **Community** - Condividi strategie e interagisci con altri investitori
- **Manuale e Academy** - Guide dall'ABC degli ETF all'asset allocation avanzata
- **Alert Prezzo** - Notifiche personalizzabili su soglie di prezzo
- **Impostazioni** - Profilo, notifiche, preferenze, sicurezza e gestione dati
- **Onboarding** - Wizard iniziale per personalizzare l'esperienza
- **Tour Guidato** - Introduzione interattiva alle funzionalita principali

## Tecnologie

**Backend:**
- Python 3.11+
- Flask
- Flask-CORS
- Gunicorn (WSGI server di produzione)

**Frontend:**
- HTML5 / CSS3 / JavaScript (ES6+)
- Chart.js per i grafici
- LocalStorage per la persistenza client-side

## Requisiti

- Python 3.11 o superiore
- pip

## Installazione Locale

1. Clona il repository:
```bash
git clone https://github.com/tuo-username/etf-tracker.git
cd etf-tracker
```

2. Crea un virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure
venv\Scripts\activate  # Windows
```

3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

4. Avvia l'applicazione:
```bash
python app.py
```

5. Apri il browser all'indirizzo `http://localhost:5000`

## Deploy su Render

### Metodo 1: Blueprint (consigliato)

1. Carica il codice su GitHub
2. Crea un nuovo **Web Service** su Render
3. Collega il repository GitHub
4. Render rilevera automaticamente il file `render.yaml` e configurera il servizio

### Metodo 2: Manuale

1. Crea un nuovo **Web Service** su Render
2. Scegli **Python 3** come runtime
3. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Aggiungi la variabile d'ambiente:
   - `SECRET_KEY`: una stringa casuale di almeno 32 caratteri
   - `PYTHON_VERSION`: `3.11.0`

## Struttura del Progetto

```
etf-tracker/
|-- app.py              # Backend Flask con API REST
|-- requirements.txt    # Dipendenze Python
|-- Procfile            # Configurazione processo Render
|-- render.yaml         # Blueprint Render
|-- README.md           # Questo file
|-- templates/
|   '-- index.html      # Template HTML principale
'-- static/
    |-- css/
    |   '-- style.css   # Foglio di stile completo
    '-- js/
        |-- data.js     # Dati statici (ETF, portafogli, ecc.)
        |-- utils.js    # Funzioni di utilita e icone
        |-- charts.js   # Wrapper Chart.js
        '-- app.js      # Logica SPA principale
```

## Dati

L'applicazione include un database statico di **13 ETF** reali con:
- Dati di prezzo e performance (1D, 1Y, 5Y)
- Informazioni dettagliate (TER, AUM, replica, distribuzione)
- **6 portafogli modello** con allocazione e metriche storiche
- **6 corsi Academy** e **16 capitoli** del manuale formativo

I dati del portafoglio utente vengono salvati in **LocalStorage** (lato client).

## Autenticazione

Il sistema supporta:
- Login con email e password
- Login sociale (Google)
- Sessione persistente via LocalStorage

In modalita demo, l'autenticazione e simulata lato client per semplicita di deploy.

## Licenza

MIT License - vedi file LICENSE per i dettagli.

## Disclaimer

ETF Tracker e uno strumento di analisi e non costituisce consulenza finanziaria. Gli investimenti in ETF comportano rischi, inclusa la possibile perdita del capitale. Sempre consultare un consulente finanziario qualificato prima di prendere decisioni di investimento.
