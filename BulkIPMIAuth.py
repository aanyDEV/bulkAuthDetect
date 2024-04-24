from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests  
import pandas as pd
from termcolor import colored
import re
import urllib3
import sys
# from bs4 import BeautifulSoup

def MEMS(enum1, c):
    user = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8"]
    passwd = ["passwd1", "passwd2", "passwd3", "passwd4", "passwd5", "passwd6", "passwd7", "passwd8"]#password dan user asli sudah tidak ditampakkan lagi
    
    ai = 0
    for cred1, cred2 in zip(user,passwd):
        devGigabyte = pd.read_csv('devDCIM.csv')
        lholho = devGigabyte.iloc[c].to_string(index=False)
        nama = lholho.split('\n')
        naaa = nama[0]
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_argument('--ignore-certificate-errors')
        options.set_capability('unhandledPromptBehavior', 'accept')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        chrome_driver = '/chromedriver_win32'
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(enum1)
        ai += 1
        print(colored(f"Tes Auth ke {ai}","cyan"))
        print("Target     :",naaa)
        print("IP         :",nakniknuk)
        time.sleep(3)
        sc = requests.get(driver.current_url)
        halaman = driver.page_source
        print(halaman)
        Gigabyte = re.search(r"MergePoint® Embedded Management Software",halaman)
        Supermicro = re.search(r"Please Login",halaman)
        Intel = re.search(r"../res/banner_left.png",halaman)
        Idrac8 = re.search(r"/images/Ttl_2_iDRAC7_Base_ML.png",halaman)
        # Idrac9 = re.search(r"Integrated Dell Remote Access Controller 9",halaman)
        if Gigabyte != None and sc.status_code == 200 :
            print("Manufacture: Gigabyte")
            try:
                lapo = driver.find_element(By.XPATH,'//input[@id=\'user\']')
                lapo.send_keys(cred1)
                
                lapo = driver.find_element(By.XPATH,'//input[@id=\'password\']')
                lapo.send_keys(cred2)
                
                lapo = driver.find_element(By.XPATH,'//a[@id=\'btnOK\']//span[1]')
                lapo.click()
                time.sleep(3)
                anjay = driver.current_url
                sc = requests.get(anjay)
                time.sleep(1)
                halaman = driver.page_source
                ngecek = re.search(r"Firmware Information", halaman)
                if ngecek == None and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                elif ngecek != None and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
                elif ngecek == None and sc.status_code != 200:
                    print(colored(f"Silahkan cek koneksi terlebih dahulu\n", "red"))
                else:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
            except requests.exceptions.ConnectionError:
                print(colored(f"Auth menggunakan akun {cred1} gagal", "red"))
            driver.quit()
        elif Supermicro != None and sc.status_code == 200:
            print("Manufacture: Supermicro")
            driver.get(enum1)
            try:
                lapo = driver.find_element(By.XPATH,'//input[@name=\'name\']')
                lapo.send_keys(cred1)
                
                lapo = driver.find_element(By.XPATH,'//input[@name=\'pwd\']')
                lapo.send_keys(cred2)
                
                lapo = driver.find_element(By.XPATH,'//input[@id=\'login_word\']')
                lapo.click()
                time.sleep(3)
                anjay = driver.current_url
                time.sleep(2)
                sc = requests.get(anjay)
                if anjay == enum1 and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                elif anjay != enum1 and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
                elif anjay == enum1 and sc.status_code != 200:
                    print(colored(f"Silahkan cek koneksi terlebih dahulu\n", "red"))
                else:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
            except requests.exceptions.ConnectionError:
                print(colored(f"Auth menggunakan akun {cred1} gagal", "red"))
            driver.quit()
        elif Idrac8 != None and sc.status_code == 200:
            print("Manufacture: Dell - IDRAC 8")
            driver.get(enum1)
            try:
                lapo = driver.find_element(By.XPATH,'//input[@id=\'user\']')
                lapo.send_keys(cred1)
                
                lapo = driver.find_element(By.XPATH,'//input[@id=\'password\']')
                lapo.send_keys(cred2)
                
                lapo = driver.find_element(By.XPATH,'//span[@id=\'submit_lbl\']')
                lapo.click()
                time.sleep(3)
                anjay = driver.current_url
                time.sleep(1)
                sc = requests.get(anjay)
                if anjay == enum1 and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                elif anjay != enum1 and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
                elif anjay == enum1 and sc.status_code != 200:
                    print(colored(f"Silahkan cek koneksi terlebih dahulu\n", "red"))
                else:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
            except requests.exceptions.ConnectionError:
                print(colored(f"Auth menggunakan akun {cred1} gagal", "red"))
            driver.quit()
        elif Intel != None and sc.status_code == 200:
            print("Manufacture: Intel")
            driver.get(enum1)
            # print(enum1)
            lapo = driver.find_element(By.XPATH,'//input[@id=\'login_username\']')
            lapo.send_keys(cred1)
            
            lapo = driver.find_element(By.XPATH,'//input[@id=\'login_password\']')
            lapo.send_keys(cred2)
            
            lapo = driver.find_element(By.XPATH,'//input[@id=\'LOGIN_VALUE_1\']')
            lapo.click()
            time.sleep(3)
            anjay = driver.current_url
            time.sleep(1)
            sc = requests.get(anjay)
            halaman = driver.page_source
            # print(halaman)
            # print(anjay)
            ngecek = re.search(r"../lib/eExt.js",halaman)
            if ngecek != None and sc.status_code == 200 and enum1 != anjay:
                print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
            elif ngecek == None and sc.status_code == 200 and enum == anjay:
                print(colored(f"Auth menggunakan akun {cred1} gagal1\n", "red"))
            elif ngecek == None and sc.status_code != 200:
                print(colored(f"Auth menggunakan akun {cred1} gagal2\n", "red"))
            else:
                print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
            driver.quit()

try: 
    urllib3.disable_warnings()
    urllib3.util.ssl_.DEFAULT_CIPHERS +=":!DH"
    i=0
    if i <= 119:
        ipDCIM = pd.read_csv('ipDCIM.csv')
        ip = ipDCIM.shape[0]
        for tektek in range(ip):
            alamat = ipDCIM.iloc[i]['target']
            i += 1
            print(colored("\n------------------------------------------------------------------------------","magenta"))
            print(colored(f"--------------------------------Tes Auth ke {i}--------------------------------","yellow"))
            if pd.notnull(alamat):
                tektek = alamat.split(',')
                try:
                    for url in tektek:
                        url = url.strip()
                        url2 = "http://" + str(url) + "/"
                        url3 = "https://"+ str(url) + "/"
                        nakniknuk = url
                        # try:
                        sc = requests.get(url2, verify=False, timeout=20)
                        if sc.status_code == 200 :
                            enum = url2
                            MEMS(enum, i)
                            print(enum)
                        else:
                            sc = requests.get(url3, verify=False, timeout=20)
                            if sc.status_code == 200 :
                                enum = url3
                                print(enum)
                                MEMS(enum, i)
                except requests.exceptions.ConnectionError:
                    user = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8"]
                    passwd = ["passwd1", "passwd2", "passwd3", "passwd4", "passwd5", "passwd6", "passwd7", "passwd8"]#password dan user asli sudah tidak ditampakkan lagi
                    sc = requests.get(enum)
                    if sc.status_code == 200:
                        for cred1, cred2 in zip(user,passwd):
                            options = webdriver.ChromeOptions()
                            # options.add_argument('--headless')
                            options.add_argument('--silent')
                            options.add_argument('--log-level=3')
                            options.add_argument('--ignore-certificate-errors')
                            options.set_capability('unhandledPromptBehavior', 'accept')
                            options.add_experimental_option('excludeSwitches', ['enable-logging'])
                            prefs = {"profile.default_content_setting_values.notifications": 2}
                            options.add_experimental_option("prefs", prefs)
                            chrome_driver = '/chromedriver_win32'
                            driver = webdriver.Chrome(chrome_driver, options=options)
                            driver.get(enum)
                            
                            if driver.current_url == enum+"restgui/start.html" and sc.status_code == 200:
                                print("Manufacture: Dell - IDRAC 9")
                                driver.get(enum)
                                lapo = driver.find_element(By.XPATH,'//input[@name=\'username\']')
                                lapo.send_keys(cred1)
                                
                                lapo = driver.find_element(By.XPATH,'//input[@name=\'password\']')
                                lapo.send_keys(cred2)
                                
                                lapo = driver.find_element(By.XPATH,'//button[@type=\'submit\']')
                                lapo.click()
                                time.sleep(3)
                                anjay = driver.current_url
                                time.sleep(1)
                                print(enum)
                                print(anjay)
                                sc = requests.get(anjay)
                                if anjay == enum and sc.status_code == 200:
                                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                                elif anjay != enum+"restgui/start.html" and sc.status_code == 200:
                                    print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
                                elif anjay == enum and sc.status_code != 200:
                                    print(colored(f"Silahkan cek koneksi terlebih dahulu\n", "red"))
                                else:
                                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                                driver.quit()
                            else:
                                print(f"\n{nakniknuk}")
                                print(colored("IP tidak bisa di kunjungi bosqiuu :V\n","red"))
                    else:
                        print(f"\n{nakniknuk}")
                        print(colored("IP tidak bisa di kunjungi bosqiuu :V\n","red"))
            continue
    else:
        print("\nAuth Sudah bosquee :*\n")
        sys.exit()
except KeyboardInterrupt:
    print("\nProses dicancel, program auto bongkeng bosquee :V\n")