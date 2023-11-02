from app import app
from contacts import contacts

app.register_blueprint(contacts)

# starting the app
app.run(port=3000, debug=True)