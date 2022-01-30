def lenth(a, b):
    len = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return len


addresses = {
    (0, 2): 'Почтовое отделение',
    (2, 5): 'Ул. Грибоедова, 104/25',
    (5, 2): 'Ул. Бейкер стрит, 221б',
    (6, 6): 'Ул. Большая Садовая, 302-бис',
    (8, 3): 'Вечнозелёная Аллея, 742'
}
points = []
post = tuple()
for point, addres in addresses.items():
    if addres == 'Почтовое отделение':
        post = point
    else:
        points.append(point)
len_rout = 0
route = [post]
l = 0

print(route[0],'->', end=' ')
while len(points) > 0:
    for index, i_point in enumerate(points):
        if index == 0:
            l = lenth(i_point, route[-1])
            route.append(i_point)
            if len(points) == 1:
                l += lenth(post, route[-1])
        elif l > lenth(i_point, route[-2]):
            l = lenth(i_point, route[-2])
            route[-1] = i_point
    len_rout += l
    points.remove(route[-1])
    print('{}[{}] ->'.format(route[-1], len_rout), end=' ')
route.append(post)
print('{}[{}]'.format(route[-1], len_rout))

print('Кратчайший путь почтальона:')
for index, i in enumerate(route):
    print('{num}: {address}'.format(
        num=index + 1, address=addresses[i]
    ))
print('Общая длина маршрута составила:', len_rout)
