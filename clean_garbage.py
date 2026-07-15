import re

files = ['dental-seo-services.html', 'healthcare-seo-services.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find garbage chunks that start with '",a=a.removeChild' and end where the javascript block naturally ended.
    # The javascript block ended before a <script> or </body> or some other tag.
    # But since BS4 parsed it, some parts of it were converted to <f.length...> tags.
    # Actually, we can just find the start of the garbage block: '",a=a.removeChild'
    # And remove everything from there up to the next valid HTML tag that belongs to the head or body.
    # In the head, the garbage text starts right after: <link as="script" fetchpriority="low" href="/_next/static/chunks/7fb057bda326d798.js" rel="preload"/>
    # And it probably ends right before: </head>
    
    start_idx = html.find('",a=a.removeChild')
    if start_idx != -1:
        # Find </head>
        end_idx = html.find('</head>', start_idx)
        if end_idx != -1:
            garbage = html[start_idx:end_idx]
            print(f"Found garbage in {filename}, length: {len(garbage)}")
            # Let's write the garbage to a file to inspect it
            with open(f"{filename}.garbage.txt", "w", encoding="utf-8") as gf:
                gf.write(garbage)
            
            # Replace the garbage with nothing
            html = html[:start_idx] + html[end_idx:]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Cleaned {filename}")
