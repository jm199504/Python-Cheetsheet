import json

# 生成字典数据集
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

# 将字典转换为json对象，indent=4表示前面有4个字符且自动换行
json_str = json.dumps(data,indent=4)

# 读取jspn对象
data2 = json.loads(json_str)

# 将json对象写入文件
with open('Json_test_data.json', 'w') as f:
    json.dump(data, f)

# 读取json文件
with open('Json_test_data.json', 'r') as f:
    data3 = json.load(f)
