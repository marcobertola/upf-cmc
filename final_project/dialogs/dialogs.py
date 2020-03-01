from tts.tts import *
import random
import datetime

# Dialog Ids
#######################
ID_FIND_REQUEST_IS_READY = 1
ID_ASK_FOR_BUDGET = 2
ID_WELCOME = 3
ID_SHOW_LIST_OF_STRIKER = 4
ID_NO_VERB = 5
ID_ASK_ATTRIBUTE = 6
ID_FIND_HAS_PLAYER_NAME = 7
ID_ASK_PLAYER_ROLE = 8
ID_ASK_QUANTIFIER = 9
ID_BUDGET_NOT_VALID = 10
ID_THANKS = 11
ID_GOODBYE = 12
ID_INTENT_NOT_CLEAR = 13
ID_HELP = 14
ID_HOW_CAN_I_HELP_YOU = 15
ID_INCREASE_BUDGET = 16
ID_PLAYER_LIST = 17
ID_CONFIRM_BUY = 18
ID_RESTART_QUERY = 19
ID_TELL_ME_NAME = 20
ID_CONFIRM_BUY_HIM = 21
ID_PURCHASE_COMPLETE = 23
ID_NO_RESULTS = 24


########################


class DialogManager:
    text = ""
    voice = VoiceTTS()

    def saySomething(self):
        print(self.text)
        self.voice.processTextToSpeech(self.text)

    def processDialog(self, dial_id, list_parameters=[]):

        if dial_id == ID_HELP:
            self.text = "Don't worry I can help you. Are you looking for a striker, defender or striker. " \
                        " Are you looking for someone fast or strong? Just ask and .don't forget " \
                        "to tell me your budget! "

        if dial_id == ID_HOW_CAN_I_HELP_YOU:
            dt = datetime.datetime.now()
            case = random.randint(0, 2)
            greeting = ""
            greeting_2 = ""
            if dt.time() < datetime.time(12):
                greeting = "Good Morning"
                greeting_2 = "What a lovely morning"
            else:
                greeting = "Good Afternoon"
                greeting_2 = "What a lovely afternoon"

            if case == 0:
                self.text = "{0}! I am Leo, how can I help?".format(greeting)
            elif case == 1:
                self.text = "{0}! I am Leo, the best transfer market bot available. How may I be of service?".format(
                    greeting_2)
            elif case == 2:
                self.text = "Hi! I am Leo and I will help you find the best players. What are you looking for?"

        if dial_id == ID_INTENT_NOT_CLEAR:
            case = random.randint(0, 2)
            if case == 0:
                self.text = "Sorry, I didn't quite get that."
            elif case == 1:
                self.text = "Sorry, can you repeat that again?"
            elif case == 2:
                self.text = "Sorry, I missed that."

        if dial_id == ID_GOODBYE:
            case = random.randint(0, 2)
            if case == 0:
                self.text = "See you! Good luck in the league"
            elif case == 1:
                self.text = "It was a pleasure working with you. Bye!"
            elif case == 2:
                self.text = "Bye"

        if dial_id == ID_THANKS:
            case = random.randint(0, 1)
            if case == 0:
                self.text = "Ok, thanks!"
            if case == 1:
                self.text = "Thank you."

        if dial_id == ID_BUDGET_NOT_VALID:
            case = random.randint(0, 1)
            if case == 0:
                self.text = "Budget value seems invalid. Please use digits"
            elif case == 1:
                self.text = "Alas! My computing powers are limited. Please input a digit."
            elif case == 2:
                self.text = "Please specify the budget in digits."

        if dial_id == ID_ASK_FOR_BUDGET:
            case = random.randint(0, 2)
            if case == 0:
                self.text = "What's the allocated budget?(in millions)"
            elif case == 1:
                self.text = "Let's get the financial out of the way. Please specify your budget in millions."
            elif case == 2:
                self.text = "I bet the management gave you a huge transfer budget. All the values are in millions."

        if dial_id == ID_WELCOME:
            case = random.randint(0, 2)
            if case == 0:
                self.text = "Great! You are just a couple of questions away from a perfect player for your team."
            elif case == 1:
                self.text = "I understand that the transfer deadline is fast approaching. Not to worry, you are in " \
                            "safe hands. "
            elif case == 2:
                self.text = "I remember when I first started playing football, oh the smell of freshly cut " \
                            "grass, and..., oops! sorry I am getting distracted. Let's find you a player."

        if dial_id == ID_SHOW_LIST_OF_STRIKER:
            case - random.randint(0, 2)
            if case == 0:
                self.text = "This is the list of the {0} you are looking for".format(list_parameters[0])
            elif case == 1:
                self.text = "According to my sophisticated calculations, these are the best {0} for you.".format(
                    list_parameters[0])
            elif case == 2:
                self.text = "Here are some of the {0} for your team.".format(list_parameters[0])
        if dial_id == ID_NO_VERB:
            self.text = "Remember that you can always ask me to find " \
                        "or buy football players."

        if dial_id == ID_ASK_ATTRIBUTE:
            statement = ""
            if list_parameters[0] == "defender":
                statement = "Excellent choice. A strong defense is what every team is after."
            elif list_parameters[0] == "midfielder":
                statement = "Looking to boost the engine room? Excellent."
            elif list_parameters[0] == "forward":
                statement = "A lethal strike force can turn games on it's head."
            case = random.randint(0, 1)
            if case == 0:
                self.text = "{0} What quality interests you the most? You can choose speed,strength,or other " \
                            "attributes." \
                    .format(statement, list_parameters[0])
            elif case == 1:
                self.text = "{0} Are you looking for a fast, strong or a young upcoming talent? Tell me anything you " \
                            "need." \
                    .format(statement, list_parameters[0])

        if dial_id == ID_FIND_HAS_PLAYER_NAME:
            self.text = "Ok, here you have all the details for {0} ".format(list_parameters[0])

        if dial_id == ID_ASK_PLAYER_ROLE:
            case = random.randint(0, 2)
            if case == 0:
                self.text = "What player role do you need?"
            elif case == 1:
                self.text = "Are you looking for a defender, midfielder or a goal machine? "
            elif case == 2:
                self.text = "What position are you looking to improve?"

        if dial_id == ID_ASK_QUANTIFIER:
            case = random.randint(0, 1)
            if case == 0:
                self.text = "Are you looking for the best or an average {1}.Remember everything comes at a price.".format(
                    list_parameters[0],
                    list_parameters[1])
            elif case == 1:
                self.text = "Best {0} are costly while cheaper ones are average. Are you looking for an average or a " \
                            "best player?".format(list_parameters[0])
        if dial_id == ID_FIND_REQUEST_IS_READY:
            case = random.randint(0, 1)
            if 0 == case:
                self.text = "Ok, I will start searching for a {0} with a {1} {2}".format(list_parameters[0],
                                                                                         list_parameters[1],
                                                                                         list_parameters[2])
            elif 1 == case:
                self.text = "Ok, I search for a {1} {2} {0}".format(list_parameters[0], list_parameters[1],
                                                                    list_parameters[2])
        if dial_id == ID_INCREASE_BUDGET:
            self.text = "I didn't find any players. You need to increase the budget."
        if dial_id == ID_PLAYER_LIST:
            self.text = "Here's the list of the players I found."
        if dial_id == ID_CONFIRM_BUY:
            self.text = "Do you want to buy one of these players?"
        if dial_id == ID_RESTART_QUERY:
            self.text = "I feel bad the results are not what you expected, let's look for someone else"
        if dial_id == ID_TELL_ME_NAME:
            self.text = "Perfect! Please, tell me the name of the player you want. "
        if dial_id == ID_CONFIRM_BUY_HIM:
            self.text = "Perfect! Do you wanna buy him?"
        if dial_id == ID_PURCHASE_COMPLETE:
            self.text = "Good choice! Merry Christmas!"
        if dial_id == ID_NO_RESULTS:
            self.text = self.text = "Sorry, there is no {0} with a {1} {2}. Let's start again".format(
                list_parameters[0], list_parameters[1], list_parameters[2])

        self.saySomething()
