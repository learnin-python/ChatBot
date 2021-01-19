from functions import *

# Create chatbot
bot = create_bot('Jordan')

# Train all Data
train_all_data(bot)

# Check identity
identity = input("State your identity please: ")

# rules for responding at different identities
def check_identity(identity):

    owner_list = ['Mark', 'Jane']
    id_one = 'Mark',
    id_two = 'Jane'
    if id_one in owner_list:
        print("Welcome, Mark. Happy to have you at home.")
    elif id_two in owner_list:
        print("Mark is out right now, But you are welcome to the house.")
    else:
        print("Your access is denied here")
        exit()

    return identity
# Train chatbot with your custom data
house_owner = [
    "Who is the owner of the house?"
    "Mark Nicholas is the owner of the house"
]
custom_train(bot, house_owner)

print("------ Training custom Data ------")

# Start chatbot
start_chatbot(bot)
