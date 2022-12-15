import requests


get_req = requests.get('http://127.0.0.1:8000/items/0')
print(f"Get request content: {get_req.content.decode()}")

a = input("item name> ")
post_req = requests.post('http://127.0.0.1:8000/items/create', data={"item_name":a})
print(f"Post request content: {post_req.content.decode()}")

a = input("item name> ")
put_req = requests.put('http://127.0.0.1:8000/items/create', data={"item_name":a})
print(f"Put request content: {put_req.content.decode()}")

a = input("item id> ")
delete_req = requests.delete((f'http://127.0.0.1:8000/items/{a}'))
print(f"Delete request content: {delete_req.content.decode()}")