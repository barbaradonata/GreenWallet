import glob

def fix_mojibake(text):
    res = ""
    i = 0
    while i < len(text):
        c = text[i]
        if c in ('├', '┬', 'Γ', 'Ã'):  # Common CP850 / CP1252 starters for C3, C2, E2
            # Try 3 chars first, then 2 chars
            for length in (3, 2):
                if i + length <= len(text):
                    chunk = text[i:i+length]
                    try:
                        raw = chunk.encode('cp850')
                        fixed = raw.decode('utf-8')
                        res += fixed
                        i += length
                        break
                    except:
                        pass
            else:
                res += c
                i += 1
        else:
            res += c
            i += 1
    return res

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    fixed_text = fix_mojibake(text)
    
    if fixed_text != text:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(fixed_text)
        print("Fixed mojibake in", f)
