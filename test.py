import base64


with open(str("test_image.png"), "rb") as imageFile:
    print(base64.b64encode(imageFile.read()))
#with open('test_text_file.txt', 'r') as file:
    #print(base64.b64encode(str(file.read()).encode('base64')))
    #print(str(file.read()).encode('utf-8'))
    #print(base64.b64encode(str(file.read())))
