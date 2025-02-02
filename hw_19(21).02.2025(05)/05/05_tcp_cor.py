import sys
import socket
import urllib.parse

ADDR = ('127.0.0.1', 7001)
PAYLOAD_BYTE_LEN = 4
READ_BYTES = 1024


def start_acceptor():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(ADDR)
  sock.listen(1)
  print(f"server started and wait connection on {ADDR[0]}:{ADDR[1]}")

  while True:
    c_sock, c_addr = sock.accept()
    print(f"new client connected from {c_addr[0]}:{c_addr[1]}")
    
    buff = bytes()   
    buff += c_sock.recv(READ_BYTES)
    payload_size = int.from_bytes(buff[0:PAYLOAD_BYTE_LEN])
    if(len(buff) >= PAYLOAD_BYTE_LEN + payload_size):
      payload = buff[PAYLOAD_BYTE_LEN:PAYLOAD_BYTE_LEN + payload_size]
      buff = buff[PAYLOAD_BYTE_LEN + payload_size:]
  
    request = buff.decode()
    print(f"Запрос:\n{request}")
    
    
    message = "Введите сообщение в формате: http://127.0.0.1:7001/?message=СООБЩЕНИЕ"
    if "GET /?message=" in request:
      start_index = request.index("GET /?message=") + len("GET /?message=")
      end_index = request.index(" HTTP", start_index)
      message = urllib.parse.unquote(request[start_index:end_index])
    
    
    html_content = f"<html><body><h2>{message}</h2></body></html>"
    
    response = f"HTTP/1.1 200 OK\r\n"
    response += f"Content-Type: text/html; charset=utf-8\r\n"
    # response += f"Content-Length: {len(html_content)}\r\n"
    response += f"\r\n"
    response += html_content
    
    c_sock.sendall(response.encode())


if __name__ == "__main__":
    start_acceptor()
