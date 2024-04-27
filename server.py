import http.server
import socketserver

# Request handler class
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the response here
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")  # Example response

def run_server():
    # Define the IP address and port number for your server
    IP = '127.0.0.1'  # Localhost
    PORT = 8000
    # Create the server
    with socketserver.TCPServer((IP, PORT), MyRequestHandler) as server:
        print(f"Server started at {IP}:{PORT}")
        server.serve_forever()