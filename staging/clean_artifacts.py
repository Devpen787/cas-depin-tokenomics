import re

file_path = 'sections/personC_modeling.tex'
bib_file = 'bibliography.bib'

def clean_tex(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 1. Aggressive citation cleaning
    # Target: \cite{Key...} where ... contains garbage like {}; ]}; etc.
    # We assume valid keys are Alphanumeric+Year (e.g., Morris2019).
    
    # Logic: Find \cite{ followed by some content.
    # We expect the key to always start with a wordchar.
    # regex: \\cite\{([a-zA-Z0-9]+)[^}]*\}
    # This keeps just the alphanumeric part and closes the brace.
    # But we also need to handle trailing garbage OUTSIDE the brace if the previous script messed up brackets.
    
    # Example problem: \cite{Morris2019{}; -> Key is Morris2019, garbage is {}; inside? or outside?
    # If the file has \cite{Morris2019{}; ... it implies the original text was [CITE:Morris2019{};
    
    # Let's clean the KEY first inside the cite.
    # Replace \cite{Key...} with \cite{Key}
    content = re.sub(r'\\cite\{([a-zA-Z0-9]+)[^}]*\}', r'\\cite{\1}', content)
    
    # 2. Cleanup artifacts often left by pandoc around citations
    # e.g. {[} \cite{...} {]}
    # or \cite{...} {};
    
    # Remove standalone {} or [] or {]} or {[}
    content = content.replace('{]}', '')
    content = content.replace('{[}', '')
    content = content.replace('{}{}', '')
    content = content.replace('{}', '') # Empty braces
    
    # 3. Fix potential "Runaway argument" if braces are unbalanced
    # (Hard to fully solve with regex, but cleaning garbage helps)
    
    # 4. Remove duplicate semicolons or punctuation
    content = content.replace(';.', '.')
    content = content.replace('..', '.')
    
    # 5. Fix double numbering in TOC if any escaped (e.g. \section{5. Methodology})
    # (Just a safety fallback)
    content = re.sub(r'\\section\{\d+(\.\d+)*\s+', r'\\section{', content)
    content = re.sub(r'\\subsection\{\d+(\.\d+)*\s+', r'\\subsection{', content)
    
    with open(file_path, 'w') as f:
        f.write(content)
        
    print(f"Cleaned artifacts in {file_path}")

def clean_bib(bib_file):
    # Ensure keys are clean in bib file too (e.g. Morris2019{, -> Morris2019,)
    with open(bib_file, 'r') as f:
        content = f.read()
        
    # Fix @misc{Key{, -> @misc{Key,
    content = re.sub(r'@(\w+)\{([a-zA-Z0-9]+)[^,]*,\s*', r'@\1{\2,\n', content)
    
    # Remove TODO lines if they are messing up
    # (Optional, but let's keep them for now)
    
    with open(bib_file, 'w') as f:
        f.write(content)
    print(f"Cleaned {bib_file}")

clean_tex(file_path)
clean_bib(bib_file)
