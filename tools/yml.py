import yaml

def read_history():
    # 读取 YAML 文件
    with open('./history/message_history.yml', 'r') as file:
        chat_data = yaml.safe_load(file)
    return chat_data["chats"]
