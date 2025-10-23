
#from pymilvus import MilvusClient
#
#client = MilvusClient(uri="http://localhost:19530", token="root:Milvus")


from pymilvus import MilvusClient
client = MilvusClient(uri="http://192.168.10.195:19530")
print(client.get_server_version())

