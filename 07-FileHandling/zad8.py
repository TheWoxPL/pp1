file = open("text.txt", "r", encoding="Utf-8")
file_content=file.read()
# for line in file:
#     print(line)
print(file_content)
file.close()