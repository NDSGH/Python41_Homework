import sys
import os
import socket

ADDR = ("127.0.0.1", 7001)


def run_client(*msg):
  print("client")
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  for m in msg:
      sock.sendto(m.encode(), ADDR)
  sock.close()
  print("client done")
  
  
def run_server():
  print("server")
  sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind(ADDR)
  
  while True:
    print("server loop")
    c_data, c_addr = sock.recvfrom(65536)
    
    print(f"received: {c_data} from {c_addr}")


if __name__ == "__main__":
  match(sys.argv):
    case [_]: run_server()
    case [_, *msg]: run_client(*msg)
