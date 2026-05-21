from bot.db import get_connection
from bot.matcher import detect_region_from_state_or_pincode


def get_dealer_contact(location_text: str):

    conn = get_connection()

    row = conn.execute("""
        SELECT name, phone
        FROM dealer_contacts
        WHERE LOWER(location) = LOWER(?)
    """, (location_text.strip(),)).fetchone()

    conn.close()

    if not row:
        return None

    return dict(row)


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


def format_dealer_contact(contact: dict) -> str:
    return (
        "Please contact your area sales agent:\n"
        f"Name: {contact['name']}\n"
        f"Phone: {contact['phone']}"
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

