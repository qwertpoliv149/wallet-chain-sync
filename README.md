# CryptoCheckpoint

**CryptoCheckpoint** — это инструмент командной строки на Python, который анализирует криптовалютные кошельки на предмет подозрительных транзакций и возможных скамов. Проверка происходит по последним 10 транзакциям на наличие подозрительных URL или адресов.

## Возможности

- Поддержка Bitcoin-адресов (используется Blockchair API)
- Анализирует последние транзакции адреса
- Ищет паттерны скама (giveaway, airdrop и пр.)
- Выводит предупреждение, если есть подозрительная активность

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python cryptocheckpoint.py <bitcoin_address>
```

Пример:

```bash
python cryptocheckpoint.py 1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY
```

## Заметки

- Используется Blockchair API, для массового использования потребуется API-ключ.
- Работает только с Bitcoin (в текущей версии).

## Лицензия

MIT License
