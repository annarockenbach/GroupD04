import socket

HOST = input("Enter server IP address: ")

PORT = 12345

def start_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    name_request = client.recv(1024).decode()

    name = input(name_request)

    client.send(name.encode())

    while True:

        message = client.recv(1024).decode()

        print(message)

        if "Game finished" in message:

            break

        if "Time is up" in message:

            break

        answer = input("Answer: ")

        client.send(answer.encode())

    client.close()


if __name__ == "__main__":

    start_client()