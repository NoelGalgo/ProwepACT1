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
        parsed = urlparse(self.path)
        ruta = parsed.path
        query = parse_qs(parsed.query)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))


if __name__ == "__main__":
    print("Servidor escuchando en http://localhost:8000")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
