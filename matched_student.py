import requests

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

def main():
    # 手动输入学号范围和姓名
    start_id = int(input("请输入学号起始值: "))
    end_id = int(input("请输入学号结束值: "))
    student_name = input("请输入学生姓名: ")

    last_success_result = None  # 用于存储最后一次成功的请求结果
    
    for student_id in range(start_id, end_id + 1):  # 包括结束值
        try:
            result = fetch_matched_students(student_id, student_name)
            print('\033[31m' + "[Search] " + '\033[0m' + f"学号 {student_id} 的匹配结果是：{result}")
            last_success_result = result  # 更新最后一次成功的请求结果
        except requests.exceptions.RequestException as e:
            print(f"学号 {student_id} 请求失败: {e}")


if __name__ == '__main__':
    main()