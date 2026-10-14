
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyWebsite(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Docker Website</title>
            <style>
                body {
                    font-family: Arial;
                    text-align: center;
                    background: #eef2ff;
                    padding: 80px 20px;
                }
                .card {
                    background: white;
                    padding: 35px;
                    border-radius: 15px;
                    max-width: 550px;
                    margin: auto;
                    box-shadow: 0 4px 15px #cccccc;
                }
                h1 { color: #4338ca; }
                p { color: #444444; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Hello from Docker!</h1>
                <p>My first webpage is running inside a container.</p>
                <p>DevOps Practical Practice</p>
            </div>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), MyWebsite)
print("Website running on port 8000")
server.serve_forever()
