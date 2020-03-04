def sort_key(i):
    r = list(map(int, i[1].split('-')))
    r.append(Borrowers[i[0][0]])
    r.append(i[0][1])
    return tuple(r)

current = 'Books'
Books = dict()
Borrowers = dict()
Checkouts = dict()

while True:
    line = input()

    if line == 'Books':
        current = line
        continue
    elif line == 'Borrowers':
        current = line
        continue
    elif line == 'Checkouts':
        current = line
        continue
    elif line == 'EndOfInput':
        break
    elif current == 'Books':
        bid, bname = line.split('~')
        Books[bid] = bname
    elif current == 'Borrowers':
        uid, name = line.split('~')
        Borrowers[uid] = name
    elif current == 'Checkouts':
        usr,acc_no,due_date = line.split('~')
        Checkouts[(usr,acc_no)] = due_date

output = sorted(Checkouts.items(), key = sort_key)

for i in output:
    line = i[1] + '~' + Borrowers[i[0][0]] + '~' + i[0][1] + Books[i[0][1]]
    print(line)