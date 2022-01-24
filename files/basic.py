with open("files/fruits.txt", "a+") as myfile:
    myfile.write("\nTomatoe")
    myfile.seek(0)
    content = myfile.read()    

print(content)