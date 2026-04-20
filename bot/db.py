import sqlite3
from config import Config


def get_connection():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_sessions (
            phone TEXT PRIMARY KEY,
            step TEXT,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS dealer_contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_key TEXT NOT NULL,
            contact_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            note TEXT DEFAULT ''
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer_contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_key TEXT NOT NULL,
            shop_name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS pan_india_shops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            shop_name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS message_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT NOT NULL,
            inbound_text TEXT,
            outbound_text TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def get_session(phone: str):
    conn = get_connection()
    row = conn.execute(
        "SELECT step FROM user_sessions WHERE phone = ?",
        (phone,)
    ).fetchone()
    conn.close()
    return row["step"] if row else None


def set_session(phone: str, step: str):
    conn = get_connection()
    conn.execute("""
        INSERT INTO user_sessions (phone, step, updated_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(phone) DO UPDATE SET
            step = excluded.step,
            updated_at = CURRENT_TIMESTAMP
    """, (phone, step))
    conn.commit()
    conn.close()


def clear_session(phone: str):
    conn = get_connection()
    conn.execute("DELETE FROM user_sessions WHERE phone = ?", (phone,))
    conn.commit()
    conn.close()


def log_message(phone: str, inbound_text: str, outbound_text: str):
    conn = get_connection()
    conn.execute("""
        INSERT INTO message_logs (phone, inbound_text, outbound_text)
        VALUES (?, ?, ?)
    """, (phone, inbound_text, outbound_text))
    conn.commit()
    conn.close()

