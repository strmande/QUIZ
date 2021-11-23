from random import shuffle


class Question:
    __keys = ['a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self, question, point):
        self.question = question
        self.__point = point
        self.__correct = True
        self.__answers = []

    def add_answer(self, answer):
        self.__answers.append(answer)

    def ask_question(self, number):
        print(f'{number}. {self.question}')
        shuffle(self.__answers)
        for index, answer in enumerate(self.__answers):
            print(f'   {self.__keys[index]}. {answer.get_answer()}')

        answer = input('Your answer: ')
        while answer not in self.__keys:
            print('Invalid input! Please choose from the options above.')
            print()
            answer = input('Enter you answer: ')

        if not self.__answers[self.__keys.index(answer)].is_correct():
            self.__correct = False

        print()

    def get_point(self):
        return self.__point

    def get_status(self):
        return self.__correct
