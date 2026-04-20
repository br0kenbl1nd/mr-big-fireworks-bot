from flask import request, abort
from twilio.request_validator import RequestValidator
from config import Config

validator = RequestValidator(Config.TWILIO_AUTH_TOKEN)


def validate_twilio_request():
    signature = request.headers.get("X-Twilio-Signature", "")
    form_data = request.form.to_dict(flat=True)

    # After ProxyFix, request.url is usually correct
    url = request.url

    if not validator.validate(url, form_data, signature):
        print("Twilio validation failed")
        print("Validation URL:", url)
        print("Signature present:", bool(signature))
        abort(403)

