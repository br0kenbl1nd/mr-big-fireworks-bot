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

        # Tamil Nadu / Karnataka / Goa / Pondicherry
        ("tamil_nadu_karnataka", "Rathinam Crackers (Sivakasi)", "9940410118"),
        ("tamil_nadu_karnataka", "Shyam Crackers (Hosur)", "9731488885"),
        ("tamil_nadu_karnataka", "Saptha Giri Crackers (Hosur)", "7010647199"),
        ("tamil_nadu_karnataka", "Thamarai Trader (Hosur)", "9443365248"),
        ("tamil_nadu_karnataka", "SR Traders (Sivakasi)", "8110955172"),
        ("tamil_nadu_karnataka", "NPK Crackers (Sivakasi)", "8668039416"),
        ("tamil_nadu_karnataka", "GOAT Crackers (Sivakasi)", "9789692701"),
        ("tamil_nadu_karnataka", "KAK Pazhamudhir Solai (Chennai)", "9342960596"),
        ("tamil_nadu_karnataka", "Padma Crackers (Salem)", "9865946937"),
        ("tamil_nadu_karnataka", "Sri Saravana Traders (Gudiyatham)", "9994900146"),

        # Andhra Pradesh / Telangana
        ("andhra_telangana", "Suvarna Lakshmi Fireworks (Amaravathi, Guntur)", "9866881438"),
        ("andhra_telangana", "B.R.R Fireworks (Bhongir)", "9396743883"),
        ("andhra_telangana", "Ganesh Fireworks (Jagtial)", "9989821003"),
        ("andhra_telangana", "Harsha Traders (Rajam)", "9491570056"),
        ("andhra_telangana", "S.R.R.S Fireworks (Karimnagar)", "9000710007"),
        ("andhra_telangana", "KVR Trading Company (Chilakaluripet)", "9182415388"),
        ("andhra_telangana", "Sri Lakshmi Narayana Crackers (Pallaralam)", "9848919661"),
        ("andhra_telangana", "Krishna Agencies (Yadadri)", "9966089998"),
        ("andhra_telangana", "Rudra Traders (Siddipet)", "9949930005"),
        ("andhra_telangana", "Sri Aruna Enterprises (Palakol)", "7382958971"),

        # Kerala
        ("kerala", "Kambar Fireworks (Aluva)", "9387330017"),
        ("kerala", "Champion Enterprises (Irinjalakuda)", "9447994435"),
        ("kerala", "Vinod Traders (Thrissur)", "9447036297"),
        ("kerala", "Chinesh Verity Crackers (Kunnamkulam)", "7012255089"),
        ("kerala", "Kokken Crackers (Thrissur)", "8848769394"),
        ("kerala", "Sree Anaswara Agencies (Sulthan Bathery, Wayanad)", "9447756096"),

        # Madhya Pradesh / Central Region
        ("madhya_pradesh", "Shree Devganga Trader (Raipur)", "9303277747"),
        ("madhya_pradesh", "Agrawal Fataka Kendra (Khamgaon)", "9518559276"),
        ("madhya_pradesh", "Parasram D Karwaikar And Sons (Nagpur)", "9326772644"),
        ("madhya_pradesh", "Iswardas And Sons (Nagpur)", "9420251992"),
        ("madhya_pradesh", "Sheetal Traders (Satna)", "9406723693"),
        ("madhya_pradesh", "Shiv Fataka Center (Paratwada)", "8329805167"),
        ("madhya_pradesh", "Shiv Shakti Enterprises (Rajnandgaon)", "9827102566"),
        ("madhya_pradesh", "Sai Baba Agency (Indore)", "9826668222"),

        # Maharashtra
        ("maharashtra", "Unecha Trading Company (Pune)", "7387500281"),
        ("maharashtra", "Sahakar Nagar Fataka (Pune)", "9371000653"),
        ("maharashtra", "Jalan Fireworks (Pune)", "9822214130"),
        ("maharashtra", "Astavinayak Metal (Pune)", "9423223883"),
        ("maharashtra", "Bhagyashree Enterprises (Malad)", "9930053550"),

        # Gujarat / Rajasthan
        ("gujarat_rajasthan", "Rakesh Stores (Savli)", "9429110744"),
        ("gujarat_rajasthan", "Laxmi General Store (Bhilad)", "9825117836"),
        ("gujarat_rajasthan", "I B Trading Co (Baroda)", "9824021741"),
        ("gujarat_rajasthan", "Vanmalidas Devkaran Kesaria (Rajkot)", "9429169439"),
        ("gujarat_rajasthan", "Ambica Ashish Tradelink (Ahmedabad)", "9825015041"),
        ("gujarat_rajasthan", "Shiv Tradelink (Surat)", "7041199999"),

        # East India
        ("east_india", "Nandi Fireworks (Bhubaneswar)", "7008845950"),
        ("east_india", "Rony Enterprises Pvt Ltd (Siliguri)", "8637099151"),
        ("east_india", "Goutam Saha (Agartala)", "9436129841"),
        ("east_india", "Bikas Agencies (Bargarh, Odisha)", "981044133"),
        ("east_india", "Burima Fireworks (Howrah)", "9830513395"),
        ("east_india", "Sri Sai Fireworks (Chas)", "9334240010"),
        ("east_india", "Maa Durga Store (Hojai)", "8486888888"),

        # North India
        ("north_india", "Rewatilal Satyendrakumar Jain (Ajmer)", "9352200167"),
        ("north_india", "Shree Ganesh Trading Center (Sadalpur)", "9460192615"),
        ("north_india", "Rahul Enterprises M.R Fireworks (Ludhiana)", "8859793767"),
        ("north_india", "Gupta Traders (Kota)", "9414183280"),
        ("north_india", "Manglam (Bhilwara)", "9460351222"),
        ("north_india", "Nirmal General Store Rama Traders (Udaipur)", "9780749643"),
        ("north_india", "A Mercury Crackers (Bareilly)", "9557149655"),
        ("north_india", "G.K Enterprises (Ferozpur)", "9814553072"),
        ("north_india", "Singla Trading Company (Nabha)", "9855000401"),

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

