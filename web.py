from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse, parse_qs


class WebRequestHandler(BaseHTTPRequestHandler):

    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def get_response(self):
        return f"""
        <h1> Hola Web </h1>
        <p> URL Parse Result: {self.url()} </p>
        <p> Path Original: {self.path} </p>
        <p> Headers: {self.headers} </p>
        <p> Query: {self.query_data()} </p>
        """

    def do_GET(self):

        if self.path == "/":
            with open("home.html", "r", encoding="utf-8") as f:
                html = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")


if __name__ == "__main__":
    print("Servidor escuchando en http://localhost:8000")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
