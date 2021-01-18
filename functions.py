# Function to create the chatbot
# We have the read_only to false so the chatbot learns from the user input as
def create_bot(name)
    from chatterbot import Chatbot
    Bot = ChatBot(name = name,
                  read_only = False,
                  logic_adapters = ["chatterbot.logic.BestMatch"],
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    return Bot



# Function to train the bot with a variety of topics
# The language we have chosen is english
# We can train the bot for other languages as well




# Function to train the bot with custom data
# It uses listTrainer to train data from Lists



# Function to start and take responses form the chatbot
# The chatbot stays runnning unless a world is typed the bye_list