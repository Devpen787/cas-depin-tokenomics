import re

tex_file = 'sections/personC_modeling.tex'

with open(tex_file, 'r') as f:
    content = f.read()

def clean_header_content(text):
    # 1. Strip \texorpdfstring{A}{B} -> A
    # We take the first arg (LaTeX view).
    # Regex: \\texorpdfstring\s*\{(.*?)\}\s*\{.*?\}
    # This is hard with nested braces.
    # But usually pandoc does \texorpdfstring{\textbf{...}}{...}
    # Let's try to just unwrap it if it matches that pattern.
    
    # Simple strategy: removing \textbf{...} is the big win.
    # text = re.sub(r'\\textbf\s*\{(.*?)\}', r'\1', text) 
    # ^ problematic if nested.
    
    # Iterative cleaning of specific artifacts:
    
    # Remove \hfill\break
    text = text.replace(r'\hfill\break', ' ')
    
    # Remove \textbf{ at start of header?
    # Or just remove all \textbf inside headers?
    # User said "some bold some not". Headers should usually NOT have manual \textbf.
    # Let's strip \textbf{...} wrappers.
    # We can do this by simple string replacement if we assume balanced braces aren't super complex in titles.
    # Actually, let's just remove the command string "\textbf{" and the closing "}".
    # Risky if closing brace isn't at end.
    
    # Better: regex for \textbf{...} where ... is non-greedy?
    # re.sub(r'\\textbf\{(.*?)\}', r'\1', text)
    
    return text

lines = content.split('\n')
new_lines = []

for line in lines:
    # Check if it's a section command
    match = re.match(r'^(\s*\\(?:sub)*section\{|\\paragraph\{)(.*)$', line)
    if match:
        prefix = match.group(1)
        rest = match.group(2)
        
        # 'rest' contains the title + closing brace(s) + potential labels.
        # It's hard to parse line-by-line if brace closes on next line (which happens in this file!)
        # File view shows:
        # \section{5.Methodology: Simulation-Based Stress
        # Testing}\label{...}
        # It spans lines!
        pass

# Since headers span lines, we must process the whole string or use a smarter regex.
# Let's go back to processing 'content' as a whole string.

# PATTERN: Section command -> arguments.
# 1. Unify whitespace for easier matching? No, dangerous.

# Regex approach for specific garbage:

# A. Remove \texorpdfstring{...}{...} keeping ... (first arg)
#    Matches: \texorpdfstring { arg1 } { arg2 }
#    We will try to reduce it to arg1.
#    Since we know Pandoc structure is often \texorpdfstring{\textbf{Title}}{Title},
#    let's just attack the specific string "\texorpdfstring".
#    If we remove "\texorpdfstring{" and the mid-part "}{...}", we are left with open braces?
#    No, that's messy.

#    Let's Regex match widely:
#    \\texorpdfstring\s*\{\s*(.*?)\s*\}\s*\{.*?\}
#    This assumes no inner braces. Pandoc usually doesn't nest deeply in headers.
content = re.sub(r'\\texorpdfstring\s*\{\s*(\\textbf\s*\{.*?\})\s*\}\s*\{.*?\}', r'\1', content, flags=re.DOTALL)
# Now we might have just \textbf{Title} left.

# B. Remove \textbf{...}
#    Again, handle simplest case: \textbf{Title}
content = re.sub(r'\\textbf\s*\{\s*(.*?)\s*\}', r'\1', content, flags=re.DOTALL)

# C. Remove \hfill\break
content = re.sub(r'\\hfill\\break', ' ', content)

# D. Remove Section Numbering (Robust)
#    Look for \section{NUMBER[.]TITLE
#    Number can be "5." or "5.1" or "5"
#    Space is optional (e.g. "5.Methodology")
#    We only want to match at the START of the title text.
#    Context: After \section{ or \subsection{
#    Regex: (\\(?:sub)*section\{)\s*(\d+(?:\.\d+)*\.?)\s*(.*)
#    Replace: \1\3

#    We need to run this multiple times or safely.
#    Let's match the command, then the number.
#    Note: 'content' has newlines.
content = re.sub(r'(\\(?:sub)*section\{)\s*(\d+(?:\.\d+)*\.?)\s*', r'\1', content)

# E. Clean upp ".." or spaces
#    (Optional)

with open(tex_file, 'w') as f:
    f.write(content)

print("Cleaned formatting and numbering.")
