import re

# Fix personC_modeling.tex
tex_file = 'sections/personC_modeling.tex'
with open(tex_file, 'r') as f:
    content = f.read()

# Replace \cite{Key{} with \cite{Key}
# The generic pattern of the error is \cite{Key{} or similar.
# We want to remove the trailing { inside the citation command
# and also potentially the trailing } if it was captured weirdly.
# Based on the error log: Citation 'Morris2019{}' undefined.
# So the latex code is likely \cite{Morris2019{}
# We want \cite{Morris2019}
new_content = re.sub(r'\\cite\{([^}]+)\{\}', r'\\cite{\1}', content)

with open(tex_file, 'w') as f:
    f.write(new_content)

print(f"Cleaned {tex_file}")

# Fix bibliography.bib
bib_file = 'bibliography.bib'
with open(bib_file, 'r') as f:
    content = f.read()

# Fix keys: @misc{Key{, -> @misc{Key,
content = re.sub(r'@misc\{([^,]+)\{,', r'@misc{\1,', content)

# Fix fields: {TODO: ... Key{}, -> {TODO: ... Key},
content = re.sub(r'\{TODO: ([^}]+)\{\},', r'{TODO: \1},', content)

with open(bib_file, 'w') as f:
    f.write(content)

print(f"Cleaned {bib_file}")
