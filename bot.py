class Bot:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def greet(self):
        return f"Hello {self.name}, how may I help you today?"

    def questions(self, user_input):
        try:
            responses = {
                "what's your name": f"My name is {self.name}.",
                "how old are you": f"I am {self.age} years old.",
                "what is your gender": f"I am {self.sex}.",
                "hello": self.greet(),
                "hi": self.greet(),
            }

            user_input = user_input.lower().strip()
            return responses.get(user_input, "I'm not sure how to answer that.")
        except Exception as e:
            return f"Error occurred: {str(e)}"
