rez1 = []
file = open('Young_Gvard.txt')
lens = len(file.readlines())
f = open('Young_Gvard.txt')
for w in range(lens):
    s = f.readline()
    m = s.split(' ')
    rez = []
    banned = [',', '?', '!', '«', '»', ':', '.', '\(', '\)', '…', ';', '\n', '"']
    for i in range(len(m)):
        m[i] = m[i].lower()
        for ban in banned:
            if (ban in m[i]): m[i] = m[i].replace(ban, "")
        if '-' in m[i]:
            rez.append(i)
        if '—' in m[i]:
            rez.append(i)
    rez.reverse()
    for t in rez:
        m.pop(t)
    mass = [x for x in m if len(x) > 3]
    mass = list(set(mass))
    rez1.append(mass)
def f():
    rez2 = []
    for i in rez1:
        for d in i:
            rez2.append(d)
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    cnt = 0
    for w in rez2:
        lol = set(w)
        for d in nums:
            if d in lol:
                rez2[cnt] = 'число'
        cnt += 1
    return [rez2, len(rez2)]
def rll():
    s1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    m1 = []
    for i in range(len(s1)):
        m1.append(s1[i])
    return m1
# print(f())
