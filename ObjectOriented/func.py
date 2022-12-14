from employee import NhanVien
import json


def add_employee(lt, name, age, salary):
    x = NhanVien(name, age, salary)
    lt.append(x)


def list_employee(lt):
    for info in lt:
        print(info)


def arrange_employee(lt):
    lt = sorted(lt, reverse=True)


def save_as_byte(lt):
    with open('D:/data/employee.bin', mode='wb') as f:
        text = json.dumps(lt)
        f.write(bytes(text))


def read_byte():
    with open('D:/data/employee.bin', mode='wb') as f:
        content = f.read()
        decode = content.decode()
        print(decode)
