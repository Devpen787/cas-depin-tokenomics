import re

tex_file = 'sections/personC_modeling.tex'

with open(tex_file, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Pattern: \command{NUMBER. Title} or \command{\textbf{NUMBER. Title}}
    # We want to remove the "NUMBER. " part.
    # Regex approach:
    # Look for \section{, \subsection{, \subsubsection{
    # Then optionally \textbf{
    # Then digits and dots
    # Then space
    # Keep the rest.
    
    # Simple regex to strip "X.Y.Z " from start of section titles.
    # Handle optional \textbf{ wrapper inside.
    
    # We will do this carefully.
    
    if line.strip().startswith('\\section') or line.strip().startswith('\\subsection') or line.strip().startswith('\\subsubsection') or line.strip().startswith('\\paragraph'):
        
        # 1. Remove optional \textbf{ at the start of the title content if it exists, and the closing }
        # Often pandoc produces \section{\textbf{Title...}}
        # But we need to match the brace structure.
        
        # Let's just try to remove the specific "Number." pattern.
        # Examples:
        # \section{Methodology...} (Already cleaned some)
        # \subsection{5.1 Purpose...}
        # \subsection{\textbf{6.2 Stress Scenarios...}}
        
        # Regex replacement:
        # Replace: (\\(sub)*section\{)(\\textbf\{)?(\d+(\.\d+)*\.?\s+)(.*)
        # With: \1\2\5
        
        # Explanation:
        # Group 1: command open: \\(section|subsection|subsubsection|paragraph)\{
        # Group 2: Optional \\textbf\{
        # Group 3: The number part: \d+(\.\d+)*\.?\s+  (e.g., "5.1 " or "6.2.3 ")
        # Group 5: The rest of the title
        
        # Note: This is fragile with nested braces, but usually headers are simple.
        
        # We also need to handle cases where the dot is missing or different.
        
        cleaned = re.sub(
            r'(\\(?:sub)*section\{|\\paragraph\{)(\\textbf\{)?(\d+(?:\.\d+)*\.?\s+)',
            r'\1\2',
            line
        )
        
        # Also clean specific "Results" weirdness like "\section{4. Results}" if it exists (though "4." might be matched above)
        
        new_lines.append(cleaned)
    else:
        new_lines.append(line)

with open(tex_file, 'w') as f:
    f.writelines(new_lines)

print("Cleaned manual numbering from section headers.")
