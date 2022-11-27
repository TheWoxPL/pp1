import re
text="To be, or not to be, that is the question"
found=re.findall("\w+",text)
print(f"Number of words: {len(found)}")