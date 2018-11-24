# ChatBot-Python

This is a simple Chat Bot using DialogFlow, Python and Flask.

There is a simple Web UI which which lets the user interact with the bot.

## Steps to run the application 

1. Clone the project -- git clone "https://github.com/rubenquadros/ChatBot-Python.git"

2. Create your own bot at DialogFlow -- https://console.dialogflow.com/

3. Get your DialogFlow API key -- https://console.cloud.google.com/apis/credentials

   a. Select Dialogflow integrations under Service account.
   
   b. Then select JSON under key type.
   
   c. Next, make sure at the top menu that your bot is selected as the project name.
   
   d. Finally, click on the Create button to download the your API key
   
4. In index.py file change the following parameters:

   a. project_id  to your Project ID
   
   b. google_application_credentials to the directory where you JSON file is present.

5. Install the dependencies required by running "pip install -r requirements.txt" in the project root folder.

6. Finally run your application -- flask run

   Your app should now be running on http://localhost:5000 
