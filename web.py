from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse, parse_qs


class WebRequestHandler(BaseHTTPRequestHandler):

    contenido = {
        "/": """
        <html>
            <h1>Inicio</h1>
            <a href="/proyecto/1">Proyecto 1</a><br>
            <a href="/proyecto/2">Proyecto 2</a><br>
            <a href="/proyecto/3">Proyecto 3</a>
        </html>
        """,

        "/proyecto/1": "<html><h1>Proyecto 1</h1></html>",
        "/proyecto/2": "<html><h1>Proyecto 2</h1></html>",
        "/proyecto/3": "<html><h1>Proyecto 3</h1></html>",
    }

    def do_GET(self):

        ruta = self.path

        if ruta in self.contenido:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.contenido[ruta].encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")


if __name__ == "__main__":
    print("Servidor escuchando en http://localhost:8000")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()

