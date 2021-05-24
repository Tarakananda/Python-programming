data = {
"id": "0001",
"type":"donut",
"name":"Cake",
"image":{
"url":"images/001.jpg",
"width":200,
"height":200
},
"thumbnail":{
"url":"images/tumbnails/0001.jpg",
"width":32,
"height":32
}
}

for key,value in data.items():
    if isinstance(value,str):
        print(key.ljust(20),value)
    elif isinstance(value,dict):
        for skey,svalue in value.items():
            finalkey= key+ "." +skey
            print(finalkey.ljust(20),skey)