class User:
    def __init__(self, username) -> None:
        self._username = username
        self._id = 0
        self._question_bank = {}
        self._next_question_id = 0



    # @property
    # def question_id(self):
    #     return self._question_id   
    
    # @question_id.setter   
    # def change_question_id(self, value):
    #     self.question_id = value

    # @question_id.setter
    # def reset_question_id(self):
    #     self.question_id = 0

    
    # library.question_id #id
    # library.change_question_id = 17 #.change_question_id(17)
    # library.reset_question_id # reset to zero




    def get_username(self):
        return self._username

    def get_user_id(self):
        return self._id

    def get_user_question_bank(self):
        return self._question_bank

    def get_next_question_id(self):
        return self._next_question_id

    def set_user_id(self, id):
        self._id = id

    def set_next_question_id(self):
        self._next_question_id += 1
        return f"{self._id}.{self._next_question_id}"

    def add_question_to_user(self, question_object):
        self._question_bank[question_object.get_question_id()
                            ] = question_object


class Question:
    def __init__(self, id, subject, question, answer) -> None:
        self._question_id = id
        self._question = question
        self._answer = answer
        self._subject = subject

    def get_question_id(self):
        return self._question_id

    def get_question(self):
        return self._question

    def get_answer(self):
        return self._answer

    def get_subject(self):
        return self._subject

    def get_question_info(self):
        return f"Subject: {self._subject}, Question: {self._question}, Answer: {self._answer}"


class Library:
    def __init__(self) -> None:
        self._questions = {}
        self._members = {}
        self._last_user_id = 0
        self._last_question_id = 0

    def get_questions(self):
        return self._questions

    def get_members(self):
        return self._members

    def add_lib_user(self, user_obj):
        self._last_user_id += 1
        user_obj.set_user_id(self._last_user_id)
        self._members[user_obj.get_username()] = user_obj
        return f"{user_obj.get_username()} added to library"

    def add_question(self, q_dict) #user, subject, question, answer):
        user = q_dict['name']
        subject = q_dict['subject']
        question = q_dict['question']
        answer = q_dict['answer']
        
        if user in self._members:
            
            question_id = self._members[user].set_next_question_id()
            question_obj = question_id
            question_obj = Question(question_id, subject, question, answer)
            self._members[user].add_question_to_user(question_obj)
            self._questions[question_id] = question_obj


p1 = User("Jesse")
p2 = User("Bob")
p3 = User("Sara")

lib = Library()

lib.add_lib_user(p1)
lib.add_lib_user(p2)
lib.add_lib_user(p3)

print(lib.get_members())
question1_info = "Jesse", "Math", "What is one plus one?", "Two"
question_dict = {
    'name': 'Jesse',
    'subject' : 'Math',
    'question': 'What is one plus one',
    'answer' : "Two"
}


lib.add_question(question_dict)
lib.add_question("Jesse", "Math", "What is two plus two?", "Three")
lib.add_question("Jesse", "History", "What is today?",
                 "Monday - Boo Mondays!!!")
lib.add_question("Jesse", "Misc", "What color is the sun?", "Yellow")
lib.add_question("Jesse", "Math", "What color is the sky", "Blue")

print(lib.get_questions())
print(p1.get_user_question_bank())


# members = lib.get_members()
# print(members[1].get_username())
