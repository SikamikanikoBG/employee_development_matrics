import streamlit as st

# Define user credentials (username and password)
user_credentials = {
    "peteto": "Alfi112233_",
    "mitko": "MySkills112233_",
    "arso": "12345687",  # Admin user Arso
    "vercheto": "BisiPisis112233_",
    "eli": "SeniorDb112233_"
    # Add more users as needed
}
def display_user(username, password):
    if username in user_credentials and password == user_credentials[username]:
        return username, f"Welcome, {username}!"
    else:
        return False, "Invalid credentials. Please try again."
