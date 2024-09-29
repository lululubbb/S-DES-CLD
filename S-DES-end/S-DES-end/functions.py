import numpy as np

# 密钥扩展
# 密钥置换P10
def p10(arr):
    arr = np.array(arr)
    a = np.array([6, 2, 0, 4, 1, 9, 3, 8, 7, 5])
    reordered_arr = np.zeros_like(arr)
    reordered_arr[a] = arr
    return reordered_arr

# 压缩置换盒p8
def p8(arr):
    arr = np.array(arr)
    # 对输入数组进行切片操作，从索引 2 开始到数组结束,放弃前两个数字
    arr = arr[2:]
    # 数组中的每个数字表示剩余输入数组中元素的新位置索引
    pbox = np.array([1, 3, 5, 0, 2, 4, 7, 6])
    reordered_arr = np.zeros_like(arr)
    # 将切片后的 arr 中的元素按照数组 pbox 中指定的索引重新排列到 reordered_arr 中
    # 转换后的第1位是原来的第0位
    reordered_arr[pbox] = arr
    return reordered_arr

# 循环左移
def left_shift(arr):
    arr = np.roll(arr, -1)
    return arr

# 初始置换盒
def initial_permutation(arr):
    arr = np.array(arr)
    # 数组中的每个数字表示原数组中元素的新位置索引。
    a = np.array([3, 0, 2, 4, 6, 1, 7, 5])
    # 用零初始化
    reordered_arr = np.zeros_like(arr)
    # 将输入数组 arr 中的元素按照数组 a 中指定的索引重新排列到 reordered_arr 中
    # 转换后的第三位是原来的第0位即原来的第0位学者到第三位
    reordered_arr[a] = arr
    return reordered_arr


# 最终置换盒
def final_permutation(arr):
    arr = np.array(arr)
    a = np.array([1, 5, 2, 0, 3, 7, 4, 6])
    reordered_arr = np.zeros_like(arr)
    reordered_arr[a] = arr
    return reordered_arr

# 轮函数
# EPBox
def EPBox(input_array):
    input_array = np.array(input_array)
    # 创建一个新的数组，将输入数组 input_array 复制并连接到它自己的副本之后
    # 1 2 3 4 1 2 3 4
    input_array = np.concatenate([input_array.copy(), input_array.copy()])
    # 数组中的每个数字表示新创建的长数组中元素的新位置索引
    a = np.array([1, 2, 3, 0, 7, 4, 5, 6])
    # 创建一个与连接后的 input_array 形状和数据类型相同的新数组 reordered_arr
    reordered_arr = np.zeros_like(input_array)
    # 将连接后的 input_array 中的元素按照数组 a 中指定的索引重新排列到 reordered_arr 中
    reordered_arr[a] = input_array
    return reordered_arr


# 轮函数替换Sbox1
def SBox1(arr):
    arr = np.array(arr)
    x = arr[[0, 3]]
    y = arr[[1, 2]]
    dic = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 2,
        (1, 1): 3
    }
    mapped_x = dic[tuple(x)]
    mapped_y = dic[tuple(y)]

    sbox1 = [[np.array([0, 1]), np.array([0, 0]), np.array([1, 1]), np.array([1, 0])],
             [np.array([1, 1]), np.array([1, 0]), np.array([0, 1]), np.array([0, 0])],
             [np.array([0, 0]), np.array([1, 0]), np.array([0, 1]), np.array([1, 1])],
             [np.array([1, 1]), np.array([0, 1]), np.array([0, 0]), np.array([1, 0])]]
    return sbox1[mapped_x][mapped_y]


# 轮函数替换Sbox2
def SBox2(arr):
    arr = np.array(arr)
    x = arr[[0, 3]]
    y = arr[[1, 2]]
    dic = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 2,
        (1, 1): 3
    }
    mapped_x = dic[tuple(x)]
    mapped_y = dic[tuple(y)]
    sbox2 = [[np.array([0, 0]), np.array([0, 1]), np.array([1, 0]), np.array([1, 1])],
             [np.array([1, 0]), np.array([1, 1]), np.array([0, 1]), np.array([0, 0])],
             [np.array([1, 1]), np.array([0, 0]), np.array([0, 1]), np.array([1, 0])],
             [np.array([1, 0]), np.array([0, 1]), np.array([0, 0]), np.array([1, 1])]]
    return sbox2[mapped_x][mapped_y]

# 替换函数SBox
# 对加轮密钥之后产生的8bit拆分成左右两个部分分别做SBox1和SBox2替换
def SBox(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    result1 = SBox1(left)
    result2 = SBox2(right)
    output = np.concatenate([result1, result2])
    return output


# SPBox
def SPBox(arr):
    a = np.array([3, 0, 2, 1])
    reordered_arr = np.zeros_like(arr)
    reordered_arr[a] = arr
    return reordered_arr

# 分割
def split(arr):
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    return left, right

# 密钥生成
# 先对10bit的密钥做P10运算，然后分割成左右两部分
# 左右两部分分别进行左移运算后，再并做P8运算，然后生成第一轮密钥K1
# 对之前分别左移后的左右两部分再次分别进行左移运算，再合并做P8运算，然后生成第二轮密钥K2
def generate_key(arr):
    arr = p10(np.array(arr))
    # 生成密钥1
    left, right = split(arr)
    left = left_shift(left)
    right = left_shift(right)
    middle1 = np.concatenate((left, right))
    k1 = p8(middle1)
    # 生成密钥2
    left = left_shift(left)
    right = left_shift(right)
    middle2 = np.concatenate((left, right))
    k2 = p8(middle2)
    return k1, k2

# F：轮函数
# 即四个转换步骤EPBox、加轮密钥异或运算、SBox、SPBox的搭配最后4bit输出结果
def f_function(input_arr, k):
    input_arr = EPBox(input_arr)
    arr = np.bitwise_xor(input_arr, k)
    arr = SBox(arr)
    arr = SPBox(arr)
    return arr

# 加密算法
# 先对明文分组做初始置换、然后将结果与生成的密钥k1进行fk运算，再将结果进行交换
# 再将结果与生成的密钥K2进行fk运算，最后进行最终置换，得到密文
# fk运算就是将8bit结果分成左右两部分，右边部分不变
# 左边部分变为 原来左半部分与 原来右边部分和第一/二轮密钥做轮函数F运算后的结果 做异或运算的最终结果
def encode(key, content):
    content = initial_permutation(content)
    left, right = split(content)
    k1, k2 = generate_key(key)
    temp1 = f_function(right, k1)
    # 交换
    right2 = np.bitwise_xor(temp1, left)
    left2 = right
    temp2 = f_function(right2, k2)
    left3 = np.bitwise_xor(left2, temp2)
    arr = np.concatenate([left3, right2])
    return final_permutation(arr)

# 解密
# 与加密类似，只是K1，K2顺序改变
def decode(key, content):
    content = initial_permutation(content)
    left, right = split(content)
    k1, k2 = generate_key(key)
    temp1 = f_function(right, k2)
    right2 = np.bitwise_xor(temp1, left)
    left2 = right
    temp2 = f_function(right2, k1)
    left3 = np.bitwise_xor(left2, temp2)
    return final_permutation(np.concatenate([left3, right2]))

# 字符串转为二进制数组
def string_change(string):
    # 检查 string 是否是 bytes 对象
    # 如果 string 不是 bytes 类型，那么使用 encode 方法将其编码成 bytes 类型的对象
    if not isinstance(string, bytes):
        string = string.encode('ISO-8859-1')
    # format(c, '08b')：将每个字节 c 格式化为一个 8 位的二进制字符串，不足 8 位的前面补零
    arr = np.array([format(c, '08b') for c in string]).tolist()
    arr = [np.array(list(c)) for c in arr]
    arr = [c.astype(int) for c in arr]
    return arr

# 二进制数组加密为字符串
# 将字符串转换成二进制数组然后对二进制数组进度S-DES加密
# 然后再将加密后的二进制数据转换成字符串
def encode_str(key, string):
    arr = string_change(string)
    # print (arr)
    en_arr = [encode(key, c) for c in arr]
    # print(en_arr)
    en_arr = [c.astype(str) for c in en_arr]
    # print(en_arr)
    en_arr = [''.join(c.tolist()) for c in en_arr]
    en_arr = [int(c, 2) for c in en_arr]
    obj_string = bytes(en_arr)
    # obj_string = str(obj_string)
    return obj_string.decode('ISO-8859-1')

def encode_str2(key, string):
    arr = string_change(string)
    # print (arr)
    en_arr = [encode(key, c) for c in arr]
    # print(en_arr)
    en_arr = [c.astype(str) for c in en_arr]
    # print(en_arr)
    en_arr = [''.join(c.tolist()) for c in en_arr]
    en_arr = [int(c, 2) for c in en_arr]
    obj_string = bytes(en_arr)
    # obj_string = str(obj_string)
    return obj_string
# 密文解密为字符串
# 将加密后形成的字符串转换为二进制数组然后对其进行解密
# 再将解密后得到的二进制数组转化成字符串
def decode_str(key, string):
    arr = string_change(string)
    de_arr = [decode(key, c) for c in arr]
    # print(de_arr)
    de_arr = [c.astype(str) for c in de_arr]
    # print(de_arr)
    de_arr = [''.join(c.tolist()) for c in de_arr]
    de_arr = [int(c, 2) for c in de_arr]
    obj_string = bytes(de_arr)
    # print(type(obj_string.decode('ISO-8859-1')))
    return obj_string.decode('ISO-8859-1')

def decode_str2(key, string):
    arr = string_change(string)
    de_arr = [decode(key, c) for c in arr]
    # print(de_arr)
    de_arr = [c.astype(str) for c in de_arr]
    # print(de_arr)
    de_arr = [''.join(c.tolist()) for c in de_arr]
    de_arr = [int(c, 2) for c in de_arr]
    obj_string = bytes(de_arr)
    # print(type(obj_string.decode('ISO-8859-1')))
    return obj_string

# 暴力破解
def brute_force_sdes( plaintext, ciphertext):
    possible_keys = []
    # for 循环遍历所有可能的 10 位密钥
    for key in range(1024):  # 2^10
        # 每个密钥转换为 10 位的二进制数组
        binary_key = np.array([int(b) for b in format(key, '010b')])
        # 根据每个可能的密钥会生成的密文
        encrypted_text = encode(binary_key, plaintext)
        # 比较密文是否相等
        if np.array_equal(encrypted_text, ciphertext):
            possible_keys.append(' '.join(map(str, binary_key)))
            # 将找到的密钥列表转换为字符串，每个密钥之间用换行符分隔
    key_str = '\n'.join(possible_keys)
    #         possible_keys.append(binary_key.tolist())
    # key_str = '\n'.join([' '.join(map(str, k)) for k in possible_keys])
    return key_str

