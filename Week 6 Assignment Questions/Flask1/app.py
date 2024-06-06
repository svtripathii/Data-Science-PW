from flask import Flask

app = Flask(__name__)

@app.route("/")
def company_details():
    """Displays company name, location, and contact details."""
    company_name = "ABC Corporation"
    location = "India"
    contact_details = "999-999-9999"
    return f"""
    Company Name: {company_name}<br>
    Location: {location}<br>
    Contact Detail: {contact_details}
    """

@app.route("/welcome")
def welcome():
    """Displays a welcome message."""
    return "Welcome to ABC Corporation"

if __name__ == "__main__":
    app.run(debug=True)
