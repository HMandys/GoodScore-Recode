import os
import webbrowser
import time
import base64
import json
import requests
from urllib.parse import urlparse, parse_qs, unquote
import utils

def fetch_matched_students(xuehao, student_name):
    url = 'https://hfs-be.yunxiao.com/v2/users/matched-students'
    params = {'roleType': '1', 'identityType': '1', 'identityCode': xuehao, 'studentName': student_name}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def option_1():
    os.system("cls")
    print("功能 1: 查询匹配学生信息")
    start_id = int(input("请输入学号起始值: "))
    end_id = int(input("请输入学号结束值: "))
    student_name = input("请输入学生姓名: ")

    for student_id in range(start_id, end_id + 1):
        result = fetch_matched_students(student_id, student_name)
        if result:
            print(f"[Search] 学号 {student_id} 的匹配结果是：{result}")
        else:
            print(f"学号 {student_id} 请求失败")
    input("按回车键返回主菜单...")

def option_2():
    os.system("cls")
    print("功能 2: 邮箱验证")
    print("正在打开邮箱验证网站，请稍等...")
    webbrowser.open("https://mail.cx/zh/")

    email = input("请输入你的邮箱地址：")
    password = input("请输入你的密码：")
    url = 'https://hfs-be.yunxiao.com/v2/native-users/verification-email'
    data = {'email': email, 'password': password, 'roleType': 1}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("响应内容: ", response.text)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    input("按回车键返回主菜单...")

def option_4(paper_id, pid, exam_id):
    headers = {
        'Cookie': f"hfs-session-id={utils.read_from_file('token.txt')}",
        "Content-Type": "application/json"
    }
    url = f"https://hfs-be.yunxiao.com/v3/exam/{exam_id}/papers/{paper_id}/answer-picture?pid={pid}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data["code"] != 0:
            print("失败！原因: "+data["msg"])
            return
        answer_sheet = data.get("data", {}).get("url", [])
        for i, url in enumerate(answer_sheet):
            utils.download_image(url, f"{i}_{paper_id}_{pid}_{exam_id}.jpg")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    input("按回车键返回主菜单...")

def option_5(user, password):
    data = {
        "loginName": user,
        "loginType": 1,
        "password": base64.b64encode(password.encode('utf-8')),
        "rememberMe": 1,
        "roleType": 1
    }
    try:
        response = requests.post("https://hfs-be.yunxiao.com/v2/users/sessions", data=data)
        response.raise_for_status()
        j = response.json()
        if j["code"] != 0:
            print("登录失败,请检查账号密码。")
            return
        utils.write_to_file("token.txt", j["data"]["token"])
        print("登录完成")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")

def option_6():
    headers = {'Cookie': f"hfs-session-id={utils.read_from_file('token.txt')}", "Content-Type": "application/json"}
    response = requests.get("https://hfs-be.yunxiao.com/v3/exam/list", headers=headers)

    try:
        data = response.json()
        if data.get("data", {}).get("list"):
            exam_list = data["data"]["list"]
            print(f"共有: {len(exam_list)} 条数据")
            for exam in exam_list:
                exam_name = exam.get('name', '无名考试')
                exam_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(exam.get('time', 0) / 1000))
                max_score = exam.get('manfen', '未知')
                score = exam.get('score', '未知')

                print(f"考试名称: {exam_name}")
                print(f"考试时间: {exam_time}")
                print(f"满分: {max_score}  得分: {score}")
                print("-" * 40)
        else:
            print("没有找到任何考试记录。")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    except ValueError as e:
        print(f"JSON 解析失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    input("按回车键返回主菜单...")

def option_3():
    os.system("cls")
    print("功能 3: 验证邮箱链接")
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
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"deviceType": 3, "verificationType": 1, "verificationEmailToken": mail_token}

        response = requests.post(api_url, headers=headers, data=data)
        response.raise_for_status()

        print("验证成功！", response.json())

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    input("按回车键返回主菜单...")

def main():
    options = {
        1: option_1,
        2: option_2,
        3: option_3,
        4: option_4,
        5: option_5,
        6: option_6,
        7: exit
    }

    while True:
        os.system("cls")
        print("请选择要执行的功能：")
        print("1. 查询匹配学生信息 (不需要登录)")
        print("2. 邮箱验证 (不需要登录)")
        print("3. 验证邮箱链接 (不需要登录)")
        print("4. 获取答题卡图片 (登录后使用)")
        print("5. 登录 (在进行部分操作前必须登录)")
        print("6. 获取所有考试列表 (登录后使用)")
        print("7. 退出")
        print("注意：如果您在使用某些需要登录权限的功能时遇到问题，可能是由于尚未登录所致。所有需要登录的功能仅在成功登录后才能正常使用。为了确保您能够顺利使用软件的全部功能，建议您在使用软件前先完成登录操作，登录后再继续使用相关功能。")

        try:
            choice = int(input("请输入功能编号：").strip())
            if choice in options:
                if choice == 4:
                    paper_id = input("请输入 Paper ID: ")
                    pid = input("请输入 PID: ")
                    exam_id = input("请输入 Exam ID: ")
                    options[choice](paper_id, pid, exam_id)
                elif choice == 5:
                    options[choice](input("用户名: "), input("密码: "))
                else:
                    options[choice]()
            else:
                print("无效选项，请重新输入！")
        except ValueError:
            print("输入无效，请输入数字！")

if __name__ == "__main__":
    main()
