from functions import *

# Create chatbot
bot = create_bot('Jordan')

# Train all Data
train_all_data(bot)

# Check identity
identity = input("State your identity please: ")

# rules for responding at different identities
if identity == "Mark":
    print("Welcome, Mark. Happy to have you at home.")
elif identity == "Jane":
    print("Mark is out right now, But you are welcome to the house.")
else:
    print("Your access is denied here")
    exit()

# Train chatbot with your custom data
house_owner = [
    "Who is the owner of the house?"
    "Mark Nicholas is the owner of the house"
]
custom_train(bot, house_owner)

print("------ Training custom Data ------")
# write and train your custom data here IF hte identity is Mark
if identity == 'Mark':
    city_born = [
        "Where was I born?",
        "Mark, you were born in Seattle."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is The Great Gatsby."
    ]

    fav_movie = [
        "What is my favourite movie?",
        "You have watched Interstellar more times than I can count."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You have always loved baseball."
    ]
    # Train chatbot with your custom data
    custom_train(bot, city_born)
    custom_train(bot, fav_book)
    custom_train(bot, fav_movie)
    custom_train(bot, fav_sports)

# Start chatbot
start_chatbot(bot)
