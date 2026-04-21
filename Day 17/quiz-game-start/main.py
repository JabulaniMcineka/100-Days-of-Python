from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for question in question_data["results"]:
    question_text = question["question"] 
    question_answer= question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
    
print("You jhave completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



# question_data = {
#     "response_code": 0,
#     "results": [
#         {
#             "type": "boolean",
#             "difficulty": "easy",
#             "category": "Science: Computers",
#             "question": "Linus Torvalds created Linux and Git.",
#             "correct_answer": "True",
#             "incorrect_answers": ["False"],
#         },



#         question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},