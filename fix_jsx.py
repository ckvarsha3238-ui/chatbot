import os

def fix_jsx(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply fixes
    
    # 1. Fix Insights tab placeholder structure (actually I found it was balanced, but let's double check)
    # Wait, I found Market Analysis was the one with the error.
    
    # 2. Fix Market Analysis tab unclosed div for lg:col-span-3
    # Target: line 915 area
    target_market = '                    </div>\n\n                    <div className="lg:col-span-1 space-y-6">'
    fix_market = '                    </div>\n                  </div>\n\n                  <div className="lg:col-span-1 space-y-6">'
    
    # Actually, let's use a more robust regex replacement for the market analysis section
    # Find the lg:col-span-3 div and its content up to the side column
    import re
    
    # Let's just fix the specific lines I know are wrong.
    
    # Fix 1: The Match Score div I added previously should be closed correctly. (Already is)
    
    # Fix 2: The side column nesting in Market Analysis
    # Let's search for the specific pattern around line 915
    market_pattern = r'(<p className="mt-8 text-xs text-\[#8B949E\]">Historical recruitment volume and market demand trajectory for <strong className="text-white">\{selectedDomain\}</strong> based on database analytics\.</p>\s+</div>)(\s+<div className="lg:col-span-1 space-y-6">)'
    if re.search(market_pattern, content):
        print("Found market pattern, applying fix...")
        content = re.sub(market_pattern, r'\1\n                  </div>\n\2', content)
    else:
        print("Market pattern not found via regex, trying literal...")
        # Fallback to literal if regex fails
        literal_target = '                    <p className="mt-8 text-xs text-[#8B949E]">Historical recruitment volume and market demand trajectory for <strong className="text-white">{selectedDomain}</strong> based on database analytics.</p>\n                  </div>\n\n                  <div className="lg:col-span-1 space-y-6">'
        literal_fix = '                    <p className="mt-8 text-xs text-[#8B949E]">Historical recruitment volume and market demand trajectory for <strong className="text-white">{selectedDomain}</strong> based on database analytics.</p>\n                  </div>\n                </div>\n\n                <div className="lg:col-span-1 space-y-6">'
        if literal_target in content:
             content = content.replace(literal_target, literal_fix)
             print("Applied literal fix for Market Analysis.")
        else:
             print("Literal target not found for Market Analysis.")

    # Fix 3: Remove trailing spaces in major tags
    content = content.replace('</main >', '</main>')
    content = content.replace('</div >', '</div>')
    content = content.replace('</header >', '</header>')

    # Final check of div balance
    open_divs = content.count('<div')
    close_divs = content.count('</div')
    self_closings = len(re.findall(r'<div[^>]*/>', content))
    actual_opens = open_divs - self_closings
    print(f"New Balance: {actual_opens} opens, {close_divs} closes. Diff: {actual_opens - close_divs}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_jsx(r'c:\Users\N.VARSHA\OneDrive\Desktop\AI_career\frontend\src\app\page.tsx')
