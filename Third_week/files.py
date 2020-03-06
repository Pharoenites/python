with open('text.txt', 'w', encoding='utf-8') as f:
    f.write("Привет, мир!")

with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.upper()
        print(line)