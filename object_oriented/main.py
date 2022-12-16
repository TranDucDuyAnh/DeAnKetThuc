import func


danh_sach = []
path = 'D:/data'
file = 'employee.dat'


def main():
    #
    func.add_employee(danh_sach, 'Trần Hữu Bảo Anh', 20, 50000)
    func.add_employee(danh_sach, 'Lê Thanh Đức', 19, 44500)
    func.add_employee(danh_sach, 'Nguyễn Văn Huy Hoàng', 23, 75000)
    func.add_employee(danh_sach, 'Phạm Nhật Huy', 22, 69000)
    #
    func.list_employee(danh_sach)
    #
    ds2 = func.arrange_employee(danh_sach)
    #
    func.save_as_byte(ds2, path, file)
    #
    content = func.load_byte(path, file)
    func.read_line_by_line(content)


if __name__ == '__main__':
    main()
