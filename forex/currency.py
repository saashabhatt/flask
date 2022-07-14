from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyCodes()

def check_curr_validity(curr):
    """Is currency legit?
    >>> check_curr_validity('inr')
    True

    >>> check_curr_validity("sfasdgdag")
    False
    """
    curr = curr.upper()
    return c.get_currency_name(curr) is not None

def get_amt(bcurr, tcurr, amt):
    """Get amount converted to target currency
    >>> get_amt('USD','usd', 100)
    '100.0'

    >>> get_amt('eur','eur', 1000)
    '1,000.0'
    """
    bcurr = bcurr.upper()
    tcurr = tcurr.upper()
    c = CurrencyRates()
    res = round(c.convert(bcurr, tcurr, amt), 2)
    return "{:,}".format(res)

def currency_symbol(tcurr):
    """
    >>> currency_symbol('usd')
    '$'
    """
    tcurr = tcurr.upper()
    c = CurrencyCodes()
    return c.get_symbol(tcurr)
