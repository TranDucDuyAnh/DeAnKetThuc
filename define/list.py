import random
import pickle
import os


# Viết hàm sinh ngẫu nhiên các giá trị cho 1 list các số thực trong khoảng [a, b];
def rand_list(a: int, b: int, m: int) -> list:
    t = []
    for i in range(m):
        x = random.random() * (b - a) + a
        t.append(x)
    return t


# Viết hàm sắp xếp list các số thực ở trên theo chiều tăng dần (nếu tham số reverse= True),
# giảm dần (nếu tham số reverse= False);
def arrange_list(t: list, m: int, reverse: bool) -> list:
    cl = t.copy()
    if not reverse:
        for i in range(m-1):
            for j in range(i+1, m):
                if cl[i] < cl[j]:
                    cl[i], cl[j] = cl[j], cl[i]
    else:
        for i in range(0, m-1):
            for j in range(i+1, m):
                if cl[i] > cl[j]:
                    cl[i], cl[j] = cl[j], cl[i]
    return cl


# Viết hàm tìm kiếm số n trong list:
# a. Nếu không tìm thấy thì thông báo ra màn hình là không tìm thấy số n trong list;
# b. Nếu tìm thấy thì hiển thị ra màn hình tất cả các vị trí trong list có giá trị bằng với n.
def find_in_list(t: list, m: int, n: float):
    found = False
    pos = []
    for i in range(m):
        if n == t[i]:
            found = True
            pos.append(i)
    if found:
        print('Giá trị xuất hiện ở các vị trí:', pos)
    else:
        print('Không tìm thấy giá trị trong list')


# Viết hàm lưu list vào tập tin có tùy chọn tham số để xác định là lưu tập tin văn bản hay tập
# tin nhị phân

# t = văn bản; b = nhị phân
def save_list(t: list, path: str, file: str, st: str):
    if st != 't' and st != 'b':
        print('Hãy nhập st là t (văn bản) hoặc b (nhị phân)')
    elif st == 't':
        try:
            with open(os.path.join(path, file), 'wt') as f:
                f.write(str(t))
            print('List đã được lưu')
        except Exception as e:
            print('Lưu bị lỗi')
            print(e)
    elif st == 'b':
        try:
            with open(os.path.join(path, file), 'wb') as f:
                pickle.dump(t, f)
            print('List đã được lưu')
        except Exception as e:
            print('Lưu bị lỗi')
            print(e)
