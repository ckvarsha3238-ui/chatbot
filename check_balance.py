import re

def check_balance(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    balance = 0
    
    # We want to find <div but NOT <div ... />
    # And we want to find </div>
    
    for i, line in enumerate(lines):
        # Find all <div tags
        openings = re.findall(r'<div', line)
        # Find all self-closing <div ... />
        self_closings = re.findall(r'<div[^>]*/>', line)
        # Find all </div>
        closings = re.findall(r'</div', line)
        
        diff = len(openings) - len(self_closings) - len(closings)
        balance += diff
        
        if diff != 0:
            print(f"L{i+1}: balance={balance} (diff={diff}, o={len(openings)}, sc={len(self_closings)}, c={len(closings)})")
            print(f"   Content: {line.strip()}")

    print(f"\nFinal Balance: {balance}")

if __name__ == '__main__':
    check_balance(r'c:\Users\N.VARSHA\OneDrive\Desktop\AI_career\frontend\src\app\page.tsx')
