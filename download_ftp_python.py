from ftplib import FTP
import os 
import shutil
from datetime import datetime


ftp_ontime = FTP('host')
ftp_ontime.login('usuer', 'pssd')

#pasta = ftp_ontime.cwd('recebidos')

ftp_ontime.cwd('recebidos')
arquivos = ftp_ontime.nlst()

download = r"arquivos\\"
scan = os.scandir(download)


for n in arquivos:
    ftp_ontime.retrbinary("RETR "+n, open(download+n, 'wb').write)
    print(f'arquivo {n} baixado ')
    #deleta arquivo apos download
    ftp_ontime.delete(n)


