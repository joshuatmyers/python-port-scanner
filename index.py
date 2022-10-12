import socket
import threading 
from queue import Queue # stops ports scanning multiple times

# uses sockets to connect to a port and then display that the port in question is open
target = "127.0.0.1" #insert ip here (localhost used)

queue = Queue()
openPorts = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False 

def fillQueue(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open".format(port))
            openPorts.append(port)
        
portList = range(1, 1024)
fillQueue(portList)

threadList = []

# creates 100 threads
for t in range(100):
    # refers to worker function without calling it
    thread = threading.Thread(target=worker)
    threadList.append(thread)

# opens all threads
for thread in threadList:
    thread.start()

# waits for all threads to finish until it continues with code
for thread in threadList:
    thread.join()

print("Open ports are: ", openPorts)

