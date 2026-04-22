"""
ETF Tracker - Flask Application
Portfolio tracking, ETF search, analytics, and community.
"""

from flask import Flask, render_template, jsonify, request, session
from flask_cors import CORS
from functools import wraps
import os
import json
from datetime import datetime, timedelta
import secrets

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
CORS(app)

# ─── DATA STORE (in-memory with JSON persistence) ───
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data_store.json')

def load_data():
    """Load data from JSON file or return defaults."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'users': {},
        'portfolios': {},
        'alerts': [],
        'community_posts': [],
        'settings': {},
        'onboarding': {}
    }

def save_data(data):
    """Persist data to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, default=str)

data_store = load_data()

# ─── AUTH DECORATOR ───
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated

# ═══════════════════════════════════════════════════════════
# ROUTES
# ═══════════════════════════════════════════════════════════

@app.route('/')
def index():
    """Main application entry point."""
    return render_template('index.html')

# ─── AUTH API ───

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login or register a user."""
    payload = request.get_json() or {}
    email = payload.get('email', '').lower().strip()
    name = payload.get('name', 'Investitore')
    auth_method = payload.get('method', 'email')
    
    if not email:
        return jsonify({'error': 'Email required'}), 400
    
    user_id = secrets.token_hex(16)
    session['user_id'] = user_id
    session['email'] = email
    session['name'] = name
    
    if email not in data_store['users']:
        data_store['users'][email] = {
            'name': name,
            'email': email,
            'auth_method': auth_method,
            'created_at': datetime.now().isoformat(),
            'portfolio': [],
            'settings': {
                'currency': 'EUR',
                'language': 'it',
                'theme': 'dark',
                'hide_values': False,
                'email_alerts': True,
                'email_newsletter': True,
                'push_alerts': True
            }
        }
        save_data(data_store)
    
    return jsonify({
        'success': True,
        'user': {
            'email': email,
            'name': data_store['users'][email]['name'],
            'initials': ''.join(w[0] for w in data_store['users'][email]['name'].split())[:2].upper()
        }
    })

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """Clear session."""
    session.clear()
    return jsonify({'success': True})

@app.route('/api/auth/me')
def me():
    """Get current user info."""
    if 'user_id' not in session:
        return jsonify({'authenticated': False})
    email = session.get('email', '')
    user = data_store['users'].get(email, {})
    return jsonify({
        'authenticated': True,
        'user': {
            'email': email,
            'name': user.get('name', session.get('name', 'Investitore')),
            'initials': ''.join(w[0] for w in user.get('name', session.get('name', 'Investitore')).split())[:2].upper()
        }
    })

# ─── PORTFOLIO API ───

@app.route('/api/portfolio', methods=['GET'])
@login_required
def get_portfolio():
    """Get user's portfolio holdings."""
    email = session['email']
    user = data_store['users'].get(email, {})
    return jsonify(user.get('portfolio', []))

@app.route('/api/portfolio', methods=['POST'])
@login_required
def update_portfolio():
    """Add/update portfolio holdings."""
    email = session['email']
    payload = request.get_json() or {}
    holdings = payload.get('holdings', [])
    
    if email in data_store['users']:
        data_store['users'][email]['portfolio'] = holdings
        save_data(data_store)
    
    return jsonify({'success': True, 'holdings': holdings})

@app.route('/api/portfolio/etf', methods=['POST'])
@login_required
def add_etf_to_portfolio():
    """Add a single ETF to portfolio."""
    email = session['email']
    payload = request.get_json() or {}
    
    new_etf = {
        'isin': payload.get('isin'),
        'ticker': payload.get('ticker'),
        'name': payload.get('name'),
        'shares': float(payload.get('shares', 0)),
        'avgPrice': float(payload.get('avgPrice', 0)),
        'currentPrice': float(payload.get('currentPrice', 0)),
        'asset': payload.get('asset', ''),
        'region': payload.get('region', ''),
        'weight': float(payload.get('weight', 0)),
        'added_at': datetime.now().isoformat()
    }
    
    if email in data_store['users']:
        portfolio = data_store['users'][email].get('portfolio', [])
        existing = next((h for h in portfolio if h['isin'] == new_etf['isin']), None)
        if existing:
            total_shares = existing['shares'] + new_etf['shares']
            total_cost = existing['shares'] * existing['avgPrice'] + new_etf['shares'] * new_etf['avgPrice']
            existing['shares'] = total_shares
            existing['avgPrice'] = total_cost / total_shares if total_shares > 0 else 0
        else:
            portfolio.append(new_etf)
        data_store['users'][email]['portfolio'] = portfolio
        save_data(data_store)
        return jsonify({'success': True, 'portfolio': portfolio})
    
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/portfolio/etf/<isin>', methods=['DELETE'])
@login_required
def remove_etf_from_portfolio(isin):
    """Remove an ETF from portfolio."""
    email = session['email']
    if email in data_store['users']:
        portfolio = data_store['users'][email].get('portfolio', [])
        portfolio = [h for h in portfolio if h['isin'] != isin]
        data_store['users'][email]['portfolio'] = portfolio
        save_data(data_store)
        return jsonify({'success': True, 'portfolio': portfolio})
    return jsonify({'error': 'User not found'}), 404

# ─── ALERTS API ───

@app.route('/api/alerts', methods=['GET'])
@login_required
def get_alerts():
    """Get user's price alerts."""
    email = session['email']
    alerts = [a for a in data_store['alerts'] if a.get('user_email') == email]
    return jsonify(alerts)

@app.route('/api/alerts', methods=['POST'])
@login_required
def create_alert():
    """Create a new price alert."""
    email = session['email']
    payload = request.get_json() or {}
    
    alert = {
        'id': secrets.token_hex(8),
        'user_email': email,
        'etf': payload.get('etf', ''),
        'isin': payload.get('isin', ''),
        'type': payload.get('type', 'below'),
        'threshold': float(payload.get('threshold', 0)),
        'currentPrice': float(payload.get('currentPrice', 0)),
        'active': True,
        'channels': payload.get('channels', ['email']),
        'created_at': datetime.now().isoformat()
    }
    
    data_store['alerts'].append(alert)
    save_data(data_store)
    return jsonify({'success': True, 'alert': alert})

@app.route('/api/alerts/<alert_id>', methods=['PATCH'])
@login_required
def toggle_alert(alert_id):
    """Toggle alert active state."""
    for alert in data_store['alerts']:
        if alert['id'] == alert_id and alert.get('user_email') == session.get('email'):
            alert['active'] = not alert['active']
            save_data(data_store)
            return jsonify({'success': True, 'alert': alert})
    return jsonify({'error': 'Alert not found'}), 404

@app.route('/api/alerts/<alert_id>', methods=['DELETE'])
@login_required
def delete_alert(alert_id):
    """Delete an alert."""
    data_store['alerts'] = [a for a in data_store['alerts'] 
                           if not (a['id'] == alert_id and a.get('user_email') == session.get('email'))]
    save_data(data_store)
    return jsonify({'success': True})

# ─── COMMUNITY API ───

@app.route('/api/community/posts', methods=['GET'])
def get_community_posts():
    """Get community posts."""
    return jsonify(data_store.get('community_posts', []))

@app.route('/api/community/posts', methods=['POST'])
@login_required
def create_post():
    """Create a community post."""
    payload = request.get_json() or {}
    post = {
        'id': secrets.token_hex(8),
        'user': payload.get('user', session.get('name', 'Anonimo')),
        'avatar': payload.get('avatar', 'AN'),
        'content': payload.get('content', ''),
        'likes': 0,
        'comments': [],
        'created_at': datetime.now().isoformat()
    }
    data_store['community_posts'].insert(0, post)
    save_data(data_store)
    return jsonify({'success': True, 'post': post})

@app.route('/api/community/posts/<post_id>/like', methods=['POST'])
def like_post(post_id):
    """Like/unlike a post."""
    for post in data_store['community_posts']:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            save_data(data_store)
            return jsonify({'success': True, 'likes': post['likes']})
    return jsonify({'error': 'Post not found'}), 404

# ─── SETTINGS API ───

@app.route('/api/settings', methods=['GET'])
@login_required
def get_settings():
    """Get user settings."""
    email = session['email']
    user = data_store['users'].get(email, {})
    return jsonify(user.get('settings', {}))

@app.route('/api/settings', methods=['POST'])
@login_required
def update_settings():
    """Update user settings."""
    email = session['email']
    payload = request.get_json() or {}
    if email in data_store['users']:
        data_store['users'][email]['settings'].update(payload)
        save_data(data_store)
        return jsonify({'success': True, 'settings': data_store['users'][email]['settings']})
    return jsonify({'error': 'User not found'}), 404

# ─── ONBOARDING API ───

@app.route('/api/onboarding', methods=['POST'])
@login_required
def save_onboarding():
    """Save onboarding preferences."""
    email = session['email']
    payload = request.get_json() or {}
    data_store['onboarding'][email] = payload
    save_data(data_store)
    return jsonify({'success': True})

# ─── STATIC DATA API ───

@app.route('/api/data/etf')
def get_etf_data():
    """Return all ETF data."""
    return jsonify(ETF_DATABASE)

@app.route('/api/data/etf/<isin>')
def get_etf_detail(isin):
    """Return single ETF detail."""
    etf = next((e for e in ETF_DATABASE if e['isin'] == isin), None)
    if etf:
        return jsonify(etf)
    return jsonify({'error': 'ETF not found'}), 404

@app.route('/api/data/models')
def get_model_portfolios():
    """Return model portfolios."""
    return jsonify(MODEL_PORTFOLIOS)

@app.route('/api/data/backtest')
def get_backtest_data():
    """Return backtest historical data."""
    return jsonify(BACKTEST_DATA)

# ═══════════════════════════════════════════════════════════
# STATIC DATA
# ═══════════════════════════════════════════════════════════

ETF_DATABASE = [
    {"isin": "IE00B4L5Y983", "ticker": "SWDA", "name": "iShares Core MSCI World UCITS ETF", "issuer": "iShares", "asset": "Azionario", "region": "Globale Sviluppati", "ter": 0.20, "aum": 82400, "price": 92.45, "chg1d": 0.42, "chg1y": 14.80, "chg5y": 72.30, "replication": "Fisica", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 5},
    {"isin": "IE00BK5BQT80", "ticker": "VWCE", "name": "Vanguard FTSE All-World UCITS ETF", "issuer": "Vanguard", "asset": "Azionario", "region": "Globale", "ter": 0.22, "aum": 18900, "price": 118.22, "chg1d": 0.38, "chg1y": 17.70, "chg5y": 68.40, "replication": "Fisica", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 5},
    {"isin": "IE00BKM4GZ66", "ticker": "EIMI", "name": "iShares Core MSCI EM IMI UCITS ETF", "issuer": "iShares", "asset": "Azionario", "region": "Emergenti", "ter": 0.18, "aum": 21300, "price": 32.18, "chg1d": -0.24, "chg1y": 9.40, "chg5y": 28.60, "replication": "Fisica", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 4},
    {"isin": "IE00B3F81R35", "ticker": "AGGH", "name": "iShares Core Global Aggregate Bond UCITS ETF", "issuer": "iShares", "asset": "Obbligazionario", "region": "Globale", "ter": 0.10, "aum": 5800, "price": 48.32, "chg1d": 0.08, "chg1y": -2.50, "chg5y": -8.20, "replication": "Campionamento", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 4},
    {"isin": "IE00B579F325", "ticker": "SGLD", "name": "Invesco Physical Gold ETC", "issuer": "Invesco", "asset": "Commodities", "region": "Globale", "ter": 0.12, "aum": 16400, "price": 195.40, "chg1d": 0.92, "chg1y": 29.50, "chg5y": 82.10, "replication": "Fisica", "distribution": "N/A", "domicile": "Irlanda", "rating": 5},
    {"isin": "IE00B5BMR087", "ticker": "CSSPX", "name": "iShares Core S&P 500 UCITS ETF", "issuer": "iShares", "asset": "Azionario", "region": "USA", "ter": 0.07, "aum": 97200, "price": 548.30, "chg1d": 0.55, "chg1y": 18.20, "chg5y": 94.50, "replication": "Fisica", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 5},
    {"isin": "IE00B3VWN518", "ticker": "PHAU", "name": "WisdomTree Physical Gold", "issuer": "WisdomTree", "asset": "Commodities", "region": "Globale", "ter": 0.39, "aum": 3200, "price": 258.40, "chg1d": 0.91, "chg1y": 29.10, "chg5y": 81.60, "replication": "Fisica", "distribution": "N/A", "domicile": "Jersey", "rating": 4},
    {"isin": "IE00B02KXL92", "ticker": "INDA", "name": "iShares MSCI India UCITS ETF", "issuer": "iShares", "asset": "Azionario", "region": "India", "ter": 0.65, "aum": 1800, "price": 8.92, "chg1d": 0.32, "chg1y": 16.40, "chg5y": 68.80, "replication": "Campionamento", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 3},
    {"isin": "IE00BKWQ0G16", "ticker": "USPY", "name": "SPDR S&P 500 UCITS ETF", "issuer": "SPDR", "asset": "Azionario", "region": "USA", "ter": 0.03, "aum": 13400, "price": 62.80, "chg1d": 0.56, "chg1y": 18.30, "chg5y": 94.80, "replication": "Fisica", "distribution": "Accumulazione", "domicile": "Irlanda", "rating": 5},
    {"isin": "IE00BFMXYX26", "ticker": "VUKE", "name": "Vanguard FTSE 100 UCITS ETF", "issuer": "Vanguard", "asset": "Azionario", "region": "UK", "ter": 0.09, "aum": 3900, "price": 38.40, "chg1d": 0.11, "chg1y": 7.20, "chg5y": 25.40, "replication": "Fisica", "distribution": "Distribuzione", "domicile": "Irlanda", "rating": 4},
    {"isin": "LU0292107645", "ticker": "XCHA", "name": "Xtrackers MSCI China UCITS ETF", "issuer": "Xtrackers", "asset": "Azionario", "region": "Cina", "ter": 0.65, "aum": 780, "price": 12.40, "chg1d": -0.82, "chg1y": -8.20, "chg5y": -18.40, "replication": "Sintetica", "distribution": "Accumulazione", "domicile": "Lussemburgo", "rating": 2},
    {"isin": "IE00B810Q511", "ticker": "VECP", "name": "Vanguard EUR Corporate Bond UCITS ETF", "issuer": "Vanguard", "asset": "Obbligazionario", "region": "Eurozona", "ter": 0.09, "aum": 3800, "price": 48.20, "chg1d": 0.06, "chg1y": 4.80, "chg5y": -2.40, "replication": "Campionamento", "distribution": "Distribuzione", "domicile": "Irlanda", "rating": 4},
    {"isin": "IE00BZ163G84", "ticker": "VGEA", "name": "Vanguard EUR Eurozone Government Bond UCITS ETF", "issuer": "Vanguard", "asset": "Obbligazionario", "region": "Eurozona", "ter": 0.07, "aum": 2400, "price": 22.40, "chg1d": 0.10, "chg1y": 1.60, "chg5y": -6.80, "replication": "Campionamento", "distribution": "Distribuzione", "domicile": "Irlanda", "rating": 4},
]

MODEL_PORTFOLIOS = [
    {
        "id": "all-weather", "name": "All-Weather", "author": "Ray Dalio",
        "philosophy": "Bilanciato per performare in ogni scenario economico: crescita, recessione, inflazione, deflazione.",
        "risk": "Medio-Basso", "riskLevel": 2,
        "allocation": [
            {"name": "Azioni Globali", "value": 30, "color": "#0A2540"},
            {"name": "Treasury Lungo", "value": 40, "color": "#1E5AA0"},
            {"name": "Treasury Medio", "value": 15, "color": "#5A7A9A"},
            {"name": "Oro", "value": 7.5, "color": "#B8860B"},
            {"name": "Commodities", "value": 7.5, "color": "#8A5A00"}
        ],
        "cagr": 6.8, "maxDD": -12.4, "sharpe": 0.82
    },
    {
        "id": "bogleheads", "name": "Bogleheads 3-Fund", "author": "John Bogle",
        "philosophy": "Semplicita ed efficienza: tre ETF, massima diversificazione, costi minimi.",
        "risk": "Medio", "riskLevel": 3,
        "allocation": [
            {"name": "MSCI World", "value": 60, "color": "#0A2540"},
            {"name": "Emerging Markets", "value": 20, "color": "#1E5AA0"},
            {"name": "Aggregate Bond", "value": 20, "color": "#5A7A9A"}
        ],
        "cagr": 8.1, "maxDD": -22.8, "sharpe": 0.71
    },
    {
        "id": "permanent", "name": "Permanent Portfolio", "author": "Harry Browne",
        "philosophy": "Quattro asset non correlati in parti uguali. Minimalista, robusto, anti-crisi.",
        "risk": "Basso", "riskLevel": 1,
        "allocation": [
            {"name": "Azioni", "value": 25, "color": "#0A2540"},
            {"name": "Oro", "value": 25, "color": "#B8860B"},
            {"name": "Bond Lungo", "value": 25, "color": "#1E5AA0"},
            {"name": "Cash/Bond Breve", "value": 25, "color": "#5A7A9A"}
        ],
        "cagr": 5.9, "maxDD": -8.2, "sharpe": 0.74
    },
    {
        "id": "growth", "name": "Growth 90/10", "author": "Long-term aggressive",
        "philosophy": "Per orizzonti lunghi (20+ anni): massimizza crescita accettando alta volatilita.",
        "risk": "Alto", "riskLevel": 4,
        "allocation": [
            {"name": "MSCI World", "value": 70, "color": "#0A2540"},
            {"name": "Emerging Markets", "value": 20, "color": "#1E5AA0"},
            {"name": "Aggregate Bond", "value": 10, "color": "#5A7A9A"}
        ],
        "cagr": 9.4, "maxDD": -31.5, "sharpe": 0.68
    }
]

# Generate backtest data
import random
random.seed(42)
BACKTEST_DATA = []
base_months = 120
for i in range(base_months):
    t = i / 12
    BACKTEST_DATA.append({
        "month": f"'{int(14 + t)}",
        "myPortfolio": round(10000 * (1.084 ** t) + (i % 5 - 2) * 200),
        "allWeather": round(10000 * (1.068 ** t) + (i % 7 - 3) * 150),
        "benchmark": round(10000 * (1.075 ** t) + (i % 6 - 3) * 180)
    })

# Default community posts
if not data_store.get('community_posts'):
    data_store['community_posts'] = [
        {
            "id": "post1", "user": "Marco R.", "avatar": "MR", "time": "3h fa",
            "content": "Dopo 4 anni di PAC mensile su VWCE, finalmente ho raggiunto i 50k investiti. Lezione piu grande: non guardare il portafoglio tutti i giorni.",
            "likes": 127, "comments": [
                {"user": "InvestorPro", "avatar": "IP", "time": "2h fa", "content": "Ottimo risultato! Anche io su VWCE da 3 anni.", "likes": 24},
                {"user": "LongTermView", "avatar": "LT", "time": "4h fa", "content": "Concordo. Non cercare di fare market timing con il PAC.", "likes": 18}
            ],
            "portfolio": {"cagr": 8.9, "vol": 14.2, "assets": 3}
        },
        {
            "id": "post2", "user": "Sara E.", "avatar": "SE", "time": "1g fa",
            "content": "Chiedo consiglio: ha senso aggiungere un ETF sui mercati di frontiera al mio portafoglio All-World + EM? Quale peso dare?",
            "likes": 45, "comments": [
                {"user": "ETFGuru", "avatar": "EG", "time": "6h fa", "content": "Considera di diversificare con un 5-10% di mercati di frontiera.", "likes": 12}
            ],
            "portfolio": {"cagr": 7.4, "vol": 13.8, "assets": 2}
        },
        {
            "id": "post3", "user": "Luca F.", "avatar": "LF", "time": "2g fa",
            "content": "Condivido il mio portafoglio FIRE: SWDA 70%, EIMI 15%, AGGH 10%, SGLD 5%. Obiettivo indipendenza finanziaria entro il 2035.",
            "likes": 203, "comments": [
                {"user": "SaraETF", "avatar": "SE", "time": "8h fa", "content": "Complimenti! Quale broker usi per i PAC automatici?", "likes": 7}
            ],
            "portfolio": {"cagr": 9.1, "vol": 15.4, "assets": 4}
        }
    ]
    save_data(data_store)

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
