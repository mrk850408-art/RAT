import socket
from colorama import Fore, Back, Style


def socket_create():
    global host, port, s
    host = "127.0.0.1"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)

socket_create()

print(Back.BLACK+Fore.RED+"""



                                                                                                                                                                        
   SSSSSSSSSSSSSSS EEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNTTTTTTTTTTTTTTTTTTTTTTTIIIIIIIIIINNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLL             
 SS:::::::::::::::SE::::::::::::::::::::EN:::::::N       N::::::NT:::::::::::::::::::::TI::::::::IN:::::::N       N::::::NE::::::::::::::::::::EL:::::::::L             
S:::::SSSSSS::::::SE::::::::::::::::::::EN::::::::N      N::::::NT:::::::::::::::::::::TI::::::::IN::::::::N      N::::::NE::::::::::::::::::::EL:::::::::L             
S:::::S     SSSSSSSEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NT:::::TT:::::::TT:::::TII::::::IIN:::::::::N     N::::::NEE::::::EEEEEEEEE::::ELL:::::::LL             
S:::::S              E:::::E       EEEEEEN::::::::::N    N::::::NTTTTTT  T:::::T  TTTTTT  I::::I  N::::::::::N    N::::::N  E:::::E       EEEEEE  L:::::L               
S:::::S              E:::::E             N:::::::::::N   N::::::N        T:::::T          I::::I  N:::::::::::N   N::::::N  E:::::E               L:::::L               
 S::::SSSS           E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N        T:::::T          I::::I  N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     L:::::L               
  SS::::::SSSSS      E:::::::::::::::E   N::::::N N::::N N::::::N        T:::::T          I::::I  N::::::N N::::N N::::::N  E:::::::::::::::E     L:::::L               
    SSS::::::::SS    E:::::::::::::::E   N::::::N  N::::N:::::::N        T:::::T          I::::I  N::::::N  N::::N:::::::N  E:::::::::::::::E     L:::::L               
       SSSSSS::::S   E::::::EEEEEEEEEE   N::::::N   N:::::::::::N        T:::::T          I::::I  N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     L:::::L               
            S:::::S  E:::::E             N::::::N    N::::::::::N        T:::::T          I::::I  N::::::N    N::::::::::N  E:::::E               L:::::L               
            S:::::S  E:::::E       EEEEEEN::::::N     N:::::::::N        T:::::T          I::::I  N::::::N     N:::::::::N  E:::::E       EEEEEE  L:::::L         LLLLLL
SSSSSSS     S:::::SEE::::::EEEEEEEE:::::EN::::::N      N::::::::N      TT:::::::TT      II::::::IIN::::::N      N::::::::NEE::::::EEEEEEEE:::::ELL:::::::LLLLLLLLL:::::L
S::::::SSSSSS:::::SE::::::::::::::::::::EN::::::N       N:::::::N      T:::::::::T      I::::::::IN::::::N       N:::::::NE::::::::::::::::::::EL::::::::::::::::::::::L
S:::::::::::::::SS E::::::::::::::::::::EN::::::N        N::::::N      T:::::::::T      I::::::::IN::::::N        N::::::NE::::::::::::::::::::EL::::::::::::::::::::::L
 SSSSSSSSSSSSSSS   EEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNN      TTTTTTTTTTT      IIIIIIIIIINNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLL
                                                                                                                                                                        
                                                                                 by sudo-scorpion""")

print(Style.RESET_ALL)

while True:
    print(Fore.GREEN+f'[*] listening as {host}:{port}')
    conn, addr = s.accept()
    print(Fore.GREEN+f'[+] client connected {addr}')

    conn.send(b'connected')


    while True:
        cmd = input('>>> ')
        conn.send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        result = conn.recv(1024).decode()
        print(result)

    conn.close()

    if input(Fore.RED+'Wait for new client y/n ') == 'n':
        break

s.close()
