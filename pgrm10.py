SEPARATOR = "<SEPARATOR>"

class TCPServer:
    def __init__(self):
        self.files = {
            "sample.txt": "This is a sample text file."
        }
    
    def handle_command(self, command):
        parts = command.split(SEPARATOR)
        action = parts[0]
        if action == "UPLOAD":
            filename = parts[1]
            content = parts[2]

            self.files[filename] = content
            return "file uploaded successfully"

        elif action == "DOWNLOAD":
            filename = parts[1]
            if filename in self.files:
                return self.files[filename]
            else:
                return "file not found"

        


class TCPClient:
    def __init__(self, server):
        self.server = server
    
    def upload(self, filename, content):
        command = f"UPLOAD{SEPARATOR}{filename}{SEPARATOR}{content}"
        return self.server.handle_command(command)
      
    def download(self, filename):
        command = f"DOWNLOAD{SEPARATOR}{filename}"
        response =  self.server.handle_command(command)
        if response == "file not found":
            print("File not found")
        else:
            print(f"Downloaded file: {filename}")
            print(f"Content: {response}")

def main():
    server = TCPServer()
    client = TCPClient(server)
    
    # Test upload
    client.upload("test.txt", "Hello, World!")
    
    # Test download
    client.download("test.txt")
    client.download("nonexistent.txt")

main()