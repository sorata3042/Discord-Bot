# Discord-Bot

This repository is here to display the code used and is not completely functional; the bot would require other files such as those stated in requirements in order to function. My bot is currently hosted on Heroku. 

## Important Links
Documentation for discord python api: [discord.py](https://discordpy.readthedocs.io/en/latest/index.html).

Click [here](https://discordapp.com/oauth2/authorize?client_id=610685983242846219&permissions=8&scope=bot) to add my bot to a discord server and type !help for all of the commands. 

## Description
The main file is the discord-bot.py file. The rest of the .py files are placed in a separate folder labeled /cogs. 

In order for the program to run there should be a token.txt file that contains a token pulled from the [discord developer portal](https://discordapp.com/developers/). 
My token is not uploaded for security. 

## Requirements
For pictures.py the code requires a folder /temp. This folder holds the temporary images that get uploaded. GetImage.py is used to create a connection with Google Photos API and to obtain said images from Google Photos. It requires  OAuth2 credential verification through a token .pickle file through running the code and a credential .json file from Google Cloud Platform. 

Procfile and requirements.txt are needed for me to run my bot on [heroku](https://heroku.com/).


