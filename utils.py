import requests

def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"图片已保存到 {file_path}")
    else:
        print(f"请求失败，状态码：{response.status_code}")

def write_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def read_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()  # 读取整个文件内容
    return content