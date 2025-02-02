import sys
import socket

ADDR = ('127.0.0.1', 7003)
PAYLOAD_BYTE_LEN = 4
READ_BYTES = 1000

def start_acceptor():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(ADDR)
  sock.listen(1)
  print(f"server started and wait connection on {ADDR[0]}:{ADDR[1]}")

  c_sock, c_addr = sock.accept()
  print(f"new client connected from {c_addr[0]}:{c_addr[1]}")
  buff = bytes()
  while True:
    buff += c_sock.recv(READ_BYTES)
    payload_size = int.from_bytes(buff[0:PAYLOAD_BYTE_LEN])
    if(len(buff) >= PAYLOAD_BYTE_LEN+payload_size):
      payload = buff[PAYLOAD_BYTE_LEN:PAYLOAD_BYTE_LEN+payload_size]
      buff = buff[PAYLOAD_BYTE_LEN+payload_size:]
      text = payload.decode()
      print(f"new message: {text}")
      if text == "shutdown":
        print("exiting")
        c_sock.close()
        sock.close()
        return


def start_client():
  def to_proto_message(str):
    payload = str.encode()
    payload_size = len(payload).to_bytes(PAYLOAD_BYTE_LEN)
    return payload_size + payload
    
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(ADDR)
  for message in ["кто", "идет", "за", "shutdown"]:
    proto_msg = to_proto_message(message);
    print(f"sending message: {message}, raw: {proto_msg}")
    sock.sendall(proto_msg)


if __name__ == "__main__":
  if len(sys.argv) == 1:
    start_acceptor()
  else:
    start_client()

