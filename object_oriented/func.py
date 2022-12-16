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
