# coding:utf-8
username = ""
password = ""
server = ""
while(True):
    print("please input option and its value. u username p Passwoed s Server_IP exit")

    line = raw_input()
    if(line == "exit"):
        break

    words = line.split()
    if(len(words) != 2):
        print("Error")
        continue

    if(words[0] == "u"):
        username = words[1]
    elif(words[0] == "p"):
        password = words[1]
    elif(words[0] == "s"):
        server = words[1]
    else:
        print("Error")

print("username ="+username)
print("password ="+password)
print("server ="+server)
