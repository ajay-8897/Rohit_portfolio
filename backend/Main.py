import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIR = ROOT / "frontend"


PROFILE = {
    "name": "Rohit Kumar",
    "title": "AML/KYC Analyst",
    "experience_years": "4+",
    "location": "Ambala Cantt., Haryana",
    "email": "rohitkumartiwari7056@gmail.com",
    "phone": "+91 870 816 1164",
    "linkedin": "https://www.linkedin.com/in/rohit-kumar-048721384/",
}


class PortfolioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIR), **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/api/profile":
            body = json.dumps(PROFILE).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return

        super().do_GET()

    def log_message(self, format_string, *args):
        print("%s - %s" % (self.address_string(), format_string % args))


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 4173), PortfolioHandler)
    print("Portfolio running at http://127.0.0.1:4173")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()