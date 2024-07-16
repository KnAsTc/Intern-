# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:12:21 2021

@author: qqwdf
"""


# server.py

def do_some_stuffs_with_input(input_string):  
    """
    This is where all the processing happens.

    Let's just read the string backwards
    """

    print("Processing that nasty input!")
    return input_string[::-1]

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 1024*1024+34):#更改MAX_BUFFER_SIZE 

    # the input is in bytes, so decode it
   

    # MAX_BUFFER_SIZE is how big the message can be
    # this is test if it's sufficiently big
    import sys
    import io
    
    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)
    siz = sys.getsizeof(input_from_client_bytes)
    if  siz >= MAX_BUFFER_SIZE:
     print("The length of input is probably too long: {}".format(siz))
    
        # decode input and strip the end of line
    input_from_client = input_from_client_bytes.decode("utf-8").rstrip()
    
        
        #更改新增儲存檔案
    filename ='log.json'
    f = io.open(filename, mode="w", encoding="utf-8")
    f.write(input_from_client)
    f.close()
        
        
    print(input_from_client)


def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("169.254.163.220", 12345))
        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    print('Socket now listening')

    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()
    soc.close()


start_server()  
