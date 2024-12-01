import requests
import utils

n = input("学生真实姓名: ")
b = input("学号/考号: ")
si = utils.read_from_file("token.txt")
headers = {
    'Cookie': f"hfs-session-id={si}",
    "Content-Type": "application/json"
}
r = requests.get(f"https://hfs-be.yunxiao.com/v2/users/matched-students?roleType=1&studentName={n}&identityType=1&identityCode={b}")
j = r.json()
if j["code"] != 0:
    print(j["msg"])
else:
    students = j.get("data", {}).get("students", [])
    if students:
        for student in students:
            print("-" * 40)
            print(f"学生ID: {student.get('studentId')}")
            print(f"学生姓名: {student.get('studentName')}")
            print(f"学校ID: {student.get('schoolId')}")
            print(f"学校名称: {student.get('schoolName')}")
            print(f"是否需要验证码: {student.get('needAuthCode')}")
            print("-" * 40)
    else:
        print("没有找到匹配的学生信息")
    student_id = input("学生ID(请和输出的内容保持一致): ")
    # school_authcode = input("学校验证码(如果无无需填写): ")
    data = {
        "identityCode": b,
        "identityType": 1,
        "schoolAuthCode": "",
        "studentId": student_id,
    }
    bind_school = requests.put("https://hfs-be.yunxiao.com/v2/users/bind-student",headers=headers,data=data)
    print(bind_school.text)