from fastapi import APIRouter, HTTPException, Header, Request
from typing import List
import json
import stripe
import os
from dotenv import load_dotenv

stripe_router = APIRouter(prefix="/stripe")

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

@stripe_router.post("/api/webhook/stripe")
async def webhook(request: Request, stripe_signature: str = Header(str)):
    event = None
    payload = await request.body()

    try:
        event = json.loads(payload)
    except json.decoder.JSONDecodeError as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return {"error": str(e)}
    if endpoint_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        try:
            event = stripe.Webhook.construct_event(
                payload, stripe_signature, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return {"error": str(e)}

    # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
        print('Payment for {} succeeded'.format(payment_intent['amount']))
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event['type'] == 'payment_method.attached':
        payment_method = event['data']['object']  # contains a stripe.PaymentMethod
        # Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
        print(f'payment method: {payment_method}')
    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(event['type']))

    return {"status": "success"}