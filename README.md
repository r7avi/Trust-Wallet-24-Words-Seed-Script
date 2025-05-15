# 🌐 Crypto Wallet Generator

This Python script generates a secure 24-word BIP-39 mnemonic phrase and derives wallet information for multiple cryptocurrencies using the `bip_utils` library. It supports 24 popular cryptocurrencies compatible with Trust Wallet where possible. 🚀

---

## ✨ Features

- 🔑 Generates a secure 24-word BIP-39 mnemonic phrase.  
- 💰 Supports wallet derivation for 24 cryptocurrencies, including Bitcoin, Ethereum, Binance Coin, and more.  
- 🛤️ Uses standard BIP-44 derivation paths (`m/44'/coin'/0'/0/0`).  
- 🖥️ Displays the mnemonic phrase securely without exposing private keys or addresses.  
- ⚠️ Includes error handling for unsupported coins or derivation issues.  
- ⏰ Keeps the script running for 10 minutes to allow safe copying of the mnemonic.  

---

## 🪙 Supported Cryptocurrencies

The script supports the following coins:

| Coin                | Symbol | Emoji  |
|---------------------|--------|--------|
| Bitcoin             | BTC    | 🟠     |
| Ethereum            | ETH    | 🔷     |
| Binance Coin        | BNB    | 🟡     |
| Litecoin            | LTC    | ⚪     |
| Dogecoin            | DOGE   | 🐶     |
| Bitcoin Cash        | BCH    | 🟢     |
| Tron                | TRX    | 🔴     |
| Ripple              | XRP    | ⚫     |
| Solana              | SOL    | 💜     |
| Polygon             | MATIC  | 🟣     |
| Avalanche           | AVAX   | ❄️     |
| Fantom              | FTM    | 👻     |
| Arbitrum            | ARB    | 🔵     |
| Optimism            | OP     | 🔴     |
| Cosmos              | ATOM   | 🌌     |
| Kava                | KAVA   | 🌱     |
| Harmony             | ONE    | 🎵     |
| Algorand            | ALGO   | 🌐     |
| Stellar             | XLM    | ⭐     |
| Near Protocol       | NEAR   | 🌍     |
| Tezos               | XTZ    | 🍵     |
| Elrond              | EGLD   | 🏰     |
| EOS                 | EOS    | 🌅     |
| Filecoin            | FIL    | 📂     |

---

## 🛠️ Prerequisites

- 🐍 Python 3.8+  
- 📦 `bip_utils` library  

---

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/r7avi/Trust-Wallet-24-Words-Seed-Script.git
cd Trust-Wallet-24-Words-Seed-Script

# Install required packages
pip install bip_utils

## 📥 Usage
Run the script
python wallet_generator.py

The script will:
Generate and display a 24-word mnemonic phrase.
Derive wallet information for each supported cryptocurrency (without showing sensitive data).


Stay active for 10 minutes to allow secure copying of the mnemonic.

⚠️ Important: Store the mnemonic phrase securely (e.g., offline on paper). Never share it or store it digitally in an unsecured environment.

🔒 Security Notes





🔐 Mnemonic Security: The mnemonic phrase is the key to all derived wallets. Store it securely and never share it.



🖥️ Offline Usage: For maximum security, run this script on an air-gapped (offline) computer.



🚫 No Sensitive Data Displayed: Private keys and public addresses are not shown to minimize risks.



⚠️ Use at Your Own Risk: Verify the code and use responsibly.

📚 Dependencies





bip_utils: Python library for BIP-39, BIP-44, and cryptocurrency standards.



time: Standard Python library for adding a delay.
