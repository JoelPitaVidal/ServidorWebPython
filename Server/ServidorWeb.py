# Importamos las clases necesarias para crear un servidor HTTP
from http.server import HTTPServer, BaseHTTPRequestHandler

# Definimos una clase que manejará las solicitudes HTTP
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Manejo especial para el favicon.ico
        if self.path == "/favicon.ico":
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()
            try:
                with open("favicon.ico", "rb") as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, "Favicon no encontrado")
            return

        # Manejo de la solicitud de styles.css
        if self.path == "/styles.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            try:
                with open("Html/styles.css", "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "Archivo CSS no encontrado")
            return

        # Servir el archivo index.html
        try:
            with open("Html/index.html", "r", encoding="utf-8") as f:
                html_content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404, "Archivo HTML no encontrado")

# Función para iniciar el servidor
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 2000)  # El servidor escucha en todas las interfaces (''), puerto 2000
    httpd = server_class(server_address, handler_class)
    print("Servidor HTTP en ejecución en el puerto 2000...")
    httpd.serve_forever()

# Si el script se ejecuta directamente, iniciamos el servidor
if __name__ == "__main__":
    run()
