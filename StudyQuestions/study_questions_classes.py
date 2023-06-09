class User:
    def __init__(self, id, username) -> None:
        self._user_id = id
        self._username = username
        self._question_bank = {}

    def get_user_id(self):
        return self._user_id
    
    def get_username(self):
        return self._username
    
    def get_user_question_bank(self):
        return self._question_bank
    
    def add_question_to_user(self, question_object):
        pass



class Question:
    def __init__(self, id, question, answer, subject) -> None:
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
        self._last_user_id = 000
        self._last_question_id = 000

    def get_questions(self):
        return self._questions

    def get_members(self):
        return self._members

    def create_user(self, username):
        self._last_user_id += 1
        user = User(self._last_user_id, username)
        self._members[user.get_user_id()] = user

    


lib = Library()
lib.create_user('jesse')
lib.create_user('bob')
lib.create_user('sara')

print(lib.get_members())

# members = lib.get_members()
# print(members[1].get_username())
         
