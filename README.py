import re
import random

class Maaya:
    negative_response = ("no","sorry")
    exit_commands = ("quit","exit","bye")
    random_questions = (
                            "Why are you here?",
                            "Are there any humans here",
                            "Whats ur favrite food",
                            "Which galaxy are you from?")
    def __init__(self):
        self.alientalks = {
                            'developer_of_program':r'\s*developer\s',
                            'about_you':r'\s*you\s'
        }
    
    def greet(self):
        self.name = input("how may I call you?")
        response_to_user = input(f"Hi {self.name}, I am an aliien from galaxy2025 and I would like to know about your Planet. Nice that we could chat. Would you tell about your Planet..\n")
        if response_to_user in self.negative_response:
            print("Okeyy, we can connect back later on a different topic..")
            return self.chat()
        
    def make_exit(self,reply):
        if reply in self.exit_commands:
            print("Bye! Take Care.. See yaaaah")
            return True
        
    def chat(self):
        response_to_user = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(response_to_user):
            response_to_user(self.match_reply(response_to_user))
            
    def match_reply(self, response_to_user):
        if 'developer' in response_to_user:
            return self.developer_string()
        elif 'you' in response_to_user:
            return "I'm an alien"
        else:
            self.no_intent_matched()
        
    def developer_string(self):
        response = ("This is the developer. I an alien", "I have no developer")
        return random.choice(response)
    
    def no_intent_match(self):
        response = { "Could you tell again, I couldnt get that dudee"}
        return random.choice(response)
        
alien1 = Maaya()
alien1.greet()
