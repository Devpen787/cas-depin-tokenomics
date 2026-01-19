import re

tex_file = 'sections/personC_modeling.tex'

with open(tex_file, 'r') as f:
    content = f.read()

# 1. Manually fix the specific broken "Implications for Builders" block
# The pattern found in grep:
# \subsection{\texorpdfstring{Implications\\ ... Recommendations)}{...}}
# We match loosely to capture the whole \subsection ending in the label or just the }}
regex_implications = r'\\subsection\{\\texorpdfstring\{Implications\\\\.*?Recommendations\)\}\{(.*?)\}\}'
# Actually, let's just match the specific messy string if we can. 
# But regex is better.
# We want to replace it with: \subsection{Implications for Builders (Design Recommendations)}

# Look for: \subsection{\texorpdfstring{Implications\\ <stuff> }{ <stuff> }}
content = re.sub(
    r'\\subsection\{\\texorpdfstring\{Implications\\\\\s*Implications for Builders \(Design\s*Recommendations\)\}\{.*?\}\}',
    r'\\subsection{Implications for Builders (Design Recommendations)}',
    content,
    flags=re.DOTALL
)

# 2. General cleanup (similar to v3 but careful)

# Remove \texorpdfstring{A}{B} keeping A.
# We assume A and B match simple braces or we use non-greedy matching.
# We iterate until no changes to catch nested stuff?
# Or just simple regex for non-nested case.
# \texorpdfstring{...}{...}
# Pattern: \\texorpdfstring\s*\{(.*?)\}\s*\{.*?\}
# This fails if { contains }.
# Let's rely on the fact that we fixed the complex one manually. Rest should be simple.
content = re.sub(r'\\texorpdfstring\s*\{(.*?)\}\s*\{.*?\}', r'\1', content, flags=re.DOTALL)

# Remove \textbf{...}
content = re.sub(r'\\textbf\s*\{(.*?)\}', r'\1', content, flags=re.DOTALL)

# Remove \hfill\break
content = re.sub(r'\\hfill\\break', ' ', content)

# Remove numbering at start of titles
# \section{5. Title}
content = re.sub(r'(\\(?:sub)*section\{)\s*(\d+(?:\.\d+)*\.?)\s*', r'\1', content)

# Remove any residual double spaces
content = content.replace('  ', ' ')

with open(tex_file, 'w') as f:
    f.write(content)

print("Cleaned messy headers in personC_modeling.tex")
