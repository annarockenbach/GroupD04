# GAME CONTROLLER
import socket
import threading
import time

from GroupD04_puzzle import puzzles     
from GroupD04_email import send_email

# Define the server address and port
host = '127.0.0.1' 
port = 12345
clients = []
scores = {}
hints_used = {}
finish_time = {}

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print("Waiting for players")

    #threads = []
    #print(f"Server listening on {host}:{port}") idkkkk

    player_threads = []

    for i in range(2):
        connection, address = server_socket.accept()

        player_thread = threading.Thread(
            target=client,
            args=(connection, address, i)
        )
        player_thread.start()
        player_threads.append(player_thread)

        # wait for both players to finish
        for t in player_threads:
            t.join()

    if scores[0] > scores[1]:
        winner = "Player 1"
    elif scores[1] > scores[0]:
        winner = "Player 2"
    else:
        winner = "Tie"

    #maybe just put it in email
    print(f"""Final Results:
    Player 1 Score: {scores[0]} | Time: {finish_times[0]:.2f}s
    Player 2 Score: {scores[1]} | Time: {finish_times[1]:.2f}s
    Winner: {winner}""")  

    ###send_email

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        # Receive data from the client
        message = client_socket.recv(1024).decode()
        print(f"Received from client: {message}")
        # Echo the message back to the client
        client_socket.send(f"Echo: {message}".encode())
        # Close the connection with the client
        client_socket.close()


def client(connection, address, id):
    print(f"Player {id} connected: {address}")

    scores[id] = 0
    hints_used[id] = 0

    start_time = time.time()

    for puzzle in puzzles:
        connection.send(puzzle["question"].encode())

        while True:
            data = connection.recv(1024).decode()

            if data.lower() == "hint":
                if hints_used[id] < 2:
                    connection.send(f"Hint: {puzzle['hint']}".encode())
                    hints_used[id] += 1
                    scores[id] -= 2
                else:
                    connection.send("No hints left!".encode())

            elif data.upper() == puzzle["answer"]:
                connection.send("Correct!".encode())
                scores[id] += 10
                break
            else:
                connection.send("Wrong. Try again.".encode())

if __name__ == "__main__":
    start_server()