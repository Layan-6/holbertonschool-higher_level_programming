#!/usr/bin/env python3
"""
3. Simple API with http.server
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = 8000

class APIHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self, content_type='text/plain', status=200):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
    
    def do_GET(self):
        path = self.path
        
        if path == '/':
            self._set_headers('text/plain', 200)
            response = "Hello, this is a simple API"
            self.wfile.write(response.encode('utf-8'))
        
        elif path == '/data':
            self._set_headers('application/json', 200)
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        
        elif path == '/status':
            self._set_headers('text/plain', 200)
            self.wfile.write(b"OK")
        
        elif path == '/info':
            self._set_headers('application/json', 200)
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))
        
        else:
            self._set_headers('text/plain', 404)
            self.wfile.write(b"Endpoint not found")
    
    def log_message(self, format, *args):
        pass

def main():
    server = HTTPServer(('', PORT), APIHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()

if __name__ == '__main__':
    main()
