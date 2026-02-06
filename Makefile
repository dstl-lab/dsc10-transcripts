include .env
export DATABASE_URL

DB_NAME = database-$(shell date +%Y-%m-%d).db

.PHONY: db

db: objects.parquet
	uv run python3 build_db.py $(DB_NAME)

objects.parquet: dump_parquet.py
	uv run python3 dump_parquet.py
