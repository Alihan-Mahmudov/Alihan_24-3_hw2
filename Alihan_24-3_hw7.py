ten = list(range(1, 11))

evens = list(filter(lambda x: x % 2 == 0, ten))
evens = list(map(lambda x: x**2, evens))
print(ten)

while True:
    def ind(inde=ten, user=input('введите индекс: ')):
        if user == 'exit':
            print('досвидания!')
            exit()
        try:
            print(inde[int(user)])
        except ValueError:
            print('введите целое число!')
        except IndexError:
            print('введите число от 0 до 9!')
    ind()