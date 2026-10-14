
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyWebsite(BaseHTTPRequestHandler):
    def do_GET(self):
        name = os.getenv("NAME", "Student")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = f"<h1>Hello {name}!</h1><p>My Docker Website</p>"
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 8000), MyWebsite)
server.serve_forever()


