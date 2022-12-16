import func


def main():
    danh_sach = []

    func.add_employee(danh_sach, 'Trần Hữu Bảo Anh', 20, 50000)
    func.add_employee(danh_sach, 'Lê Thanh Đức', 19, 44500)
    func.add_employee(danh_sach, 'Nguyễn Văn Huy Hoàng', 23, 75000)
    func.add_employee(danh_sach, 'Phạm Nhật Huy', 22, 69000)

    func.list_employee(danh_sach)

    func.arrange_employee(danh_sach)

    func.save_as_byte(danh_sach)


if __name__ == '__main__':
    main()
