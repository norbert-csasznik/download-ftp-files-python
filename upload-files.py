from ftplib import FTP
import os 
import shutil

ftp_ontime = FTP('host')
ftp_ontime.login('user', 'pssw')

download = r"arquivos"
scan = os.scandir(download)

ftp_ontime.cwd('/recebidos/backup')

for n in scan:
    if n.is_file():
        arq = open(n, 'rb')
        nome = n.name      
        try:
            ftp_ontime.storbinary(f"STOR {nome}", arq)
            arq.close()
        except Exception as erro:
            print(erro)
      
