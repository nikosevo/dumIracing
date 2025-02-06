from http.server import BaseHTTPRequestHandler, HTTPServer

class FakeIRacingAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/get_sim_status?object=simStatus":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'running:1')  # Trick app into thinking iRacing is running
        else:
            self.send_response(404)
            self.end_headers()

# Start the fake server on iRacing's expected port (32034)
def run_server():
    server_address = ('127.0.0.1', 32034)
    httpd = HTTPServer(server_address, FakeIRacingAPI)
    print("Fake iRacing API is running on port 32034...")
    httpd.serve_forever()

run_server()
