import socket

def prog_client(comando):
   print(comando)
   
   host = "192.168.5.10"
   port = 3001
   
   client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
   client_socket.connect((host,port))
   
   client_socket.send(comando)
   data = client_socket.recv(1024)
   
   client_socket.close()
   print("comando inviato"), repr(data)


if __name__ == "__main__":
    cmd = "*1*1*311##"    
    prog_client(cmd)
    

#dispositivo luce A= 2(Area 2), PL= 4(Punto luce 4) -->where="24"
#dispositivo luminoso A= 03, PL= 11su bus locale 01-->where="0311#4#01"
