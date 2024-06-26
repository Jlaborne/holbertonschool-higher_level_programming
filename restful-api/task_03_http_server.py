#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""
import http.server
import json

PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Represent a class"""
    def do_GET(self):
        if self.path == '/':
            # Handle the root endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # Handle the /data endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            # Handle the /status endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            # Handle the /info endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())
        else:
            # Handle undefined endpoints
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

httpd = http.server.HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)
print(f"Serving at port {PORT}")
httpd.serve_forever()
