import requests
import json
import utils

url_template = "https://hfs-be.yunxiao.com/v3/exam/${examId}/papers/${paperId}/answer-picture?pid=${pid}"
params = {
    "paperId": "xxxx",
    "pid": "xxxx",
    "examId": "xxxx",
}

# 将参数替换到URL模板中
url = url_template.replace("${examId}", params["examId"]).replace("${paperId}", params["paperId"]).replace("${pid}", params["pid"])

# 定义headers，包括认证token
headers = {
    'Cookie': 'hfs-session-id=your-session-id',
    "Content-Type": "application/json"
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 保存返回的图片
    data = json.loads(response.content)
    answersheet = data["data"]["url"]
    for i in range(len(answersheet)):
        utils.download_image(answersheet[i], f"{i}_{params['paperId']}_{params['pid']}_{params['examId']}.jpg")
else:
    print("请求失败，状态码：", response.status_code)


