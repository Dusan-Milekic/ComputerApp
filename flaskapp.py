import http.server
import socketserver
import webbrowser
import threading

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

# Function to start server
def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
        server_thread = threading.Thread(target=start_server)
        server_thread.start()

# Open web url
def open_browser():
    webbrowser.open(f"http://localhost:{PORT}/static/")

# Create nit for server

def run_all():
    start_server()
    open_browser()




