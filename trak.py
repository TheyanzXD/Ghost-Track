#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import time
import os
import phonenumbers
import hashlib
import socket
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
# --- Import inquirer untuk menu ---
import inquirer

# Warna untuk tampilan
Bl = '\033[30m'  # Black
Re = '\033[1;31m'  # Red
Gr = '\033[1;32m'  # Green
Ye = '\033[1;33m'  # Yellow
Blu = '\033[1;34m'  # Blue
Mage = '\033[1;35m'  # Magenta
Cy = '\033[1;36m'  # Cyan
Wh = '\033[1;37m'  # White
Rs = '\033[0m'     # Reset

def clear():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    """Menampilkan banner utama"""
    clear()
    print(f"""
{Gr}       ________               __      ______                __
{Gr}      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
{Gr}     / / __/ __ \\/ __ \\/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
{Gr}    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,< 
{Gr}    \\____/_/ /_/\\____/____/\\__/     /_/ /_/   \\__,_/\\___/_/|_|{Wh}
              [ + ]  C O D E   B Y  Y A N X X D  [ + ]
    """)

def run_banner():
    """Menampilkan banner sebelum setiap fungsi"""
    clear()
    time.sleep(0.5)
    print(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o    `.        {Wh}|       {Gr}@CODE BY YANZXD      {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)

def is_option(func):
    """Decorator untuk menampilkan banner sebelum menjalankan fungsi"""
    def wrapper(*args, **kwargs):
        run_banner()
        return func(*args, **kwargs)
    return wrapper

@is_option
def IP_Track():
    """Melacak informasi dari alamat IP"""
    try:
        ip = input(f"{Wh}\n Enter IP target : {Gr}").strip()
        if not ip:
            print(f"{Re}Error: IP address cannot be empty.{Rs}")
            return
        print()
        print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
        response = requests.get(f"http://ipwho.is/{ip}", timeout=10)
        if response.status_code != 200:
            print(f"{Re}Error: Unable to fetch data. Status code: {response.status_code}{Rs}")
            return
        ip_data = response.json()
        # Validasi data yang diterima
        if not ip_data.get('success', True):
            print(f"{Re}Error: {ip_data.get('message', 'Unknown error')}{Rs}")
            return
        time.sleep(1)
        print(f"{Wh}\n IP target       :{Gr} {ip}")
        print(f"{Wh} Type IP         :{Gr} {ip_data.get('type', 'N/A')}")
        print(f"{Wh} Country         :{Gr} {ip_data.get('country', 'N/A')}")
        print(f"{Wh} Country Code    :{Gr} {ip_data.get('country_code', 'N/A')}")
        print(f"{Wh} City            :{Gr} {ip_data.get('city', 'N/A')}")
        print(f"{Wh} Continent       :{Gr} {ip_data.get('continent', 'N/A')}")
        print(f"{Wh} Continent Code  :{Gr} {ip_data.get('continent_code', 'N/A')}")
        print(f"{Wh} Region          :{Gr} {ip_data.get('region', 'N/A')}")
        print(f"{Wh} Region Code     :{Gr} {ip_data.get('region_code', 'N/A')}")
        print(f"{Wh} Latitude        :{Gr} {ip_data.get('latitude', 'N/A')}")
        print(f"{Wh} Longitude       :{Gr} {ip_data.get('longitude', 'N/A')}")
        lat = ip_data.get('latitude')
        lon = ip_data.get('longitude')
        if lat and lon:
            try:
                lat_int = int(float(lat))
                lon_int = int(float(lon))
                print(f"{Wh} Maps            :{Gr} https://www.google.com/maps/@{lat_int},{lon_int},8z")
            except (ValueError, TypeError):
                print(f"{Wh} Maps            :{Gr} N/A")
        else:
            print(f"{Wh} Maps            :{Gr} N/A")
        print(f"{Wh} EU              :{Gr} {ip_data.get('is_eu', 'N/A')}")
        print(f"{Wh} Postal          :{Gr} {ip_data.get('postal', 'N/A')}")
        print(f"{Wh} Calling Code    :{Gr} {ip_data.get('calling_code', 'N/A')}")
        print(f"{Wh} Capital         :{Gr} {ip_data.get('capital', 'N/A')}")
        print(f"{Wh} Borders         :{Gr} {ip_data.get('borders', 'N/A')}")
        flag_data = ip_data.get('flag', {})
        print(f"{Wh} Country Flag    :{Gr} {flag_data.get('emoji', 'N/A')}")
        connection_data = ip_data.get('connection', {})
        print(f"{Wh} ASN             :{Gr} {connection_data.get('asn', 'N/A')}")
        print(f"{Wh} ORG             :{Gr} {connection_data.get('org', 'N/A')}")
        print(f"{Wh} ISP             :{Gr} {connection_data.get('isp', 'N/A')}")
        print(f"{Wh} Domain          :{Gr} {connection_data.get('domain', 'N/A')}")
        timezone_data = ip_data.get('timezone', {})
        print(f"{Wh} ID              :{Gr} {timezone_data.get('id', 'N/A')}")
        print(f"{Wh} ABBR            :{Gr} {timezone_data.get('abbr', 'N/A')}")
        print(f"{Wh} DST             :{Gr} {timezone_data.get('is_dst', 'N/A')}")
        print(f"{Wh} Offset          :{Gr} {timezone_data.get('offset', 'N/A')}")
        print(f"{Wh} UTC             :{Gr} {timezone_data.get('utc', 'N/A')}")
        print(f"{Wh} Current Time    :{Gr} {timezone_data.get('current_time', 'N/A')}")
    except requests.exceptions.Timeout:
        print(f"{Re}Error: Request timed out.{Rs}")
    except requests.exceptions.RequestException as e:
        print(f"{Re}Error: {e}{Rs}")
    except json.JSONDecodeError:
        print(f"{Re}Error: Invalid JSON response.{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def phoneGW():
    """Melacak informasi dari nomor telepon"""
    try:
        user_phone = input(
            f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}"
        ).strip()
        if not user_phone:
            print(f"{Re}Error: Phone number cannot be empty.{Rs}")
            return
        # Parsing nomor telepon
        parsed_number = phonenumbers.parse(user_phone, "ID")
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{Re}Error: Invalid phone number format.{Rs}")
            return
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
            parsed_number, "ID", with_formatting=True
        )
        number_type = phonenumbers.number_type(parsed_number)
        timezone_list = timezone.time_zones_for_number(parsed_number)
        timezone_str = ', '.join(timezone_list)
        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Location             :{Gr} {location}")
        print(f" {Wh}Region Code          :{Gr} {region_code}")
        print(f" {Wh}Timezone             :{Gr} {timezone_str}")
        print(f" {Wh}Operator             :{Gr} {jenis_provider}")
        print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
        print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
        print(f" {Wh}International format :{Gr} {formatted_number}")
        print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(
            f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}"
        )
        print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
        else:
            print(f" {Wh}Type                 :{Gr} This is another type of number")
    except phonenumbers.NumberParseException as e:
        print(f"{Re}Error: Invalid phone number format - {e}{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def TrackLu():
    """Melacak keberadaan username di berbagai platform sosial"""
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}").strip()
        if not username:
            print(f"{Re}Error: Username cannot be empty.{Rs}")
            return
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "YouTube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://t.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        print(f"\n {Wh}Scanning username: {Gr}{username}{Wh}...")
        for site in social_media:
            url = site['url'].format(username)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    results[site['name']] = url
                else:
                    results[site['name']] = f"{Ye}Not found{Rs}"
            except requests.exceptions.RequestException:
                results[site['name']] = f"{Ye}Error connecting{Rs}"
        print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
        print()
        for site, result in results.items():
            status_color = Gr if "http" in result else Ye
            print(f" {Wh}[ {Gr}+ {Wh}] {site:<15} : {status_color}{result}{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def showIP():
    """Menampilkan IP publik pengguna"""
    try:
        response = requests.get('https://api.ipify.org/', timeout=10)
        if response.status_code == 200:
            user_ip = response.text
            print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
            print(f"\n {Wh}[ {Gr}+ {Wh}] Your IP Address : {Gr}{user_ip}")
        else:
            print(f"{Re}Error: Unable to fetch your IP address. Status code: {response.status_code}{Rs}")
    except requests.exceptions.Timeout:
        print(f"{Re}Error: Request timed out.{Rs}")
    except requests.exceptions.RequestException as e:
        print(f"{Re}Error: {e}{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

# --- Fungsi JOMOK48 Ditambahkan ---
@is_option
def ip_lookup_jomok():
    """Melakukan lookup informasi IP menggunakan API ip-api.com"""
    try:
        ip = input(f"{Wh}\nMasukkan IP Address atau Domain: {Gr}").strip()
        if not ip:
            print(f"{Re}Input kosong, batal.{Rs}")
            return
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=6).json()
        print(f"\n{Wh}=== {Gr}Hasil IP Lookup {Wh}===")
        for key, value in response.items():
            print(f"{Wh}{key.capitalize():15}: {Gr}{value}{Rs}")
    except requests.exceptions.Timeout:
        print(f"{Re}Error: Request timed out.{Rs}")
    except requests.exceptions.RequestException as e:
        print(f"{Re}Error: {e}{Rs}")
    except json.JSONDecodeError:
        print(f"{Re}Error: Invalid JSON response.{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def website_status_jomok():
    """Memeriksa status dan waktu respon website"""
    try:
        url = input(f"{Wh}\nMasukkan URL (contoh: https://google.com): {Gr}").strip()
        if not url:
            print(f"{Re}Input kosong, batal.{Rs}")
            return
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url
        start = time.time()
        res = requests.get(url, timeout=8)
        end = time.time()
        print(f"\n{Wh}=== {Gr}Hasil Pengecekan {Wh}===")
        print(f"{Wh}Status Code : {Gr}{res.status_code}{Rs}")
        print(f"{Wh}Waktu Respon: {Gr}{round(end - start, 3)} detik{Rs}")
    except requests.exceptions.Timeout:
        print(f"{Re}Website tidak dapat diakses (timeout)!{Rs}")
    except requests.exceptions.RequestException as e:
        print(f"{Re}Website tidak dapat diakses! Error: {e}{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def password_strength_jomok():
    """Menganalisis kekuatan password"""
    try:
        password = input(f"{Wh}\nMasukkan password: {Gr}")
        if password == "":
            print(f"{Re}Input kosong, batal.{Rs}")
            return
        score = 0
        if len(password) >= 8: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in "!@#$%^&*()_+-=[]{};':,.<>/?\\|" for c in password): score += 1

        levels = ["Sangat Lemah", "Lemah", "Sedang", "Kuat", "Sangat Kuat"]
        strength_text = levels[score]
        color = Gr if score >= 3 else Ye if score >= 2 else Re
        print(f"\n{Wh}Kekuatan Password: {color}{strength_text} ({score}/4){Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def port_scanner_jomok():
    """Melakukan scanning port umum pada target"""
    try:
        target = input(f"{Wh}\nMasukkan target (IP/Domain): {Gr}").strip()
        if not target:
            print(f"{Re}Input kosong, batal.{Rs}")
            return
        print(f"{Wh}\nScanning port umum (cepat)...{Rs}")
        open_ports = []
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            try:
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
            except Exception:
                pass # Abaikan error koneksi
            finally:
                sock.close()
        if open_ports:
            ports_str = ', '.join(map(str, open_ports))
            print(f"{Wh}Port terbuka: {Gr}{ports_str}{Rs}")
        else:
            print(f"{Wh}Tidak ada port umum yang terbuka.{Rs}")
    except socket.gaierror:
        print(f"{Re}Error: Hostname could not be resolved.{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")

@is_option
def hash_generator_jomok():
    """Menghasilkan hash MD5, SHA1, dan SHA256 dari teks"""
    try:
        text = input(f"{Wh}\nMasukkan teks yang akan di-hash: {Gr}")
        if text == "":
            print(f"{Re}Input kosong, batal.{Rs}")
            return
        print(f"\n{Wh}=== {Gr}Hash Hasil {Wh}===")
        print(f"{Wh}MD5   : {Gr}{hashlib.md5(text.encode()).hexdigest()}{Rs}")
        print(f"{Wh}SHA1  : {Gr}{hashlib.sha1(text.encode()).hexdigest()}{Rs}")
        print(f"{Wh}SHA256: {Gr}{hashlib.sha256(text.encode()).hexdigest()}{Rs}")
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
    except Exception as e:
        print(f"{Re}Unexpected error: {e}{Rs}")
# --- Akhir Fungsi JOMOK48 ---

# Definisi opsi menu - Diperbarui untuk menyertakan fungsi JOMOK48
options = [
    {'num': 1, 'text': 'IP Tracker      ', 'func': IP_Track},
    {'num': 2, 'text': 'Show Your IP', 'func': showIP},
    {'num': 3, 'text': 'Phone Number Tracker', 'func': phoneGW},
    {'num': 4, 'text': 'Username Tracker', 'func': TrackLu},
    {'num': 5, 'text': 'Domain Info Lookup       ', 'func': ip_lookup_jomok},
    {'num': 6, 'text': 'Website Status checker      ', 'func': website_status_jomok},
    {'num': 7, 'text': 'Password Strength       ', 'func': password_strength_jomok},
    {'num': 8, 'text': 'Port Open Scanner       ', 'func': port_scanner_jomok},
    {'num': 9, 'text': 'Hash Generator        ', 'func': hash_generator_jomok},
    {'num': 0, 'text': 'Exit', 'func': exit}
]

def display_menu():
    """Menampilkan banner utama"""
    banner()

def get_user_choice():
    """Mendapatkan pilihan pengguna menggunakan inquirer"""
    try:
        # Buat daftar pilihan untuk inquirer
        choices = [f"[{opt['num']}] {opt['text']}" for opt in options]
        questions = [inquirer.List('choice', message="Select Option", choices=choices, carousel=True)]
        answers = inquirer.prompt(questions)
        if answers is None: # Jika pengguna menekan Ctrl+C
            return 0
        selected_choice = answers['choice']
        # Ekstrak nomor dari pilihan yang dipilih
        selected_num = int(selected_choice.split(']')[0].replace('[', ''))
        return selected_num
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Exit{Rs}")
        return 0
    except Exception as e:
        print(f"{Re}Error getting user choice: {e}{Rs}")
        return None

def execute_choice(choice):
    """Menjalankan fungsi berdasarkan pilihan pengguna"""
    for opt in options:
        if opt['num'] == choice:
            if 'func' in opt:
                try:
                    opt['func']()
                    input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press Enter to continue...{Rs}')
                except KeyboardInterrupt:
                    print(f"\n{Wh}[ {Re}! {Wh}] {Re}Operation cancelled by user.{Rs}")
                    time.sleep(1)
            else:
                print('No function detected')
            return
    print(f"{Re}Error: Option not found.{Rs}")

def main():
    """Fungsi utama program"""
    while True:
        display_menu()
        choice = get_user_choice()
        if choice is None:
            time.sleep(1)
            continue
        if choice == 0:
            print(f"{Wh}[ {Gr}+ {Wh}] {Gr}Thank you for using Ghost Tracker!{Rs}")
            time.sleep(1)
            break
        if any(opt['num'] == choice for opt in options):
            execute_choice(choice)
        else:
            print(f"{Re}Error: Invalid option. Please select a valid option.{Rs}")
            time.sleep(2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Wh}[ {Re}! {Wh}] {Re}Exit{Rs}")
        time.sleep(1)