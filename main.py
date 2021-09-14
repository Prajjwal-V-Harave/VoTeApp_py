# Import database module.
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
firebase_admin.initialize_app()
firebase_instance = firebase_admin.get_app()
default_app = firebase_admin.initialize_app(firebase_admin.credentials.Certificate("google-services.json"), {'databaseURL':"https://voteapp-1e334-default-rtdb.asia-southeast1.firebasedatabase.app"})


# Get a database reference to our posts
ref = db.reference('https://voteapp-1e334-default-rtdb.asia-southeast1.firebasedatabase.app')
# Read the data at the posts reference (this is a blocking operation)
print(ref.get())