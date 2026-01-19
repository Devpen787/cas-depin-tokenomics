import re

tex_file = 'sections/personC_modeling.tex'

with open(tex_file, 'r') as f:
    content = f.read()

# Helper regex components
# Number pattern: digits, dots, digits... optional dot, whitespace
number_pattern = r'\s*\d+(?:\.\d+)*\.?\s+'

# 1. Handle \texorpdfstring{\textbf{NUMBER...
# (Already had this, keeping it)
content = re.sub(
    r'(\\texorpdfstring\s*\{\s*\\textbf\s*\{)(' + number_pattern + ')',
    r'\1',
    content
)

# 2. NEW: Handle \texorpdfstring{NUMBER... (No bold at start)
# e.g. \texorpdfstring{7. Implications...
content = re.sub(
    r'(\\texorpdfstring\s*\{)(' + number_pattern + ')',
    r'\1',
    content
)

# 3. NEW: Handle numbers inside internal \textbf, especially with \hfill\break
# e.g. \textbf{\hfill\break 7.1 Implications...
# We match \textbf followed by optional garbage key chars, then a number.
# Be careful not to match math or other things.
# Limiting to \hfill\break context or just start of bold content.
content = re.sub(
    r'(\\textbf\s*\{\s*(?:\\hfill\\break\s*)?)(' + number_pattern + ')',
    r'\1',
    content
)

# 4. Handle second argument of \texorpdfstring
# }\{NUMBER...
content = re.sub(
    r'(\}\s*\{)(' + number_pattern + ')',
    r'\1',
    content
)

# 5. Standard fallback for keys section headers without texorpdfstring
content = re.sub(
    r'(\\(?:sub)*section\{|\\paragraph\{)(\\textbf\{)?(' + number_pattern + ')',
    r'\1\2',
    content
)

with open(tex_file, 'w') as f:
    f.write(content)

print(f"Cleaned numbering from {tex_file}")
