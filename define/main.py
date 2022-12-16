import list as lt


def main():
    t = lt.rand_list(-5, 5)
    lt.save_list(t, 'D:/data/list.txt', 't')

    down = lt.arrange_list(t, False)
    lt.save_list(down, 'D:/data/down.txt', 't')

    lt.find_in_list(down, 0)


if __name__ == '__main__':
    main()
