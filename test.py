import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store players and their corresponding teams
players = {}
team_batting = []
team_bowling = []

# Function to start the game
def start_game(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Book Cricket! Please enter the names of players for batting and bowling teams.")

# Function to add players to batting team
def add_batting_players(update: Update, context: CallbackContext):
    global team_batting
    text = update.message.text
    players_list = text.split(",")
    team_batting = [player.strip() for player in players_list]
    update.message.reply_text("Batting team set!")

# Function to add players to bowling team
def add_bowling_players(update: Update, context: CallbackContext):
    global team_bowling
    text = update.message.text
    players_list = text.split(",")
    team_bowling = [player.strip() for player in players_list]
    update.message.reply_text("Bowling team set!")

# Function to simulate a ball
def simulate_ball(update: Update, context: CallbackContext):
    global team_batting, team_bowling
    runs = random.randint(1, 6)  # Generate random runs between 1 and 6
    bowler = random.choice(team_bowling)
    batsman = random.choice(team_batting)
    update.message.reply_text(f"{batsman} is batting against {bowler} and scores {runs} runs!")
    update.message.reply_text(f"Live Score: {runs} runs")
    # Update score here and post in the group

# Function to handle unknown commands
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that command.")

def main():
    # Set up the Telegram bot
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Define command handlers
    dp.add_handler(CommandHandler("start", start_game))
    dp.add_handler(MessageHandler(Filters.regex(r'^/add_batting_players'), add_batting_players))
    dp.add_handler(MessageHandler(Filters.regex(r'^/add_bowling_players'), add_bowling_players))
    dp.add_handler(MessageHandler(Filters.regex(r'^/simulate_ball'), simulate_ball))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Start the bot
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
