

import webbrowser
f = open('helloworld.html','w')
message = """<html>
<head></head>
<body><p>Hello, This is how python is embedded in an html file</p>
</html>"""
f.write(message)
f.close()
print(f)
webbrowser.open_new_tab('helloworld.html')
