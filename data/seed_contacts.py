from bot.db import get_connection, init_db


def seed():
    init_db()
    conn = get_connection()

    conn.execute("DELETE FROM dealer_contacts")
    conn.execute("DELETE FROM customer_contacts")
    conn.execute("DELETE FROM pan_india_shops")

    dealer_rows = [
        ("tamil nadu", "Arun", "+91XXXXXXXXXX", "Sales Agent - Tamil Nadu"),
        ("kerala", "Biju", "+91XXXXXXXXXX", "Sales Agent - Kerala"),
        ("karnataka", "Manoj", "+91XXXXXXXXXX", "Sales Agent - Karnataka"),
        ("chennai", "Arun", "+91XXXXXXXXXX", "Sales Agent - Chennai"),
    ]

    customer_rows = [
        ("tamil nadu", "Mr. Big Fireworks TN Desk", "+91XXXXXXXXXX"),
        ("kerala", "Mr. Big Fireworks Kerala Desk", "+91XXXXXXXXXX"),
        ("chennai", "Mr. Big Fireworks Chennai Shop", "+91XXXXXXXXXX"),
        ("madurai", "Mr. Big Fireworks Madurai Shop", "+91XXXXXXXXXX"),
    ]

    pan_rows = [
        ("Mr. Big Fireworks Online Dispatch 1", "+91XXXXXXXXXX"),
        ("Mr. Big Fireworks Online Dispatch 2", "+91XXXXXXXXXX"),
    ]

    conn.executemany("""
        INSERT INTO dealer_contacts (location_key, contact_name, phone, note)
        VALUES (?, ?, ?, ?)
    """, dealer_rows)

    conn.executemany("""
        INSERT INTO customer_contacts (location_key, shop_name, phone)
        VALUES (?, ?, ?)
    """, customer_rows)

    conn.executemany("""
        INSERT INTO pan_india_shops (shop_name, phone)
        VALUES (?, ?)
    """, pan_rows)

    conn.commit()
    conn.close()
    print("Seed data inserted.")


if __name__ == "__main__":
    seed()

