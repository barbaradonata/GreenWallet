import glob
import re

def replacer(match):
    classes = match.group(1).split()
    if 'bg-background' not in classes:
        classes.insert(0, 'bg-background')
    if 'text-on-surface' not in classes and 'text-on-background' not in classes:
        classes.insert(1, 'text-on-surface')
    return '<body class="' + ' '.join(classes) + '">'

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'<body class="(.*?)">', replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
