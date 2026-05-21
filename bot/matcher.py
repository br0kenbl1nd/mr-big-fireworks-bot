from rapidfuzz import fuzz
from data.region_mapping import REGION_GROUPS


def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def detect_region_from_state_or_pincode(user_input: str):
    text = normalize(user_input)

    # Basic pincode logic based on first digit
    # India PIN zones:
    # 1/2 = North, 3 = West, 4 = Maharashtra/MP area,
    # 5 = AP/Telangana/Karnataka, 6 = South, 7/8 = East
    digits = "".join(ch for ch in text if ch.isdigit())

    if len(digits) == 6:
        first_digit = digits[0]

        if first_digit in ["1", "2"]:
            return "north_india"

        if first_digit == "3":
            return "gujarat_rajasthan"

        if first_digit == "4":
            # This includes Maharashtra, MP, Chhattisgarh areas.
            # We can default to Maharashtra unless you want more detailed mapping.
            return "maharashtra"

        if first_digit == "5":
            return "andhra_telangana"

        if first_digit == "6":
            return "tamil_nadu_karnataka"

        if first_digit in ["7", "8"]:
            return "east_india"

    # Exact or fuzzy state matching
    best_region = None
    best_score = 0

    for region_key, aliases in REGION_GROUPS.items():
        for alias in aliases:
            score = fuzz.ratio(text, alias)

            if alias in text:
                score = max(score, 95)

            if score > best_score:
                best_score = score
                best_region = region_key

    if best_score >= 75:
        return best_region

    return None