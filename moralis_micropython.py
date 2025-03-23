# moralis_micropython.py
import urequests 
import ujson

def validate_date(date_text):
    if date_text:
        if len(date_text) != 10 or date_text[4] != '-' or date_text[7] != '-':
            raise ValueError(f"Invalid date format: {date_text}. Expected YYYY-MM-DD.")

class MoralisMicroPython: # # MoralisMicroPython
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://deep-index.moralis.io/api/v2.2/'
        self.headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key
        }

    def _get(self, endpoint, params=None):
        url = self.base_url + endpoint
        if params:
            query_string = '&'.join(f'{key}={value}' for key, value in params.items() if value is not None)
            url += f'?{query_string}'
        #print(f"Requesting: {url}")
        try:
            response = urequests.get(url, headers=self.headers)
            if response and response.status_code == 200:
                return response.json()
            else:
                print("Invalid response:", response)
                if response:
                    print("Response content:", response.content)
                    response.close()
                raise Exception(f'HTTP Error: {response.status_code if response else 'No Response'}')
        except Exception as e:
            print("Exception occurred:", e)
            raise e

    def _post(self, endpoint, data):
        url = self.base_url + endpoint
        response = urequests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            response.close()
            raise Exception(f'Error {response.status_code}: {response.text}')
    
    # Agrega nuevo método para POST con params
    def _post_with_params(self, endpoint, params, data):
        url = self.base_url + endpoint
        if params:
            query_string = '&'.join(f'{key}={value}' for key, value in params.items() if value is not None)
            url += f'?{query_string}'
        
        print(f"Requesting POST: {url}")
        response = urequests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            result = response.content.decode('utf-8')
            response.close()
            return result
        else:
            print("Invalid response:", response.status_code)
            print("Response content:", response.content.decode('utf-8'))
            response.close()
            raise Exception(f'Error {response.status_code}: {response.text}')
    
    def get_wallet_token_balances(self, address, chain='eth', to_block=None, token_addresses=None, exclude_spam=False):
        endpoint = f'{address}/erc20'
        params = {
            'chain': chain,
            'to_block': to_block,
            'token_addresses': ','.join(token_addresses) if token_addresses else None,
            'exclude_spam': str(exclude_spam).lower()
        }
        return self._get(endpoint, params)

    def get_wallet_token_balances_prices(self, address, chain='eth', to_block=None, token_addresses=None):
        endpoint = f'wallets/{address}/tokens'
        params = {
            'chain': chain,
            'to_block': to_block,
            'token_addresses': ','.join(token_addresses) if token_addresses else None
        }
        return self._get(endpoint, params)

    def get_wallet_approvals(self, address, chain='eth', limit=100, cursor=None):
        endpoint = f'{address}/erc20/approvals'
        params = {
            'chain': chain,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)


    def get_token_price(self, address, chain='eth', exchange=None, to_block=None):
        endpoint = f'erc20/{address}/price'
        params = {
            'chain': chain,
            'exchange': exchange,
            'to_block': to_block
        }
        return self._get(endpoint, params)
    
    def get_multiple_token_prices(self, tokens, chain='eth', include=None):
        endpoint = 'erc20/prices'
        # Construir lista de tokens correctamente
        token_list = [{"token_address": token} for token in tokens]
        params = {
            'chain': chain,
            'include': include
        }
        data = {
            'tokens': token_list
        }
        return self._post_with_params(endpoint, params, data)
    
    def _format_date(self, date_str):
        if date_str and 'T' not in date_str:
            return date_str + "T00:00:00.000"
        return date_str

    def get_pair_candlesticks(self, address, chain='eth', from_date=None, to_date=None, timeframe='1h', currency='usd', limit=None):
        from_date = self._format_date(from_date)
        to_date = self._format_date(to_date)
        endpoint = f'pairs/{address}/ohlcv'
        params = {
            'chain': chain,
            'fromDate': from_date,
            'toDate': to_date,
            'timeframe': timeframe,
            'currency': currency,
            'limit': limit
        }
        return self._get(endpoint, params)

    def get_swaps_by_pair_address(self, address, chain='eth', from_block=None, to_block=None, from_date=None, to_date=None, limit=100, cursor=None):
        endpoint = f'pairs/{address}/swaps'
        params = {
            'chain': chain,
            'from_block': from_block,
            'to_block': to_block,
            'from_date': from_date,
            'to_date': to_date,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)

    def get_swaps_by_token_address(self, address, chain='eth', from_block=None, to_block=None, from_date=None, to_date=None, limit=100, cursor=None):
        endpoint = f'erc20/{address}/swaps'
        params = {
            'chain': chain,
            'from_block': from_block,
            'to_block': to_block,
            'from_date': from_date,
            'to_date': to_date,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)

    def get_swaps_by_wallet_address(self, address, chain='eth', from_block=None, to_block=None, from_date=None, to_date=None, limit=100, cursor=None):
        endpoint = f'wallets/{address}/swaps'
        params = {
            'chain': chain,
            'from_block': from_block,
            'to_block': to_block,
            'from_date': from_date,
            'to_date': to_date,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)

    def get_wallet_token_transfers(self, address, chain='eth', from_block=None, to_block=None, from_date=None, to_date=None, limit=100, cursor=None):
        endpoint = f'{address}/erc20/transfers'
        params = {
            'chain': chain,
            'from_block': from_block,
            'to_block': to_block,
            'from_date': from_date,
            'to_date': to_date,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)

    def get_token_transfers(self, address, chain='eth', from_block=None, to_block=None, from_date=None, to_date=None, limit=100, cursor=None):
        endpoint = f'erc20/{address}/transfers'
        params = {
            'chain': chain,
            'from_block': from_block,
            'to_block': to_block,
            'from_date': from_date,
            'to_date': to_date,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)

    def get_volume_stats_by_chain(self, chain='eth'):
        endpoint = 'volume/chains'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_volume_stats_by_category(self, chain='eth'):
        endpoint = 'volume/categories'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_time_series_volume(self, chain='eth', timeframe='1d'):
        endpoint = 'volume/timeseries'
        params = {
            'chain': chain,
            'timeframe': timeframe
        }
        return self._get(endpoint, params)

    def get_time_series_volume_by_category(self, category, chain='eth', timeframe='1d'):
        endpoint = f'volume/timeseries/{category}'
        params = {
            'chain': chain,
            'timeframe': timeframe
        }
        return self._get(endpoint, params)

    def get_token_pairs(self, token_address, chain='eth'):
        endpoint = f'{token_address}/pairs'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_pair_stats(self, address, chain='eth'):
        endpoint = f'pairs/{address}/stats'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_aggregated_token_pair_stats(self, token_address, chain='eth'):
        endpoint = f'{token_address}/pairs/stats'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_pair_address(self, token0_address, token1_address, chain='eth'):
        endpoint = f'{token0_address}/{token1_address}/pairAddress'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_pair_reserves(self, pair_address, chain='eth'):
        endpoint = f'{pair_address}/reserves'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_token_analytics(self, address, chain='eth'):
        endpoint = f'tokens/{address}/analytics'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_multiple_token_analytics(self, addresses, chain='eth'):
        endpoint = f'tokens/{addresses}/analytics'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_token_stats(self, address, chain='eth'):
        endpoint = f'erc20/{address}/stats'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_token_holders(self, token_address, chain='eth', limit=100, cursor=None):
        endpoint = f'erc20/{token_address}/owners'
        params = {
            'chain': chain,
            'limit': limit,
            'cursor': cursor
        }
        return self._get(endpoint, params)

    def get_token_holder_stats(self, token_address, chain='eth'):
        endpoint = f'erc20/{token_address}/holders'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_historical_token_holders(self, token_address, chain='eth', timeframe='1d'):
        endpoint = f'erc20/{token_address}/holders/historical'
        params = {
            'chain': chain,
            'timeframe': timeframe
        }
        return self._get(endpoint, params)

    def get_snipers_by_pair_address(self, address, chain='eth'):
        endpoint = f'pairs/{address}/snipers'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_trending_tokens(self, chain='eth'):
        endpoint = 'tokens/trending'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_top_gainers_tokens(self, chain='eth'):
        endpoint = 'discovery/tokens/top-gainers'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_top_losers_tokens(self, chain='eth'):
        endpoint = 'discovery/tokens/top-losers'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_top_erc20_tokens_by_market_cap(self, chain='eth'):
        endpoint = 'market-data/erc20s/top-tokens'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def get_filtered_tokens(self, chain='eth'):
        endpoint = 'discovery/tokens'
        params = {
            'chain': chain
        }
        return self._get(endpoint, params)

    def search_tokens(self, query, chain='eth'):
        endpoint = 'tokens/search'
        params = {
            'query': query,
            'chain': chain
        }
        return self._get(endpoint, params)


