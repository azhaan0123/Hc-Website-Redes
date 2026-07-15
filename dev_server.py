import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))

class HealthCompilerDevHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PAGES_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path).path
        clean_path = parsed_path.lstrip('/')
        
        # 1. If requesting root /, serve index.html if it exists, otherwise serve custom Navigation Hub
        if clean_path == '' or clean_path == 'index.html':
            if os.path.exists(os.path.join(PAGES_DIR, 'index.html')):
                self.path = '/index.html'
                return super().do_GET()
            else:
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(self.generate_nav_hub().encode('utf-8'))
                return

        # 2. Check if exact file exists (for CSS, JS, images, etc.)
        exact_path = os.path.join(PAGES_DIR, clean_path)
        if os.path.exists(exact_path) and os.path.isfile(exact_path):
            return super().do_GET()

        # 3. Intelligent HTML Routing: map /path/to/basename -> basename.html
        basename = os.path.basename(clean_path)
        if not basename.endswith('.html'):
            html_candidate = basename + '.html'
        else:
            html_candidate = basename

        # Handle special mappings (e.g. /contact -> demo.html if contact.html doesn't exist)
        if html_candidate == 'contact.html' and not os.path.exists(os.path.join(PAGES_DIR, 'contact.html')):
            html_candidate = 'demo.html'

        candidate_path = os.path.join(PAGES_DIR, html_candidate)
        if os.path.exists(candidate_path) and os.path.isfile(candidate_path):
            self.path = '/' + html_candidate
            return super().do_GET()

        # 4. If still not found, check if clean_path.html exists
        if os.path.exists(exact_path + '.html'):
            self.path = '/' + clean_path + '.html'
            return super().do_GET()

        # 5. Fallback to standard handler (will 404)
        return super().do_GET()

    def generate_nav_hub(self):
        files = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith('.html') and f != 'index.html'])
        
        cards_html = ""
        for f in files:
            name = f.replace('.html', '').replace('-', ' ').title()
            cards_html += f"""
            <a href="/{f}" class="card">
              <div class="card-header">
                <span class="badge">Verified Safe</span>
                <span class="icon">↗</span>
              </div>
              <h3>{name}</h3>
              <p class="filename">{f}</p>
            </a>
            """
            
        return f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="utf-8">
  <title>Health Compiler - Dev Server Hub</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/css/styles.css">
  <style>
    :root {{
      --primary: #e32168;
      --accent: #fb5b87;
    }}
    body {{
      margin: 0;
      padding: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #081E13;
      color: #ffffff;
      min-height: 100vh;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 60px 24px;
    }}
    header {{
      margin-bottom: 60px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      padding-bottom: 40px;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 9999px;
      background: rgba(227, 33, 104, 0.15);
      border: 1px solid rgba(227, 33, 104, 0.4);
      color: #fb5b87;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 20px;
    }}
    h1 {{
      font-size: 48px;
      font-weight: 800;
      margin: 0 0 16px 0;
      letter-spacing: -0.03em;
      line-height: 1.1;
    }}
    h1 span {{
      color: #fb5b87;
    }}
    p.sub {{
      font-size: 20px;
      color: rgba(255,255,255,0.7);
      margin: 0;
      max-width: 600px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
    }}
    .card {{
      display: block;
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 20px;
      padding: 28px;
      text-decoration: none;
      color: inherit;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .card:hover {{
      background: rgba(227, 33, 104, 0.08);
      border-color: rgba(227, 33, 104, 0.5);
      transform: translateY(-4px);
      box-shadow: 0 16px 32px -8px rgba(0,0,0,0.5), 0 0 0 1px rgba(227,33,104,0.2);
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }}
    .badge {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(0, 221, 140, 0.15);
      color: #00DD8C;
      border: 1px solid rgba(0, 221, 140, 0.3);
    }}
    .icon {{
      font-size: 18px;
      color: rgba(255,255,255,0.4);
      transition: transform 0.3s ease, color 0.3s ease;
    }}
    .card:hover .icon {{
      transform: translate(3px, -3px);
      color: #fb5b87;
    }}
    h3 {{
      font-size: 22px;
      font-weight: 700;
      margin: 0 0 8px 0;
      letter-spacing: -0.01em;
    }}
    .filename {{
      font-size: 14px;
      color: rgba(255,255,255,0.5);
      margin: 0;
      font-family: monospace;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="pill">● Dev Server Running</div>
      <h1>Health Compiler <span>Redesign Hub</span></h1>
      <p class="sub">Explore all 23 redesigned pages. Intelligent URL routing maps navigation links directly to static HTML deliverables.</p>
    </header>
    <div class="grid">
      {cards_html}
    </div>
  </div>
</body>
</html>"""

if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    ports = [3000, 8000, 8080, 5000, 3001, 8001]
    for port in ports:
        try:
            server_address = ('', port)
            httpd = HTTPServer(server_address, HealthCompilerDevHandler)
            print(f"==================================================")
            print(f"[+] Health Compiler Dev Server running!")
            print(f"[*] Local URL: http://localhost:{port}")
            print(f"[*] Serving directory: {PAGES_DIR}")
            print(f"==================================================")
            httpd.serve_forever()
            break
        except OSError:
            continue

