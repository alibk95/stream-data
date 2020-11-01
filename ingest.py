import requests

with requests.get("http://127.0.0.1:8080/request_data/100", stream=True) as re:
    buffer = ""
    for chunk in re.iter_content(chunk_size=1):
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            print(t)
            buffer = ""
        else:
            buffer += chunk.decode()