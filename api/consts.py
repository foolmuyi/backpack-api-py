from collections import namedtuple


API_URL = 'https://api.backpack.exchange'

# CONTENT_TYPE = 'Content-Type'
X_API_KEY = 'X-API-KEY'
X_SIGNATURE = 'X-SIGNATURE'
X_TIMESTAMP = 'X-TIMESTAMP'
X_WINDOW = 'X-WINDOW'
DEFAULT_WINDOW = '5000'

# ACCEPT = 'Accept'
# COOKIE = 'Cookie'
# LOCALE = 'Locale='

# APPLICATION_JSON = 'application/json'

# Endpoint Type
PUBLIC = 'public'
AUTH = 'Authenticated'

# Request Method
GET = "GET"
POST = "POST"
PATCH = "PATCH"


Endpoint = namedtuple('Endpoint',['type', 'method', 'path', 'instruction'])

# Public Endpoints
# Assets
ASSETS = Endpoint(PUBLIC, GET, '/api/v1/assets', None)  # Get assets
COLLATERAL = Endpoint(PUBLIC, GET, '/api/v1/collateral', None) # Get collateral
# Borrow Lend Markets
BORROW_LEND_MARKETS = Endpoint(PUBLIC, GET, '/api/v1/borrowLend/markets', None)  # Get borrow lend markets
BORROW_LEND_MARKETS_HISTORY = Endpoint(PUBLIC, GET, '/api/v1/borrowLend/markets/history', None)  # Get borrow lend market history
# Markets
MARKETS = Endpoint(PUBLIC, GET, '/api/v1/markets', None)  # Get markets
MARKET = Endpoint(PUBLIC, GET, '/api/v1/market', None)  # Get market
TICKER = Endpoint(PUBLIC, GET, '/api/v1/ticker', None)  # Get ticker
TICKERS = Endpoint(PUBLIC, GET, '/api/v1/tickers', None)  # Get tickers
DEPTH = Endpoint(PUBLIC, GET, '/api/v1/depth', None)  # Get depth
K_LINES = Endpoint(PUBLIC, GET, '/api/v1/klines', None)  # Get K-lines
MARK_PRICES = Endpoint(PUBLIC, GET, '/api/v1/markPrices', None)  # Get all mark prices
OPEN_INTEREST = Endpoint(PUBLIC, GET, '/api/v1/openInterest', None)  # Get open interest
FUNDING_RATES = Endpoint(PUBLIC, GET, '/api/v1/fundingRates', None)  # Get funding interval rates
# System
STATUS = Endpoint(PUBLIC, GET, '/api/v1/status', None)  # Status
PING = Endpoint(PUBLIC, GET, '/api/v1/ping', None)  # Ping
SYSTEM_TIME = Endpoint(PUBLIC, GET, '/api/v1/time', None)  # Get system time
# Trades
RECENT_TRADES = Endpoint(PUBLIC, GET, '/api/v1/trades', None)  # Get recent trades
HISTORICAL_TRADES = Endpoint(PUBLIC, GET, '/api/v1/trades/history', None)  # Get historical trades

# Authenticated Endpoints
ACCOUNT = '/api/v1/account'  # Get account
UPDATE_ACCOUNT = '/api/v1/account'  # Update account
