
#!/usr/bin/python

try:
    import requests
    print("Requests imported!")
    import textwrap
    print("textwrap imported!")
except ImportError as e:
    print(e)

request_object = requests.get("http://www.google.co.in")
response = request_object.content
wrapper = textwrap.TextWrapper(width=100)
wrapped_content_list = wrapper.wrap(text=response)

for line in wrapped_content_list:
    print(line)

print(response)