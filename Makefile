install:
	pip install poetry && \
	poetry install
start:
	poetry run python BotTg2/BotTg2.py