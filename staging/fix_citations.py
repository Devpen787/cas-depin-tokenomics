import re
import os

tex_file = 'sections/personC_modeling.tex'
bib_file = 'bibliography.bib'

# Read tex file
with open(tex_file, 'r') as f:
    content = f.read()

# Pattern for Pandoc-escaped brackets: {[}{[}CITE:Key{]}{]}
# Also handle potential unescaped [[CITE:Key]] or [CITE:Key]
# We want to capture 'Key'
# Regex explanation:
# \{?\[?\}\?\{?\[?CITE:  -> Matches start sequence like {[}{[}CITE: or [[CITE:
# ([^\]\}]+)             -> Captures the Key (chars that aren't ] or })
# \}?\]?\}?\]?           -> Matches end sequence
pattern = r'(?:\{\[\}\{?\[?|\[\[?)CITE:([^\]\}]+)(?:\}\{?\]?\}?|\]\]?)'

citations_found = set()

def replace_cite(match):
    key = match.group(1).strip()
    citations_found.add(key)
    return f'\\cite{{{key}}}'

new_content = re.sub(pattern, replace_cite, content)

# Write updated tex file
with open(tex_file, 'w') as f:
    f.write(new_content)

print(f"Updated {tex_file}. Found {len(citations_found)} citations.")

# Update bibliography
if not os.path.exists(bib_file):
    existing_bib = ""
else:
    with open(bib_file, 'r') as f:
        existing_bib = f.read()

new_entries = []
for key in sorted(citations_found):
    if key not in existing_bib:
        entry = f"""
@misc{{{key},
  author = {{TODO: Author for {key}}},
  title = {{TODO: Title for {key}}},
  year = {{2025}},
  note = {{Citation extracted from draft}}
}}
"""
        new_entries.append(entry)

if new_entries:
    with open(bib_file, 'a') as f:
        f.write("".join(new_entries))
    print(f"Added {len(new_entries)} placeholder entries to {bib_file}.")
else:
    print("No new bib entries needed.")
