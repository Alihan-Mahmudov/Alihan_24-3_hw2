data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = [i for i in data if len(i) != 4 ]
codes = [i for i in data if len(i) == 4 ]
operator = {}

while len(designations) != 0 and len(codes) != 0:
    q = {
        designations[0]: {codes[0]}
    }
    del designations[0]
    del codes [0]
    operator.update(q)

del operator["Katel"]
del operator["Fonex"]

operator['O!'].add('0700')
operator['O!'].add('0500')
operator['Megacom'].add('0999')
operator['Megacom'].add('0555')
operator['Beeline'].add('0222')
operator['Beeline'].add('0777')

for a, b in operator.items():
    print(f'{a} - {b}')


