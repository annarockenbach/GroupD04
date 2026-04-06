class Player:
    def __init__(self, name):
        self.name = name
        self.stage = 0
        self.score = 0
        self.hints_used = 0
        self.finished = False

    def next_stage(self):
        self.stage += 1

    def add_score(self, points):
        self.score += points

    def use_hint(self):
        self.hints_used += 1

    def finish_game(self):
        self.finished = True

    def show_status(self):
        return (
            f"Player: {self.name}\n"
            f"Current Stage: {self.stage}\n"
            f"Score: {self.score}\n"
            f"Hints Used: {self.hints_used}\n"
            f"Finished: {self.finished}"
        )
