n = int(input())
turn = []
for i in range(n):
    gogo = input()
    if 'Кто последний?' in gogo:
        go1 = gogo.split('-')
        d = len(go1[1])
        turn.append(go1[1][:d - 1])
    if 'Я только спросить!' in gogo:
        go1 = gogo.split('-')
        d = len(go1[1])
        surname = go1[1][:d - 1]
        turn.insert(0, surname)
    if gogo == 'Следующий!':
        if len(turn) == 0:
            print('В очереди никого нет.')
        else:
            print('Заходит' + turn[0] + '!')
            del turn[0]