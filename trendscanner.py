import requests

def extract_list_of_USDT_cryptopairs():
    r = requests.get('https://finnhub.io/api/v1/crypto/symbol?exchange=binance&token=c1aiaan48v6v5v4gv69g')
    #'symbol' used in candle endpoint
    symbol_data_full = r.json()
    cryptocoin = set()
    for symbol in symbol_data_full:
        split = symbol['displaySymbol'].split('/')
        cryptocoin.add(split[0])
        cryptocoin.add(split[1])
    usd_cryptopairs = set()
    for coin in list(cryptocoin):
        for symbol in symbol_data_full:
            if coin in symbol['displaySymbol'] and 'USDT' in symbol['displaySymbol']:
                usd_cryptopairs.add(symbol['symbol'])
    return list(usd_cryptopairs)
