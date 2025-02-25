# Importamos las clases necesarias para crear un servidor HTTP
from http.server import HTTPServer, BaseHTTPRequestHandler

# Definimos una clase que manejará las solicitudes HTTP
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Manejo especial para la solicitud del favicon.ico
        if self.path == "/favicon.ico":
            self.send_response(200)  # Respuesta HTTP 200 (OK)
            self.send_header("Content-type", "image/x-icon")  # Tipo de contenido: ícono
            self.end_headers()
            # Abrimos y enviamos el archivo favicon.ico en modo binario
            with open("favicon.ico", "rb") as f:
                self.wfile.write(f.read())
            return  # Salimos de la función para no ejecutar el código siguiente

        # Si la solicitud no es para favicon.ico, respondemos con una página HTML
        self.send_response(200)  # Respuesta HTTP 200 (OK)
        self.send_header("Content-type", "text/html")  # Tipo de contenido: HTML
        self.end_headers()  # Finalizamos los encabezados de la respuesta

        # Contenido HTML que se enviará al cliente
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Python Web</title>
            <link rel="icon" href="/favicon.ico">  <!-- Enlace al favicon -->
        </head>
        <body>
            <h1>Hola buenos días</h1>
            <p>Este es un servidor HTTP básico en Python.</p>
        </body>
        </html>
        """
        # Enviamos la respuesta HTML al cliente
        self.wfile.write(html_content.encode("utf-8"))

# Función para iniciar el servidor
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 2000)  # El servidor escucha en todas las interfaces (''), puerto 2000
    httpd = server_class(server_address, handler_class)  # Creamos el servidor con la dirección y el manejador
    print("Servidor HTTP en ejecución en el puerto 2000...")
    httpd.serve_forever()  # El servidor se ejecuta de manera continua

# Si el script se ejecuta directamente, iniciamos el servidor
if __name__ == "__main__":
    run()
