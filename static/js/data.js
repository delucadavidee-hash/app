// ═══════════════════════════════════════════
// ETF Tracker - Static Data
// ═══════════════════════════════════════════

const COLORS = {
    NAVY: '#0A2540', NAVY_DARK: '#061528', NAVY_LIGHT: '#1E3A5F',
    BLUE: '#1E5AA0', GREEN: '#0F7B3F', GREEN_LIGHT: '#86EFAC',
    RED: '#B42318', GRAY_50: '#F7F9FC', GRAY_100: '#EDF1F7',
    GRAY_200: '#DCE3ED', GRAY_400: '#8A94A6', GRAY_600: '#4B5768'
};

const ETF_DATABASE = [
    { isin: 'IE00B4L5Y983', ticker: 'SWDA', name: 'iShares Core MSCI World UCITS ETF', issuer: 'iShares', asset: 'Azionario', region: 'Globale Sviluppati', ter: 0.20, aum: 82400, price: 92.45, chg1d: 0.42, chg1y: 14.80, chg5y: 72.30, replication: 'Fisica', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 5 },
    { isin: 'IE00BK5BQT80', ticker: 'VWCE', name: 'Vanguard FTSE All-World UCITS ETF', issuer: 'Vanguard', asset: 'Azionario', region: 'Globale', ter: 0.22, aum: 18900, price: 118.22, chg1d: 0.38, chg1y: 17.70, chg5y: 68.40, replication: 'Fisica', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 5 },
    { isin: 'IE00BKM4GZ66', ticker: 'EIMI', name: 'iShares Core MSCI EM IMI UCITS ETF', issuer: 'iShares', asset: 'Azionario', region: 'Emergenti', ter: 0.18, aum: 21300, price: 32.18, chg1d: -0.24, chg1y: 9.40, chg5y: 28.60, replication: 'Fisica', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 4 },
    { isin: 'IE00B3F81R35', ticker: 'AGGH', name: 'iShares Core Global Aggregate Bond UCITS ETF', issuer: 'iShares', asset: 'Obbligazionario', region: 'Globale', ter: 0.10, aum: 5800, price: 48.32, chg1d: 0.08, chg1y: -2.50, chg5y: -8.20, replication: 'Campionamento', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 4 },
    { isin: 'IE00B579F325', ticker: 'SGLD', name: 'Invesco Physical Gold ETC', issuer: 'Invesco', asset: 'Commodities', region: 'Globale', ter: 0.12, aum: 16400, price: 195.40, chg1d: 0.92, chg1y: 29.50, chg5y: 82.10, replication: 'Fisica', distribution: 'N/A', domicile: 'Irlanda', rating: 5 },
    { isin: 'IE00B5BMR087', ticker: 'CSSPX', name: 'iShares Core S&P 500 UCITS ETF', issuer: 'iShares', asset: 'Azionario', region: 'USA', ter: 0.07, aum: 97200, price: 548.30, chg1d: 0.55, chg1y: 18.20, chg5y: 94.50, replication: 'Fisica', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 5 },
    { isin: 'IE00B53SZB19', ticker: 'SXR8', name: 'iShares Core S&P 500 UCITS ETF (Dist)', issuer: 'iShares', asset: 'Azionario', region: 'USA', ter: 0.07, aum: 8200, price: 72.15, chg1d: 0.54, chg1y: 17.90, chg5y: 91.20, replication: 'Fisica', distribution: 'Distribuzione', domicile: 'Irlanda', rating: 4 },
    { isin: 'IE00B4WXJJ64', ticker: 'IBTM', name: 'iShares $ Treasury Bond 7-10yr UCITS ETF', issuer: 'iShares', asset: 'Obbligazionario', region: 'USA', ter: 0.07, aum: 5400, price: 193.20, chg1d: 0.14, chg1y: 1.80, chg5y: -6.20, replication: 'Fisica', distribution: 'Distribuzione', domicile: 'Irlanda', rating: 4 },
    { isin: 'IE00B1FZS798', ticker: 'IDTL', name: 'iShares $ Treasury Bond 20+yr UCITS ETF', issuer: 'iShares', asset: 'Obbligazionario', region: 'USA', ter: 0.07, aum: 1900, price: 3.82, chg1d: 0.22, chg1y: -4.60, chg5y: -28.40, replication: 'Fisica', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 3 },
    { isin: 'IE00B3VWN518', ticker: 'PHAU', name: 'WisdomTree Physical Gold', issuer: 'WisdomTree', asset: 'Commodities', region: 'Globale', ter: 0.39, aum: 3200, price: 258.40, chg1d: 0.91, chg1y: 29.10, chg5y: 81.60, replication: 'Fisica', distribution: 'N/A', domicile: 'Jersey', rating: 4 },
    { isin: 'IE00B02KXL92', ticker: 'INDA', name: 'iShares MSCI India UCITS ETF', issuer: 'iShares', asset: 'Azionario', region: 'India', ter: 0.65, aum: 1800, price: 8.92, chg1d: 0.32, chg1y: 16.40, chg5y: 68.80, replication: 'Campionamento', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 3 },
    { isin: 'IE00BKWQ0G16', ticker: 'USPY', name: 'SPDR S&P 500 UCITS ETF', issuer: 'SPDR', asset: 'Azionario', region: 'USA', ter: 0.03, aum: 13400, price: 62.80, chg1d: 0.56, chg1y: 18.30, chg5y: 94.80, replication: 'Fisica', distribution: 'Accumulazione', domicile: 'Irlanda', rating: 5 },
];

const MODEL_PORTFOLIOS = [
    { id: 'all-weather', name: 'All-Weather', author: 'Ray Dalio', philosophy: 'Bilanciato per performare in ogni scenario economico: crescita, recessione, inflazione, deflazione.', risk: 'Medio-Basso', riskLevel: 2, allocation: [{ name: 'Azioni Globali', value: 30, color: '#0A2540' }, { name: 'Treasury Lungo', value: 40, color: '#1E5AA0' }, { name: 'Treasury Medio', value: 15, color: '#5A7A9A' }, { name: 'Oro', value: 7.5, color: '#B8860B' }, { name: 'Commodities', value: 7.5, color: '#8A5A00' }], cagr: 6.8, maxDD: -12.4, sharpe: 0.82 },
    { id: 'bogleheads', name: 'Bogleheads 3-Fund', author: 'John Bogle', philosophy: 'Semplicita ed efficienza: tre ETF, massima diversificazione, costi minimi.', risk: 'Medio', riskLevel: 3, allocation: [{ name: 'MSCI World', value: 60, color: '#0A2540' }, { name: 'Emerging Markets', value: 20, color: '#1E5AA0' }, { name: 'Aggregate Bond', value: 20, color: '#5A7A9A' }], cagr: 8.1, maxDD: -22.8, sharpe: 0.71 },
    { id: 'permanent', name: 'Permanent Portfolio', author: 'Harry Browne', philosophy: 'Quattro asset non correlati in parti uguali. Minimalista, robusto, anti-crisi.', risk: 'Basso', riskLevel: 1, allocation: [{ name: 'Azioni', value: 25, color: '#0A2540' }, { name: 'Oro', value: 25, color: '#B8860B' }, { name: 'Bond Lungo', value: 25, color: '#1E5AA0' }, { name: 'Cash/Bond Breve', value: 25, color: '#5A7A9A' }], cagr: 5.9, maxDD: -8.2, sharpe: 0.74 },
    { id: 'growth', name: 'Growth 90/10', author: 'Long-term aggressive', philosophy: 'Per orizzonti lunghi (20+ anni): massimizza crescita accettando alta volatilita.', risk: 'Alto', riskLevel: 4, allocation: [{ name: 'MSCI World', value: 70, color: '#0A2540' }, { name: 'Emerging Markets', value: 20, color: '#1E5AA0' }, { name: 'Aggregate Bond', value: 10, color: '#5A7A9A' }], cagr: 9.4, maxDD: -31.5, sharpe: 0.68 },
    { id: 'coffeehouse', name: 'Coffeehouse Portfolio', author: 'Bill Schultheis', philosophy: 'Sette asset class diverse in pesi uguali tra azioni. Diversificazione smart con 40% bond.', risk: 'Medio', riskLevel: 3, allocation: [{ name: 'S&P 500 Large', value: 10, color: '#0A2540' }, { name: 'US Large Value', value: 10, color: '#1E5AA0' }, { name: 'US Small', value: 10, color: '#1E5AA0' }, { name: 'US Small Value', value: 10, color: '#6BA3E8' }, { name: 'Internazionali', value: 10, color: '#5A7A9A' }, { name: 'REITs', value: 10, color: '#B8860B' }, { name: 'Aggregate Bond', value: 40, color: '#F59E0B' }], cagr: 7.6, maxDD: -25.8, sharpe: 0.69 },
    { id: 'golden-butterfly', name: 'Golden Butterfly', author: 'Tyler (Portfolio Charts)', philosophy: 'Bilancia crescita azionaria con oro e treasuries, privilegia small cap value. Stabile e redditizio.', risk: 'Medio-Basso', riskLevel: 2, allocation: [{ name: 'US Total Stock', value: 20, color: '#0A2540' }, { name: 'US Small Value', value: 20, color: '#1E5AA0' }, { name: 'Treasury Lungo', value: 20, color: '#5A7A9A' }, { name: 'Treasury Breve', value: 20, color: '#6BA3E8' }, { name: 'Oro', value: 20, color: '#B8860B' }], cagr: 7.2, maxDD: -13.8, sharpe: 0.85 },
];

const COMMUNITY_POSTS = [
    { id: 1, user: 'Marco R.', avatar: 'MR', time: '3h fa', content: 'Dopo 4 anni di PAC mensile su VWCE, finalmente ho raggiunto i 50k investiti. Lezione piu grande: non guardare il portafoglio tutti i giorni.', likes: 127, comments: 34, portfolio: { cagr: 8.9, vol: 14.2, assets: 3 } },
    { id: 2, user: 'Sara E.', avatar: 'SE', time: '1g fa', content: 'Chiedo consiglio: ha senso aggiungere un ETF sui mercati di frontiera al mio portafoglio All-World + EM? Quale peso dare?', likes: 45, comments: 28, portfolio: { cagr: 7.4, vol: 13.8, assets: 2 } },
    { id: 3, user: 'Luca F.', avatar: 'LF', time: '2g fa', content: 'Condivido il mio portafoglio FIRE: SWDA 70%, EIMI 15%, AGGH 10%, SGLD 5%. Obiettivo indipendenza finanziaria entro il 2035.', likes: 203, comments: 67, portfolio: { cagr: 9.1, vol: 15.4, assets: 4 } },
];

const CORRELATION_MATRIX = [
    { etf: 'SWDA', SWDA: 1.00, VWCE: 0.98, EIMI: 0.72, AGGH: 0.15, SGLD: 0.08 },
    { etf: 'VWCE', SWDA: 0.98, VWCE: 1.00, EIMI: 0.78, AGGH: 0.18, SGLD: 0.10 },
    { etf: 'EIMI', SWDA: 0.72, VWCE: 0.78, EIMI: 1.00, AGGH: 0.22, SGLD: 0.14 },
    { etf: 'AGGH', SWDA: 0.15, VWCE: 0.18, EIMI: 0.22, AGGH: 1.00, SGLD: 0.31 },
    { etf: 'SGLD', SWDA: 0.08, VWCE: 0.10, EIMI: 0.14, AGGH: 0.31, SGLD: 1.00 },
];

const ALERTS_DATA = [
    { id: 1, etf: 'VWCE', isin: 'IE00BK5BQT80', type: 'below', threshold: 115, currentPrice: 118.22, active: true, channels: ['email', 'push'] },
    { id: 2, etf: 'SWDA', isin: 'IE00B4L5Y983', type: 'below', threshold: 88, currentPrice: 92.45, active: true, channels: ['email'] },
    { id: 3, etf: 'EIMI', isin: 'IE00BKM4GZ66', type: 'rebalance', threshold: 3, currentPrice: 32.18, active: true, channels: ['push'] },
    { id: 4, etf: 'SGLD', isin: 'IE00B579F325', type: 'above', threshold: 200, currentPrice: 195.40, active: true, channels: ['email', 'push'] },
];

const ACADEMY_COURSES = [
    { level: 'Base', title: "Cos'e un ETF e perche investirci", lessons: 8, duration: '45 min' },
    { level: 'Base', title: 'Scegliere il tuo primo ETF', lessons: 6, duration: '30 min' },
    { level: 'Intermedio', title: 'Asset allocation per obiettivi', lessons: 12, duration: '1h 20min' },
    { level: 'Intermedio', title: 'PAC vs PIC: strategie a confronto', lessons: 9, duration: '55 min' },
    { level: 'Avanzato', title: 'Ribilanciamento e finestre ottimali', lessons: 10, duration: '1h 15min' },
    { level: 'Avanzato', title: 'Factor investing con ETF', lessons: 14, duration: '2h 10min' },
];

// Portfolio history for chart generation
function generatePortfolioHistory(months = 60) {
    const data = [];
    let value = 30000;
    let benchmark = 30000;
    for (let i = 0; i < months; i++) {
        value = value * (1 + (0.007 + (Math.sin(i/4) * 0.004)));
        benchmark = benchmark * (1 + (0.006 + (Math.cos(i/5) * 0.003)));
        const d = new Date(2021, i, 1);
        data.push({
            month: d.toLocaleDateString('it-IT', { month: 'short', year: '2-digit' }),
            portfolio: Math.round(value),
            benchmark: Math.round(benchmark)
        });
    }
    return data;
}

function generatePriceHistory(months = 48, basePrice = 72) {
    const data = [];
    let price = basePrice;
    for (let i = 0; i < months; i++) {
        price = price * (1 + (0.005 + Math.sin(i/3) * 0.008 + Math.cos(i/7) * 0.004));
        const d = new Date(2022, i, 1);
        data.push({
            month: d.toLocaleDateString('it-IT', { month: 'short', year: '2-digit' }),
            price: Math.round(price * 100) / 100
        });
    }
    return data;
}

function generateBacktestData(range = '10Y') {
    const mapping = { '1Y': 12, '3Y': 36, '5Y': 60, '10Y': 120 };
    const n = mapping[range] || 120;
    const data = [];
    for (let i = 0; i < n; i++) {
        const t = i / 12;
        data.push({
            month: `'${14 + Math.floor(t)}`,
            myPortfolio: Math.round(10000 * Math.pow(1.084, t) + Math.sin(i/3) * 600),
            allWeather: Math.round(10000 * Math.pow(1.068, t) + Math.sin(i/4) * 350),
            benchmark: Math.round(10000 * Math.pow(1.075, t) + Math.sin(i/3.5) * 800)
        });
    }
    return data;
}

// Manual content (key chapters)
const MANUAL_MODULES = [
    {
        id: 'etf', title: 'Gli ETF', subtitle: "Tutto quello che devi sapere prima di comprarne uno",
        color: '#1E5AA0', icon: 'pie-chart',
        chapters: [
            { id: 'etf-1', num: 1, title: "Cos'e davvero un ETF", readTime: '6 min' },
            { id: 'etf-2', num: 2, title: 'Replica fisica vs sintetica', readTime: '5 min' },
            { id: 'etf-3', num: 3, title: 'I costi: TER, spread, commissioni', readTime: '7 min' },
            { id: 'etf-4', num: 4, title: 'Accumulazione vs distribuzione', readTime: '5 min' },
            { id: 'etf-5', num: 5, title: 'Come leggere il KID', readTime: '8 min' },
            { id: 'etf-6', num: 6, title: 'Liquidita, AUM e tracking error', readTime: '6 min' },
            { id: 'etf-7', num: 7, title: 'UCITS, domicilio, hedging valutario', readTime: '7 min' },
            { id: 'etf-8', num: 8, title: 'Gli errori piu comuni nella scelta', readTime: '6 min' },
        ]
    },
    {
        id: 'portfolio', title: 'Costruire il portafoglio',
        subtitle: "L'arte di mettere insieme tanti pezzi per un risultato coerente",
        color: '#0F7B3F', icon: 'briefcase',
        chapters: [
            { id: 'pf-1', num: 1, title: 'Prima di tutto: obiettivi, orizzonte, fondo emergenza', readTime: '8 min' },
            { id: 'pf-2', num: 2, title: 'Asset allocation: il 90% del risultato', readTime: '9 min' },
            { id: 'pf-3', num: 3, title: 'Rischio: volatilita e drawdown spiegati', readTime: '7 min' },
            { id: 'pf-4', num: 4, title: 'Diversificazione e correlazione', readTime: '6 min' },
            { id: 'pf-5', num: 5, title: 'PAC vs PIC: confronto numerico', readTime: '8 min' },
            { id: 'pf-6', num: 6, title: 'Quanti ETF servono davvero', readTime: '5 min' },
            { id: 'pf-7', num: 7, title: 'Ribilanciamento: quando e come', readTime: '7 min' },
            { id: 'pf-8', num: 8, title: 'Psicologia: i bias che ti rovineranno', readTime: '9 min' },
        ]
    }
];

// Chapter summaries for display
const CHAPTER_SUMMARIES = {
    'etf-1': { title: "Cos'e davvero un ETF", keyPoints: ["Un ETF e un fondo negoziato in borsa che contiene molti titoli in una sola quota", "Replica un indice in modo passivo e trasparente", "Costi molto piu bassi dei fondi attivi: tipicamente 0.10-0.30% annuo", "Diversificazione immediata con una singola operazione", "Si compra e vende in borsa come un'azione, in tempo reale"] },
    'etf-2': { title: 'Replica fisica vs sintetica', keyPoints: ["Fisica: l'ETF possiede davvero i titoli dell'indice", "Sintetica: usa uno swap con una banca per ottenere il rendimento", "Il 95% degli ETF UCITS europei e fisico", "Sintetico puo avere vantaggi fiscali sui dividendi USA", "Rischio controparte limitato al 10% per normativa UCITS"] },
    'etf-3': { title: 'I costi: TER, spread, commissioni', keyPoints: ['TER: costo annuo di gestione, il piu importante', 'Spread bid-ask: costo ad ogni operazione', 'Commissioni broker: variabili da 0 a 20+ euro', 'Su 30 anni, 1% di costi extra puo costare oltre 100.000 euro', 'Scegli broker con commissioni basse sui PAC'] },
    'etf-4': { title: 'Accumulazione vs distribuzione', keyPoints: ['ACC reinvesta automaticamente i dividendi', 'DIST te li gira sul conto', 'In Italia: 26% tasse sui dividendi DIST subito, sulle plusvalenze ACC solo alla vendita', 'Su 30 anni, ACC puo generare 10-15% di patrimonio in piu', 'In fase di accumulo: preferisci ACC'] },
    'pf-1': { title: 'Prima di tutto: obiettivi, orizzonte, fondo emergenza', keyPoints: ['Definisci obiettivo, orizzonte temporale e importo target', 'Piu lungo e l orizzonte, piu rischio puoi prenderti', 'Sotto i 5 anni, evita investimenti azionari', 'Il fondo emergenza (3-6 mesi di spese) viene prima degli ETF', 'Tieni il fondo emergenza in un conto deposito liquido'] },
    'pf-2': { title: 'Asset allocation: il 90% del risultato', keyPoints: ["L'asset allocation spiega oltre il 90% del risultato", 'Ripartire tra azioni/bond/altro conta piu della scelta del singolo ETF', 'Regola del 110 meno l eta come punto di partenza', 'Le obbligazioni servono a ridurre volatilita e drawdown', "L'allocazione strategica e fissa: si ribilancia, non si stravolge"] },
};
