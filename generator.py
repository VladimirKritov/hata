import os.path
import logging

from config import CHATS


logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)


def generate_docker_compose_yaml():
    with open('docker-compose.yml', 'w') as file:
        main_block = """
version: '3'

services:
        """
        file.write(main_block)
        for chat in CHATS.keys():
            for location in CHATS[chat]['locations']:
                flat_and_house_block = f"""
  {location}_flat:
    build:
      context: .
    volumes:
      - ./:/home/project
    command: python olx.py flat {location} {CHATS[chat]['id']}

  {location}_house:
    build:
      context: .
    volumes:
      - ./:/home/project
    command: python olx.py house {location} {CHATS[chat]['id']}
            """
                file.write(flat_and_house_block)
                file_path = f"data/data_{CHATS[chat]['id']}.txt"
                if not os.path.exists(file_path):
                    with open(file_path, 'w'):
                        logging.info(
                            f'[generator] Створення файлу: {file_path}'
                        )
                logging.info(
                    f'[generator] Створення конфігу для населеного '
                    f'пункту: {location}'
                )


if __name__ == '__main__':
    generate_docker_compose_yaml()
