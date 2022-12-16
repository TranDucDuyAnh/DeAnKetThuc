import draw


def main():
    x, y0, y1, y2, y3 = draw.get_list_value()
    draw.draw_plot(x, y0, y1, y2, y3)


if __name__ == '__main__':
    main()