from puzzles import get_question, check_answer, get_hint, get_points, get_total_puzzles

stage = 0
hint_used = 0

print("Total puzzles:", get_total_puzzles())
print("Question:", get_question(stage))

answer = input("Enter your answer (or type hint): ")

if answer.lower() == "hint":
    print("Hint 1:", get_hint(stage, 0))
    answer = input("Enter your answer: ")

if check_answer(stage, answer):
    print("Correct!")
    print("Points earned:", get_points(stage))
else:
    print("Wrong!")
