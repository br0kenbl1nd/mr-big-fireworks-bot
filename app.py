import os
import logging
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from twilio.twiml.messaging_response import MessagingResponse

from bot.db import init_db, get_session, set_session, clear_session, log_message
from bot.messages import (
    welcome_message,
    ask_location_message,
    invalid_message,
    supplier_message,
    no_match_message,
)
from bot.services import (
    get_dealer_contact,
    get_customer_contacts,
    format_dealer_contact,
    format_customer_contacts,
)
from bot.security import validate_twilio_request
from config import Config

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=Config.LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

init_db()


@app.before_request
def verify_request():
    if request.path == "/whatsapp" and request.method == "POST":
        if Config.TWILIO_AUTH_TOKEN:
            validate_twilio_request()


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_text = request.values.get("Body", "").strip()
    sender = request.values.get("From", "").strip()
    lowered = incoming_text.lower()

    response = MessagingResponse()
    msg = response.message()

    current_step = get_session(sender)

    if lowered in {"hi", "hello", "start", "menu", "restart"}:
        clear_session(sender)
        outbound = welcome_message()
        msg.body(outbound)
        log_message(sender, incoming_text, outbound)
        return str(response)

    if current_step == "awaiting_dealer_location":
        contact = get_dealer_contact(incoming_text)
        if contact:
            outbound = format_dealer_contact(contact)
            clear_session(sender)
        else:
            outbound = no_match_message()
        msg.body(outbound)
        log_message(sender, incoming_text, outbound)
        return str(response)

    if current_step == "awaiting_customer_location":
        local_contacts, pan_india = get_customer_contacts(incoming_text)
        if local_contacts:
            outbound = format_customer_contacts(local_contacts, pan_india)
            clear_session(sender)
        else:
            outbound = no_match_message()
        msg.body(outbound)
        log_message(sender, incoming_text, outbound)
        return str(response)

    if lowered == "1":
        set_session(sender, "awaiting_dealer_location")
        outbound = ask_location_message()
        msg.body(outbound)
        log_message(sender, incoming_text, outbound)
        return str(response)

    if lowered == "2":
        set_session(sender, "awaiting_customer_location")
        outbound = ask_location_message()
        msg.body(outbound)
        log_message(sender, incoming_text, outbound)
        return str(response)

    if lowered == "3":
        clear_session(sender)
        outbound = supplier_message()
        msg.body(outbound)
        log_message(sender, incoming_text, outbound)
        return str(response)

    outbound = f"{welcome_message()}\n\n{invalid_message()}"
    msg.body(outbound)
    log_message(sender, incoming_text, outbound)
    return str(response)


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)

