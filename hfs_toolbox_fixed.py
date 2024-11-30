import os
import webbrowser
import requests
from urllib.parse import urlparse, parse_qs, unquote


def fetch_matched_students(xuehao, studentName):
    url = 'https://hfs-be.yunxiao.com/v2/users/matched-students'
    params = {
        'roleType': '1',
        'identityType': '1',
        'identityCode': xuehao,
        'studentName': studentName
    }
    response = requests.get(url, params=params)
    return response.json()


def option_1():
    os.system("cls")  # 清屏
    print("执行功能 1: 查询匹配学生信息")
    start_id = int(input("请输入学号起始值: "))
    end_id = int(input("请输入学号结束值: "))
    student_name = input("请输入学生姓名: ")

    for student_id in range(start_id, end_id + 1):
        try:
            result = fetch_matched_students(student_id, student_name)
            print('\033[31m' + "[Search] " + '\033[0m' + f"学号 {student_id} 的匹配结果是：{result}")
        except requests.exceptions.RequestException as e:
            print(f"学号 {student_id} 请求失败: {e}")

    input("按回车键返回主菜单...")  # 等待用户返回


def option_2():
    os.system("cls")  # 清屏
    print("执行功能 2: 邮箱验证")

    # 自动打开默认浏览器访问指定网站
    print("正在打开邮箱验证网站，请稍等...")
    webbrowser.open("https://mail.cx/zh/")

    email = input("请输入你的邮箱地址：")
    password = input("请输入你的密码：")

    url = 'https://hfs-be.yunxiao.com/v2/native-users/verification-email'
    data = {
        'email': email,
        'password': password,
        'roleType': 1
    }

    try:
        response = requests.post(url, data=data)
        print("响应内容: ", response.text)
    except requests.exceptions.RequestException as e:
        print('请求失败：', e)

    input("按回车键返回主菜单...")  # 等待用户返回


def option_3():
    os.system("cls")  # 清屏
    print("执行功能 3: 验证邮箱链接")
    url = input("请输入验证链接: ").strip()

    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        mail_token = unquote(query_params.get("mailToken", [""])[0])

        if not mail_token:
            print("验证链接中未找到 mailToken 参数！")
            return

        api_url = "https://hfs-be.yunxiao.com/v2/native-users/activation"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "deviceType": 3,
            "verificationType": 1,
            "verificationEmailToken": mail_token,
        }

        response = requests.post(api_url, headers=headers, data=data)

        if response.status_code == 200:
            print("验证成功！")
            print(response.json())
        else:
            print(f"验证失败！状态码：{response.status_code}，响应内容：{response.text}")

    except Exception as e:
        print(f"发生错误：{e}")

    input("按回车键返回主菜单...")  # 等待用户返回


def main():
    while True:
        os.system("cls")  # 清屏
        print("请选择要执行的功能：")
        print("1. 查询匹配学生信息")
        print("2. 邮箱验证")
        print("3. 验证邮箱链接")
        print("4. 退出")
        choice = input("请输入功能编号（1/2/3/4）：").strip()

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            print("程序已退出！")
            break
        else:
            print("输入无效，请重新输入！")
            input("按回车键继续...")


if __name__ == "__main__":
    main()
