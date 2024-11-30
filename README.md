# GoodScore-Recode

#hfs_toolbox_fixed.py
 主程序

#matched_students.py
 匹配学生
 接口：https://hfs-be.yunxiao.com/v2/users/matched-students
 'roleType': '1'
 'identityType': '1'
 'identityCode': xuehao,
 'studentName': studentName

#sign_up.py
 通过邮箱注册好分数学生版账号
 接口：https://hfs-be.yunxiao.com/v2/native-users/verification-email
 'email': email
 'password': password
 'roleType': 1

#yan_zheng.py
 邮箱收到的链接验证账号，验证账号后才能绑定学生
 接口：https://hfs-be.yunxiao.com/v2/native-users/activation
 headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
     "Content-Type": "application/x-www-form-urlencoded",}
 data = {
     "deviceType": 3,
     "verificationType": 1,
     "verificationEmailToken": mail_token,}
