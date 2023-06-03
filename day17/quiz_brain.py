class Quiz:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)? ")
        if self.check_answer(answer):
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, answer):
        return self.questions_list[self.question_number].answer == answer