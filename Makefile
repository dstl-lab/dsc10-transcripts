include .env
export DATABASE_URL

.PHONY: db

db: objects.parquet
	uv run python3 build_db.py

objects.parquet: dump_parquet.py
	uv run python3 dump_parquet.py
