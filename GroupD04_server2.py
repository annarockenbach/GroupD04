import socket
import time
import json
from email_results import send_email
from puzzles import puzzles   # IMPORT puzzles here

HOST = "0.0.0.0"
PORT = 12345

TIME_LIMIT = 120

players = []
scores = {}
hints_used = {}


def update_leaderboard(name, score):

    try:
        with open("leaderboard.json", "r") as file:
            data = json.load(file)
    except:
        data = {}

    data[name] = score

    with open("leaderboard.json", "w") as file:
        json.dump(data, file)


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

            while not solved:

                elapsed = time.time() - start_time

                if elapsed > TIME_LIMIT:

                    conn.send("Time is up! Game over.\n".encode())

                    conn.close()

                    return

                message = puzzle["question"] + "\n(Type 'hint' if needed)"

                conn.send(message.encode())

                answer = conn.recv(1024).decode().upper()

                if answer == "HINT":

                    if hints_used[name] < 2:

                        conn.send(("Hint: " + puzzle["hint"] + "\n").encode())

                        hints_used[name] += 1

                    else:

                        conn.send("No hints left!\n".encode())

                elif answer == puzzle["answer"]:

                    conn.send("Correct!\n".encode())

                    scores[name] += 1

                    solved = True

                else:

                    conn.send("Wrong answer. Try again.\n".encode())

    end_time = time.time()

    player_results = {}

    for name in scores:

        player_results[name] = (
            scores[name],
            -hints_used[name],
            -(end_time - start_time)
        )

    winner = max(player_results, key=player_results.get)

    for conn, name in players:

        result = f"Game finished! Winner: {winner}"

        conn.send(result.encode())

        send_email(
            name,
            scores[name],
            hints_used[name],
            end_time - start_time
        )

        update_leaderboard(name, scores[name])

        conn.close()

    print("Game finished successfully.")


if __name__ == "__main__":

    start_server()