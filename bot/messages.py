from config import Config

COMPANY_DESCRIPTION = (
    "Mr. Big Fireworks offers dealership support, retail fireworks purchases, "
    "event supply assistance, and supplier coordination across multiple locations."
)


def welcome_message() -> str:
    return (
        f"Hi, thank you for contacting Mr. Big Fireworks.\n\n"
        f"{COMPANY_DESCRIPTION}\n\n"
        f"If you are a licensed shop looking for dealership please press 1.\n"
        f"If you are looking to purchase crackers for your own use or for events please press 2.\n"
        f"If you are a supplier please press 3."
    )


def ask_location_message() -> str:
    return "Please send your location. You can enter your city or state."


def invalid_message() -> str:
    return (
        "Please press:\n"
        "1 for dealership\n"
        "2 for personal or event purchase\n"
        "3 for supplier"
    )


def supplier_message() -> str:
    return (
        f"Please contact our Supply Manager:\n"
        f"{Config.SUPPLY_MANAGER_NAME}\n"
        f"{Config.SUPPLY_MANAGER_PHONE}"
    )


def no_match_message() -> str:
    return (
        "Sorry, we could not identify your location.\n"
        "Please send only your city or state name."
    )
