"""Dumps the objects table from PostgreSQL into objects.parquet."""

import json
import os

import pandas as pd
from sqlalchemy import create_engine


def main():
    database_url = os.environ["DATABASE_URL"]
    engine = create_engine(database_url)
    df = pd.read_sql_table("objects", engine)

    # Convert UUID columns to strings
    for col in ["id", "user_id", "course_id"]:
        df[col] = df[col].astype(str)

    # Convert object_data jsonb to JSON strings
    df["object_data"] = df["object_data"].apply(
        lambda x: json.dumps(x) if x is not None else None
    )

    df.to_parquet("objects.parquet", index=False)
    print(f"Wrote {len(df)} rows to objects.parquet")


if __name__ == "__main__":
    main()
