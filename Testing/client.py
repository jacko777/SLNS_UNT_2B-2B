import socket
import sys


def main():
    HOST = "localhost"
    PORT = 6454
    address = (HOST, PORT)
    
    data = " ".join(sys.argv[1:]) #Parsing command line arguments
    
    #UDP SOCKET
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    sock.sendto(data + "\n", address) #UDP Simply sends data like a loco
    #received = sock.recv(1024)
    
    received, (IPSender, SenderSocket) = sock.recvfrom(1024)
    
    print "Sent:     {}".format(data)
    print "Received: {}".format(received)
    print "Sent by: {}".format(IPSender)


if __name__ == '__main__':
    
    #while True:
    main()
    
    
