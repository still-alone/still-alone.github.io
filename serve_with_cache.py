import http.server
import socketserver
import os

class CachingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "public, max-age=31536000")
        print("Cache-Control header added")  # Добавляем печать для проверки
        super().end_headers()

    def translate_path(self, path):
        # Set the root directory for the server
        root = os.path.join(os.getcwd())
        return os.path.join(root, path.lstrip('/'))

PORT = 8000

Handler = CachingHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
