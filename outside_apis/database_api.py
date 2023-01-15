from multiprocessing import Process
import os
from datetime import datetime


from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv('CONNECTION_STRING'))
if "ecommerce"  in client.list_database_names():
  db = client[os.getenv('DB_NAME')]
  collection = db[os.getenv('COLLECTION_NAME')]


def create_collections():

    if "ecommerce" not in client.list_database_names():
        db = client[os.getenv('DB_NAME')]
        

        # Create a connection to the MongoDB server

        # Create the collections

        # check if existis collectinos
        collections = ["products", "categories", "products_categories", "users", "addresses", "cart",
                       "orders", "invoices", "invoices_details", "payments", "reviews", "coupons",
                       "shipping", "taxes", "webhooks", "webhooks_logs", "conversation_logs"]

        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)
                print(f"{collection} collection created.")
        print(f"All collections created in {os.getenv('DB_NAME')} database.")
       
        # Products collection
        products = [
            {"name": "Product 1", "price": 10.99, "category_id": "123",
                "description": "Product 1 description"},
            {"name": "Product 2", "price": 15.99, "category_id": "456",
                "description": "Product 2 description"},
            {"name": "Product 3", "price": 20.99, "category_id": "789",
                "description": "Product 3 description"}
        ]
        db.products.insert_many(products)

        # Categories collection
        categories = [
            {"name": "Category 1", "description": "Category 1 description"},
            {"name": "Category 2", "description": "Category 2 description"},
            {"name": "Category 3", "description": "Category 3 description"}
        ]
        db.categories.insert_many(categories)

        # Users collection
        users = [
            {"name": "John Doe", "email": "johndoe@example.com",
                "password": "password123"},
            {"name": "Jane Doe", "email": "janedoe@example.com",
                "password": "password456"},
            {"name": "Mike Smith", "email": "mikesmith@example.com",
                "password": "password789"}
        ]
        db.users.insert_many(users)

        # Addresses collection
        addresses = [
            {"user_id": "123", "address1": "123 Main St", "city": "Anytown",
                "state": "NY", "zip": "12345", "type_adress": "billing address"},
            {"user_id": "456", "address1": "456 Park Ave", "city": "Anytown",
                "state": "NY", "zip": "67890", "type_adress": "billing address"},
            {"user_id": "789", "address1": "789 Elm St", "city": "Anytown",
                "state": "NY", "zip": "11111", "type_adress": "billing address"}
        ]
        db.addresses.insert_many(addresses)

        # Cart collection
        cart = [
            {"user_id": "123", "product_id": "abc", "quantity": 2},
            {"user_id": "456", "product_id": "def", "quantity": 1},
            {"user_id": "789", "product_id": "ghi", "quantity": 3}
        ]
        db.cart.insert_many(cart)

        # Orders collection
        orders = [
            {"user_id": "123", "billing_address_id": "abc",
                "shipping_address_id": "def", "status": "pending"},
            {"user_id": "456", "billing_address_id": "ghi",
                "shipping_address_id": "jkl", "status": "pending"},
            {"user_id": "789", "billing_address_id": "mno",
                "shipping_address_id": "pqr", "status": "pending"}
        ]
        db.orders.insert_many(orders)

        # Invoices collection
        invoices = [
            {"order_id": "123", "invoice_date": datetime.now(), "total": 10.99},
            {"order_id": "456", "invoice_date": datetime.now(), "total": 15.99},
            {"order_id": "789", "invoice_date": datetime.now(), "total": 20.99}
        ]
        db.invoices.insert_many(invoices)

        # Invoices details collection
        invoices_details = [
            {"invoice_id": "123", "product_id": "abc",
                "quantity": 2, "price": 10.99},
            {"invoice_id": "456", "product_id": "def",
                "quantity": 1, "price": 15.99},
            {"invoice_id": "789", "product_id": "ghi", "quantity": 3, "price": 20.99}
        ]
        db.invoices_details.insert_many(invoices_details)

        # Payments collection
        payments = [
            {"invoice_id": "123", "method": "credit_card",
                "payment_date": datetime.now(), "amount": 10.99},
            {"invoice_id": "456", "method": "paypal",
                "payment_date": datetime.now(), "amount": 15.99},
            {"invoice_id": "789", "method": "p2p",
                "payment_date": datetime.now(), "amount": 20.99}


        ]
        db.payments.insert_many(payments)

        # Reviews collection
        reviews = [
            {"product_id": "123", "user_id": "abc", "review": "Product 1 review"},
            {"product_id": "456", "user_id": "def", "review": "Product 2 review"},
            {"product_id": "789", "user_id": "ghi", "review": "Product 3 review"}
        ]
        db.reviews.insert_many(reviews)

        # Coupons collection
        coupons = [
            {"code": "SALE10", "start_date": "2022-01-01",
                "end_date": "2022-12-31", "discount": 10, "status": "active"},
            {"code": "SALE15", "start_date": "2022-01-01",
                "end_date": "2022-12-31", "discount": 15, "status": "active"},
            {"code": "SALE20", "start_date": "2022-01-01",
                "end_date": "2022-12-31", "discount": 20, "status": "active"},
            {"code": "FREESHIPPING", "start_date": "2023-02-01",
                "end_date": "2023-02-28", "discount": 0, "status": "active"}
        ]

        db.coupons.insert_many(coupons)

        # Products categories collection
        products_categories = [
            {"product_id": "123", "category_id": "abc"},
            {"product_id": "456", "category_id": "def"},
            {"product_id": "789", "category_id": "ghi"}
        ]
        db.products_categories.insert_many(products_categories)

        # Shipping collection
        shipping = [
            {"order_id": "123", "shipping_date": datetime.now(
            ), "tracking_number": "1234567890", "status": "shipped"},
            {"order_id": "456", "shipping_date": datetime.now(
            ), "tracking_number": "1234567890", "status": "shipped"},
            {"order_id": "789", "shipping_date": datetime.now(
            ), "tracking_number": "1234567890", "status": "shipped"}
        ]
        db.shipping.insert_many(shipping)

        # Taxes collection
        taxes = [
            {"description": "Sales Tax", "percentage": 8.875, "status": "active"},
            {"description": "Import Tax", "percentage": 5, "status": "active"},
            {"description": "VAT Tax", "percentage": 16, "status": "active"}
        ]
        db.taxes.insert_many(taxes)

        # Webhooks collection
        webhooks = [
            {"event": "order_created",
                "url": "http://example.com/webhooks/order_created", "status": "active"},
            {"event": "payment_received",
                "url": "http://example.com/webhooks/payment_received", "status": "active"},
            {"event": "product_updated",
                "url": "http://example.com/webhooks/product_updated", "status": "active"}
        ]
        db.webhooks.insert_many(webhooks)

        # Webhooks_logs collection
        webhooks_logs = [
            {"webhook_id": "123", "event": "order_created", "payload": {
                "order_id": "123", "user_id": "abc"}, "status": "success", "response_code": 200},
            {"webhook_id": "456", "event": "payment_received", "payload": {
                "order_id": "456", "user_id": "def"}, "status": "success", "response_code": 200},
            {"webhook_id": "789", "event": "product_updated", "payload": {
                "order_id": "789", "user_id": "ghi"}, "status": "success", "response_code": 200}
        ]
        db.webhooks_logs.insert_many(webhooks_logs)

        # Conversation_logs collection

        conversation_logs = [
            {"user_id": "123", "conversation_id": "abc",
                "message": "Hello, how can I help you?", "date": datetime.now()},
            {"user_id": "456", "conversation_id": "def",
                "message": "I'm looking for a new phone", "date": datetime.now()},
            {"user_id": "789", "conversation_id": "ghi",
                "message": "I'm interested in buying the new iPhone", "date": datetime.now()}
        ]

        db.conversation_logs.insert_many(conversation_logs)
        # Print the list of collections


def create_user(user: dict) -> bool:
    '''
    Create a new user

    Parameters:
        - user(dict)

    Returns:
        - bool, 0 for failure and 1 for success
    '''

    result = collection.find_one(
        {
            'telegram_id': user['telegram_id']
        }
    )

    if not result:
        result = collection.insert_one(user)
        return result.acknowledged
    return False


def insert_message(telegram_id: int, message: dict) -> bool:
    '''
    Update messages for the user

    Parameters:
        - telegram_id(int): user telegram id
        - message(dict): mesage document to insert

    Returns:
        - bool, 0 for failure and 1 for success
    '''

    result = collection.find_one_and_update(
        {
            'telegram_id': telegram_id
        },
        {
            '$push': {
                'messages': message
            }
        }
    )

    if not result:
        return False
    else:
        return True


def save_message_to_db(data: dict, response: str) -> bool:
    '''
    Process thewhole body and update the db

    Parameters:
        - data(dict): the incoming request from Telegram

    Returns:
        - bool, 0 for failure and 1 for success
    '''

    message = {
        'query': data['message'],
        'response': response,
        'created_at': datetime.now().strftime('%d/%m/%Y, %H:%M')
    }

    user = {
        'first_name': data['first_name'],
        'telegram_id': data['sender_id'],
        'messages': [message]
    }

    result = create_user(user)

    if result:
        return True
    else:
        result = insert_message(data['sender_id'], message)
        return result
