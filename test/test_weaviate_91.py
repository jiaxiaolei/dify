import weaviate

client = weaviate.Client("http://localhost:8080") # 连接到你的 Weaviate 实例

# 获取所有数据（示例）
result = client.query.get("YourClassName", ["property1", "property2"]).do()
print(result)

# 带过滤器的查询
result = client.query.get("YourClassName", ["property1", "property2"]).with_where({
    "path": ["property1"],
    "operator": "Equal",
    "valueText": "someValue"
}).do()
print(result)

# 基于向量相似度的查询
result = client.query.get("YourClassName", ["property1", "property2"]).with_near_text({
    "concepts": ["search query"]
}).do()
print(result)
