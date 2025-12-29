#!/usr/bin/env python3
"""
3. Develop a simple API using Python with the 'http.server' module
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Handle GET requests"""
        
        # Root endpoint
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # يجب أن يكون النص مطابقاً تماماً
            self.wfile.write(b"Hello, this is a simple API")
            
        # Data endpoint
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        # Status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            
        # Info endpoint
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))
            
        # Any other endpoint - must return 404
        else:
            self.send_response(404)  # <-- هذا مهم جداً
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
