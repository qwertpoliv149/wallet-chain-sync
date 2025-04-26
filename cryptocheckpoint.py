"""
CryptoCheckpoint: Умная проверка на потенциальные скамы в криптовалютных кошельках.
"""

import requests
import re
import json
from datetime import datetime
from urllib.parse import urlparse


def is_suspicious_url(url):
    bad_keywords = ["airdrop", "bonus", "double", "free", "giveaway"]
    netloc = urlparse(url).netloc
    return any(word in netloc.lower() for word in bad_keywords)


def fetch_transactions(address):
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Не удалось получить данные по адресу.")
    data = response.json()
    return data


def analyze_wallet(address):
    print(f"Проверка адреса: {address}")
    try:
        data = fetch_transactions(address)
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return

    txs = data["data"][address]["transactions"]
    suspicious_count = 0

    for txid in txs[:10]:  # Проверяем только 10 последних транзакций
        tx_url = f"https://api.blockchair.com/bitcoin/dashboards/transaction/{txid}"
        tx_data = requests.get(tx_url).json()
        if "data" not in tx_data:
            continue
        outputs = tx_data["data"][txid]["outputs"]
        for output in outputs:
            if "recipient" in output:
                if is_suspicious_url(output["recipient"]):
                    suspicious_count += 1

    if suspicious_count > 0:
        print(f"⚠️ Обнаружено подозрительных транзакций: {suspicious_count}")
    else:
        print("✅ Адрес выглядит безопасным (на основе последних транзакций).")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CryptoCheckpoint: анализ подозрительных криптоадресов.")
    parser.add_argument("address", help="Биткойн-адрес для анализа")
    args = parser.parse_args()

    analyze_wallet(args.address)
