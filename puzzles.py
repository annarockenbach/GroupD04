
puzzles = [
    {
        "question": "What has keys but can't open locks?",
        "answer": "piano",
        "hint": "It is a musical instrument."
    },
    {
        "question": "I speak without a mouth and hear without ears. What am I?",
        "answer": "echo",
        "hint": "You often hear it in mountains or empty places."
    },
    {
        "question": "What has a head and a tail but no body?",
        "answer": "coin",
        "hint": "It is money."
    },
    {
        "question": "The more you take, the more you leave behind. What are they?",
        "answer": "footsteps",
        "hint": "You make them when you walk."
    },
    {
        "question": "What gets wetter the more it dries?",
        "answer": "towel",
        "hint": "You use it after a shower."
    }
]


def get_total_puzzles():
    return len(puzzles)

def get_puzzle(stage):
    if stage >= 0 and stage < len(puzzles):
        return puzzles[stage]
    return None


def get_question(stage):
    puzzle = get_puzzle(stage)
    if puzzle:
        return puzzle["question"]
    return None


def get_hint(stage):
    puzzle = get_puzzle(stage)
    if puzzle:
        return puzzle["hint"]
    return None


def check_answer(stage, user_answer):
    puzzle = get_puzzle(stage)

    if puzzle is None:
        return False

    correct_answer = puzzle["answer"].lower().strip()
    user_answer = user_answer.lower().strip()

    return user_answer == correct_answer
