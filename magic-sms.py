import requests,sys, os, platform, random
from concurrent.futures import ThreadPoolExecutor
from cryptography.fernet import Fernet
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pyfiglet import Figlet


from colorama import init, Fore
init(autoreset=True)

greed = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
white = Fore.WHITE

if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Linux" and "kali" in platform.uname()[2]:
    os.system("clear")
    
#pyfiglet here
font = "standard"  # Replace with your desired font
text_to_display = "Magic-Sender"
fig = Figlet(font=font).renderText(text_to_display)
print(yellow+fig)
print(f"""
    {greed}Coded by Pop(G)
                {white}Blackcteam
                {greed}telegram:t.me/iampopg
""")

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()

def get_file_path(message):
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = askopenfilename(filetypes=[("Text Files", "*")],title=f"{message}")
    root.destroy()
    return file_path

def sms(number, encrypted_message):
    url = 'https://app.sms-magic.com/api/v1/sendListAsyncSmsMms'
    # with open('session.txt','r') as read:
    #     session = read.read()
    
        
    #4066331761
    if number.startswith('+'):
        number = number[1:]
    
    
    #magic panda cookies
    # print('here')
    with open('resources/magic_panda1.txt','r') as read:
        mAgic_pAnda = read.read()
        # print(len(mAgic_pAnda))
        input('')
        if len(mAgic_pAnda) == 0:
            input("Please put your cookies into 'magic_panda1' and try again")
            sys.exit()
        
    #magic panda2 cookies
    with open('resources/magic_panda2.txt','r') as read:
        mAgic_pAnda2 = read.read()
        # print(len(mAgic_pAnda2))
        if len(mAgic_pAnda2) == 0:
            input("Please put your cookies into 'magic_panda2' and try again")
            sys.exit()

    #magic sender id
    with open('resources/sender_id.txt','r') as read:
        sender_id = read.read()
        
    headers = {
        'Cookie': f'_ga=GA1.2.441484378.1701508331; _gid=GA1.2.1535000307.1701508331; _gcl_au=1.1.336062993.1701508335; _ga_CT8R28KJB3=GS1.2.1701508335.1.1.1701508516.60.0.0; _clck=v665j9%7C2%7Cfh7%7C0%7C1431; _clsk=kkvdb8%7C1701508403766%7C3%7C1%7Cq.clarity.ms%2Fcollect; __hstc=267168209.d247311fa2d1191b2ef997fbc763a7b8.1701508338578.1701508338578.1701508338578.1; hubspotutk=d247311fa2d1191b2ef997fbc763a7b8; __hssrc=1; __hssc=267168209.3.1701508338578; device_token=6obXq0fycgdoQjJbW0JNlxTppsF2Bg9CZ5PIHReBuAV9fZWzcIorVgd6jRNrgMnoWv4ZdVeWThqf8bOf2UXFrrZSMD+ynFKcVzAej0zcZQ1fd/tYV0NBbFdM96ljt4UTWprvE0Bj2nZaJYg67m886/GXiDRPSVBpmMfz3GLeIELc=; mAgIC_pAnDa={mAgic_pAnda}; mAgIC_r_pAnDa={mAgic_pAnda2}; apP_enV_nAmE=us-app; _gat_UA-46389882-3=1',    
        'User-Agent': 'Mozilla/5.0 (X11; Windows x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Content-Length': '134',
        'Origin': 'https://app.sms-magic.com',
        'Referer': f'https://app.sms-magic.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers'
        
    }
    payload = {
        "smstext": decrypt_message(encrypted_message),
        "mms_url_str": "",
        "sender_id": f"{sender_id}",
        "mobile_list": number,
        "subject": "",
        "campaign_id": 0
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print(response.text)
        print(greed + f'message sent succefully to {number}')
        print()
    elif response.status_code == 400:
        print(red + f'unable to send message to {number}')
        print(response.text)
        print()
    else:
        print(response.status_code)
        print(response.text)
        print()

def process_numbers(numbers, encrypted_message):
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(sms, number.strip(), encrypted_message) for number in numbers]

def run():
    if not os.path.exists('resources'):
        os.makedirs('resources')
        file_names = ['magic_panda1.txt', 'magic_panda2.txt', 'sender_id.txt']
        for file_name in file_names:
            file_path = os.path.join('resources', file_name)
            with open(file_path, 'w') as file:
                file.write(''.format(file_name))
                
    from time import sleep
    input("There will be a pop up to select number list first and message to send.. please ENTER to continue")
    print()
    n = "Selecet your NUMBER list"
    path = get_file_path(n)
    # sleep(1)
    m="Select your MESSAGE file"
    message_path = get_file_path(m)

    try:
        with open(message_path, 'r') as message_file:
            message = message_file.read()
            if len(message) == 0:
                input(red+ f"There is no Content inside {path}, put your Content and try again")
                sys.exit()

        encrypted_message = encrypt_message(message)

        with open(path, 'r') as numbers_file:
            numbers = numbers_file.readlines()
            if len(numbers) == 0:
                input(red+ f"There is no number inside {path}, put number to file and try again")
                sys.exit()


        process_numbers(numbers, encrypted_message)
        print()
        print('DONE')
        print(f"{yellow}[{len(numbers)}] sent successfully {white}== {red}[0] Not successful")
        # print(f"{red}ATT Network is not stable")

    except KeyboardInterrupt:
        print()
        print('bye')
        sys.exit()
    except FileNotFoundError as e:
        print("File not found, please try again")
    except TypeError:
        print("make sure you select the number file and message file")
        run()

run()