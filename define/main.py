import list as lt


low = -5
high = 5
items = 10
# Saving
path = 'D:/data'
file1 = 'list.txt'
file2 = 'down.txt'


def main():
    t = lt.rand_list(low, high, items)
    lt.save_list(t, path, file1, 't')

    down = lt.arrange_list(t, items, False)
    lt.save_list(down, path, file2, 't')

    lt.find_in_list(down, items, 1)


if __name__ == '__main__':
    main()
