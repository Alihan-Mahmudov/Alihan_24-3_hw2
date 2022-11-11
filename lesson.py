# file = open('file.txt', 'w', encoding='UTF-8')
# file.write("Бишкек")
# file.close()

with open('new.txt', 'a', encoding='UTF-8')as file:
    file.write('python programming languag')

with open('file.txt', 'r', encoding='UTF-8')as file:
    print(file.read)

























