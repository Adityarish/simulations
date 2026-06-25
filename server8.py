import socket

HOST = "127.0.0.1"
PORT = 8080

def handle_request(request):
    request_lines = request.splitlines()
    if request_lines:
        request_line = request_lines[0]
        method, path = request_line.split()[:2]
        if method == "GET" and path =="/hello":
            body="Hello World!"
            response = (
                "HTTP/1.0 200 OK\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
        else:
            body = "404 NOT found"
            response = (
                "HTTP/1.0 404 Not Found\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
        return response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        print("Received request:\n", data)
        response = handle_request(data)
        conn.sendall(response.encode())

