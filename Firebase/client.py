from config import firebase_config
import firebase_admin

app = firebase_admin.initialize_app(options=firebase_config)
db = firebase_admin.firestore.client(app)