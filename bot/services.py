from bot.db import get_connection
from bot.matcher import best_match_location


def get_dealer_contact(location_text: str):
    key = best_match_location(location_text, "dealer_contacts")
    if not key:
        return None

    conn = get_connection()
    row = conn.execute("""
        SELECT contact_name, phone, note
        FROM dealer_contacts
        WHERE location_key = ?
        LIMIT 1
    """, (key,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_customer_contacts(location_text: str):
    key = best_match_location(location_text, "customer_contacts")
    if not key:
        return None, []

    conn = get_connection()
    local_rows = conn.execute("""
        SELECT shop_name, phone
        FROM customer_contacts
        WHERE location_key = ?
    """, (key,)).fetchall()

    pan_rows = conn.execute("""
        SELECT shop_name, phone
        FROM pan_india_shops
    """).fetchall()
    conn.close()

    return [dict(r) for r in local_rows], [dict(r) for r in pan_rows]


def format_dealer_contact(contact: dict) -> str:
    return (
        "Please contact your area sales agent:\n"
        f"Name: {contact['contact_name']}\n"
        f"Phone: {contact['phone']}\n"
        f"{contact['note']}"
    )


def format_customer_contacts(local_contacts: list, pan_india: list) -> str:
    lines = ["Please contact the nearest shop/contact for your location:"]
    for item in local_contacts:
        lines.append(f"{item['shop_name']} - {item['phone']}")

    if pan_india:
        lines.append("")
        lines.append("Pan-India shipping shops:")
        for item in pan_india:
            lines.append(f"{item['shop_name']} - {item['phone']}")

    return "\n".join(lines)
