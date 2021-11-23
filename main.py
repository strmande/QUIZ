from quiz import Quiz
from question import Question
from answer import Answer

# O(1)
# O(n)
# O(log n)
# O(n^2)

quiz = Quiz('Quiz 1')

# Question 1
question = Question('What year are we in?', 2)


answer = Answer('2010', False)
question.add_answer(answer)

answer = Answer('2021', True)
question.add_answer(answer)

answer = Answer('2000', False)
question.add_answer(answer)
quiz.add_question(question)

# Question 2
question = Question('What month are we currently in?', 2)

answer = Answer('May', True)
question.add_answer(answer)

answer = Answer('April', False)
question.add_answer(answer)
quiz.add_question(question)

# Question 3
question = Question('What planet are we on?', 5)

answer = Answer('Mars', False)
question.add_answer(answer)

answer = Answer('Venus', False)
question.add_answer(answer)

answer = Answer('Jupiter', False)
question.add_answer(answer)

answer = Answer('Earth', True)
question.add_answer(answer)
quiz.add_question(question)

# Question 4
question = Question('Who is the president of the US in 2021', 6)

answer = Answer('Trump', False)
question.add_answer(answer)

answer = Answer('Obama', False)
question.add_answer(answer)

answer = Answer('Biden', True)
question.add_answer(answer)

answer = Answer('Kanye', False)
question.add_answer(answer)
quiz.add_question(question)

# Question 5
question = Question('What country is in the continent of Asia?', 5)

answer = Answer('India', True)
question.add_answer(answer)

answer = Answer('Grece', False)
question.add_answer(answer)

answer = Answer('France', False)
question.add_answer(answer)

answer = Answer('England', False)
question.add_answer(answer)

answer = Answer('Mexico', False)
question.add_answer(answer)

answer = Answer('Brazil', False)
question.add_answer(answer)
quiz.add_question(question)


## Alternative (preferred)
# =================================================================================================
# qs_as = [
#     (
#         'What country is in the continent of Asia?',
#         5,
#         [
#             ('India', True),
#             ('Grece', False),
#             ('France', False),
#             ('England', False),
#             ('Mexico', False),
#             ('Brazil', False)
#         ]
#     ),
#     (
#         'Who is the president of the US in 2021?',
#         5,
#         [
#             ('Trump', False),
#             ('Obama', False),
#             ('Kanye', False),
#             ('Biden', True)

#         ]
#     ),
#     (
#         'What planet are we on?',
#         5,
#         [
#             ('Venus', False),
#             ('Earth', True),
#             ('Jupiter', False),
#             ('Mars', False),
#         ]
#     ),
#     (
#         'What month are we currently in?',
#         5,
#         [
#             ('April', False),
#             ('May', True)
#         ]
#     ),
#     (
#         'What year are we in?',
#         5,
#         [
#             ('2000', False),
#             ('2021', True),
#             ('2010', False)
#         ]
#     ),
# ]

# for qa in qsxx_as:
#     question = Question(qa[0], qa[1])

#     for ans in qa[2]:
#         answer = Answer(ans[0], ans[1])
#         question.add_answer(answer)

#     quiz.add_question(question)

# =================================================================================================


quiz.start()
quiz.calculate_score()
quiz.show_result()
