
# Function to create the chatbot
# We have the read_only to false so the chatbot learns from the user input as
def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name=name,
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return Bot


# Function to train the bot with a variety of topics
# The language we have chosen is english
# We can train the bot for other languages as well
def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")


# Function to train the bot with custom data
# It uses listTrainer to train data from Lists
def custom_train(Bot, conversation):
    from chatterbot.trainers import ListenTrainer
    trainer = ListenTrainer(Bot)
    trainer.train(conversation)


# Function to start and take responses form the chatbot
# The chatbot stays runnning unless a world is typed the bye_list
def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Jordan. How can I Help you")
    bye_list = ["bye jordan", "bye", "good bye"]

    while (True):
        user_input == input("me: ")
        if user_input.lower() in bye_list:
            print("Jordan: Good bye and have a blessed day!")
            break
        reponse = Bot.get_reponse(user_input)
        print("Jordan:", response)
