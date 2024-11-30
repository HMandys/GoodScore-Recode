import requests
from urllib.parse import urlparse, parse_qs, unquote

def verify_email_from_input():
    """
    输入验证链接，提取 mailToken 并使用 API 验证账号。
    """
    # Step 1: 用户输入链接
    url = input("请输入验证链接: ").strip()
    
    try:
        # Step 2: 提取 mailToken 参数
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        mail_token = unquote(query_params.get("mailToken", [""])[0])
        
        if not mail_token:
            print("验证链接中未找到 mailToken 参数！")
            return
        
        # Step 3: 模拟 API 调用完成验证
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

        # Step 4: 处理 API 返回结果
        if response.status_code == 200:
            print("验证成功！")
            print(response.json())
        else:
            print(f"验证失败！状态码：{response.status_code}，响应内容：{response.text}")

    except Exception as e:
        print(f"发生错误：{e}")

# 调用函数
verify_email_from_input()
