# GoodScore-Recode

## hfs_toolbox_fixed.py
是一个工具箱的版本所有的相关文件已经整合到了这么一个文件中方便用户使用

## matched_students.py
匹配学生  
接口：https://hfs-be.yunxiao.com/v2/users/matched-students  
参数：  
- `'roleType': '1'`  
- `'identityType': '1'`  
- `'identityCode': xuehao`  
- `'studentName': studentName

## sign_up.py
通过邮箱注册好分数学生版账号  
接口：https://hfs-be.yunxiao.com/v2/native-users/verification-email  
参数：  
- `'email': email`  
- `'password': password`  
- `'roleType': 1`

## yan_zheng.py
邮箱收到的链接验证账号，验证账号后才能绑定学生  
接口：https://hfs-be.yunxiao.com/v2/native-users/activation  
请求头：  
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}
```

## 请求数据

```python
data = {
    "deviceType": 3,
    "verificationType": 1,
    "verificationEmailToken": mail_token,
}
```

# 接口列表
- 登录接口: https://hfs-be.yunxiao.com/v2/users/sessions     
- 绑定学生接口：https://hfs-be.yunxiao.com/v2/users/bind-student    
- 匹配学生接口：https://hfs-be.yunxiao.com/v2/users/matched-students     
- 用户快照接口: https://hfs-be.yunxiao.com/v2/user-center/user-snapshot  
- 考试列表接口: https://hfs-be.yunxiao.com/v3/exam/list?start=0&limit=100    
- 考试概览接口: https://hfs-be.yunxiao.com/v3/exam/${examId}/overview    
- 考试排名接口: https://hfs-be.yunxiao.com/v3/exam/${examId}/rank-info  
- 答题图片接口: https://hfs-be.yunxiao.com/v3/exam/${examId}/papers/${paperId}/answer-picture?pid=${pid}    
- 试卷排名接口: https://hfs-be.yunxiao.com/v3/exam/${examId}/papers/${paperId}/rank-info    
- 试卷题目列表接口：https://hfs-be.yunxiao.com/v3/exam/{self.exam.examId}/papers/{self.paperId}/question-detail  
