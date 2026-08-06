import glob
import re

html_entities = {
    'á': '&aacute;',
    'à': '&agrave;',
    'â': '&acirc;',
    'ã': '&atilde;',
    'é': '&eacute;',
    'ê': '&ecirc;',
    'í': '&iacute;',
    'ó': '&oacute;',
    'ô': '&ocirc;',
    'õ': '&otilde;',
    'ú': '&uacute;',
    'ç': '&ccedil;',
    'Á': '&Aacute;',
    'À': '&Agrave;',
    'Â': '&Acirc;',
    'Ã': '&Atilde;',
    'É': '&Eacute;',
    'Ê': '&Ecirc;',
    'Í': '&Iacute;',
    'Ó': '&Oacute;',
    'Ô': '&Ocirc;',
    'Õ': '&Otilde;',
    'Ú': '&Uacute;',
    'Ç': '&Ccedil;'
}

def escape_html(text):
    # We must only replace in text content, not inside <script> tags or html attributes if possible.
    # Actually, HTML entities work fine inside HTML attributes (like title="Voc&ecirc;").
    # For <script> tags, it might break if used inside JS strings.
    # We will split by <script> tags to avoid touching JS code.
    
    parts = re.split(r'(?i)(<script.*?>.*?</script>)', text, flags=re.DOTALL)
    for i in range(0, len(parts), 2): # Even indices are HTML, odd are Scripts
        for char, entity in html_entities.items():
            parts[i] = parts[i].replace(char, entity)
            
    return "".join(parts)

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            text = file.read()
            
        new_text = escape_html(text)
        
        if text != new_text:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_text)
            print("Escaped HTML entities in", f)
    except Exception as e:
        print("Error in", f, e)
