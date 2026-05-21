from bot.db import get_connection
from bot.matcher import detect_region_from_state_or_pincode


def get_customer_contacts(location_text: str):
    region_key = detect_region_from_state_or_pincode(location_text)

    if not region_key:
        return None, []

    conn = get_connection()

    local_rows = conn.execute("""
        SELECT shop_name, phone
        FROM customer_contacts
        WHERE location_key = ?
    """, (region_key,)).fetchall()

    pan_rows = conn.execute("""
        SELECT shop_name, phone
        FROM pan_india_shops
    """).fetchall()

    conn.close()

    return [dict(r) for r in local_rows], [dict(r) for r in pan_rows]