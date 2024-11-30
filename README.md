# GoodScore-Recode <br>
 <br>
#hfs_toolbox_fixed.py <br>
 主程序 <br>
 <br>
#matched_students.py <br>
 匹配学生 <br>
 接口：https://hfs-be.yunxiao.com/v2/users/matched-students <br>
 'roleType': '1' <br>
 'identityType': '1' <br>
 'identityCode': xuehao, <br>
 'studentName': studentName <br>
 <br>
#sign_up.py <br>
 通过邮箱注册好分数学生版账号 <br>
 接口：https://hfs-be.yunxiao.com/v2/native-users/verification-email <br>
 'email': email <br>
 'password': password <br><br>
 'roleType': 1 <br>
 <br>
#yan_zheng.py <br>
 邮箱收到的链接验证账号，验证账号后才能绑定学生 <br>
 接口：https://hfs-be.yunxiao.com/v2/native-users/activation <br>
 headers = { <br>
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36", <br>
     "Content-Type": "application/x-www-form-urlencoded",} <br>
 data = { <br>
     "deviceType": 3, <br>
     "verificationType": 1, <br>
     "verificationEmailToken": mail_token,} <br> 
     
#最后附上一些接口 
  "login": "https://hfs-be.yunxiao.com/v2/users/sessions", 
  "userSnapshot": "https://hfs-be.yunxiao.com/v2/user-center/user-snapshot", 
  "examList": "https://hfs-be.yunxiao.com/v3/exam/list?start=0&limit=100", 
  "examOverview": "https://hfs-be.yunxiao.com/v3/exam/${examId}/overview", 
  "examRankInfo": "https://hfs-be.yunxiao.com/v3/exam/${examId}/rank-info", 
  "answerPicture": "https://hfs-be.yunxiao.com/v3/exam/${examId}/papers/${paperId}/answer-picture?pid=${pid}", 
  "paperRankInfo": "https://hfs-be.yunxiao.com/v3/exam/${examId}/papers/${paperId}/rank-info", 
