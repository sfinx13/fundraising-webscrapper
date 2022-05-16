SHELL := /bin/bash
.DEFAULT_GOAL := help
.PHONY: help
VENV=env
PYTHON=$(VENV)/bin/python3
PIP=$(VENV)/bin/pip

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1\3/p' \
	| column -t  -s ':' \

clean: ## : Clean up the __pycache__ folder    
	@bash -l -c 'rm -rf __pycache__ && rm -rf __pycache__/'
	@bash -l -c 'rm -rf $(VENV)'

venv: ## : Create virtual environnement
	@bash -c -l 'python -m venv $(VENV)'

setup: ## : Install dependencies
	@bash -c -l '[[ "$(VIRTUAL_ENV)" == *"$(VENV)"* ]] && pip install -r requirements.txt || echo "Please create virtual environnement"'

build: ## : Build container
	@bash -c -l 'docker build -t app-webscrapping .'

run: ## : Run container
	@bash -c -l 'docker run -it -v "$PWD":/app app-webscrapping'