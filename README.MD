# Servidor HTTP en Python

Este proyecto implementa un servidor HTTP simple en Python que sirve una página HTML, una hoja de estilos CSS y un ícono `favicon.ico`.

## 📌 Características
- Servidor HTTP basado en `http.server`.
- Responde a solicitudes para:
  - `index.html` (página principal).
  - `styles.css` (hoja de estilos).
  - `favicon.ico` (ícono del sitio).
- Manejo de errores si los archivos no existen.

## 📁 Estructura del Proyecto
```
/Proyecto
│── server.py          # Código del servidor HTTP
│── /Html
│   ├── index.html     # Página web principal
│   ├── styles.css     # Hoja de estilos
│── /icono
│   ├── favicon.ico    # Ícono del sitio
```

## 🚀 Instalación y Ejecución
### 1️⃣ Clona el repositorio
```sh
 git clone https://github.com/tu-usuario/tu-repositorio.git
 cd tu-repositorio
```

### 2️⃣ Ejecuta el servidor
Asegúrate de tener Python instalado y ejecuta:
```sh
python server.py
```
El servidor se ejecutará en `http://localhost:2000/`.

## 🖥️ Uso
- Abre tu navegador y visita `http://localhost:2000/` para ver la página web.
- El servidor cargará `index.html` con `styles.css` correctamente.

## 📜 Código Principal
El servidor utiliza `http.server` para manejar las solicitudes GET y servir los archivos necesarios.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()
            try:
                with open("../icono/favicon.ico", "rb") as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, "Favicon no encontrado")
            return

        if self.path == "/styles.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            try:
                with open("../Html/styles.css", "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "Archivo CSS no encontrado")
            return

        try:
            with open("../Html/index.html", "r", encoding="utf-8") as f:
                html_content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404, "Archivo HTML no encontrado")

# Iniciar el servidor
def run():
    server_address = ('', 2000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Servidor HTTP en ejecución en el puerto 2000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
```

## 🛠️ Mejoras futuras
- Agregar soporte para otros tipos de archivos como imágenes y scripts JavaScript.
- Implementar rutas dinámicas.

📌 **Desarrollado con Python** 🐍

