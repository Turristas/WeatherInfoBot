install:
	pip install poetry && \
	poetry install
start:
	poetry run python WeatherInfoBot/main.py
