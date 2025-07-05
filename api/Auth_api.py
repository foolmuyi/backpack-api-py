from .client import Client
from .consts import *


class AuthAPI(Client):

    def __init__(self, api_key, api_secret, proxy=None):
        Client.__init__(self, api_key=api_key, api_secret=api_secret, proxy=proxy)

    # Get account
    def get_account(self):
        return self._request_without_params(GET, ACCOUNT, ACCOUNT_QUERY)

    # Update account
    def update_account(self, autoBorrowSettlements, autoLend, autoRepayBorrows, leverageLimit):
        params = {'autoBorrowSettlements': autoBorrowSettlements, 'autoLend': autoLend, 
                  'autoRepayBorrows': autoRepayBorrows, 'leverageLimit': leverageLimit}
        return self._request_with_params(PATCH, INSTRUMENT_INFO, params)