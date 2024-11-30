import requests

# 手动输入你的邮箱和密码
email = input("请输入你的邮箱地址：")
password = input("请输入你的密码：")

# 设置请求的 URL 和数据
url = 'https://hfs-be.yunxiao.com/v2/native-users/verification-email'
data = {
    'email': email,
    'password': password,
    'roleType': 1
}

# 发送 POST 请求
try:
    response = requests.post(url, data=data)
    # 直接输出 API 返回的内容
    print(response.text)
except requests.exceptions.RequestException as e:
    print('请求失败：', e)