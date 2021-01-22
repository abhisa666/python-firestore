import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import random

# Use the application default credentials
cred = credentials.Certificate("./web-kiosk-b3b51-firebase-adminsdk-3qw0x-9c311e9247.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

products = [{
    "image":"https://firebasestorage.googleapis.com/v0/b/web-kiosk-b3b51.appspot.com/o/cheetos.jpg?alt=media&token=a1b9ffdc-c5ee-4d6f-a9c4-26916d437fba",
    "name":"Cheetos",
    "price":10,
    "quantity":1,
    "upc":"0028400589895"
},{
    "image":"https://firebasestorage.googleapis.com/v0/b/web-kiosk-b3b51.appspot.com/o/dasanidrops.png?alt=media&token=2b32e666-fbf3-4dab-a0da-b32aac881041",
    "name":"Dasani Drops",
    "price":20,
    "quantity":1,
    "upc":"0049000001211"
},{
    "image":"https://firebasestorage.googleapis.com/v0/b/web-kiosk-b3b51.appspot.com/o/coke.jpg?alt=media&token=7b8b6567-9ffe-4955-b76f-6dc9a5a04979",
    "name":"Coca-Cola",
    "price":15,
    "quantity":1,
    "upc":"0049000052350"
},{
    "image":"https://firebasestorage.googleapis.com/v0/b/web-kiosk-b3b51.appspot.com/o/Nescafe.jpg?alt=media&token=c1268d05-a984-4ca4-9a35-64109b455c35",
    "name":"Nescafe Clasico",
    "price":40,
    "quantity":1,
    "upc":"0745352115209"
}]

random_index = random.randint(0,3)

print(products[random_index])

col_ref = db.collection(u'users').document(u'abhisa666@gmail.com').collection(u'cart')

col_ref.document(products[random_index]["upc"]).set(products[random_index])





