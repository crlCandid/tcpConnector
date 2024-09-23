import socket

target_addr = input('Enter IP: ')
target_port = int(input('Enter Port: '))
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_addr, target_port))
except socket.error as e:
    print(f"Socket error: {e}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

zpl_bulk = """
^XA
^FO50,50^A0,N,50,50^FDLabel 1: Hello, World!^FS
^XZ
^XA
^FO50,50^A0,N,50,50^FDLabel 2: This is the second label!^FS
^XZ
^XA
^FO50,50^A0,N,50,50^FDLabel 3: Yet another label!^FS
^XZ
"""

zpl_single = """
^XA
^FO50,50^A0,N,50,50^FDLabel 1: Hello, Single World!^FS
^XZ
"""
zpl_template = '^XA\n\n\n^CI28\n^PR8\n^LL406\n^PW812\n\n^FX BLACK BOX (TR)\n^FO686,102\n^GB120,120,100\n^FS\n\n^FX STAGE BOX (TR)\n^FO692,132\n^FB110,1,,C\n^AVN\n^FR\n\n^FD1^FS\n\n^FX STAGE X of Y (TR)\n^FO692,232\n^FB110,1,,C\n^ARN\n^FD1 of 10\\&\n^FS\n\n^FX PATIENT DETAILS\n^FO106,90\n^ATN\n^FDTaylor Dewitt\n^FS\n\n^FX PRESCRIBED DOCTOR ID\n^FO106,145\n^AQN\n^AAN,20^FDClear Aligner^FS\n^FO0,120\n^FS\n\n^FX LEFT ALIGNER ID\n^FO106,170\n^GB47,25,2^FS\n^FO116,175^AAN,20^FDSN^FS\n^FO156,175^AAN,20^FDVPKS2L01^FS\n^FO106,197\n^GB47,25,2^FS\n^FO112,202^AAN,20^FDLOT^FS\n^FO158,202^AAN,20^FD088492^FS\n\n^FX RIGHT ALIGNER ID\n^FO406,170\n^GB47,25,2^FS\n^FO416,175^AAN,20^FDSN^FS\n^FO456,175^AAN,20^FDVPKS2U01^FS\n^FO406,197\n^GB47,25,2^FS\n^FO412,202^AAN,20^FDLOT^FS\n^FO458,202^AAN,20^FD088492^FS\n\n^FX LEFT DATAMATRIX\n^FO106,230\n^BXN,4,200,,,,_\n^FD_10100850004223314112024-081008849221VPKS2L01^FS\n\n^FX LEFT UDI\n^FO213,240^ABN^FD(01)00850004223314^FS\n^FO213,260^ABN^FD(10)088492^FS\n^FO213,280^ABN^FD(11)2024-08^FS\n^FO213,300^ABN^FD(21)VPKS2L01^FS\n^FO213,320^ABN^FD(31)FGS-2002^FS\n\n^FX RIGHT DATAMATRIX\n^FO406,230\n^BXN,4,200,,,,_\n^FD_10100850004223314112024-081008849221VPKS2U01^FS\n\n^FX RIGHT UDI\n^FO513,240^ABN^FD(01)00850004223314^FS\n^FO513,260^ABN^FD(10)088492^FS\n^FO513,280^ABN^FD(11)2024-08^FS\n^FO513,300^ABN^FD(21)VPKS2U01^FS\n^FO513,320^ABN^FD(31)FGS-2002^FS\n\n\n^FXRX ONLY\n^FO700,355^A0N,20^FDRx Only^FS\n\n^FX MANUFACTURER ICON & NAME\n^FO105,350\n^GFA,75,75,3, 00003C00003C00003C00003C00003C00003C00003C00003C10413C30C33C38E3BC79E7BC7DF7FCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFCFFFFFC^FS\n^FO135,355\n^A0N,18\n^FDCandid Care Co^FS\n^FO135,372^A0N,15^FD12502 Col. El Realito Tijuana, BC 22250^FS\n\n^FX DATE AND ICON\n^FO550,350\n^GFA,108,108,4,0000000000001F0000001F0000001B0000001B0000001B0000001B0000001B0000001B000C30DB001C71DB001E79FB003EFBFB0037DF7B0073CF3B00638E3B006000030060000300600003006000030060000300600003006000030060000300600003007FFFFF003FFFFE00^FS\n^FO580,355^A0N,20^FD2024-08^FS\n\n^FX Note part one\n^FO105,370\n^A0N,15\n^FS\n^XZ'

while True:
    doCycle = input('Run cycle? y/n')

    if doCycle == 'n':
        client.close()
        exit()

    option = int(input("""Select Option:
    1 - Single
    2 - Bulk
    3 - Cycle
    4 - Template
    """))

    if option == 1:
        print ('Single')
        client.sendall(zpl_single.encode())

    if option == 2:
        print ('Bulk')
        client.sendall(zpl_bulk.encode())

    if option == 3:
        count = int(input('Enter cycle count: '))

        for x in range(count):
            client.sendall(zpl_single.encode())
    
    if option == 4:
        print ('Template')
        client.sendall(zpl_template.encode())