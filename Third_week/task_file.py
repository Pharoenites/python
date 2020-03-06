with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()

print(len(content))

content_col = content.split()
print(len(content_col))

content_v = content.replace('.', '!')
#print(content_v)

with open('referat2.txt', 'w', encoding='utf-8') as f:
    f.write(content_v)
