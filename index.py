from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher
from google.oauth2 import service_account

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# run Flask app
if __name__ == "__main__":
    app.run()


@app.route('/send_message', methods=['POST'])
def send_message():
    project_id = "idiot-5d56a"
    session_id = "12345"
    language_code = "en"
    messages = request.form['my-message']
    google_application_credentials = service_account.Credentials.from_service_account_file(
        r'C:\Users\Ruben\Downloads\Idiot-b0b2d6cde4af.json')
    session_client = dialogflow.SessionsClient(credentials=google_application_credentials)
    session = session_client.session_path(project_id, session_id)

    if messages:
        text_input = dialogflow.types.TextInput(
            text=messages, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        my_response = response.query_result.fulfillment_text

    else:
        my_response = "I didn't quite get that."

    return my_response
