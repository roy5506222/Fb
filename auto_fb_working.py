import os
import sys
import time
import json
import random
import re
import hashlib
import signal
from urllib.parse import quote
from datetime import datetime

# Import Rich and Colorama for a beautiful interface
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.spinner import Spinner

import requests
from bs4 import BeautifulSoup
from faker import Faker

#_________|LOOP|_________#
oks = []
cps = []
loop = 0

init(autoreset=True)
console = Console()

# Enable Bold Font in Terminal
os.system("echo -e '\033[1m'")

# Function to generate unique key
def get_unique_id():
    try:
        unique_str = str(os.getuid()) + os.getlogin() if os.name != 'nt' else str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(f'Error generating unique ID: {e}')
        exit(1)

# Centralized function to print bold text
def print_bold(text, delay=0.1):
    """Prints text in bold with a typing effect"""
    console.print(text, style="bold", end='', flush=True)
    time.sleep(delay)
    print()

def check_password():
    password = "ALEX KHAN"
    attempts = 3

    while attempts > 0:
        print_stylish_line() 
        entered_password = input(Style.BRIGHT + Fore.YELLOW + "[•] ENTER PASSWORD ▶ ")
        if entered_password == password:
            print(Style.BRIGHT + Fore.GREEN + "[✓] Password correct! Proceeding...")
            print_stylish_line()
            return True
        else:
            attempts -= 1
            print(Style.BRIGHT + Fore.RED + f"[✗] Incorrect password! You have {attempts} attempts left.")
            print_stylish_line()

    print(Style.BRIGHT + Fore.RED + "[✗] Too many incorrect attempts. Exiting")
    print_stylish_line()
    sys.exit(1)
   
def banner():
    # Clear screen
    os.system("clear" if os.name == "posix" else "cls")

    # Generate ASCII text
    try:
        import pyfiglet
        text = pyfiglet.figlet_format("AUTO  FB", font="epic")
    except ImportError:
        text = """
  _    _           ____   _____   _          _ _ 
 | |  | |         |  _ \\ |  __ \\ | |        | | |
 | |__| | __ _ ___| |_) || |__) || |__   ___| | |
 |  __  |/ _` / __|  _ < |  ___/ | '_ \\ / _ \\ | |
 | |  | | (_| \\__ \\ |_) || |     | |_) |  __/ | |
 |_|  |_|\\__,_|___/____/ |_|     |_.__/ \\___|_|_|
        """

    # Color palette
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
        Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
    ]

    # Print each character with random color and immediate reset
    for line in text.splitlines():
        for ch in line:
            if ch.strip() == "":
                print(" ", end="")
            else:
                color = random.choice(colors)
                print(Style.BRIGHT + color + ch + Style.RESET_ALL, end="")
        print()
        time.sleep(0.02)
        
# Unicode Bold Text Converter
def bold_unicode(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    bold = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    return ''.join(bold[normal.index(c)] if c in normal else c for c in text)
       
def print_stylish_line():
    """Prints a bright, stylish line."""
    console.print("[bold cyan]━" * 64 + "[/bold cyan]")

def ____useragent____():
    version = random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model = random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9','Reno 9 A','Reno 9 Pro','Reno 9 Pro+','Reno A','Reno Ace','Reno Ace 2','Reno K3','Reno Z','Reno10','Reno11','Reno2','RENO3','Reno4','Reno5','Reno8','Reno9','RX17 Neo','S1','S17','S3','S4','T29','Ulike 2','V5','V8821','Watch 2 46mm','Watch 41mm','Watch 46mm','X','x20','x22','X50Pro','X54','X9017','X907','Y15','Y21','Y3','Z1'])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''

#_________|EXTRACTOR|_________#
def extractor(data):
    try:
        soup = BeautifulSoup(data, "html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error": str(e)}

#_________|FAKE EMAIL|_________#
def GetEmail():
    try:
        # Use 1secmail - more reliable
        domain = random.choice(['1secmail.com', '1secmail.org', '1secmail.net'])
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        email = f"{username}@{domain}"
        print(Style.BRIGHT + Fore.CYAN + f"[✓] Email generated: {email}" + Style.RESET_ALL)
        return email
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"[✗] Error generating email: {e}" + Style.RESET_ALL)
        return None

#_________|FAKE EMAIL CODE|_________#
def GetCode(email):
    try:
        username, domain = email.split('@')
        
        for attempt in range(20):
            try:
                response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}', timeout=10)
                if response.status_code == 200:
                    messages = response.json()
                    if messages:
                        for msg in messages:
                            if 'FB-' in msg.get('subject', '') or 'Facebook' in msg.get('from', '') or 'FB-' in msg.get('subject', '').upper():
                                msg_response = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={msg["id"]}', timeout=10)
                                if msg_response.status_code == 200:
                                    content = msg_response.text
                                    patterns = [
                                        r'FB-(\d{6})',
                                        r'code\s*[is:]+\s*(\d{6})',
                                        r'verification\s*code\s*[is:]+\s*(\d{6})',
                                        r'(\d{6})'
                                    ]
                                    for pattern in patterns:
                                        match = re.search(pattern, content, re.IGNORECASE)
                                        if match:
                                            code = match.group(1)
                                            print(Style.BRIGHT + Fore.GREEN + f"[✓] Code found: {code}" + Style.RESET_ALL)
                                            return code
                time.sleep(3)
            except:
                pass
        return None
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"[✗] Error getting code: {e}" + Style.RESET_ALL)
        return None

# ================= COLORS =================
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"

BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"

RESET      = "\033[0m"
BOLD       = "\033[1m"
DIM        = "\033[2m"
ITALIC     = "\033[3m"
UNDERLINE  = "\033[4m"
BLINK      = "\033[5m"
REVERSE    = "\033[7m"
HIDDEN     = "\033[8m"

RESET_BOLD      = "\033[21m"
RESET_DIM       = "\033[22m"
RESET_UNDERLINE = "\033[24m"
RESET_BLINK     = "\033[25m"
RESET_REVERSE   = "\033[27m"
RESET_HIDDEN    = "\033[28m"

def print_developer_info():
    print(
        f"{Style.BRIGHT}{CYAN}╭━━━━━━━━━━━━━━━━━━━━━━ -- {bold_unicode('TOOL INFO')} -- ━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"{Style.BRIGHT}{CYAN}┃{RESET}{Style.BRIGHT}{GREEN} {bold_unicode('[•] Developer')}  ▶  {GREEN}{bold_unicode('SahiiL  '):<23}                    {Style.BRIGHT}{CYAN}┃\n"
        f"{Style.BRIGHT}{CYAN}┃{RESET}{Style.BRIGHT}{GREEN} [•] {bold_unicode('Giithub')}    ▶  {GREEN}{bold_unicode('Darkstar xd'):<23}                {Style.BRIGHT}{CYAN}    ╯\n"
        f"{Style.BRIGHT}{CYAN}┃{RESET}{Style.BRIGHT}{GREEN} [•] {bold_unicode('Team ')}      ▶  {GREEN}{bold_unicode('Darkstar '):<23}                    {Style.BRIGHT}{CYAN}╮\n"
        f"{Style.BRIGHT}{CYAN}┃{RESET}{Style.BRIGHT}{GREEN} [•] {bold_unicode('Tool')}       ▶  {GREEN}{bold_unicode('Fb Auto Account Creator'):<22}                    {Style.BRIGHT}{CYAN}┃\n"        
        f"{Style.BRIGHT}{CYAN}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯{RESET}"
    )

#_________|MENU|_________#
def poco():
    print(Style.BRIGHT + Fore.CYAN + "╭━━━━━━━━━━━━━━━━━━━━━━━━ < MENU > ━━━━━━━━━━━━━━━━━━━━━━━╮" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "┃ " + Style.BRIGHT + Fore.GREEN + "[1] Start".ljust(56) + Style.BRIGHT + Fore.CYAN + "┃" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "┃ " + Style.BRIGHT + Fore.RED + "[2] Exit".ljust(56) + Style.BRIGHT + Fore.CYAN + "┃" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.CYAN + "╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯" + Style.RESET_ALL)

    print_stylish_line()

    choice = input(Style.BRIGHT + Fore.WHITE + "[?] Choose an option ▶ " + Style.RESET_ALL).strip()

    print_stylish_line()

    if choice == "1":
        ____create____()
    elif choice == "2":
        print(Style.BRIGHT + Fore.RED + "Exiting... Goodbye!" + Style.RESET_ALL)
        exit()
    else:
        print(Style.BRIGHT + Fore.RED + "Invalid choice!" + Style.RESET_ALL)
        return poco()
        
#_________|MODULE|_________#
def progres(current, num_accounts, delay):
    for _ in range(int(delay), 0, -1):
        print(Style.BRIGHT + Fore.GREEN + f"\r-[CREATE-START]-[{current}/{num_accounts}]-[OK:{len(oks)}]-[CP:{len(cps)}]" + Style.RESET_ALL, end="")
        time.sleep(1)
        
#_________|CREATE|_________#
def ____create____():
    global oks, cps
    print(Style.BRIGHT + Fore.CYAN + "[━] EXAMPLE : Eriix , Eren , Hiitler , Sahiil" + Style.RESET_ALL)
    print_stylish_line()
    firstname = input(Style.BRIGHT + Fore.WHITE + "ENTER FIRST NAME : " + Style.RESET_ALL)
    print_stylish_line()

    print(Style.BRIGHT + Fore.CYAN + "[━] EXAMPLE : Oīīx | Ewxo | Xwd | Khan" + Style.RESET_ALL)
    print_stylish_line()
    lastname = input(Style.BRIGHT + Fore.WHITE + "ENTER LAST NAME : " + Style.RESET_ALL)
    print_stylish_line()

    print(Style.BRIGHT + Fore.CYAN + "[━] EXAMPLE : 5000 , 1000 , 7777 , 9999" + Style.RESET_ALL)
    print_stylish_line()
    num_accounts = int(input(Style.BRIGHT + Fore.WHITE + "[+] ENTER LIMIT : " + Style.RESET_ALL))
    print_stylish_line()

    print(Style.BRIGHT + Fore.CYAN + "[━] EXAMPLE : 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8" + Style.RESET_ALL)
    print_stylish_line()
    delay = int(input(Style.BRIGHT + Fore.WHITE + "ENTER BETWEEN TIME : " + Style.RESET_ALL))
    print(Style.BRIGHT + Fore.GREEN + f"TOTAL CREATE LIMIT : {num_accounts}" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "IF NO RESULT, TURN AIRPLANE MODE ON / OFF" + Style.RESET_ALL)
    print_stylish_line()
    
    for make in range(int(num_accounts)):
        print(Style.BRIGHT + Fore.GREEN + f"\n-[CREATE-START]-[{make + 1}/{num_accounts}]-[OK:{len(oks)}]-[CP:{len(cps)}]" + Style.RESET_ALL)
        
        ses = requests.Session()
        
        try:
            print(Style.BRIGHT + Fore.CYAN + "[1/4] Getting registration page..." + Style.RESET_ALL)
            response = ses.get(
                url='https://mbasic.facebook.com/reg',
                params={"_rdr":""},
                headers={"User-Agent": ____useragent____()},
                timeout=30
            )
            
            print(Style.BRIGHT + Fore.CYAN + "[2/4] Extracting form data..." + Style.RESET_ALL)
            formula = extractor(response.text)
            
            print(Style.BRIGHT + Fore.CYAN + "[3/4] Generating email..." + Style.RESET_ALL)
            email2 = GetEmail()
            
            if not email2:
                print(Style.BRIGHT + Fore.RED + "[✗] Failed to generate email. Skipping..." + Style.RESET_ALL)
                continue
            
            password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%', k=12))
            
            print(Style.BRIGHT + Fore.CYAN + "[4/4] Submitting registration..." + Style.RESET_ALL)
            payload = {
                'lsd': formula.get('lsd', ''),
                'jazoest': formula.get('jazoest', ''),
                'fb_dtsg': formula.get('fb_dtsg', ''),
                'firstname': firstname,
                'lastname': lastname,
                'reg_email__': email2,
                'reg_email_confirmation__': email2,
                'reg_passwd__': password,
                'sex': '2',
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1992,2009)),
                'ref': 'https://mbasic.facebook.com',
                'referrer': '',
            }
            
            headers = {
                "User-Agent": ____useragent____(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://mbasic.facebook.com",
                "Referer": "https://mbasic.facebook.com/reg",
            }
            
            reg_response = ses.post(
                'https://mbasic.facebook.com/reg/',
                data=payload,
                headers=headers,
                timeout=30,
                allow_redirects=False
            )
            
            cookies = ses.cookies.get_dict()
            if 'c_user' in cookies:
                uid = cookies['c_user']
                print(Style.BRIGHT + Fore.GREEN + f"\n[✓] Account created successfully! UID: {uid}" + Style.RESET_ALL)
                print(Style.BRIGHT + Fore.CYAN + f"[✓] Email: {email2}" + Style.RESET_ALL)
                print(Style.BRIGHT + Fore.CYAN + f"[✓] Password: {password}" + Style.RESET_ALL)
                
                print(Style.BRIGHT + Fore.YELLOW + "[⏳] Waiting for verification code..." + Style.RESET_ALL)
                valid = GetCode(email2)
                
                if valid:
                    print(Style.BRIGHT + Fore.GREEN + f"[✓] Verification code: {valid}" + Style.RESET_ALL)
                    confirm_result = confirm_id(email2, uid, valid, ses)
                    
                    if confirm_result:
                        cookie_str = ";".join([f"{k}={v}" for k, v in cookies.items()])
                        print(Style.BRIGHT + Fore.GREEN + f"\n-[DARKSTAR-OK] {uid} | {password}" + Style.RESET_ALL)
                        print_stylish_line()
                        
                        output_dir = os.path.expanduser('~')
                        output_file = os.path.join(output_dir, 'DARKSTAR-AUTO-CRATE-OK-ID.txt')
                        with open(output_file, 'a') as f:
                            f.write(f"{uid}|{password}|{cookie_str}|{email2}\n")
                        
                        oks.append(uid)
                    else:
                        print(Style.BRIGHT + Fore.YELLOW + "[⚠] Account created but verification may be pending" + Style.RESET_ALL)
                        cookie_str = ";".join([f"{k}={v}" for k, v in cookies.items()])
                        output_dir = os.path.expanduser('~')
                        output_file = os.path.join(output_dir, 'DARKSTAR-AUTO-CRATE-OK-ID.txt')
                        with open(output_file, 'a') as f:
                            f.write(f"{uid}|{password}|{cookie_str}|{email2}|PENDING\n")
                        oks.append(uid)
                else:
                    print(Style.BRIGHT + Fore.RED + "[✗] No verification code received" + Style.RESET_ALL)
                    print(Style.BRIGHT + Fore.YELLOW + f"[!] Account created but needs manual verification" + Style.RESET_ALL)
                    print(Style.BRIGHT + Fore.YELLOW + f"[!] Email: {email2}" + Style.RESET_ALL)
                    print(Style.BRIGHT + Fore.YELLOW + f"[!] Password: {password}" + Style.RESET_ALL)
                    cookie_str = ";".join([f"{k}={v}" for k, v in cookies.items()])
                    output_dir = os.path.expanduser('~')
                    output_file = os.path.join(output_dir, 'DARKSTAR-AUTO-CRATE-OK-ID.txt')
                    with open(output_file, 'a') as f:
                        f.write(f"{uid}|{password}|{cookie_str}|{email2}|MANUAL\n")
                    oks.append(uid)
            else:
                print(Style.BRIGHT + Fore.RED + "[✗] Account creation failed - no c_user cookie" + Style.RESET_ALL)
                output_dir = os.path.expanduser('~')
                output_file = os.path.join(output_dir, 'DARKSTAR-FAILED.txt')
                with open(output_file, 'a') as f:
                    f.write(f"FAILED|{email2}|{password}|{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                cps.append(email2)
                
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + f"[✗] Error: {e}" + Style.RESET_ALL)
            import traceback
            traceback.print_exc()
            continue
        
        if delay > 0 and make < num_accounts - 1:
            time.sleep(delay)

#_________|CONFIRM ID|_________#
def confirm_id(mail, uid, otp, ses):
    try:
        print(Style.BRIGHT + Fore.CYAN + "[⏳] Confirming email..." + Style.RESET_ALL)
        
        confirm_urls = [
            f'https://mbasic.facebook.com/confirmemail.php?next=%2F&ref=dbl',
            f'https://mbasic.facebook.com/a/confirmemail.php',
        ]
        
        for url in confirm_urls:
            try:
                response = ses.get(url, timeout=30)
                formula = extractor(response.text)
                
                payload = {
                    'lsd': formula.get('lsd', ''),
                    'jazoest': formula.get('jazoest', ''),
                    'fb_dtsg': formula.get('fb_dtsg', ''),
                    'code': otp,
                    'submit': 'Confirm',
                }
                
                confirm_response = ses.post(
                    url,
                    data=payload,
                    headers={"User-Agent": ____useragent____()},
                    timeout=30
                )
                
                if confirm_response.status_code == 200 and 'checkpoint' not in confirm_response.url:
                    print(Style.BRIGHT + Fore.GREEN + "[✓] Email confirmed successfully!" + Style.RESET_ALL)
                    return True
                    
            except Exception as e:
                print(Style.BRIGHT + Fore.YELLOW + f"[⚠] Confirmation attempt failed: {e}" + Style.RESET_ALL)
                continue
        
        return False
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"[✗] Error confirming account: {e}" + Style.RESET_ALL)
        return False

def main():
    banner()
    print_developer_info()
    print_stylish_line() 
    print_stylish_line()    
    
    if not check_password():
        return
    
    print_stylish_line()
    
    poco()
    
def clear_screen():
    """Clears the screen"""
    os.system("clear" if os.name == "posix" else "cls")
        
#_________|END|_________#
if __name__ == '__main__':
    main()