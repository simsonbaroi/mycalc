#!/usr/bin/env python3
"""
Simple HTTP server to serve the Hospital Billing Calculator
"""
import http.server
import socketserver
import os
import sys

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler"""
    
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS"""
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        """Custom log message format"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    """Main function to start the server"""
    PORT = 5000
    HOST = '0.0.0.0'
    
    try:
        # Change to the directory containing the HTML file
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Create server
        with socketserver.TCPServer((HOST, PORT), HTTPRequestHandler) as httpd:
            print(f"Hospital Billing Calculator Server")
            print(f"Serving at http://{HOST}:{PORT}")
            print(f"Press Ctrl+C to stop the server")
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer stopped by user")
                httpd.shutdown()
                
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Error: Port {PORT} is already in use")
            print("Please stop any other services using this port and try again")
        else:
            print(f"Error starting server: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
