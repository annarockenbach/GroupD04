import socket
import time
from puzzles import puzzles
from email_results import send_email

HOST = "0.0.0.0"
PORT = 12345

TIME_LIMIT = 300  # 5 minutes total game time
MAX_HINTS = 2

players = []
scores = {}
hints_used = {}
player_times = {}


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))

    server.listen(2)

    print("Server started. Waiting for players...")

    while len(players) < 2:

        conn, addr = server.accept()

        conn.send("Enter your name: ".encode())

        name = conn.recv(1024).decode()

        players.append((conn, name))

        scores[name] = 0
        hints_used[name] = 0

        print(name, "connected.")

    print("Both players connected. Game starting!")

    start_time = time.time()

    for puzzle in puzzles:

        for conn, name in players:

            solved = False
            hint_index = 0

            while not solved:

                elapsed = time.time() - start_time

                if elapsed > TIME_LIMIT:

                    conn.send("Time is up! Game over.\n".encode())
                    conn.close()
                    return

                message = puzzle["question"] + "\n(Type 'hint' if needed)"

                conn.send(message.encode())

                answer = conn.recv(1024).decode().lower()

                if answer == "hint":

                    if hints_used[name] < MAX_HINTS:

                        if hint_index < len(puzzle["hints"]):

                            conn.send(
                                ("Hint: " +
                                 puzzle["hints"][hint_index] +
                                 "\n").encode()
                            )

                            hint_index += 1
                            hints_used[name] += 1

                        else:

                            conn.send("No more hints for this puzzle.\n".encode())

                    else:

                        conn.send("You used all hints already.\n".encode())

                elif answer == puzzle["answer"]:

                    conn.send("Correct!\n".encode())

                    scores[name] += puzzle["points"]

                    solved = True

                else:

                    conn.send("Wrong answer. Try again.\n".encode())

    end_time = time.time()

    total_time = end_time - start_time

    for name in scores:

        player_times[name] = total_time

    winner = max(
        scores,
        key=lambda name: (
            scores[name],
            -hints_used[name],
            -player_times[name]
        )
    )

    for conn, name in players:

        result = f"""
Game finished!

Winner: {winner}

Your Score: {scores[name]}
Hints Used: {hints_used[name]}
Time Taken: {round(player_times[name],2)} seconds
"""

        conn.send(result.encode())

        send_email(
            name,
            scores[name],
            hints_used[name],
            player_times[name],
            winner
        )

        conn.close()

    print("Game finished successfully.")


if __name__ == "__main__":

    start_server()
