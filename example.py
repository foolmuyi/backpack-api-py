import os
from dotenv import load_dotenv
from api.Public_api import PublicAPI
from api.Auth_api import AuthAPI
# from api.consts import *
# from api.client import Client


debug_mode = True
if debug_mode == True:
    proxy = 'http://127.0.0.1:7890'
else:
    proxy = None

load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

# Public Endpoints
public_api_client = PublicAPI(proxy=proxy)

# Get all supported assets
# result = public_api_client.get_assets()

# Get collateral parameters for assets
# result = public_api_client.get_collateral()

# Get borrow lend markets
# result = public_api_client.get_borrow_lend_markets()

# Get borrow lend market history
# result = public_api_client.get_borrow_lend_markets_history('1d', 'SOL')

# Retrieves all the markets that are supported by the exchange
# result = public_api_client.get_markets()

# Retrieves a market supported by the exchange
# result = public_api_client.get_market('SOL_USDC')

# Retrieves summarised statistics for the given market symbol
# result = public_api_client.get_ticker('SOL_USDC', '1d')

# Retrieves summarised statistics for all market symbols
# result = public_api_client.get_tickers('1d')

# Retrieves the order book depth for a given market symbol
# result = public_api_client.get_depth('SOL_USDC')

# Get K-Lines for the given market symbol
# result = public_api_client.get_k_lines('SOL_USDC', '1h', '1750694400', '1750795200', 'Last')

# Retrieves mark price, index price and the funding rate
# result = public_api_client.get_mark_prices('SOL_USDC_PERP')

# Retrieves the current open interest for the given market
# result = public_api_client.get_open_interest('SOL_USDC_PERP')

# Funding interval rate history for futures
# result = public_api_client.get_funding_rate('SOL_USDC_PERP', 100, 0)

# Get the system status, and the status message, if any
# result = public_api_client.get_status()

# Responds with pong
# result = public_api_client.ping_test()

# Retrieves the current system time
# result = public_api_client.get_system_time()

# Retrieve the most recent trades for a symbol
# result = public_api_client.get_recent_trades('SOL_USDC', 1000)

# Retrieves all historical trades for the given symbol
# result = public_api_client.get_historical_trades('SOL_USDC', 1000, 1000)


# Authenticated Endpoints
# auth_api_client = AuthAPI(api_key=api_key, api_secret=api_secret, proxy=proxy)

# Get account
# result = auth_api_client.get_account()

# Update account
print(result)