import re

files = ['dental-seo-services.html', 'healthcare-seo-services.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix vertical-align issue
    # Original: img,svg,video,canvas,audio,iframe,embed,object{vertical-align:middle;display:block}
    html = html.replace('img,svg,video,canvas,audio,iframe,embed,object{vertical-align:middle;display:block}', 'img,svg,video,canvas,audio,iframe,embed,object{display:block}')
    
    # Fix line-clamp issue
    # Original: -webkit-line-clamp:1;
    # Replacement: -webkit-line-clamp:1;line-clamp:1;
    html = re.sub(r'-webkit-line-clamp:(\d+);', r'-webkit-line-clamp:\1;line-clamp:\1;', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Fixed CSS warnings in {filename}")
