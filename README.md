# Moralis - MicroPython

A lightweight MicroPython library to interact with the main **Moralis Token API endpoints**, making it easy to retrieve essential information about tokens, swaps, holders, prices, transfers, and more across multiple blockchains like Ethereum, BSC, Polygon, and others.

This library is specifically designed for IoT environments and embedded systems, allowing efficient API calls directly from MicroPython-compatible boards (such as ESP32).

---

## 🚀 Features

- Retrieve ERC20 token balances by wallet.
- Get token prices, pairs, candlesticks, analytics, and transfers.
- Query swaps, holders, volume stats, and trending tokens.
- Access key blockchain token information easily.
- Multi-chain support (Ethereum, BSC, Polygon, etc.).

---

## 🚀 Why Use Moralis with MicroPython?

Integrating **Moralis with MicroPython** offers a powerful combination for developers aiming to bridge the gap between the Internet of Things (IoT) and blockchain ecosystems. Here's why it is a game-changer:

1. **Efficient Blockchain Data Access on Resource-Constrained Devices:**
   - MicroPython runs on devices with limited processing power and memory, such as ESP32 and ESP8266.
   - Moralis provides easy-to-use REST APIs, eliminating the need to run full blockchain nodes or perform complex RPC calls directly from the device.

2. **Rapid Prototyping for Web3 IoT Solutions:**
   - Whether you are building smart wallets, blockchain-enabled sensors, or real-time dashboards, combining Moralis with MicroPython speeds up development significantly.

3. **Multi-Chain Support Simplified:**
   - Access data from Ethereum, BSC, Polygon, and more without writing separate integrations for each blockchain.

4. **No Blockchain Expertise Required on Device:**
   - Developers can focus on their IoT application logic without worrying about low-level blockchain details or connectivity issues.

5. **Secure and Scalable Backend Infrastructure:**
   - Moralis handles backend scaling and node maintenance, freeing IoT developers from managing heavy blockchain infrastructure.

**Using Moralis with MicroPython allows small devices to leverage powerful blockchain data effortlessly and securely.**

---

## 📋 Requirements

- MicroPython-compatible device (e.g., ESP32, ESP8266).
- Wi-Fi connection.
- Valid **Moralis API Key** (You can get it from [Moralis](https://developers.moralis.com/).
---

## 📂 Installation

Upload the following files to your MicroPython board:

- `main_moralis.py` → Example usage script.
- `network_iot.py` → Wi-Fi connection handler.
- `moralis_micropython.py` → Main Moralis API library.
- `chains.json` → Dictionary containing supported blockchain chains (Ethereum, BSC, Polygon, etc.).

---

## ⚙️ Configuration

### 1. Wi-Fi Connection

Edit the following lines in `main_moralis.py` with your Wi-Fi credentials:

```python
ssid = "YOUR_SSID"
password = "YOUR_PASSWORD"
```

### 2. Moralis API Key

Add your Moralis API Key:

```python
api_key = "YOUR_API_KEY"
moralis = MoralisMicroPython(api_key=api_key)
```

### 3. Chain Configuration

The `chains.json` file should look like:

```json
{
  "eth": "eth",
  "bsc": "bsc",
  "polygon": "polygon"
}
```

You can add other supported chains as needed.

---

## 📝 Basic Usage

Here are some quick examples:

### Get ERC20 Token Balances by Wallet:

```python
balances = moralis.get_wallet_token_balances(
    address='0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326',
    chain=MORALIS_CHAINS['eth']
)
print(balances)
```

---

### Get Token Price:

```python
price = moralis.get_token_price(
    address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    chain=MORALIS_CHAINS['eth']
)
print(price)
```

---

### Get Volume Stats by Chain:

```python
volume_stats = moralis.get_volume_stats_by_chain(chain='eth')
print(volume_stats)
```

---

## 📚 Available Functions

The library implements the main Moralis Token API endpoints, including:

- `get_wallet_token_balances`
- `get_wallet_approvals`
- `get_token_price`
- `get_swaps_by_pair_address`
- `get_swaps_by_token_address`
- `get_wallet_token_transfers`
- `get_token_transfers`
- `get_token_pairs`
- `get_token_holders`
- `get_trending_tokens`
- `get_volume_stats_by_chain`
- `get_token_analytics`
- `get_token_stats`
- `get_snipers_by_pair_address`
- `get_top_gainers_tokens`
- `get_top_losers_tokens`
- `get_filtered_tokens`
- `search_tokens`
- And many more...

Check `main_moralis.py` for complete examples of each function.

---

## 📅 Running

You can use the pre-built test function to test all available endpoints:

```python
import Main_moralis
```

This will execute all examples and display the results.

---

## 📚 Resources

- [Moralis Token API Documentation](https://docs.moralis.com/web3-data-api/evm/reference/token-api)
- [MicroPython](https://micropython.org/)
---

## 🌐 License

MIT License.

---

## 💰 Donations

If you find this project useful and would like to support its development, feel free to donate:

**Ethereum (ETH) Wallet:**

`0xD000D4e44585467BA5a92C2f8618E9a008C5997a`

Thank you for your support! 🙌

