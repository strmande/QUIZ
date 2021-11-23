from random import shuffle


class Quiz:
    def __init__(self, title):
        self.__title = title
        self.__questions = []
        self.__final_score = 0
        self.__total_score = 0

    def add_question(self, question):
        self.__questions.append(question)
        self.__count_total_score(question.get_point())

    def start(self):
        shuffle(self.__questions)
        for index, question in enumerate(self.__questions):
            question.ask_question(index + 1)

    def calculate_score(self):
        for question in self.__questions:
            if question.get_status():
                self.__final_score += question.get_point()

    def __count_total_score(self, score):
        self.__total_score += score

    def show_result(self):
        print(f'{self.__title}, {len(self.__questions)} questions')
        percent = round(self.__final_score/self.__total_score * 100)
        print(f'{self.__final_score}/{self.__total_score} ( {percent}%, {self.__get_letter_grade(percent)} )')

    def get_title(self):
        return self.__title

    def __get_letter_grade(self, percent):
        grade = None
        if percent >= 90 and percent <= 100:
            grade = 'A'
        elif percent >= 80 and percent < 90:
            grade = 'B'
        elif percent >= 70 and percent < 80:
            grade = 'C'
        elif percent >= 60 and percent <= 70:
            grade = 'D'
        else:
            grade = 'F'

        return grade
