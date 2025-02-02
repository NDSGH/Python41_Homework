import sys
import os
import socket

ADDR = ".local_socket1"

def run_client(str):
  print("client")
  sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
  sock.sendto(message.encode(), ADDR)
  sock.close()
  print("client done")


def run_server():
  print("server")
  sock =  socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
  sock.bind(ADDR)
  while True:
    print("server loop")
    c_data, c_addr = sock.recvfrom(4)
    print(f"received: {c_data} from {c_addr}")

if __name__ == "__main__":
  match(sys.argv):
    case [_]: run_server()
    case [_, message]: run_client(message)
