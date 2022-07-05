import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    ban='''
\033[1;32m███████╗███████╗██╗  ██╗
\033[1;35m██╔════╝██╔════╝╚██╗██╔╝
\033[1;34m███████╗█████╗   ╚███╔╝
\033[1;36m╚════██║██╔══╝   ██╔██╗ 
\033[1;33m███████║███████╗██╔╝ ██╗
\033[1;35m╚══════╝╚══════╝╚═╝  ╚═╝
\033[41m\033[1;37m[M31THUN]   [ADNAM]   [RJ_MAMUN]   [INSAN]\x1b[0m '''
    #os.system('xdg-open https://www.facebook.com/groups/1136477216940696/');time.sleep(2)
    from AKING import Menu
    Menu()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
