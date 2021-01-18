from functions import *

# Create chatbot
bot = create_bot('Jordan')

# Train all Data
train_all_data(bot)

# Train chatbot with your custom data
house_owner = [
    "who is the owner of the house"
    "Mark Nicholas"
]
custom_train(bot, house_owner)


# Start chatbot
start_chatbot(bot)
