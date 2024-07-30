a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
import os, re, random, uuid, subprocess, requests, sys, time, json, string
from os import system
libraries_to_install = ['random', 'uuid', 'subprocess', 'requests', 'time', 'json', 'string']
[exec(f"import {lib}") if lib not in sys.modules else None for lib in libraries_to_install]
try:
	import mechanize
	moetez_folder = mechanize.Browser()
	moetez_folder.set_handle_robots(False)
	moetez_folder.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
 
def MOETEZ(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def back():
    main_menu()
def linex():
	ge0=0
G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"
pemisah = '|'
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m" 
def find_txt_file(file_path):
    user_dir, user_file = os.path.split(file_path)

    if os.path.exists(file_path) and file_path.lower().endswith('.txt'):
        return file_path
    parent_dir = os.path.dirname(user_dir)
    for root, dirs, files in os.walk(parent_dir):
        for name in files:
            if name.lower() == user_file.lower() and name.lower().endswith('.txt'):
                corrected_path = os.path.join(root, name)
                return corrected_path

    return None

def remove_duplicates_in_place(file_path):
    try:
        corrected_path = find_txt_file(file_path)

        if corrected_path:
            lines_seen = set()
            with open(corrected_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                file.seek(0)
                file.truncate()

                for line in lines:
                    if line.strip() not in lines_seen:
                        file.write(line)
                        lines_seen.add(line.strip())
            print(f"{a1}[{a3}√{a1}] {a5}𝗱𝗲𝗹𝗲𝘁𝗲𝗱")
        else:
            print(f"{a1}[{a3}×{a1}] {a5}𝘄𝗿𝗼𝗻𝗴 𝗽𝗮𝘁𝗵")
    except Exception as e:
        print(f"خطأ: {e}")
class login():
	def __init__(self):
		ids=[]
	def lo_epa(self):
		system('clear')
		print(a1+'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠤⠤⡤⠤⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢔⠲⠈⠉⠀⠀⠀⠀⡸⠀⠀⠈⣿⣿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⡡⠄⠀⠀⠀⠀⠀⠈⠀⠀⢇⠀⠀⠀⣿⣿⣿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠎⢀⣡⠴⠒⠈⠉⠉⢉⣩⣿⣶⣦⣄⡀⠀⡆⠀⠀⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣴⠉⠀⢀⠖⠉⠉⠙⠿⣿⣿⣿⣿⣿⣿⣷⣼⡀⠀⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣄⣴⠏⠀⠀⠀⠀⠀⠙⣿⣿⣿⡿⠿⠛⠁⡇⠀⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡹⠛⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⢀⡔⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣿⣿⣿⣿⠀
⠀⠀⢀⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⣿⣿⣿⣿⠀
⠀⠠⡃⢠⡤⠤⣀⣀⣀⡀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⣿⣿⣿⣿⠀
⠀⠀⠑⢼⣧⣀⣴⣿⣿⣿⣿⣷⣦⣄⠇⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⣿⣿⣿⣿⡇
⠀⠀⠀⣼⢠⠀⠈⠍⠉⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⢀⡇⢠⠀⠀⣿⣿⣿⣿⢇
⠀⠀⠀⡏⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣶⣤⣷⣶⣿⣿⣿⠏⠀
⠀⠀⢸⠇⢀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡟⠉⠃⠀⠀
⠀⠀⢸⠀⡇⠮⣀⣀⣤⣤⣭⣽⣿⣄⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⡇⠰⠐⠲⠾⠿⠿⠿⠿⠟⠛⠛⠋⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⢸⢁⠇⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠏⠸⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⢸⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
⠀⠑⠢⠤⠀⠀⠀⠀⠀⠒⣄⣀⠠⠶⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡜⢠⠃⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⠁⠈⠀⠀⠀⠀⣤⣶⣿⡿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠒⠒⠂⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
		print(f"{a40}✦"*60)
		em = str(input(f"{a18}𝗲𝗻𝘁𝗲𝗿{a4}𝘆𝗼𝘂𝗿 {a40}𝗳𝗮𝗰𝗲 {a3}𝗮𝗰𝗰𝗼𝗻𝘁 :"))
		linex()
		print(f'{a40}✦'*60)
		linex()
		ps = input(f'{a36}𝘆𝗼𝘂𝗿 {a18}𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 {a16}𝗮𝗰𝗰𝗼𝘂𝗻𝘁  :')
		linex()
		e="5990"
		ee="655"
		eee="59"
		tok1 = f"2377{e}9{eee}1{ee}"
		ei="0f140aabedfb65"
		ei2="a2263b1"
		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
		moetez_folder.addheaders = [('User-Agent', us)]
		li = "b-ap"
		lo = "od/auth.l"
		op="3f555f98"
		op2 = "d7aa0c"
		op3="58f522efm"
		sig=f"{op}fb61fc{op2}44f{op3}"
		p = moetez_folder.open(
			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
		po = json.load(p)
		if 'access_token' in po:
			toke=po['access_token']
			linex()
			print(f"{a40}✦"*60)
			MOETEZ(f'{a1}[{a3}√{a1}] {a5}𝗱𝗼𝗻𝗲 𝗻𝗼𝘄 𝗿𝗲𝘀𝘁 𝘁𝗵𝗲 𝘁𝗼𝗼𝗹 ✦')
			linex()
			open('.token.txt','w').write(toke)
			exit()
		else:
			if 'www.facebook.com' in po['error_msg']:
				print('WAIT......')
				exit(em+'|'+ps)
			else:
				linex()
				exit(f'{a1}[{a3}×{a1}] {a5}𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗲𝗻𝘁𝗲𝗿𝗲𝗱 𝘄𝗿𝗼𝗻𝗴 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻  •')
	def login_epa2(self):
		system('clear');
		print(logo)
		cooke = input(' cookie : ')
		cookie = {'Cookie': cooke}
		xyz = requests.session()
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
		req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
		cd = req['code']
		ucd = req['user_code']
		url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
			cd)
		req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
		raq = req.find('form', {'method': 'post'})
		dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
			   'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
			   'user_code': ucd}
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		dat = {}
		raq = pos.find('form', {'method': 'post'})
		for x in raq('input', {'value': True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']: x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		req = xyz.get(url, cookies=cookie).json()
		if 'access_token' in req:
			print(f' [{B}•{W}] LOGIN DONE RERUN ')
			open('.token.txt', 'w').write(req['access_token'])
			exit()
		else:
			exit('WRONG')
	def login_WALA(self):
		system('clear')
		
		
		linex()
		menu =('1')
		if menu in ['01', '1', 'A', 'a']:
			login().lo_epa()
		if menu in ['461918']:
			login().login_epa2()
		
		else:
			linex()
			MOETEZ('YOUR CHOSE IS WRONG')
			time.sleep(1)
			login_WALA()

def main_menu():
	os.system("clear")
	
	from pyfiglet import Figlet as F; from random import choice as c; print("\033[92m" + F(c(["isometric1", "isometric2"])).renderText("MOETEZ"))
	logo =                                          """   
\033[1;92m༄Mr.᭄\x1b[1;90m═══════════════════════════════════════════════\x1b[1;92m༄MOETEZ᭄
\033[1;92m༄Mr.᭄\x1b[1;90m═══════════════════════════════════════════════\x1b[1;92m༄MOETEZ᭄
                           \x1b[1;92m╔═════════════════════════════╗
                           \x1b[1;92m║➣TOOL NAME : [MAKE FILE]║
                           \x1b[1;92m║➣CHANNEL   : [𝗠َِ𝗼َِ𝗵َِ𝗮َِ𝗺َِ𝗺َِ𝗲َِ𝗱]    ║
                           \x1b[1;92m║➣TELEGRAM  : [V11Ul]       ║
                          \x1b[1;92m ║➣DEVELOPER : [MOETEZ] ║
                           \x1b[1;92m║➣Group     : [V11Ul]         ║
                           \x1b[1;92m║➣HOBBY     : [Hammadi 🐧]       ║
                           \x1b[1;92m╚═════════════════════════════╝
\033[1;92m༄Mr.᭄\x1b[1;90m═══════════════════════════════════════════════\x1b[1;92m༄MOETEZ᭄
\033[1;92m༄Mr.᭄\x1b[1;90m═══════════════════════════════════════════════\x1b[1;92m༄MOETEZ᭄
"""
	print(logo)
	print("")
	print(f"""{a5}╔═══════════════════╗    
║{a1}[{a3}1{a1}]{a5} 𝗰𝗿𝗲𝗮𝘁𝗲 𝗳𝗶𝗹𝗲 • 
║{a1}[{a3}2{a1}]{a5} 𝗰𝗵𝗮𝗻𝗴𝗲 𝗰𝗼𝗼𝗸𝗶𝗲𝘀 •
║{a1}[{a3}3{a1}]{a5} 𝗱𝗲𝗹𝗲𝘁𝗲 𝗱𝘂𝗽𝗹𝗶𝗰𝗮𝘁𝗲  𝗶𝗱𝘀 •
╚═══════════════════╝      """)
	xo = input(f'║{a1}[{a3}?{a1}]{a5} 𝗲𝗻𝘁𝗲𝗿 :')
	print("╚════════════════╝      ")
	if xo in ['1']:
		file_create_menu().file_unlimmited()
	if xo in ['2']:
		os.system('rm -rf .token.txt')
		linex()
	
		os.system('rm -rf .token.txt')
		linex()
		MOETEZ(f"{a1}[{a3}√{a1}] {a5}𝗰𝗼𝗼𝗸𝗶𝗲𝘀 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 • ")
		exit()
	if xo in ['3']:
		file_path = input(f"{a5}𝗳𝗶𝗹𝗲 𝗽𝗮𝘁𝗵 :")
		remove_duplicates_in_place(file_path)
	else:
		linex()
		MOETEZ(f'{a1}[{a3}×{a1}] {a5}𝘄𝗿𝗼𝗻𝗴 𝗰𝗵𝗼𝗶𝗰𝗲  •')
		time.sleep(1)
		main_menu()
siid=[]
sep=[]
 
class file_create_menu():
	def file_simple(self):
		os.system('clear');print(logo)
		try:
			print(f' [•] WRITE FILE NAME WITHOUT /sdcard ')
			nm  = input(f' [•] ENTER FILE NAME : ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			print(f' [×] LOCATION NOT FOUND TRY AGAIN !! ')
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			print(f' [•] PASTE UID ONE BY ONE ')
			linex()
			while True:
				ids_all = input(f" [>] ENTER UID : ")
				if ids_all == "":
					linex()
					print(f' [•] FILE SAVE AS : {lok} ')
					input(f' [>] PRESS ENTER TO BACK ')
					back()
					break
				try:
					uid = ids_all.split("|")[0]
				except:
					uid = ids_all
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth "+self.token+"",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' \033[1;35m SOMETHING WRONG WITH {uid}\033[0m ')
					if len(data) < 100:
						print(f' [×] PRIVATE FRIENDLIST OF {uid} ')
						linex()
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f' [•] SUCESSFULLY EXTRACTED {uid} [{total_idss}] \033[0m')
						linex()
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [×] CONNECTION ERROR - PRESS ENTER TO CONTINUE")
	def __init__(self):
		try:
			print('')
		except:
			pass
		self.ids = []
		self.total = []
		self.loop = 0
		try:
			self.token = open('.token.txt', 'r').read()
			uid="100061689760374"
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');print(logo)
				    os.system('.token.txt')
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;31m SOMETHING WRONG WITH THIS ID \033[0m ')
					os.system('.token.txt')
					exit()
			except Exception as e:
				os.system('clear');print(logo)
				print(f" [{B}×{W}] COOKIES EXPRIED !")
				print(e)
				login.login_WALA('')
		except Exception as e:
			print(e)
			login.login_WALA('')
	def file_unlimmited(self):
		os.system('clear')
		from pyfiglet import Figlet as F; from random import choice as c; print("\033[92m" + F(c(["slant"])).renderText("MOETEZ"))
		print("•" *60)
		limit = int("1")
		try:
			print(f"{a36}𝗲𝗻𝘁𝗲𝗿{a18} 𝘁𝗵𝗲{a4}  𝗳𝗶𝗹𝗲 {a3}𝗻𝗮𝗺𝗲 {a5}  𝘄𝗶𝘁𝗵 {a30}({a40}.txt{a30})       \n{a4}𝗳𝗼𝗿{a5} 𝗲𝘅𝗮𝗺𝗽𝗹𝗲 {a30}({a1}moetez.txt{a30})")
			nm  = input(f'{a30}[{a3}✓{a30}] {a36}𝗲𝗻??𝗲𝗿{a18} 𝘁𝗵𝗲{a4}  𝗳𝗶𝗹𝗲 {a3}𝗻𝗮𝗺𝗲 {a5} :').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			print(f'ENER THE FILE NAME WITH (.txt) ')
			time.sleep(1)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			os.system('clear')
			try:
				file = open('.temp.txt', 'r').read().splitlines()
			except:
				file = []
			os.system('clear')
			print(a1+'''⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀
⠀⠀⣠⣿⠿⠛⠛⠛⠛⠛⢿⣷⣤⣾⠿⠛⠛⠙⠛⠛⠿⠗⠀⠀⠀⠀
⠀⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠙⡿⠁⠀⢀⣤⣀⠀⠀⢀⣤⣶⡆⠀⠀
⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣧⣄⠀
⠀⢹⣿⠀⣿⣷⣄⣀⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷
⠀⠀⣁⣤⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠘⠛⠛⠛⠻⣿⣿⣿⠋⠉⠀⠀
⠀⠘⠻⢿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⢀⡀⠹⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣿⠟⢙⠛⠛⠀⠀⠀⠀⠀⣀⣴⡿⠓⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⠈⠻⢿⣦⣄⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
			print(f"{a40}✦"*60)
			for i in range(int(limit)):
				uid = input(f"{a5}𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗶𝗱 :".format(i+1))
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f'')
					if len(data) < 100:
						print('')
					else:
						for edge in data:
							node = edge['node']
							open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
							idss = len(open('.a.txt','r').readlines())
						print(f'[{idss}]\033[0m')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f"YOU HAVE BAD NET PRESS ENTER:")
			try:
				file = open('.a.txt', 'r').read().splitlines()
			except:
				file = [] 
			os.system('clear')
			print(f"{a40}✦"*60)
			print(f'{a1}[{a3}√{a1}] {a5}𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 ' + str(len(file))+' 𝗶𝗱𝘀')
			
			
			linex()
			for uid in file:
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						continue
					if len(data) < 100:
						continue
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						if 'y' in sep:
							perfector(lok)
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f'{a1}[{a3}√{a1}] {a5}𝗶𝗱 𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗲𝗱  ➩ {a1}({a3}{total_idss}{a1}) ')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					continue
			print('DONE'.format(lok))
			print('♕MOETEZ♕'.format(len(open(lok,'r').read().splitlines())))
main_menu()