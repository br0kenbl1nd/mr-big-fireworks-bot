from rapidfuzz import fuzz
from bot.db import get_connection


def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def best_match_location(input_text: str, table_name: str, column_name: str = "location_key"):
    cleaned = normalize(input_text)
    conn = get_connection()
    rows = conn.execute(
        f"SELECT DISTINCT {column_name} FROM {table_name}"
    ).fetchall()
    conn.close()

    candidates = [row[column_name] for row in rows]
    if not candidates:
        return None

    best = None
    best_score = 0

    for candidate in candidates:
        score = fuzz.partial_ratio(cleaned, candidate)
        if score > best_score:
            best = candidate
            best_score = score

    if best_score >= 75:
        return best

    return None

