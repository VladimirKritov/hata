import logging

from constants import CITIES


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
        for city in CITIES:
            flat_and_house_block = f"""
  {city}_flat:
    build:
      context: .
    volumes:
      - ./:/home/project
    command: python olx.py flat {city}

  {city}_house:
    build:
      context: .
    volumes:
      - ./:/home/project
    command: python olx.py house {city}
            """
            file.write(flat_and_house_block)
            logging.info(
                f'[generator] Створення конфігу для населеного пункту: {city}'
            )


if __name__ == '__main__':
    generate_docker_compose_yaml()
