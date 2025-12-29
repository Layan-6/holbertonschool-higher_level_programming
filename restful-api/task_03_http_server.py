#!/usr/bin/env python3
"""
3. Develop a simple API using Python with the 'http.server' module
"""

import http.server
import socketserver
import json
from http import HTTPStatus

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for a simple API
    """
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints
        """
        # Set default response headers
        self.send_response(HTTPStatus.OK)
        
        # Route based on the requested path
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        elif self.path == '/info':
            self.handle_info()
        else:
            self.handle_not_found()
    
    def handle_root(self):
        """Handle root endpoint"""
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API")
    
    def handle_data(self):
        """Handle /data endpoint - serve JSON data"""
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def handle_status(self):
        """Handle /status endpoint - API status check"""
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")
    
    def handle_info(self):
        """Handle /info endpoint - API information"""
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(info).encode('utf-8'))
    
    def handle_not_found(self):
        """Handle undefined endpoints"""
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Endpoint not found")
    
    def log_message(self, format, *args):
        """Override to suppress default log messages"""
        # You can customize logging here if needed
        pass

def run_server(port=8000):
    """
    Start the HTTP server
    """
    handler = SimpleAPIHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server started on port {port}")
        print(f"Available endpoints:")
        print(f"  http://localhost:{port}/")
        print(f"  http://localhost:{port}/data")
        print(f"  http://localhost:{port}/status")
        print(f"  http://localhost:{port}/info")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
