# SNAKEBOT

# To-do:

There's also a Trello board containing a few other todos
- [x] battlesnake-conforming web endpoints
- [ ] snake-ai v1
- [ ] come up with a cool snake name


## What is this?

- Written in Python3
- Uses Django as web framework
- Hosted in Heroku (free tiers)

####Related local code repos: 
- Try: snakebot emulator for easy changes? 
- board: game board server, for local testing

Note: local testing was really difficult the last time it was attempted

####Hints: 
don't forget to import the virtualenv environment through the venv/Scripts/Activate.ps1
read the docs silly

### How to Heroku: 
- shutting down dynos: `heroku ps:scale web=0`
- seeing logs: `heroku --logs tail/head`
- starting a dyno: `heroku ps:scale web=1`
- updating heroku app: `git push heroku  master`

