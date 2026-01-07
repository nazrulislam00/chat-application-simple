import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5555))
server.listen(1)

print("Server started")

client, addr = server.accept()
print(f"Connected to {addr}")

while True:
    message = client.recv(1024).decode()
    if message.lower() == "exit":
        break
    print("Client:", message)
    reply = input("You: ")
    client.send(reply.encode())

client.close()
server.close()
