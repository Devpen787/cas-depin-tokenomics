import re

def clean_tex(content):
    lines = content.split('\n')
    start_index = 0
    found_start = False
    
    # Robust start finding: Look for the Methodology section
    for i, line in enumerate(lines):
        if 'Methodology: Simulation-Based Stress' in line:
            start_index = i
            found_start = True
            break
            
    if not found_start:
        print("Warning: Could not find 'Methodology: Simulation-Based Stress'. Starting from beginning.")
        start_index = 0
    else:
        print(f"Found start at line {start_index}")

    # Drop everything before the start index (this removes any preceding TOC)
    lines = lines[start_index:]
    
    cleaned_lines = []
    for line in lines:
        # Robust regex to strip "X.Y.Z " from start of section titles.
        # Handles optional \textbf{ wrapper inside.
        
        if line.strip().startswith('\\section') or line.strip().startswith('\\subsection') or line.strip().startswith('\\subsubsection') or line.strip().startswith('\\paragraph'):
            # Regex replacement:
            # Replace: (\\(sub)*section\{)(\\textbf\{)?(\d+(\.\d+)*\.?\s+)(.*)
            # With: \1\2\5
            
            # This handles:
            # \section{5.Methodology...} -> \section{Methodology...}
            # \subsection{\textbf{6.2 Stress...}} -> \subsection{\textbf{Stress...}}
            
            cleaned = re.sub(
                r'(\\(?:sub)*section\{|\\paragraph\{)(\\textbf\{)?(\d+(?:\.\d+)*\.?\s+)',
                r'\1\2',
                line
            )
            cleaned_lines.append(cleaned)
        else:
            cleaned_lines.append(line)
        
    return '\n'.join(cleaned_lines)

# Read raw file
with open('staging/personC_modeling_raw.tex', 'r') as f:
    raw_content = f.read()

# Clean content
cleaned_content = clean_tex(raw_content)

# Read header from current target to preserve comments/license
# We only want the top comments, not the whole file content
with open('sections/personC_modeling.tex', 'r') as f:
    current_lines = f.readlines()

header = []
for line in current_lines:
    if line.strip().startswith('%') or line.strip() == '':
        header.append(line)
    else:
        # Stop at the first non-comment non-empty line
        break

# Combine
final_content = ''.join(header) + '\n' + cleaned_content

# Write back
with open('sections/personC_modeling.tex', 'w') as f:
    f.write(final_content)

print("Import complete.")
