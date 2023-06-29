# Apex_Tracker_App
Video Demo:  <https://youtu.be/z7h9mdkFHnE>

References
<https://blog.gitguardian.com/how-to-handle-secrets-in-python/>
don't forget to use the init_db.py to make your db.
make sure to install sql to run!
$ pip install SQlite3
you must also install the cs50 library using 
$ pip install cs50
install flask:
$ pip install Flask
install dotenv:
$ pip install python-dotenv

To Run the app,set your api key, then while in Apex_App/app use flask run.

In order to make a call, you have to got to https://portal.apexlegendsapi.com/ and make a key. then add it to the .env file like so: API_KEY="<your_Key>"

This app was created by Jack and Liam Drisdelle for Harvard's CS50 Course.

Apex Tracker App was built from scratch using the material from Week 6-9 of CS50, including material from the lectures and shorts, and templates taken from the labs and problem sets. 

This app is designed to display the user's Apex Legends account. Apex Legends is a Battle Royale Videogame with unique characters, each with their own stats and unlockable badges. We wanted to create an app that filled a need that we have heard people address before. People want to show off their cool character badges and stats without opening up the game. What is there was a way to show someone your cool account without going through the hassle of having them next to you while you open the game and wait for it to load. 

In this web application we use Python, Flask, and Jinja to pull json data from a third-party API. We have multiple HTML pages and use jinja to include them into one page where the player data is displayed. 

The first thing we did was build the app.py. In the app.py we used the get and post method to grab the player id and platform of the account(ie. XBOX, PlayStation, PC) someone wants to look up. Because the game is onmultiple platforms, we have to specify what platform the acconut is on in order to properly pull the account from the API. Then, we grab only the info we need from the API, such as selected Legend(character) and stat trackers. 

index.html is the homepage of the app. In it we have a brief description of the website, a search bar, search button, and image of the game logo. 

player.html it the page we take the user to when they successfully searched for their account. In it we use jinja to connect four html blocks. We have basics.html, banner.html, history.html, and footer.html.

Basics.html is a short div that displays the basic data of the account, such as their name, level, platform, and current rank in the game. 

Banner.html is a bit longer, because it displays their character and their selected trackers and badges they have. It is shown in a neat list form. 

History.html is the best part of this app. Everytime an account gets searched for and displayed on our app, we put their current data into a database of their account. On the bottom of the page we have a table displaying everytime they have searched for their account, including a timestamp and their current stats. Using this we can show the progress of an account as they increase their stats and rank up. 

Lastly for our html pages we have footer.html. It is a really short page with just a line of text styled onto the botom of the page reading our names as a credit watermark.

We also have a styles.css folder. We wanted the look of the app to be really clean and simple with nothing on the screen looking bulky or out of place. We took a little bit of insiration from Discord, because we believe that dark themes are less harsh to the user. A grey theme with all the text centered to the middle of the page with thin white lines in between was our end goal, and we achieved it. 

The last thing to mention is the schema.sql. It is the format of the table we are using for our database.

Thank you for reading, and we are grateful to have taken CS50.