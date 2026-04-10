import socket

HOST = input("Enter server IP address: ")
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    try:
        message = client.recv(1024).decode()

        if not message:
            break

        print(message)

        # only send input when needed
        if "Enter your name:" in message:
            client.send(input().encode())

        elif "Enter your email:" in message:
            client.send(input().encode())

        elif "(Type 'hint')" in message or "Wrong answer" in message or "Hint:" in message:
            answer = input("Your answer: ")
            client.send(answer.encode())

        elif "finished" in message.lower() or "game over" in message.lower():
            break

    except:
        break

client.close()
