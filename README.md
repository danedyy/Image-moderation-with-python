# Image-recognition-with-python
this is a computer vision software that let you moderate images base on drug, alcohol, nudity, weapons etc 
Steps to using the image moderation application:
Install flask using the instructions below
On your command line type this commands
pip install Flask
flask is now install 
Install SightEngine SDK 
pip install sightengine
configuration of sightengine:
https://sightengine.com
open the link above and signup for a free account
login and click on account and get your API credentials.
Open index.py and fill in your API details in the function below.
client = SightengineClient('API_USER', 'API_SECRET')
Now on your command line navigate to where you unzipped the source folder and open the folder in your command line and type the following command to run the program.
$ export FLASK_APP=index.py
$ flask run
If everything want successfully you will get the following response 
*  Running on http://127.0.0.1:5000/
Open the link on your browser and you are good to go.

