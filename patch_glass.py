import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False

    if 'background: rgba(255, 255, 255, 0.03);' in content:
        content = content.replace('background: rgba(255, 255, 255, 0.03);', 'background: var(--glass-fill, rgba(255, 255, 255, 0.03));')
        changed = True
    
    if 'border: 1px solid rgba(255, 255, 255, 0.08);' in content:
        content = content.replace('border: 1px solid rgba(255, 255, 255, 0.08);', 'border: 1px solid var(--glass-border, rgba(255, 255, 255, 0.08));')
        changed = True

    if 'border: 1px solid rgba(211, 193, 213, 0.1);' in content:
        content = content.replace('border: 1px solid rgba(211, 193, 213, 0.1);', 'border: 1px solid var(--glass-border, rgba(255, 255, 255, 0.08));')
        changed = True
    
    if ':root {' in content and '--glass-fill' not in content:
        content = content.replace(':root {', ':root {\n  --glass-fill: rgba(0, 0, 0, 0.05);\n  --glass-border: rgba(0, 0, 0, 0.1);')
        changed = True
    
    if '.dark {' in content and '--glass-fill' not in content:
        content = content.replace('.dark {', '.dark {\n  --glass-fill: rgba(255, 255, 255, 0.03);\n  --glass-border: rgba(255, 255, 255, 0.08);')
        changed = True
        
    # Also fix pesquisa.html which already has it hardcoded to white in :root
    if '--glass-fill: rgba(255, 255, 255, 0.03);' in content and filepath == 'pesquisa.html':
        content = content.replace('--glass-fill: rgba(255, 255, 255, 0.03);', '--glass-fill: rgba(0, 0, 0, 0.05);', 1)
        content = content.replace('--glass-border: rgba(255, 255, 255, 0.08);', '--glass-border: rgba(0, 0, 0, 0.1);', 1)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated glass-card in {filepath}")
