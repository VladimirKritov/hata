#!/bin/bash

mkdir data

echo "TOKEN = '<bot_token>'
CHATS = {
    # Вибрані міста
    'ukraine': {
        'id': 000000000,  # <chat_id>
        'locations': [
            'chernovtsy', 'ternopol', 'ivano-frankovsk', 'kolomyya',
            'yaremche', 'sokal', 'chervonograd'
        ],
    },
    # Закарпатьска область
    'zak_region': {
        'id': 000000000,  # <chat_id>
        'locations': ['zak']
    },
    # Київ
    'kiev': {
        'id': 000000000,  # <chat_id>
        'locations': ['kiev']
    },
}" > config.py
