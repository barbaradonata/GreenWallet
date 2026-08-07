import os

css_vars = '''
<style id="theme-vars">
:root {
  --color-primary: #8A05BE;
  --color-background: #f8fafc;
  --color-on-primary: #ffffff;
  --color-primary-fixed: #f7d8ff;
  --color-surface-container-high: #e2e8f0;
  --color-surface-container-lowest: #ffffff;
  --color-inverse-surface: #1e293b;
  --color-secondary: #10b981;
  --color-secondary-fixed: #d1fae5;
  --color-secondary-fixed-dim: #10b981;
  --color-outline-variant: #cbd5e1;
  --color-error: #ef4444;
  --color-on-secondary-fixed: #001f24;
  --color-inverse-primary: #941cc7;
  --color-surface-container-highest: #cbd5e1;
  --color-outline: #94a3b8;
  --color-surface-variant: #f1f5f9;
  --color-on-tertiary-fixed-variant: #8f0041;
  --color-on-secondary: #ffffff;
  --color-on-error: #ffffff;
  --color-surface-tint: #8A05BE;
  --color-error-container: #fee2e2;
  --color-tertiary: #f43f5e;
  --color-tertiary-container: #ffe4e6;
  --color-on-primary-container: #4c1d95;
  --color-on-tertiary: #ffffff;
  --color-tertiary-fixed: #ffd9e0;
  --color-tertiary-fixed-dim: #ffb1c3;
  --color-surface: #ffffff;
  --color-surface-container-low: #f8fafc;
  --color-on-surface-variant: #475569;
  --color-on-tertiary-container: #881337;
  --color-on-error-container: #7f1d1d;
  --color-primary-fixed-dim: #eab2ff;
  --color-on-secondary-container: #064e3b;
  --color-surface-container: #f1f5f9;
  --color-on-primary-fixed: #320047;
  --color-on-tertiary-fixed: #3f0019;
  --color-secondary-container: #d1fae5;
  --color-surface-bright: #ffffff;
  --color-on-background: #0f172a;
  --color-on-secondary-fixed-variant: #004f58;
  --color-on-primary-fixed-variant: #7400a0;
  --color-surface-dim: #e2e8f0;
  --color-inverse-on-surface: #f8fafc;
  --color-primary-container: #d8b4e2;
  --color-on-surface: #0f172a;
}
.dark {
  --color-primary: #8A05BE;
  --color-background: #121214;
  --color-on-primary: #ffffff;
  --color-primary-fixed: #f7d8ff;
  --color-surface-container-high: #2a2a2c;
  --color-surface-container-lowest: #0e0e10;
  --color-inverse-surface: #e5e1e4;
  --color-secondary: #10b981;
  --color-secondary-fixed: #d1fae5;
  --color-secondary-fixed-dim: #10b981;
  --color-outline-variant: #4f4253;
  --color-error: #ffb4ab;
  --color-on-secondary-fixed: #001f24;
  --color-inverse-primary: #941cc7;
  --color-surface-container-highest: #353437;
  --color-outline: #9b8c9e;
  --color-surface-variant: #353437;
  --color-on-tertiary-fixed-variant: #8f0041;
  --color-on-secondary: #003824;
  --color-on-error: #690005;
  --color-surface-tint: #8A05BE;
  --color-error-container: #93000a;
  --color-tertiary: #ffb1c3;
  --color-tertiary-container: #ab0050;
  --color-on-primary-container: #edb9ff;
  --color-on-tertiary: #66002c;
  --color-tertiary-fixed: #ffd9e0;
  --color-tertiary-fixed-dim: #ffb1c3;
  --color-surface: #121214;
  --color-surface-container-low: #1b1b1d;
  --color-on-surface-variant: #d3c1d5;
  --color-on-tertiary-container: #ffb8c8;
  --color-on-error-container: #ffdad6;
  --color-primary-fixed-dim: #eab2ff;
  --color-on-secondary-container: #00616d;
  --color-surface-container: #201f21;
  --color-on-primary-fixed: #320047;
  --color-on-tertiary-fixed: #3f0019;
  --color-secondary-container: #10b981;
  --color-surface-bright: #39393b;
  --color-on-background: #e5e1e4;
  --color-on-secondary-fixed-variant: #004f58;
  --color-on-primary-fixed-variant: #7400a0;
  --color-surface-dim: #121214;
  --color-inverse-on-surface: #303032;
  --color-primary-container: #8A05BE;
  --color-on-surface: #e5e1e4;
}
</style>
'''

toggle_script = '''
<!-- Theme Toggle Script -->
<script>
function toggleTheme() {
    const html = document.documentElement;
    if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    } else {
        html.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }
}
// Init theme
if (localStorage.getItem('theme') === 'light') {
    document.documentElement.classList.remove('dark');
} else if (localStorage.getItem('theme') === 'dark') {
    document.documentElement.classList.add('dark');
}
</script>
'''

toggle_button = '''<button onclick="toggleTheme()" class="p-xs rounded-full hover:bg-surface-variant/30 text-on-surface-variant transition-colors flex items-center justify-center w-8 h-8 md:w-10 md:h-10 border border-outline-variant/30 ml-2" title="Alternar Tema">
    <span class="material-symbols-outlined dark:hidden" style="font-size: 20px;">light_mode</span>
    <span class="material-symbols-outlined hidden dark:block" style="font-size: 20px;">dark_mode</span>
</button>'''

import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        inside_colors = False
        colors_brace_count = 0
        
        for line in lines:
            if not inside_colors and '"colors": {' in line:
                inside_colors = True
                colors_brace_count = 1
                new_lines.append(line)
                # Write variables instead
                var_names = ["primary", "background", "on-primary", "primary-fixed", "surface-container-high", "surface-container-lowest", "inverse-surface", "secondary", "secondary-fixed", "secondary-fixed-dim", "outline-variant", "error", "on-secondary-fixed", "inverse-primary", "surface-container-highest", "outline", "surface-variant", "on-tertiary-fixed-variant", "on-secondary", "on-error", "surface-tint", "error-container", "tertiary", "tertiary-container", "on-primary-container", "on-tertiary", "tertiary-fixed", "tertiary-fixed-dim", "surface", "surface-container-low", "on-surface-variant", "on-tertiary-container", "on-error-container", "primary-fixed-dim", "on-secondary-container", "surface-container", "on-primary-fixed", "on-tertiary-fixed", "secondary-container", "surface-bright", "on-background", "on-secondary-fixed-variant", "on-primary-fixed-variant", "surface-dim", "inverse-on-surface", "primary-container", "on-surface"]
                for i, v in enumerate(var_names):
                    comma = "," if i < len(var_names) - 1 else ""
                    new_lines.append(f'                    "{v}": "var(--color-{v})"{comma}\n')
                continue
                
            if inside_colors:
                colors_brace_count += line.count('{')
                colors_brace_count -= line.count('}')
                if colors_brace_count == 0:
                    inside_colors = False
                    new_lines.append(line[line.find('}'):])
                continue
            
            new_lines.append(line)
            
        content = "".join(new_lines)
        
        # 2. Add CSS vars
        if 'id="theme-vars"' not in content:
            content = content.replace('</head>', f'{css_vars}</head>')
            
        # 3. Add toggle script
        if 'toggleTheme()' not in content:
            content = content.replace('</body>', f'{toggle_script}</body>')
            
        # 4. Add toggle button
        if 'id="theme-vars"' in content:
            if filename == 'index.html':
                content = re.sub(r'(<div class="absolute top-full right-0 mt-2 w-24.*?</button>\n</div>\n</div>)', r'\1\n' + toggle_button, content, flags=re.DOTALL)
            else:
                content = re.sub(r'(<button class="p-xs rounded-full hover:bg-surface-variant/30 text-on-surface-variant transition-colors">\s*<span class="material-symbols-outlined">notifications</span>\s*</button>)', r'\1\n' + toggle_button, content)
                
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Successfully patched {filename}')
