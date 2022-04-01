setup:
	python3 -m venv .venv

deps:
	pip install -U -r requirements.txt

rsa-keys:
	python gen-keys.py sekrit

ec-keys:
	python gen-ec-keys.py sekrit

PHONY: setup deps
