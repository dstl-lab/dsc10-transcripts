#!/usr/bin/env python
import sys
from pathlib import Path

from src.dsc10_transcripts.database import create_db_and_tables, seed_db


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <transcript_file>")
        sys.exit(1)

    transcript_path = sys.argv[1]
    if not Path(transcript_path).exists():
        print(f"Error: File not found: {transcript_path}")
        sys.exit(1)

    create_db_and_tables()
    seed_db(transcript_path)


if __name__ == "__main__":
    main()
