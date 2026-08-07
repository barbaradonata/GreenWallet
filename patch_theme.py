import os
import re

colors_str = '''            "colors": {
                    "primary": "#8A05BE",
                    "background": "#121214",
                    "on-primary": "#ffffff",
                    "primary-fixed": "#f7d8ff",
                    "surface-container-high": "#2a2a2c",
                    "surface-container-lowest": "#0e0e10",
                    "inverse-surface": "#e5e1e4",
                    "secondary": "#10b981",
                    "secondary-fixed": "#d1fae5",
                    "secondary-fixed-dim": "#10b981",
                    "outline-variant": "#4f4253",
                    "error": "#ffb4ab",
                    "on-secondary-fixed": "#001f24",
                    "inverse-primary": "#941cc7",
                    "surface-container-highest": "#353437",
                    "outline": "#9b8c9e",
                    "surface-variant": "#353437",
                    "on-tertiary-fixed-variant": "#8f0041",
                    "on-secondary": "#003824",
                    "on-error": "#690005",
                    "surface-tint": "#8A05BE",
                    "error-container": "#93000a",
                    "tertiary": "#ffb1c3",
                    "tertiary-container": "#ab0050",
                    "on-primary-container": "#edb9ff",
                    "on-tertiary": "#66002c",
                    "tertiary-fixed": "#ffd9e0",
                    "tertiary-fixed-dim": "#ffb1c3",
                    "surface": "#121214",
                    "surface-container-low": "#1b1b1d",
                    "on-surface-variant": "#d3c1d5",
                    "on-tertiary-container": "#ffb8c8",
                    "on-error-container": "#ffdad6",
                    "primary-fixed-dim": "#eab2ff",
                    "on-secondary-container": "#00616d",
                    "surface-container": "#201f21",
                    "on-primary-fixed": "#320047",
                    "on-tertiary-fixed": "#3f0019",
                    "secondary-container": "#10b981",
                    "surface-bright": "#39393b",
                    "on-background": "#e5e1e4",
                    "on-secondary-fixed-variant": "#004f58",
                    "on-primary-fixed-variant": "#7400a0",
                    "surface-dim": "#121214",
                    "inverse-on-surface": "#303032",
                    "primary-container": "#8A05BE",
                    "on-surface": "#e5e1e4"
            }'''

lines = colors_str.split('\n')
new_colors_lines = [lines[0]]
keys = []
for line in lines[1:-1]:
    if ':' in line:
        key = line.split(':')[0].strip().strip('"')
        keys.append(key)
        new_colors_lines.append(f'                    "{key}": "var(--color-{key})",')
new_colors_lines[-1] = new_colors_lines[-1].rstrip(',')
new_colors_lines.append(lines[-1])
new_colors_str = '\n'.join(new_colors_lines)

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

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Replace colors in tailwind config
        content = re.sub(r'"colors":\s*\{[^}]*?(?:}[^}]*?)*\}', new_colors_str, content, count=1)
        
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
