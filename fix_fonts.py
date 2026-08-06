import glob, re
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix fonts
    content = re.sub(r'\["Plus Jakarta Sans"\]', r'["\'Plus Jakarta Sans\'", "sans-serif"]', content)
    content = re.sub(r'\["Geist"\]', r'["\'Geist\'", "sans-serif"]', content)
    content = re.sub(r'\["Inter"\]', r'["\'Inter\'", "sans-serif"]', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
