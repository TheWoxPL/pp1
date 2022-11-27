import re
text="To be, or not to be, that is the question"
found=re.findall("[eyuioa]", text)
print(f"Number of vowels: {len(found)}")