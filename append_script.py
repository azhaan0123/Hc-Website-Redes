import re

files = ['dental-seo-services.html', 'healthcare-seo-services.html']
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove old inline accordion script if present
    html = re.sub(r'<script>.*?querySelectorAll\(\'.faq-item.*?<\/script>', '', html, flags=re.DOTALL)
    
    # Remove existing custom_interactivity.js if present
    html = re.sub(r'<script src="custom_interactivity.js"><\/script>', '', html)
    
    # Append the script just before </body>
    if '</body>' in html:
        html = html.replace('</body>', '<script src="custom_interactivity.js"></script></body>')
    else:
        # If no body tag, append to end
        html += '\n<script src="custom_interactivity.js"></script>'
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename}")
