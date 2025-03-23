# Main_moralis.py

from network_iot import Network
from moralis_micropython import MoralisMicroPython
import gc
import ujson

gc.collect()

try:
    with open('chains.json', 'r') as file:
        MORALIS_CHAINS = ujson.load(file)
    print(MORALIS_CHAINS)
except Exception as e:
    print("Error al leer el archivo JSON:", e)

# Config Wi-Fi
ssid = ""
password = ""
static_ip_config = None
net = Network(ssid, password, static_ip_config)
if not net.conectar():
    print("Error al conectar la red. Saliendo...")

api_key= "_API_KEY"
moralis = MoralisMicroPython(api_key=api_key)

# bueno
get_wallet_token_balances = moralis.get_wallet_token_balances(
    address='0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326',
    chain=MORALIS_CHAINS['eth'] 
)
print(get_wallet_token_balances)
gc.collect()

# bueno
candlesticks = moralis.get_pair_candlesticks(
    address="0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8",
    chain=MORALIS_CHAINS['eth'],
    from_date="2025-01-01",
    to_date="2025-01-02",
    timeframe="1h",  # '1h', 1d', '1w'
    currency="usd"
)
print(candlesticks)
print("get_pair_candlesticks")
gc.collect()

# bueno
# Get Wallet Token Balances Prices
print(moralis.get_wallet_token_balances_prices(
    address='0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326',
    chain=MORALIS_CHAINS['eth']
))
print("get_wallet_token_balances_prices")
gc.collect()


# bueno
# Get Token Price
print(moralis.get_token_price(
    address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    chain=MORALIS_CHAINS['eth']
))
print("get_token_price")
gc.collect()


# bueno
# Get Multiple Token Prices
print(moralis.get_multiple_token_prices(
    tokens=['0xdAC17F958D2ee523a2206206994597C13D831ec7', '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'],
    chain=MORALIS_CHAINS['eth']
))
print("get_multiple_token_prices")
gc.collect()


def test_all_functions():
    # 1. get_wallet_approvals
    try:
        print("get_wallet_approvals:")
        result = moralis.get_wallet_approvals(
            address='0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326',
            chain='eth',
            limit=10
        )
        print(result)
    except Exception as e:
        print("Error en get_wallet_approvals:", e)
    
    # 2. get_swaps_by_pair_address
    try:
        print("\nget_swaps_by_pair_address:")
        result = moralis.get_swaps_by_pair_address(
            address="0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8",
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_swaps_by_pair_address:", e)
    
    # 3. get_swaps_by_token_address
    try:
        print("\nget_swaps_by_token_address:")
        result = moralis.get_swaps_by_token_address(
            address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_swaps_by_token_address:", e)
    
    # 4. get_swaps_by_wallet_address
    try:
        print("\nget_swaps_by_wallet_address:")
        result = moralis.get_swaps_by_wallet_address(
            address='0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326',
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_swaps_by_wallet_address:", e)
    
    # 5. get_wallet_token_transfers
    try:
        print("\nget_wallet_token_transfers:")
        result = moralis.get_wallet_token_transfers(
            address='0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326',
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_wallet_token_transfers:", e)
    
    # 6. get_token_transfers
    try:
        print("\nget_token_transfers:")
        result = moralis.get_token_transfers(
            address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_token_transfers:", e)
    
    # 7. get_volume_stats_by_chain
    try:
        print("\nget_volume_stats_by_chain:")
        result = moralis.get_volume_stats_by_chain(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_volume_stats_by_chain:", e)
    
    # 8. get_volume_stats_by_category
    try:
        print("\nget_volume_stats_by_category:")
        result = moralis.get_volume_stats_by_category(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_volume_stats_by_category:", e)
    
    # 9. get_time_series_volume
    try:
        print("\nget_time_series_volume:")
        result = moralis.get_time_series_volume(chain='eth', timeframe='1d')
        print(result)
    except Exception as e:
        print("Error en get_time_series_volume:", e)
    
    # 10. get_time_series_volume_by_category
    try:
        print("\nget_time_series_volume_by_category:")
        result = moralis.get_time_series_volume_by_category(category='defi', chain='eth', timeframe='1d')
        print(result)
    except Exception as e:
        print("Error en get_time_series_volume_by_category:", e)
    
    # 11. get_token_pairs
    try:
        print("\nget_token_pairs:")
        result = moralis.get_token_pairs(token_address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_token_pairs:", e)
    
    # 12. get_pair_stats
    try:
        print("\nget_pair_stats:")
        result = moralis.get_pair_stats(address="0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8", chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_pair_stats:", e)
    
    # 13. get_aggregated_token_pair_stats
    try:
        print("\nget_aggregated_token_pair_stats:")
        result = moralis.get_aggregated_token_pair_stats(token_address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_aggregated_token_pair_stats:", e)
    
    # 14. get_pair_address
    try:
        print("\nget_pair_address:")
        result = moralis.get_pair_address(
            token0_address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
            token1_address='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_pair_address:", e)
    
    # 15. get_pair_reserves
    try:
        print("\nget_pair_reserves:")
        result = moralis.get_pair_reserves(pair_address="0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8", chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_pair_reserves:", e)
    
    # 16. get_token_analytics
    try:
        print("\nget_token_analytics:")
        result = moralis.get_token_analytics(address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_token_analytics:", e)
    
    # 17. get_multiple_token_analytics
    try:
        print("\nget_multiple_token_analytics:")
        # Se espera una cadena con las direcciones separadas por comas
        result = moralis.get_multiple_token_analytics(
            addresses='0xdAC17F958D2ee523a2206206994597C13D831ec7,0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
            chain='eth'
        )
        print(result)
    except Exception as e:
        print("Error en get_multiple_token_analytics:", e)
    
    # 18. get_token_stats
    try:
        print("\nget_token_stats:")
        result = moralis.get_token_stats(address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_token_stats:", e)
    
    # 19. get_token_holders
    try:
        print("\nget_token_holders:")
        result = moralis.get_token_holders(token_address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth', limit=10)
        print(result)
    except Exception as e:
        print("Error en get_token_holders:", e)
    
    # 20. get_token_holder_stats
    try:
        print("\nget_token_holder_stats:")
        result = moralis.get_token_holder_stats(token_address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_token_holder_stats:", e)
    
    # 21. get_historical_token_holders
    try:
        print("\nget_historical_token_holders:")
        result = moralis.get_historical_token_holders(token_address='0xdAC17F958D2ee523a2206206994597C13D831ec7', chain='eth', timeframe='1d')
        print(result)
    except Exception as e:
        print("Error en get_historical_token_holders:", e)
    
    # 22. get_snipers_by_pair_address
    try:
        print("\nget_snipers_by_pair_address:")
        result = moralis.get_snipers_by_pair_address(address="0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8", chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_snipers_by_pair_address:", e)
    
    # 23. get_trending_tokens
    try:
        print("\nget_trending_tokens:")
        result = moralis.get_trending_tokens(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_trending_tokens:", e)
    
    # 24. get_top_gainers_tokens
    try:
        print("\nget_top_gainers_tokens:")
        result = moralis.get_top_gainers_tokens(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_top_gainers_tokens:", e)
    
    # 25. get_top_losers_tokens
    try:
        print("\nget_top_losers_tokens:")
        result = moralis.get_top_losers_tokens(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_top_losers_tokens:", e)
    
    # 26. get_top_erc20_tokens_by_market_cap
    try:
        print("\nget_top_erc20_tokens_by_market_cap:")
        result = moralis.get_top_erc20_tokens_by_market_cap(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_top_erc20_tokens_by_market_cap:", e)
    
    # 27. get_filtered_tokens
    try:
        print("\nget_filtered_tokens:")
        result = moralis.get_filtered_tokens(chain='eth')
        print(result)
    except Exception as e:
        print("Error en get_filtered_tokens:", e)
    
    # 28. search_tokens
    try:
        print("\nsearch_tokens:")
        result = moralis.search_tokens(query='ethereum', chain='eth')
        print(result)
    except Exception as e:
        print("Error en search_tokens:", e)
    
    gc.collect()

if __name__ == '__main__':
    test_all_functions()
    gc.collect()


