data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = [i for i in data_tuple if type(i) == str]
numbers = [i for i in data_tuple if type(i) != str]
letters.append(numbers[1])
del numbers[0]
del numbers[0]
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
numbers =[numbers[0]**2, numbers[1]**2, numbers[2]**2]








print(tuple(letters), tuple(numbers))