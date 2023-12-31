SHELL := /usr/bin/env bash -O globstar

run: frontend/dist
	docker compose up --build

frontend/node_modules: frontend/package.json
	cd frontend; npm install

frontend/dist: frontend/node_modules frontend/src/** frontend/src/**/* frontend/public/**
	cd frontend; npm run build
