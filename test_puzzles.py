from puzzles import get_question, get_hint, check_answer, get_total_puzzles

stage = 0

print("Total puzzles:", get_total_puzzles())
print("Question:", get_question(stage))

answer = input("Enter your answer: ")

if check_answer(stage, answer):
    print("Correct!")
else:
    print("Wrong!")
    print("Hint:", get_hint(stage))
