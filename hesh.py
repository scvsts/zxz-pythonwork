import hashlib
import string

def md5_hash(password):
    m = hashlib.md5()  # 构建MD5对象
    m.update(password.encode(encoding='utf-8')) #设置编码格式 并将字符串添加到MD5对象中
    password_md5 = m.hexdigest()  # hexdigest()将加密字符串 生成十六进制数据字符串值
    return password_md5

def run_hash():
    password = input("请输入一串字符")
    g = md5_hash(password)
    print("{}的哈希为：{}".format(password,g))
    return 0