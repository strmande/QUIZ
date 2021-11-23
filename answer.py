class Answer:
    def __init__(self, answer, correct_answer):
        self.__answer = answer
        self.__correct_answer = correct_answer

    def get_answer(self):
        return self.__answer

    def is_correct(self):
        return self.__correct_answer
