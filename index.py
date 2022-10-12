import socket

# uses sockets to connect to a port and then display that the port in question is open
target = "127.0.0.1" #insert ip here (localhost used)

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False 

print(portscan(80)) # enter port to scan
