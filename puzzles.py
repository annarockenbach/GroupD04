puzzles = [
    {
        "question": "What number comes next? 2, 4, 6, 8?",
        "answer": "10",
        "hints": [
            "It follows an even number pattern.",
            "Add 2 to the last number."
        ],
        "points": 10
    },
    {
        "question": "Unscramble: PNOYHT",
        "answer": "python",
        "hints": [
            "It is a programming language.",
            "You are using it for this project."
        ],
        "points": 10
    },
    {
        "question": "5 + 7 * 2 = ?",
        "answer": "19",
        "hints": [
            "Use order of operations.",
            "Multiply before adding."
        ],
        "points": 10
    },
    {
        "question": "What has keys but can't open locks?",
        "answer": "piano",
        "hints": [
            "It is a musical instrument.",
            "It has black and white keys."
        ],
        "points": 15
    },
    {
        "question": "What gets wetter the more it dries?",
        "answer": "towel",
        "hints": [
            "You use it after a shower.",
            "It helps dry your body."
        ],
        "points": 15
    }
]

def get_total_puzzles():
    return len(puzzles)

def get_puzzle(stage):
    if 0 <= stage < len(puzzles):
        return puzzles[stage]
    return None

def get_question(stage):
    puzzle = get_puzzle(stage)
    if puzzle:
        return puzzle["question"]
    return None

def check_answer(stage, user_answer):
    puzzle = get_puzzle(stage)
    if puzzle is None:
        return False

    correct_answer = puzzle["answer"].lower().strip()
    user_answer = user_answer.lower().strip()

    return user_answer == correct_answer

def get_hint(stage, hint_number):
    puzzle = get_puzzle(stage)
    if puzzle is None:
        return None

    hints = puzzle["hints"]

    if 0 <= hint_number < len(hints):
        return hints[hint_number]

    return None

def get_points(stage):
    puzzle = get_puzzle(stage)
    if puzzle:
        return puzzle["points"]
    return 0
