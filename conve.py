#This will initiate conversation
conve_logs = []
def conversation():
    turn = 1
    border = '---------------'
    while True:
        if turn%2==1:
            #client's turn
            print(border)
            print("Client")
            print("To close this session type 'stop'")
            data = input()
            if data == 'stop':
                conve_logs.append("stopped the session")
                return False
            else:
                conve_logs.append(data)
            print("Command Received")
            print(border)
        else:
            #server's turn
            print("Server")
            print("To print logs data type 'print_logs'")
            data = input()
            conve_logs.append(data)
            if data == "print_logs":
                for i,v in enumerate(conve_logs):
                    if i%2==0:
                        print("Client>>>",v)
                    else:
                        print("Server>>>",v)
        turn+=1


if __name__ == '__main__':
    conversation()

