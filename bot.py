from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Your bot token from BotFather
TOKEN = '7040662268:AAH6B7I7ciuAZ8TDayISgGMCRx2-BMhNM9U'

# Function to generate a key
def generate_key() -> str:
    return 'KEY-' + ''.join(random.choices('
BIKE-2PM-26AQ-0MEW-PJD

BIKE-0PC-364P-08DM-XYM

BIKE-3PD-KTVB-0GCP-CY2

BIKE-2Q8-Y27R-08S4-0YS

BIKE-2QM-W2RS-0JVC-7V8

BIKE-1QC-XJ6Z-0MV4-EHN

BIKE-3QG-W281-0WS4-FTG

BIKE-2Q4-W8KD-00SC-8TA

BIKE-1P4-T825-0YTM-4XX

BIKE-2PM-WRTZ-0ARC-5XG

BIKE-3Q8-RASV-06SC-03T

BIKE-3QS-HJAW-0JVW-VKT

BIKE-1P1-NJCY-04VM-QK6

BIKE-2PD-PJW6-0TSM-VTR

BIKE-0QD-J2E6-0GRW-JK4

BIKE-0QS-QJFF-0TSM-JB2

BIKE-0Q9-P3EN-04RM-WAK

BIKE-1Q5-G2A8-0GTM-TDF

BIKE-2Q1-J3DC-0EVC-G2S

BIKE-1PH-VMPN-0MS8-QC2', k=10))

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Hamster Kombat Key Generator! Type /generate to get your key.')

# Generate command handler
def generate(update: Update, context: CallbackContext) -> None:
    key = generate_key()
    update.message.reply_text(f'Here is your key: {key}')

def main() -> None:
    # Create Updater object with bot token
    updater = Updater(TOKEN)
    
    # Get dispatcher to register handlers
    dp = updater.dispatcher
    
    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("generate", generate))
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
