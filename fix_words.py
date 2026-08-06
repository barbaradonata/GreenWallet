import glob, re

replacements = {
    'Sal\ufffdrio': 'Salário',
    'est\ufffdo': 'estão',
    'Voc\ufffd': 'Você',
    'voc\ufffd': 'você',
    'Jap\ufffdo': 'Japão',
    'Alimenta\ufffd\ufffdo': 'Alimentação',
    'm\ufffddia': 'média',
    'M\ufffddia': 'Média',
    '\ufffdcone': 'ícone',
    'j\ufffd': 'já',
    'Saud\ufffdvel': 'Saudável',
    'anal\ufffdticos': 'analíticos',
    'confian\ufffda': 'confiança',
    'N\ufffdvel': 'Nível',
    'di\ufffdrio': 'diário',
    'Di\ufffdria': 'Diária',
    'Fam\ufffdlia': 'Família',
    'emerg\ufffdncia': 'emergência',
    'Bot\ufffdo': 'Botão',
    'transa\ufffd\ufffdes': 'transações',
    'atrav\ufffds': 'através',
    'Pol\ufffdtica': 'Política',
    'Banc\ufffdrio': 'Bancário',
    'Finan\ufffdas': 'Finanças',
    'finan\ufffdas': 'finanças',
    'An\ufffdlise': 'Análise',
    'usu\ufffdrios': 'usuários',
    'n\ufffdvoa': 'névoa',
    'atingir\ufffd': 'atingirá',
    'Seguran\ufffda': 'Segurança',
    'ajudar\ufffd': 'ajudará',
    'movimenta\ufffd\ufffdes': 'movimentações',
    'M\ufffds': 'Mês',
    'm\ufffds': 'mês',
    '\ufffdltimos': 'últimos',
    'Pr\ufffdximos': 'Próximos',
    'op\ufffd\ufffdes': 'opções',
    'continuar\ufffd': 'continuará',
    '\\u00e0': 'à',
    '\\u00e1': 'á',
    '\\u00e2': 'â',
    '\\u00e3': 'ã',
    '\\u00e7': 'ç',
    '\\u00e9': 'é',
    '\\u00ea': 'ê',
    '\\u00ed': 'í',
    '\\u00f3': 'ó',
    '\\u00f4': 'ô',
    '\\u00f5': 'õ',
    '\\u00fa': 'ú',
    '\\u00c0': 'À',
    '\\u00c1': 'Á',
    '\\u00c2': 'Â',
    '\\u00c3': 'Ã',
    '\\u00c7': 'Ç',
    '\\u00c9': 'É',
    '\\u00ca': 'Ê',
    '\\u00cd': 'Í',
    '\\u00d3': 'Ó',
    '\\u00d4': 'Ô',
    '\\u00d5': 'Õ',
    '\\u00da': 'Ú',
    # Fixing CP1252 / ISO-8859-1 mojibake commonly found as Ã
    'Ã£': 'ã',
    'Ã¡': 'á',
    'Ã¢': 'â',
    'Ã©': 'é',
    'Ãª': 'ê',
    'Ã­': 'í',
    'Ã³': 'ó',
    'Ã´': 'ô',
    'Ãµ': 'õ',
    'Ãº': 'ú',
    'Ã§': 'ç',
    'Ã\x83': 'Ã',
    'Ã\x89': 'É',
    'Ã\x8a': 'Ê',
    'Ã\x8d': 'Í',
    'Ã\x93': 'Ó',
    'Ã\x94': 'Ô',
    'Ã\x95': 'Õ',
    'Ã\x9a': 'Ú',
    'Ã\x87': 'Ç'
}

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            text = file.read()
        
        original_text = text
        for wrong, right in replacements.items():
            text = text.replace(wrong, right)
            
        # Clean up any remaining UFFFD if they look like standard text (this is risky, but we mapped the main ones)
        
        if text != original_text:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(text)
            print("Fixed words in", f)
    except Exception as e:
        print("Error in", f, e)
