import time
from bip_utils import (
    Bip39MnemonicGenerator, Bip39SeedGenerator,
    Bip44, Bip44Coins, Bip44Changes
)

# Top 25 supported coins (Trust Wallet compatible where possible)
supported_coins = {
    "Bitcoin (BTC)": Bip44Coins.BITCOIN,
    "Ethereum (ETH)": Bip44Coins.ETHEREUM,
    "Binance Coin (BNB)": Bip44Coins.BINANCE_CHAIN,
    "Litecoin (LTC)": Bip44Coins.LITECOIN,
    "Dogecoin (DOGE)": Bip44Coins.DOGECOIN,
    "Bitcoin Cash (BCH)": Bip44Coins.BITCOIN_CASH,
    "Tron (TRX)": Bip44Coins.TRON,
    "Ripple (XRP)": Bip44Coins.RIPPLE,
    "Solana (SOL)": Bip44Coins.SOLANA,
    "Polygon (MATIC)": Bip44Coins.POLYGON,
    "Avalanche (AVAX)": Bip44Coins.AVAX_C_CHAIN,
    "Fantom (FTM)": Bip44Coins.FANTOM_OPERA,
    "Arbitrum (ARB)": Bip44Coins.ARBITRUM,
    "Optimism (OP)": Bip44Coins.OPTIMISM,
    "Cosmos (ATOM)": Bip44Coins.COSMOS,
    "Kava (KAVA)": Bip44Coins.KAVA,
    "Harmony (ONE)": Bip44Coins.HARMONY_ONE_ETH,
    "Algorand (ALGO)": Bip44Coins.ALGORAND,
    "Stellar (XLM)": Bip44Coins.STELLAR,
    "Near Protocol (NEAR)": Bip44Coins.NEAR_PROTOCOL,
    "Tezos (XTZ)": Bip44Coins.TEZOS,
    "Elrond (EGLD)": Bip44Coins.ELROND,
    "EOS (EOS)": Bip44Coins.EOS,
    "Filecoin (FIL)": Bip44Coins.FILECOIN
}

# Generate 24-word mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(24)
print("=" * 60)
print("🔐 Your 24-word Mnemonic (BIP-39):\n")
print(mnemonic)
print("=" * 60)

# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Derive and display wallets without showing addresses, private keys, or paths
for coin_name, coin_type in supported_coins.items():
    try:
        # Derivation path: Purpose (44') -> Coin (0/60) -> Account (0) -> External (change) -> Address (0)
        bip44_ctx = Bip44.FromSeed(seed_bytes, coin_type).Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    except Exception as e:
        print(f"\n⚠️ Skipped {coin_name}: {str(e)}")

# Keep script alive for 10 minutes
print("\n⏳ Script will remain open for 10 minutes...")
time.sleep(600)