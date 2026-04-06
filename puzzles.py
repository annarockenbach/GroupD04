puzzles = [
    {
        "question": "What has keys but can't open locks?",
        "answer": "piano",
        "hints": [
            "It is a musical instrument.",
            "It has black and white keys."
        ],
        "points": 10
    },
    {
        "question": "I speak without a mouth and hear without ears. What am I?",
        "answer": "echo",
        "hints": [
            "You often hear it in mountains.",
            "It repeats your voice."
        ],
        "points": 10
    },
    {
        "question": "What has a head and a tail but no body?",
        "answer": "coin",
        "hints": [
            "It is used as money.",
            "It can be flipped in a game."
        ],
        "points": 10
    },
    {
        "question": "The more you take, the more you leave behind. What are they?",
        "answer": "footsteps",
        "hints": [
            "You make them when you walk.",
            "They stay on the ground behind you."
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
