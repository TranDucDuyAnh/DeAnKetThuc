from employee import NhanVien
import pickle
import os


def add_employee(lt, name, age, salary):
    x = NhanVien(name, age, salary)
    lt.append(x)


def list_employee(lt):
    for info in lt:
        print(info)


def arrange_employee(lt):
    clone = lt.copy()
    clone = sorted(clone, reverse=True)
    return clone


def save_as_byte(lt, path, file):
    try:
        with open(os.path.join(path, file), 'wb') as f:
            pickle.dump(lt, f)
        print('List đã được lưu')
    except Exception as e:
        print('Lưu bị lỗi')
        print(e)


def load_byte(path, file):
    try:
        with open(os.path.join(path, file), 'rb') as f:
            content = pickle.load(f)
        return content
    except Exception as e:
        print('Đọc bị lỗi')
        print(e)


def read_line_by_line(lt):
    for info in lt:
        print(info)


danh_sach = []
path = 'D:/data'
file = 'employee.dat'


def main():
    #
    add_employee(danh_sach, 'Trần Hữu Bảo Anh', 20, 50000)
    add_employee(danh_sach, 'Lê Thanh Đức', 19, 44500)
    add_employee(danh_sach, 'Nguyễn Văn Huy Hoàng', 23, 75000)
    add_employee(danh_sach, 'Phạm Nhật Huy', 22, 69000)
    #
    list_employee(danh_sach)
    #
    ds2 = arrange_employee(danh_sach)
    #
    save_as_byte(ds2, path, file)
    #
    content = load_byte(path, file)
    read_line_by_line(content)


if __name__ == '__main__':
    main()
