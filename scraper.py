from tkinter import *
import os
import pandas as pd
import numpy as np
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from heapq import merge
import pandas as pd
import numpy as np
from selenium_stealth import stealth
import time
from selenium.webdriver.common.by import By
import random
from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from io import StringIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

import logging
import seleniumwire.undetected_chromedriver as uc
import undetected_chromedriver as undetectedChromedriver
import string
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from tkinter import *
from pandastable import Table, TableModel
import numpy as np
import sys 
import pandas as pd
import numpy as np
from PyPDF2 import PdfReader
import tkinter as tk
import threading
from flask import Flask, render_template
import pandas as pd
from flask import Flask, render_template
import csv
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
import shutil
from requests import get
import requests
import subprocess 
import requests
import json
import pandas as pd
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from PyInstaller.utils.hooks import copy_metadata
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import base64
#datas = copy_metadata('google-cloud-core')

#datas += copy_metadata('google-cloud-translate')

#datas += copy_metadata('google-api-core')
logging.getLogger('selenium').setLevel(logging.WARNING)

from bs4 import BeautifulSoup
from lxml import etree
from fuzzywuzzy import fuzz    
from datetime import datetime
import matplotlib
import urllib
import urllib.request

import pywinauto
import socket

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def is_subset(subset, string):
    subset_chars = set(subset)
    for char in string:
        if char in subset_chars:
            subset_chars.remove(char)
            if not subset_chars:
                return True
    return False
# FIX
# DRIVER_PATH ='chromedriver'
# options = webdriver.ChromeOptions()
# Function to safely close and quit the driver
def safe_close_quit(driver):
    try:
        # Try to interact with the driver
        print("trying to safe close")
        print(driver.current_url)
        # If the above line does not raise an exception, the driver is still open
        driver.close()
        driver.quit()
    except WebDriverException:
        # The driver is already closed, so nothing needs to be done
        print("WebDriver is already closed.")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
]


def create_headless_driver3():
    options = undetectedChromedriver.ChromeOptions()
    options.add_argument('--log-level=3')  
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')

    driver = undetectedChromedriver.Chrome(options=options, version_main=120)
    stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
    driver.set_window_position(-10000, -2000) 
    driver.execute_script("window.open('https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903', '_blank')")
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[1])

    # Check if the iframe exists
    frames = driver.find_elements(By.CSS_SELECTOR, "iframe[src^='https://challenges.cloudflare.com/cdn-cgi']")
    if frames:
        print("Cloudflare Turnstile bypass")
        driver.switch_to.frame(frames[0])  # Switch to the first frame found
        input_element = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input')
        if input_element:
            input_element.click()
            time.sleep(3)


    return driver

# time.sleep(3)
'''

166.88.144.207:20000:<username>:<password>

166.88.144.245:20000:<username>:<password>

142.111.248.23:20000:<username>:<password>
'''

#user: InvestingRealEstate
#pass: MichaelBucci
# res: spxfnfmd1p:sbb2IJjpMSai5mp46k@ca.smartproxy.com:20000

def create_headless_driver1():
    options = uc.ChromeOptions()
    # logging.getLogger('seleniumwire').setLevel(logging.WARNING)
    options.add_argument("--headless=new")
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--ignore-certificate-errors-spki-list')
    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument("--auto-open-devtools-for-tabs")
    # proxy_arguments = {
    # 'proxy': {
    #     'http': 'http://InvestingRealEstate:MichaelBucci@166.88.144.207:20000',
    #     'https': 'https://InvestingRealEstate:MichaelBucci@166.88.144.207:20000',
    #     'no_proxy': 'localhost,127.0.0.1'
    # }
    #random_user_agent = random.choice(user_agents)
    #options.add_argument(f'user-agent={random_user_agent}')
    # }
    options.add_argument('--window-size=1920,1080')
    driver = undetectedChromedriver.Chrome(options=options, version_main=120)
    stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
    return driver



def VPN(action, myvpn=None):
    openvpn = r"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe"
    valid_actions = ["connect", "disconnect", "reconnect", "status"]
    if action in valid_actions:
        if myvpn:
            command = f'"{openvpn}" --command {action} "{myvpn}"'
        else:
            command = f'"{openvpn}" --command {action}'
        subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    else:
        print('Invalid action:', action)
        
    if action == 'connect':
        time.sleep(15)


def create_headless_driver2():
    options = uc.ChromeOptions()
    # logging.getLogger('seleniumwire').setLevel(logging.WARNING)
    options.add_argument("--headless=new")
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--ignore-certificate-errors-spki-list')
    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument("--auto-open-devtools-for-tabs")
    # proxy_arguments = {
    # 'proxy': {
    #     'http': 'http://InvestingRealEstate:MichaelBucci@166.88.144.207:20000',
    #     'https': 'https://InvestingRealEstate:MichaelBucci@166.88.144.207:20000',
    #     'no_proxy': 'localhost,127.0.0.1'
    # }
    #random_user_agent = random.choice(user_agents)
    #options.add_argument(f'user-agent={random_user_agent}')
    # }
    options.add_argument('--window-size=1920,1080')
    driver = undetectedChromedriver.Chrome(options=options, version_main=120)
    stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
    return driver


listofservers = ["armyspy.com","cuvox.de","dayrep.com","einrot.com","fleckens.hu","gustr.com","jourrapide.com","rhyta.com","superrito.com","teleworm.us"]
def getmefield(soup):
    #print(soup.text)
    try:
        div_elements =  soup.find_all('div')
    except:
        #print("Did not work!")
        return False
    
    labels = []
    values = []

    for div in div_elements:
        
        try:
            label = div.find('label').get_text().replace("\n","").strip()
        except:
            label = ""
        
        try:
            value = div.find('input').get('value')
        except:
            try:
                value = div.find('p').get_text()
            except:
                try:
                    value = div.find('textarea').get_text()
                except:
                    value = ""

        labels.append(label)
        values.append(value)

  

    data = {'Label': labels, 'Value': values}
    df = pd.DataFrame(data)
    #for column in df.columns:
    #    df[column] = df[column].str.encode("latin-1")
    
    return df

def getmenextelementbasedontext(driver,specific_text):
    from bs4 import BeautifulSoup

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the element with specific text
    
    specific_element = soup.find('h3', string=lambda text: text and specific_text in text)

    # Get the next element
    next_element = specific_element.find_next_sibling('fieldset')

    if next_element:
        return next_element.get_text().replace("Légende par défaut","").strip()
    else:
        return ""

def getmeactionnaire(text,fieldset):
    if text in fieldset.text:
        return getmefield(fieldset)



def getelementsbetweendynamic(f,a,classs,tags):
    specific_text = a
    specific_element = f.find(string=specific_text)

    # Find the element with specific text
    specific_element = f.find(string = a)
    a = specific_element.find_next("textarea", class_="textareavalidationvisuelle")
    print(a.text)
    return a

    for element in specific_element.find_all_next():
        # Find the next element with specific class and tag
        print(element.tag)
        specific_class = classs
        specific_tag = tags
        if element.tag ==tags:
            print(element.text)
            
    exit(0)
    return element
        
def getelementsbetweenstatic(f,a,classs,tags):
    specific_text = a
    specific_element = f.find(string=specific_text)

    # Find the element with specific tespecific_element = f.find(string=specific_text)xt
    specific_element = f.find(string = a)

    if specific_element:
        # Find the next element with specific class and tag
        specific_class = classs
        specific_tag = tags
        next_element = specific_element.find_next(specific_tag, class_=specific_class)
        
        if next_element:
            return next_element
        else:
            return False
    else:
        return False



    # Collect the elements between the start and end elements
    elements_between = []
    def extract_between_elements(start, end):
        current = start.find_next_sibling()
        while current and current != end:
            yield str(current)
            current = current.find_next_sibling()

    # Create a generator object
    between_elements = extract_between_elements(start_element, end_element)

    # Combine the HTML content into a single string
    html_soup_between = '\n'.join(between_elements)
    return html_soup_between
    # Print the HTML soup between the specified elements
    #print(soup_between.prettify())



def goto(linenum):
    global line
    line = linenum

timeout_duration = 5 
line = 1
timefactorsimple = 2
timefactorhard = 5






import unicodedata
from unidecode import unidecode
def formatdate(x):
    print(type(x))
    try:    
        if type(x) is str:
            if "Non disponible" in x:
                return
            #x = pd.to_datetime(x)
            #x = x.strftime('%Y/%m/%d')
            if "/" in x:
                t = x.split("/")

                return t[2]+"/"+t[0]+"/"+t[1]
            if "-" in x:
                t = x.split("-")

                return t[2]+"/"+t[0]+"/"+t[1]                
        else:
            return str(x)
    except:
        return str(x)

def formatdollars(x):
    try:
        if type(x) is str:
            if "Non disponible" in x:
                return
            x = x.replace(',', '')
            x = x.replace('$', '')
            x = x.replace(' ', '')
            x = x.replace('[^\x00-\x7F]','')
            x = unicodedata.normalize("NFKD", x)
            x = x.replace(' ', '')
            x = float(x)
            #x = x*10.7639
            return x
        else:
            return x
    except:
        return x

def formatmeter(x):
    try:
        if type(x) is str:
            if "Non disponible" in x:
                return
            if "m" in x:
                 
                x = unidecode(x)
                x = x.replace('metres 2', '')
                x = x.replace('metres','')
                x = x.replace('m2','')
                x = x.replace('m 2','')
                x = x.replace('m','')
                x = x.replace(',', '.')        
                x = x.replace(' ', '')
                x = float(x)  
                x = x*10.7639       
                return x
            else:
                return formatnumber(x)
        else:
            return x
    except:
        return x
    
def formatnumber(x):
    try:
        if type(x) is str:
            if "Non disponible" in x:
                return   
            x = unidecode(x)
            x = x.replace(',', '.')
            x = x.replace(' ', '')
            x = x.replace('%', '')
            
            x = unicodedata.normalize("NFKD", x)
            x = float(x)
            #x = x*10.7639
            return x
        else:
            return x
    except:
        return x



def formatpercent(x):
    try:
        if type(x) is str:
            if "Non disponible" in x:
                return   
            x = unidecode(x)
            x = x.replace(',', '.')
            x = x.replace(' ', '')
            x = unicodedata.normalize("NFKD", x)
            x = float(x)
            x = x/100
            return x
        else:
            return x
    except:
        return x


def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list



from datetime import datetime

curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')



"""
# Generate headers
for loop in range(0,5):

    print("\""+"NOM_Registre_"+str(loop)+"\",")
    print("\""+"Address Registre_"+str(loop)+"\",")
    
    for loop2 in range(0,3):
        print("\""+"actionnaire"+str(loop2)+"_Name_"+str(loop)+"\",")
        print("\""+"actionnaire"+str(loop2)+"_Address_"+str(loop)+"\",")

    for loop2 in range(0,10):
        print("\""+"Adminstrator"+str(loop2)+"_Name_"+str(loop)+"\",")
        print("\""+"Adminstrator"+str(loop2)+"_Address_"+str(loop)+"\",")
exit(0)
"""
mirabelheaders = ["Numbers","Adresse",
"Arrondissement",
"Numéro de lot",
"Numéro matricule",
"Utilisation prédominante",
"Dossier no",

"Nom_Evalweb_1",
"Statut aux fins d'imposition scolaire_Evalweb_1",
"Casier postal_Evalweb_1",
"Adresse postale_Evalweb_1",
"Date d'inscription au rôle_Evalweb_1",
"Condition particulière d'inscription_Evalweb_1",
"Nom_Evalweb_2",
"Statut aux fins d'imposition scolaire_Evalweb_2",
"Casier postal_Evalweb_2",
"Adresse postale_Evalweb_2",
"Date d'inscription au rôle_Evalweb_2",
"Condition particulière d'inscription_Evalweb_2",
"Nom_Evalweb_3",
"Statut aux fins d'imposition scolaire_Evalweb_3",
"Casier postal_Evalweb_3",
"Adresse postale_Evalweb_3",
"Date d'inscription au rôle_Evalweb_3",
"Condition particulière d'inscription_Evalweb_3",
"Nom_Evalweb_4",
"Statut aux fins d'imposition scolaire_Evalweb_4",
"Casier postal_Evalweb_4",
"Adresse postale_Evalweb_4",
"Date d'inscription au rôle_Evalweb_4",
"Condition particulière d'inscription_Evalweb_4",
"Nom_Evalweb_5",
"Statut aux fins d'imposition scolaire_Evalweb_5",
"Casier postal_Evalweb_5",
"Adresse postale_Evalweb_5",
"Date d'inscription au rôle_Evalweb_5",
"Condition particulière d'inscription_Evalweb_5",



"Mesure frontale",
"Superficie",
"Numéro de compte foncier",
"Zonage municipal",
"Zonage agricole",
"Nombre d'étages",
"Année de construction",

"Aire d'étages",
"Genre de construction",
"Type de bâtiment",
"Nombre de logements",
"Nombre de locaux non résidentiels",

"Nombre de chambres locatives",
"Numéro d'unité de voisinage",

"Superficie totale_1",
"Superficie en zone agricole_1",
"Superficie visée par imposition maximale_1",

"Superficie totale_2",

"Date de référence au marché_1",
"Valeur du terrain",
"Valeur du bâtiment",
"Valeur de l'immeuble",

"Date de référence au marché_2",
"Valeur de l'immeuble au rôle antérieur",

"Catégorie et classe d'immeuble à des fins d'application des taux variés de taxation",
"Valeur imposable de l'immeuble",
"Valeur non imposable de l'immeuble"
]

newordermirabelheaders2 = [
    "Numbers",
    "Adresse",
    "Arrondissement",
"Numéro de lot",
"Numéro matricule",
"Aire d'étages",
"Superficie",
"Année de construction",
"Nombre de logements",
"Nombre d'étages",




"Utilisation prédominante",
"Genre de construction",
"Type de bâtiment",

"Nombre de locaux non résidentiels",

"Nombre de chambres locatives",
"Numéro d'unité de voisinage",
"Mesure frontale",

"Numéro de compte foncier",
"Zonage municipal",
"Zonage agricole",

"Superficie totale_1",
"Superficie en zone agricole_1",
"Superficie visée par imposition maximale_1",

"Superficie totale_2",

"Date de référence au marché_1",
"Valeur du terrain",
"Valeur du bâtiment",
"Valeur de l'immeuble",

"Date de référence au marché_2",
"Valeur de l'immeuble au rôle antérieur",

"Catégorie et classe d'immeuble à des fins d'application des taux variés de taxation",
"Valeur imposable de l'immeuble",
"Valeur non imposable de l'immeuble",

"Dossier no",


"Nom_Evalweb_1",
"Statut aux fins d'imposition scolaire_Evalweb_1",
"Casier postal_Evalweb_1",
"Adresse postale_Evalweb_1",
"Date d'inscription au rôle_Evalweb_1",
"Condition particulière d'inscription_Evalweb_1",
"Nom_Evalweb_2",
"Statut aux fins d'imposition scolaire_Evalweb_2",
"Casier postal_Evalweb_2",
"Adresse postale_Evalweb_2",
"Date d'inscription au rôle_Evalweb_2",
"Condition particulière d'inscription_Evalweb_2",
"Nom_Evalweb_3",
"Statut aux fins d'imposition scolaire_Evalweb_3",
"Casier postal_Evalweb_3",
"Adresse postale_Evalweb_3",
"Date d'inscription au rôle_Evalweb_3",
"Condition particulière d'inscription_Evalweb_3",
"Nom_Evalweb_4",
"Statut aux fins d'imposition scolaire_Evalweb_4",
"Casier postal_Evalweb_4",
"Adresse postale_Evalweb_4",
"Date d'inscription au rôle_Evalweb_4",
"Condition particulière d'inscription_Evalweb_4",
"Nom_Evalweb_5",
"Statut aux fins d'imposition scolaire_Evalweb_5",
"Casier postal_Evalweb_5",
"Adresse postale_Evalweb_5",
"Date d'inscription au rôle_Evalweb_5",
"Condition particulière d'inscription_Evalweb_5",

"NOM_Registre_1",
"Address Registre_1",
"actionnaire1_Name_1",
"actionnaire1_Address_1",
"actionnaire2_Name_1",
"actionnaire2_Address_1",
"actionnaire3_Name_1",
"actionnaire3_Address_1",
"Adminstrator1_Name_1",
"Adminstrator1_Address_1",
"Adminstrator1_Fonctions actuelles_1",
"Adminstrator2_Name_1",
"Adminstrator2_Address_1",
"Adminstrator2_Fonctions actuelles_1",
"Adminstrator3_Name_1",
"Adminstrator3_Address_1",
"Adminstrator3_Fonctions actuelles_1",
"Adminstrator4_Name_1",
"Adminstrator4_Address_1",
"Adminstrator4_Fonctions actuelles_1",
"Adminstrator5_Name_1",
"Adminstrator5_Address_1",
"Adminstrator5_Fonctions actuelles_1",
"Adminstrator6_Name_1",
"Adminstrator6_Address_1",
"Adminstrator6_Fonctions actuelles_1",
"Adminstrator7_Name_1",
"Adminstrator7_Address_1",
"Adminstrator7_Fonctions actuelles_1",
"Adminstrator8_Name_1",
"Adminstrator8_Address_1",
"Adminstrator8_Fonctions actuelles_1",
"Adminstrator9_Name_1",
"Adminstrator9_Address_1",
"Adminstrator9_Fonctions actuelles_1",
"Adminstrator10_Name_1",
"Adminstrator10_Address_1",
"Adminstrator10_Fonctions actuelles_1",
"Associés1_Nom_1",
"Associés1_Type d'associé_1",
"Associés1_Adresse_1",
"Associés2_Nom_1",
"Associés2_Type d'associé_1",
"Associés2_Adresse_1",
"Associés3_Nom_1",
"Associés3_Type d'associé_1",
"Associés3_Adresse_1",
"Associés4_Nom_1",
"Associés4_Type d'associé_1",
"Associés4_Adresse_1",
"Associés5_Nom_1",
"Associés5_Type d'associé_1",
"Associés5_Adresse_1",
"Associés6_Nom_1",
"Associés6_Type d'associé_1",
"Associés6_Adresse_1",
"Associés7_Nom_1",
"Associés7_Type d'associé_1",
"Associés7_Adresse_1",
"Associés8_Nom_1",
"Associés8_Type d'associé_1",
"Associés8_Adresse_1",
"Associés9_Nom_1",
"Associés9_Type d'associé_1",
"Associés9_Adresse_1",
"Associés10_Nom_1",
"Associés10_Type d'associé_1",
"Associés10_Adresse_1",
"Code d'activité économique (CAE)_1_1",
"Activité_1_1",
"Précisions (facultatives)_1_1",
"Code d'activité économique (CAE)_2_1",
"Activité_2_1",
"Précisions (facultatives)_2_1",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_1",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_1",
"Dirigeants non membres du conseil d'administration _Name_1",
"Dirigeants non membres du conseil d'administration _Address_1",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_1",
"NOM_Registre_2",
"Address Registre_2",
"actionnaire1_Name_2",
"actionnaire1_Address_2",
"actionnaire2_Name_2",
"actionnaire2_Address_2",
"actionnaire3_Name_2",
"actionnaire3_Address_2",
"Adminstrator1_Name_2",
"Adminstrator1_Address_2",
"Adminstrator1_Fonctions actuelles_2",
"Adminstrator2_Name_2",
"Adminstrator2_Address_2",
"Adminstrator2_Fonctions actuelles_2",
"Adminstrator3_Name_2",
"Adminstrator3_Address_2",
"Adminstrator3_Fonctions actuelles_2",
"Adminstrator4_Name_2",
"Adminstrator4_Address_2",
"Adminstrator4_Fonctions actuelles_2",
"Adminstrator5_Name_2",
"Adminstrator5_Address_2",
"Adminstrator5_Fonctions actuelles_2",
"Adminstrator6_Name_2",
"Adminstrator6_Address_2",
"Adminstrator6_Fonctions actuelles_2",
"Adminstrator7_Name_2",
"Adminstrator7_Address_2",
"Adminstrator7_Fonctions actuelles_2",
"Adminstrator8_Name_2",
"Adminstrator8_Address_2",
"Adminstrator8_Fonctions actuelles_2",
"Adminstrator9_Name_2",
"Adminstrator9_Address_2",
"Adminstrator9_Fonctions actuelles_2",
"Adminstrator10_Name_2",
"Adminstrator10_Address_2",
"Adminstrator10_Fonctions actuelles_2",
"Associés1_Nom_2",
"Associés1_Type d'associé_2",
"Associés1_Adresse_2",
"Associés2_Nom_2",
"Associés2_Type d'associé_2",
"Associés2_Adresse_2",
"Associés3_Nom_2",
"Associés3_Type d'associé_2",
"Associés3_Adresse_2",
"Associés4_Nom_2",
"Associés4_Type d'associé_2",
"Associés4_Adresse_2",
"Associés5_Nom_2",
"Associés5_Type d'associé_2",
"Associés5_Adresse_2",
"Associés6_Nom_2",
"Associés6_Type d'associé_2",
"Associés6_Adresse_2",
"Associés7_Nom_2",
"Associés7_Type d'associé_2",
"Associés7_Adresse_2",
"Associés8_Nom_2",
"Associés8_Type d'associé_2",
"Associés8_Adresse_2",
"Associés9_Nom_2",
"Associés9_Type d'associé_2",
"Associés9_Adresse_2",
"Associés10_Nom_2",
"Associés10_Type d'associé_2",
"Associés10_Adresse_2",
"Code d'activité économique (CAE)_1_2",
"Activité_1_2",
"Précisions (facultatives)_1_2",
"Code d'activité économique (CAE)_2_2",
"Activité_2_2",
"Précisions (facultatives)_2_2",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_2",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_2",
"Dirigeants non membres du conseil d'administration _Name_2",
"Dirigeants non membres du conseil d'administration _Address_2",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_2",
"NOM_Registre_3",
"Address Registre_3",
"actionnaire1_Name_3",
"actionnaire1_Address_3",
"actionnaire2_Name_3",
"actionnaire2_Address_3",
"actionnaire3_Name_3",
"actionnaire3_Address_3",
"Adminstrator1_Name_3",
"Adminstrator1_Address_3",
"Adminstrator1_Fonctions actuelles_3",
"Adminstrator2_Name_3",
"Adminstrator2_Address_3",
"Adminstrator2_Fonctions actuelles_3",
"Adminstrator3_Name_3",
"Adminstrator3_Address_3",
"Adminstrator3_Fonctions actuelles_3",
"Adminstrator4_Name_3",
"Adminstrator4_Address_3",
"Adminstrator4_Fonctions actuelles_3",
"Adminstrator5_Name_3",
"Adminstrator5_Address_3",
"Adminstrator5_Fonctions actuelles_3",
"Adminstrator6_Name_3",
"Adminstrator6_Address_3",
"Adminstrator6_Fonctions actuelles_3",
"Adminstrator7_Name_3",
"Adminstrator7_Address_3",
"Adminstrator7_Fonctions actuelles_3",
"Adminstrator8_Name_3",
"Adminstrator8_Address_3",
"Adminstrator8_Fonctions actuelles_3",
"Adminstrator9_Name_3",
"Adminstrator9_Address_3",
"Adminstrator9_Fonctions actuelles_3",
"Adminstrator10_Name_3",
"Adminstrator10_Address_3",
"Adminstrator10_Fonctions actuelles_3",
"Associés1_Nom_3",
"Associés1_Type d'associé_3",
"Associés1_Adresse_3",
"Associés2_Nom_3",
"Associés2_Type d'associé_3",
"Associés2_Adresse_3",
"Associés3_Nom_3",
"Associés3_Type d'associé_3",
"Associés3_Adresse_3",
"Associés4_Nom_3",
"Associés4_Type d'associé_3",
"Associés4_Adresse_3",
"Associés5_Nom_3",
"Associés5_Type d'associé_3",
"Associés5_Adresse_3",
"Associés6_Nom_3",
"Associés6_Type d'associé_3",
"Associés6_Adresse_3",
"Associés7_Nom_3",
"Associés7_Type d'associé_3",
"Associés7_Adresse_3",
"Associés8_Nom_3",
"Associés8_Type d'associé_3",
"Associés8_Adresse_3",
"Associés9_Nom_3",
"Associés9_Type d'associé_3",
"Associés9_Adresse_3",
"Associés10_Nom_3",
"Associés10_Type d'associé_3",
"Associés10_Adresse_3",
"Code d'activité économique (CAE)_1_3",
"Activité_1_3",
"Précisions (facultatives)_1_3",
"Code d'activité économique (CAE)_2_3",
"Activité_2_3",
"Précisions (facultatives)_2_3",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_3",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_3",
"Dirigeants non membres du conseil d'administration _Name_3",
"Dirigeants non membres du conseil d'administration _Address_3",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_3",
"NOM_Registre_4",
"Address Registre_4",
"actionnaire1_Name_4",
"actionnaire1_Address_4",
"actionnaire2_Name_4",
"actionnaire2_Address_4",
"actionnaire3_Name_4",
"actionnaire3_Address_4",
"Adminstrator1_Name_4",
"Adminstrator1_Address_4",
"Adminstrator1_Fonctions actuelles_4",
"Adminstrator2_Name_4",
"Adminstrator2_Address_4",
"Adminstrator2_Fonctions actuelles_4",
"Adminstrator3_Name_4",
"Adminstrator3_Address_4",
"Adminstrator3_Fonctions actuelles_4",
"Adminstrator4_Name_4",
"Adminstrator4_Address_4",
"Adminstrator4_Fonctions actuelles_4",
"Adminstrator5_Name_4",
"Adminstrator5_Address_4",
"Adminstrator5_Fonctions actuelles_4",
"Adminstrator6_Name_4",
"Adminstrator6_Address_4",
"Adminstrator6_Fonctions actuelles_4",
"Adminstrator7_Name_4",
"Adminstrator7_Address_4",
"Adminstrator7_Fonctions actuelles_4",
"Adminstrator8_Name_4",
"Adminstrator8_Address_4",
"Adminstrator8_Fonctions actuelles_4",
"Adminstrator9_Name_4",
"Adminstrator9_Address_4",
"Adminstrator9_Fonctions actuelles_4",
"Adminstrator10_Name_4",
"Adminstrator10_Address_4",
"Adminstrator10_Fonctions actuelles_4",
"Associés1_Nom_4",
"Associés1_Type d'associé_4",
"Associés1_Adresse_4",
"Associés2_Nom_4",
"Associés2_Type d'associé_4",
"Associés2_Adresse_4",
"Associés3_Nom_4",
"Associés3_Type d'associé_4",
"Associés3_Adresse_4",
"Associés4_Nom_4",
"Associés4_Type d'associé_4",
"Associés4_Adresse_4",
"Associés5_Nom_4",
"Associés5_Type d'associé_4",
"Associés5_Adresse_4",
"Associés6_Nom_4",
"Associés6_Type d'associé_4",
"Associés6_Adresse_4",
"Associés7_Nom_4",
"Associés7_Type d'associé_4",
"Associés7_Adresse_4",
"Associés8_Nom_4",
"Associés8_Type d'associé_4",
"Associés8_Adresse_4",
"Associés9_Nom_4",
"Associés9_Type d'associé_4",
"Associés9_Adresse_4",
"Associés10_Nom_4",
"Associés10_Type d'associé_4",
"Associés10_Adresse_4",
"Code d'activité économique (CAE)_1_4",
"Activité_1_4",
"Précisions (facultatives)_1_4",
"Code d'activité économique (CAE)_2_4",
"Activité_2_4",
"Précisions (facultatives)_2_4",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_4",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_4",
"Dirigeants non membres du conseil d'administration _Name_4",
"Dirigeants non membres du conseil d'administration _Address_4",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_4",
"NOM_Registre_5",
"Address Registre_5",
"actionnaire1_Name_5",
"actionnaire1_Address_5",
"actionnaire2_Name_5",
"actionnaire2_Address_5",
"actionnaire3_Name_5",
"actionnaire3_Address_5",
"Adminstrator1_Name_5",
"Adminstrator1_Address_5",
"Adminstrator1_Fonctions actuelles_5",
"Adminstrator2_Name_5",
"Adminstrator2_Address_5",
"Adminstrator2_Fonctions actuelles_5",
"Adminstrator3_Name_5",
"Adminstrator3_Address_5",
"Adminstrator3_Fonctions actuelles_5",
"Adminstrator4_Name_5",
"Adminstrator4_Address_5",
"Adminstrator4_Fonctions actuelles_5",
"Adminstrator5_Name_5",
"Adminstrator5_Address_5",
"Adminstrator5_Fonctions actuelles_5",
"Adminstrator6_Name_5",
"Adminstrator6_Address_5",
"Adminstrator6_Fonctions actuelles_5",
"Adminstrator7_Name_5",
"Adminstrator7_Address_5",
"Adminstrator7_Fonctions actuelles_5",
"Adminstrator8_Name_5",
"Adminstrator8_Address_5",
"Adminstrator8_Fonctions actuelles_5",
"Adminstrator9_Name_5",
"Adminstrator9_Address_5",
"Adminstrator9_Fonctions actuelles_5",
"Adminstrator10_Name_5",
"Adminstrator10_Address_5",
"Adminstrator10_Fonctions actuelles_5",
"Associés1_Nom_5",
"Associés1_Type d'associé_5",
"Associés1_Adresse_5",
"Associés2_Nom_5",
"Associés2_Type d'associé_5",
"Associés2_Adresse_5",
"Associés3_Nom_5",
"Associés3_Type d'associé_5",
"Associés3_Adresse_5",
"Associés4_Nom_5",
"Associés4_Type d'associé_5",
"Associés4_Adresse_5",
"Associés5_Nom_5",
"Associés5_Type d'associé_5",
"Associés5_Adresse_5",
"Associés6_Nom_5",
"Associés6_Type d'associé_5",
"Associés6_Adresse_5",
"Associés7_Nom_5",
"Associés7_Type d'associé_5",
"Associés7_Adresse_5",
"Associés8_Nom_5",
"Associés8_Type d'associé_5",
"Associés8_Adresse_5",
"Associés9_Nom_5",
"Associés9_Type d'associé_5",
"Associés9_Adresse_5",
"Associés10_Nom_5",
"Associés10_Type d'associé_5",
"Associés10_Adresse_5",
"Code d'activité économique (CAE)_1_5",
"Activité_1_5",
"Précisions (facultatives)_1_5",
"Code d'activité économique (CAE)_2_5",
"Activité_2_5",
"Précisions (facultatives)_2_5",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_5",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_5",
"Dirigeants non membres du conseil d'administration _Name_5",
"Dirigeants non membres du conseil d'administration _Address_5",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_5",
"NOM_Registre_6",
"Address Registre_6",
"actionnaire1_Name_6",
"actionnaire1_Address_6",
"actionnaire2_Name_6",
"actionnaire2_Address_6",
"actionnaire3_Name_6",
"actionnaire3_Address_6",
"Adminstrator1_Name_6",
"Adminstrator1_Address_6",
"Adminstrator1_Fonctions actuelles_6",
"Adminstrator2_Name_6",
"Adminstrator2_Address_6",
"Adminstrator2_Fonctions actuelles_6",
"Adminstrator3_Name_6",
"Adminstrator3_Address_6",
"Adminstrator3_Fonctions actuelles_6",
"Adminstrator4_Name_6",
"Adminstrator4_Address_6",
"Adminstrator4_Fonctions actuelles_6",
"Adminstrator5_Name_6",
"Adminstrator5_Address_6",
"Adminstrator5_Fonctions actuelles_6",
"Adminstrator6_Name_6",
"Adminstrator6_Address_6",
"Adminstrator6_Fonctions actuelles_6",
"Adminstrator7_Name_6",
"Adminstrator7_Address_6",
"Adminstrator7_Fonctions actuelles_6",
"Adminstrator8_Name_6",
"Adminstrator8_Address_6",
"Adminstrator8_Fonctions actuelles_6",
"Adminstrator9_Name_6",
"Adminstrator9_Address_6",
"Adminstrator9_Fonctions actuelles_6",
"Adminstrator10_Name_6",
"Adminstrator10_Address_6",
"Adminstrator10_Fonctions actuelles_6",
"Associés1_Nom_6",
"Associés1_Type d'associé_6",
"Associés1_Adresse_6",
"Associés2_Nom_6",
"Associés2_Type d'associé_6",
"Associés2_Adresse_6",
"Associés3_Nom_6",
"Associés3_Type d'associé_6",
"Associés3_Adresse_6",
"Associés4_Nom_6",
"Associés4_Type d'associé_6",
"Associés4_Adresse_6",
"Associés5_Nom_6",
"Associés5_Type d'associé_6",
"Associés5_Adresse_6",
"Associés6_Nom_6",
"Associés6_Type d'associé_6",
"Associés6_Adresse_6",
"Associés7_Nom_6",
"Associés7_Type d'associé_6",
"Associés7_Adresse_6",
"Associés8_Nom_6",
"Associés8_Type d'associé_6",
"Associés8_Adresse_6",
"Associés9_Nom_6",
"Associés9_Type d'associé_6",
"Associés9_Adresse_6",
"Associés10_Nom_6",
"Associés10_Type d'associé_6",
"Associés10_Adresse_6",
"Code d'activité économique (CAE)_1_6",
"Activité_1_6",
"Précisions (facultatives)_1_6",
"Code d'activité économique (CAE)_2_6",
"Activité_2_6",
"Précisions (facultatives)_2_6",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_6",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_6",
"Dirigeants non membres du conseil d'administration _Name_6",
"Dirigeants non membres du conseil d'administration _Address_6",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_6",
"NOM_Registre_7",
"Address Registre_7",
"actionnaire1_Name_7",
"actionnaire1_Address_7",
"actionnaire2_Name_7",
"actionnaire2_Address_7",
"actionnaire3_Name_7",
"actionnaire3_Address_7",
"Adminstrator1_Name_7",
"Adminstrator1_Address_7",
"Adminstrator1_Fonctions actuelles_7",
"Adminstrator2_Name_7",
"Adminstrator2_Address_7",
"Adminstrator2_Fonctions actuelles_7",
"Adminstrator3_Name_7",
"Adminstrator3_Address_7",
"Adminstrator3_Fonctions actuelles_7",
"Adminstrator4_Name_7",
"Adminstrator4_Address_7",
"Adminstrator4_Fonctions actuelles_7",
"Adminstrator5_Name_7",
"Adminstrator5_Address_7",
"Adminstrator5_Fonctions actuelles_7",
"Adminstrator6_Name_7",
"Adminstrator6_Address_7",
"Adminstrator6_Fonctions actuelles_7",
"Adminstrator7_Name_7",
"Adminstrator7_Address_7",
"Adminstrator7_Fonctions actuelles_7",
"Adminstrator8_Name_7",
"Adminstrator8_Address_7",
"Adminstrator8_Fonctions actuelles_7",
"Adminstrator9_Name_7",
"Adminstrator9_Address_7",
"Adminstrator9_Fonctions actuelles_7",
"Adminstrator10_Name_7",
"Adminstrator10_Address_7",
"Adminstrator10_Fonctions actuelles_7",
"Associés1_Nom_7",
"Associés1_Type d'associé_7",
"Associés1_Adresse_7",
"Associés2_Nom_7",
"Associés2_Type d'associé_7",
"Associés2_Adresse_7",
"Associés3_Nom_7",
"Associés3_Type d'associé_7",
"Associés3_Adresse_7",
"Associés4_Nom_7",
"Associés4_Type d'associé_7",
"Associés4_Adresse_7",
"Associés5_Nom_7",
"Associés5_Type d'associé_7",
"Associés5_Adresse_7",
"Associés6_Nom_7",
"Associés6_Type d'associé_7",
"Associés6_Adresse_7",
"Associés7_Nom_7",
"Associés7_Type d'associé_7",
"Associés7_Adresse_7",
"Associés8_Nom_7",
"Associés8_Type d'associé_7",
"Associés8_Adresse_7",
"Associés9_Nom_7",
"Associés9_Type d'associé_7",
"Associés9_Adresse_7",
"Associés10_Nom_7",
"Associés10_Type d'associé_7",
"Associés10_Adresse_7",
"Code d'activité économique (CAE)_1_7",
"Activité_1_7",
"Précisions (facultatives)_1_7",
"Code d'activité économique (CAE)_2_7",
"Activité_2_7",
"Précisions (facultatives)_2_7",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_7",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_7",
"Dirigeants non membres du conseil d'administration _Name_7",
"Dirigeants non membres du conseil d'administration _Address_7",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_7",
"NOM_Registre_8",
"Address Registre_8",
"actionnaire1_Name_8",
"actionnaire1_Address_8",
"actionnaire2_Name_8",
"actionnaire2_Address_8",
"actionnaire3_Name_8",
"actionnaire3_Address_8",
"Adminstrator1_Name_8",
"Adminstrator1_Address_8",
"Adminstrator1_Fonctions actuelles_8",
"Adminstrator2_Name_8",
"Adminstrator2_Address_8",
"Adminstrator2_Fonctions actuelles_8",
"Adminstrator3_Name_8",
"Adminstrator3_Address_8",
"Adminstrator3_Fonctions actuelles_8",
"Adminstrator4_Name_8",
"Adminstrator4_Address_8",
"Adminstrator4_Fonctions actuelles_8",
"Adminstrator5_Name_8",
"Adminstrator5_Address_8",
"Adminstrator5_Fonctions actuelles_8",
"Adminstrator6_Name_8",
"Adminstrator6_Address_8",
"Adminstrator6_Fonctions actuelles_8",
"Adminstrator7_Name_8",
"Adminstrator7_Address_8",
"Adminstrator7_Fonctions actuelles_8",
"Adminstrator8_Name_8",
"Adminstrator8_Address_8",
"Adminstrator8_Fonctions actuelles_8",
"Adminstrator9_Name_8",
"Adminstrator9_Address_8",
"Adminstrator9_Fonctions actuelles_8",
"Adminstrator10_Name_8",
"Adminstrator10_Address_8",
"Adminstrator10_Fonctions actuelles_8",
"Associés1_Nom_8",
"Associés1_Type d'associé_8",
"Associés1_Adresse_8",
"Associés2_Nom_8",
"Associés2_Type d'associé_8",
"Associés2_Adresse_8",
"Associés3_Nom_8",
"Associés3_Type d'associé_8",
"Associés3_Adresse_8",
"Associés4_Nom_8",
"Associés4_Type d'associé_8",
"Associés4_Adresse_8",
"Associés5_Nom_8",
"Associés5_Type d'associé_8",
"Associés5_Adresse_8",
"Associés6_Nom_8",
"Associés6_Type d'associé_8",
"Associés6_Adresse_8",
"Associés7_Nom_8",
"Associés7_Type d'associé_8",
"Associés7_Adresse_8",
"Associés8_Nom_8",
"Associés8_Type d'associé_8",
"Associés8_Adresse_8",
"Associés9_Nom_8",
"Associés9_Type d'associé_8",
"Associés9_Adresse_8",
"Associés10_Nom_8",
"Associés10_Type d'associé_8",
"Associés10_Adresse_8",
"Code d'activité économique (CAE)_1_8",
"Activité_1_8",
"Précisions (facultatives)_1_8",
"Code d'activité économique (CAE)_2_8",
"Activité_2_8",
"Précisions (facultatives)_2_8",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_8",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_8",
"Dirigeants non membres du conseil d'administration _Name_8",
"Dirigeants non membres du conseil d'administration _Address_8",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_8",
"NOM_Registre_9",
"Address Registre_9",
"actionnaire1_Name_9",
"actionnaire1_Address_9",
"actionnaire2_Name_9",
"actionnaire2_Address_9",
"actionnaire3_Name_9",
"actionnaire3_Address_9",
"Adminstrator1_Name_9",
"Adminstrator1_Address_9",
"Adminstrator1_Fonctions actuelles_9",
"Adminstrator2_Name_9",
"Adminstrator2_Address_9",
"Adminstrator2_Fonctions actuelles_9",
"Adminstrator3_Name_9",
"Adminstrator3_Address_9",
"Adminstrator3_Fonctions actuelles_9",
"Adminstrator4_Name_9",
"Adminstrator4_Address_9",
"Adminstrator4_Fonctions actuelles_9",
"Adminstrator5_Name_9",
"Adminstrator5_Address_9",
"Adminstrator5_Fonctions actuelles_9",
"Adminstrator6_Name_9",
"Adminstrator6_Address_9",
"Adminstrator6_Fonctions actuelles_9",
"Adminstrator7_Name_9",
"Adminstrator7_Address_9",
"Adminstrator7_Fonctions actuelles_9",
"Adminstrator8_Name_9",
"Adminstrator8_Address_9",
"Adminstrator8_Fonctions actuelles_9",
"Adminstrator9_Name_9",
"Adminstrator9_Address_9",
"Adminstrator9_Fonctions actuelles_9",
"Adminstrator10_Name_9",
"Adminstrator10_Address_9",
"Adminstrator10_Fonctions actuelles_9",
"Associés1_Nom_9",
"Associés1_Type d'associé_9",
"Associés1_Adresse_9",
"Associés2_Nom_9",
"Associés2_Type d'associé_9",
"Associés2_Adresse_9",
"Associés3_Nom_9",
"Associés3_Type d'associé_9",
"Associés3_Adresse_9",
"Associés4_Nom_9",
"Associés4_Type d'associé_9",
"Associés4_Adresse_9",
"Associés5_Nom_9",
"Associés5_Type d'associé_9",
"Associés5_Adresse_9",
"Associés6_Nom_9",
"Associés6_Type d'associé_9",
"Associés6_Adresse_9",
"Associés7_Nom_9",
"Associés7_Type d'associé_9",
"Associés7_Adresse_9",
"Associés8_Nom_9",
"Associés8_Type d'associé_9",
"Associés8_Adresse_9",
"Associés9_Nom_9",
"Associés9_Type d'associé_9",
"Associés9_Adresse_9",
"Associés10_Nom_9",
"Associés10_Type d'associé_9",
"Associés10_Adresse_9",
"Code d'activité économique (CAE)_1_9",
"Activité_1_9",
"Précisions (facultatives)_1_9",
"Code d'activité économique (CAE)_2_9",
"Activité_2_9",
"Précisions (facultatives)_2_9",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_9",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_9",
"Dirigeants non membres du conseil d'administration _Name_9",
"Dirigeants non membres du conseil d'administration _Address_9",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_9",
"NOM_Registre_10",
"Address Registre_10",
"actionnaire1_Name_10",
"actionnaire1_Address_10",
"actionnaire2_Name_10",
"actionnaire2_Address_10",
"actionnaire3_Name_10",
"actionnaire3_Address_10",
"Adminstrator1_Name_10",
"Adminstrator1_Address_10",
"Adminstrator1_Fonctions actuelles_10",
"Adminstrator2_Name_10",
"Adminstrator2_Address_10",
"Adminstrator2_Fonctions actuelles_10",
"Adminstrator3_Name_10",
"Adminstrator3_Address_10",
"Adminstrator3_Fonctions actuelles_10",
"Adminstrator4_Name_10",
"Adminstrator4_Address_10",
"Adminstrator4_Fonctions actuelles_10",
"Adminstrator5_Name_10",
"Adminstrator5_Address_10",
"Adminstrator5_Fonctions actuelles_10",
"Adminstrator6_Name_10",
"Adminstrator6_Address_10",
"Adminstrator6_Fonctions actuelles_10",
"Adminstrator7_Name_10",
"Adminstrator7_Address_10",
"Adminstrator7_Fonctions actuelles_10",
"Adminstrator8_Name_10",
"Adminstrator8_Address_10",
"Adminstrator8_Fonctions actuelles_10",
"Adminstrator9_Name_10",
"Adminstrator9_Address_10",
"Adminstrator9_Fonctions actuelles_10",
"Adminstrator10_Name_10",
"Adminstrator10_Address_10",
"Adminstrator10_Fonctions actuelles_10",
"Associés1_Nom_10",
"Associés1_Type d'associé_10",
"Associés1_Adresse_10",
"Associés2_Nom_10",
"Associés2_Type d'associé_10",
"Associés2_Adresse_10",
"Associés3_Nom_10",
"Associés3_Type d'associé_10",
"Associés3_Adresse_10",
"Associés4_Nom_10",
"Associés4_Type d'associé_10",
"Associés4_Adresse_10",
"Associés5_Nom_10",
"Associés5_Type d'associé_10",
"Associés5_Adresse_10",
"Associés6_Nom_10",
"Associés6_Type d'associé_10",
"Associés6_Adresse_10",
"Associés7_Nom_10",
"Associés7_Type d'associé_10",
"Associés7_Adresse_10",
"Associés8_Nom_10",
"Associés8_Type d'associé_10",
"Associés8_Adresse_10",
"Associés9_Nom_10",
"Associés9_Type d'associé_10",
"Associés9_Adresse_10",
"Associés10_Nom_10",
"Associés10_Type d'associé_10",
"Associés10_Adresse_10",
"Code d'activité économique (CAE)_1_10",
"Activité_1_10",
"Précisions (facultatives)_1_10",
"Code d'activité économique (CAE)_2_10",
"Activité_2_10",
"Précisions (facultatives)_2_10",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_10",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_10",
"Dirigeants non membres du conseil d'administration _Name_10",
"Dirigeants non membres du conseil d'administration _Address_10",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_10",
"NOM_Registre_11",
"Address Registre_11",
"actionnaire1_Name_11",
"actionnaire1_Address_11",
"actionnaire2_Name_11",
"actionnaire2_Address_11",
"actionnaire3_Name_11",
"actionnaire3_Address_11",
"Adminstrator1_Name_11",
"Adminstrator1_Address_11",
"Adminstrator1_Fonctions actuelles_11",
"Adminstrator2_Name_11",
"Adminstrator2_Address_11",
"Adminstrator2_Fonctions actuelles_11",
"Adminstrator3_Name_11",
"Adminstrator3_Address_11",
"Adminstrator3_Fonctions actuelles_11",
"Adminstrator4_Name_11",
"Adminstrator4_Address_11",
"Adminstrator4_Fonctions actuelles_11",
"Adminstrator5_Name_11",
"Adminstrator5_Address_11",
"Adminstrator5_Fonctions actuelles_11",
"Adminstrator6_Name_11",
"Adminstrator6_Address_11",
"Adminstrator6_Fonctions actuelles_11",
"Adminstrator7_Name_11",
"Adminstrator7_Address_11",
"Adminstrator7_Fonctions actuelles_11",
"Adminstrator8_Name_11",
"Adminstrator8_Address_11",
"Adminstrator8_Fonctions actuelles_11",
"Adminstrator9_Name_11",
"Adminstrator9_Address_11",
"Adminstrator9_Fonctions actuelles_11",
"Adminstrator10_Name_11",
"Adminstrator10_Address_11",
"Adminstrator10_Fonctions actuelles_11",
"Associés1_Nom_11",
"Associés1_Type d'associé_11",
"Associés1_Adresse_11",
"Associés2_Nom_11",
"Associés2_Type d'associé_11",
"Associés2_Adresse_11",
"Associés3_Nom_11",
"Associés3_Type d'associé_11",
"Associés3_Adresse_11",
"Associés4_Nom_11",
"Associés4_Type d'associé_11",
"Associés4_Adresse_11",
"Associés5_Nom_11",
"Associés5_Type d'associé_11",
"Associés5_Adresse_11",
"Associés6_Nom_11",
"Associés6_Type d'associé_11",
"Associés6_Adresse_11",
"Associés7_Nom_11",
"Associés7_Type d'associé_11",
"Associés7_Adresse_11",
"Associés8_Nom_11",
"Associés8_Type d'associé_11",
"Associés8_Adresse_11",
"Associés9_Nom_11",
"Associés9_Type d'associé_11",
"Associés9_Adresse_11",
"Associés10_Nom_11",
"Associés10_Type d'associé_11",
"Associés10_Adresse_11",
"Code d'activité économique (CAE)_1_11",
"Activité_1_11",
"Précisions (facultatives)_1_11",
"Code d'activité économique (CAE)_2_11",
"Activité_2_11",
"Précisions (facultatives)_2_11",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_11",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_11",
"Dirigeants non membres du conseil d'administration _Name_11",
"Dirigeants non membres du conseil d'administration _Address_11",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_11",
"NOM_Registre_12",
"Address Registre_12",
"actionnaire1_Name_12",
"actionnaire1_Address_12",
"actionnaire2_Name_12",
"actionnaire2_Address_12",
"actionnaire3_Name_12",
"actionnaire3_Address_12",
"Adminstrator1_Name_12",
"Adminstrator1_Address_12",
"Adminstrator1_Fonctions actuelles_12",
"Adminstrator2_Name_12",
"Adminstrator2_Address_12",
"Adminstrator2_Fonctions actuelles_12",
"Adminstrator3_Name_12",
"Adminstrator3_Address_12",
"Adminstrator3_Fonctions actuelles_12",
"Adminstrator4_Name_12",
"Adminstrator4_Address_12",
"Adminstrator4_Fonctions actuelles_12",
"Adminstrator5_Name_12",
"Adminstrator5_Address_12",
"Adminstrator5_Fonctions actuelles_12",
"Adminstrator6_Name_12",
"Adminstrator6_Address_12",
"Adminstrator6_Fonctions actuelles_12",
"Adminstrator7_Name_12",
"Adminstrator7_Address_12",
"Adminstrator7_Fonctions actuelles_12",
"Adminstrator8_Name_12",
"Adminstrator8_Address_12",
"Adminstrator8_Fonctions actuelles_12",
"Adminstrator9_Name_12",
"Adminstrator9_Address_12",
"Adminstrator9_Fonctions actuelles_12",
"Adminstrator10_Name_12",
"Adminstrator10_Address_12",
"Adminstrator10_Fonctions actuelles_12",
"Associés1_Nom_12",
"Associés1_Type d'associé_12",
"Associés1_Adresse_12",
"Associés2_Nom_12",
"Associés2_Type d'associé_12",
"Associés2_Adresse_12",
"Associés3_Nom_12",
"Associés3_Type d'associé_12",
"Associés3_Adresse_12",
"Associés4_Nom_12",
"Associés4_Type d'associé_12",
"Associés4_Adresse_12",
"Associés5_Nom_12",
"Associés5_Type d'associé_12",
"Associés5_Adresse_12",
"Associés6_Nom_12",
"Associés6_Type d'associé_12",
"Associés6_Adresse_12",
"Associés7_Nom_12",
"Associés7_Type d'associé_12",
"Associés7_Adresse_12",
"Associés8_Nom_12",
"Associés8_Type d'associé_12",
"Associés8_Adresse_12",
"Associés9_Nom_12",
"Associés9_Type d'associé_12",
"Associés9_Adresse_12",
"Associés10_Nom_12",
"Associés10_Type d'associé_12",
"Associés10_Adresse_12",
"Code d'activité économique (CAE)_1_12",
"Activité_1_12",
"Précisions (facultatives)_1_12",
"Code d'activité économique (CAE)_2_12",
"Activité_2_12",
"Précisions (facultatives)_2_12",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_12",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_12",
"Dirigeants non membres du conseil d'administration _Name_12",
"Dirigeants non membres du conseil d'administration _Address_12",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_12",
"NOM_Registre_13",
"Address Registre_13",
"actionnaire1_Name_13",
"actionnaire1_Address_13",
"actionnaire2_Name_13",
"actionnaire2_Address_13",
"actionnaire3_Name_13",
"actionnaire3_Address_13",
"Adminstrator1_Name_13",
"Adminstrator1_Address_13",
"Adminstrator1_Fonctions actuelles_13",
"Adminstrator2_Name_13",
"Adminstrator2_Address_13",
"Adminstrator2_Fonctions actuelles_13",
"Adminstrator3_Name_13",
"Adminstrator3_Address_13",
"Adminstrator3_Fonctions actuelles_13",
"Adminstrator4_Name_13",
"Adminstrator4_Address_13",
"Adminstrator4_Fonctions actuelles_13",
"Adminstrator5_Name_13",
"Adminstrator5_Address_13",
"Adminstrator5_Fonctions actuelles_13",
"Adminstrator6_Name_13",
"Adminstrator6_Address_13",
"Adminstrator6_Fonctions actuelles_13",
"Adminstrator7_Name_13",
"Adminstrator7_Address_13",
"Adminstrator7_Fonctions actuelles_13",
"Adminstrator8_Name_13",
"Adminstrator8_Address_13",
"Adminstrator8_Fonctions actuelles_13",
"Adminstrator9_Name_13",
"Adminstrator9_Address_13",
"Adminstrator9_Fonctions actuelles_13",
"Adminstrator10_Name_13",
"Adminstrator10_Address_13",
"Adminstrator10_Fonctions actuelles_13",
"Associés1_Nom_13",
"Associés1_Type d'associé_13",
"Associés1_Adresse_13",
"Associés2_Nom_13",
"Associés2_Type d'associé_13",
"Associés2_Adresse_13",
"Associés3_Nom_13",
"Associés3_Type d'associé_13",
"Associés3_Adresse_13",
"Associés4_Nom_13",
"Associés4_Type d'associé_13",
"Associés4_Adresse_13",
"Associés5_Nom_13",
"Associés5_Type d'associé_13",
"Associés5_Adresse_13",
"Associés6_Nom_13",
"Associés6_Type d'associé_13",
"Associés6_Adresse_13",
"Associés7_Nom_13",
"Associés7_Type d'associé_13",
"Associés7_Adresse_13",
"Associés8_Nom_13",
"Associés8_Type d'associé_13",
"Associés8_Adresse_13",
"Associés9_Nom_13",
"Associés9_Type d'associé_13",
"Associés9_Adresse_13",
"Associés10_Nom_13",
"Associés10_Type d'associé_13",
"Associés10_Adresse_13",
"Code d'activité économique (CAE)_1_13",
"Activité_1_13",
"Précisions (facultatives)_1_13",
"Code d'activité économique (CAE)_2_13",
"Activité_2_13",
"Précisions (facultatives)_2_13",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_13",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_13",
"Dirigeants non membres du conseil d'administration _Name_13",
"Dirigeants non membres du conseil d'administration _Address_13",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_13"

]

mirabelheaders2 = ["Numbers","Adresse",
"Arrondissement",
"Numéro de lot",
"Numéro matricule",
"Utilisation prédominante",
"Dossier no",

"Nom_Evalweb_1",
"Statut aux fins d'imposition scolaire_Evalweb_1",
"Casier postal_Evalweb_1",
"Adresse postale_Evalweb_1",
"Date d'inscription au rôle_Evalweb_1",
"Condition particulière d'inscription_Evalweb_1",
"Nom_Evalweb_2",
"Statut aux fins d'imposition scolaire_Evalweb_2",
"Casier postal_Evalweb_2",
"Adresse postale_Evalweb_2",
"Date d'inscription au rôle_Evalweb_2",
"Condition particulière d'inscription_Evalweb_2",
"Nom_Evalweb_3",
"Statut aux fins d'imposition scolaire_Evalweb_3",
"Casier postal_Evalweb_3",
"Adresse postale_Evalweb_3",
"Date d'inscription au rôle_Evalweb_3",
"Condition particulière d'inscription_Evalweb_3",
"Nom_Evalweb_4",
"Statut aux fins d'imposition scolaire_Evalweb_4",
"Casier postal_Evalweb_4",
"Adresse postale_Evalweb_4",
"Date d'inscription au rôle_Evalweb_4",
"Condition particulière d'inscription_Evalweb_4",
"Nom_Evalweb_5",
"Statut aux fins d'imposition scolaire_Evalweb_5",
"Casier postal_Evalweb_5",
"Adresse postale_Evalweb_5",
"Date d'inscription au rôle_Evalweb_5",
"Condition particulière d'inscription_Evalweb_5",



"Mesure frontale",
"Superficie",
"Numéro de compte foncier",
"Zonage municipal",
"Zonage agricole",
"Nombre d'étages",
"Année de construction",

"Aire d'étages",
"Genre de construction",
"Type de bâtiment",
"Nombre de logements",
"Nombre de locaux non résidentiels",

"Nombre de chambres locatives",
"Numéro d'unité de voisinage",

"Superficie totale_1",
"Superficie en zone agricole_1",
"Superficie visée par imposition maximale_1",

"Superficie totale_2",

"Date de référence au marché_1",
"Valeur du terrain",
"Valeur du bâtiment",
"Valeur de l'immeuble",

"Date de référence au marché_2",
"Valeur de l'immeuble au rôle antérieur",

"Catégorie et classe d'immeuble à des fins d'application des taux variés de taxation",
"Valeur imposable de l'immeuble",
"Valeur non imposable de l'immeuble",


"NOM_Registre_1",
"Address Registre_1",
"actionnaire1_Name_1",
"actionnaire1_Address_1",
"actionnaire2_Name_1",
"actionnaire2_Address_1",
"actionnaire3_Name_1",
"actionnaire3_Address_1",
"actionnaire4_Name_1",
"actionnaire4_Address_1",
"actionnaire5_Name_1",
"actionnaire5_Address_1",
"Adminstrator1_Name_1",
"Adminstrator1_Address_1",
"Adminstrator1_Fonctions actuelles_1",
"Adminstrator2_Name_1",
"Adminstrator2_Address_1",
"Adminstrator2_Fonctions actuelles_1",
"Adminstrator3_Name_1",
"Adminstrator3_Address_1",
"Adminstrator3_Fonctions actuelles_1",
"Adminstrator4_Name_1",
"Adminstrator4_Address_1",
"Adminstrator4_Fonctions actuelles_1",
"Adminstrator5_Name_1",
"Adminstrator5_Address_1",
"Adminstrator5_Fonctions actuelles_1",
"Adminstrator6_Name_1",
"Adminstrator6_Address_1",
"Adminstrator6_Fonctions actuelles_1",
"Adminstrator7_Name_1",
"Adminstrator7_Address_1",
"Adminstrator7_Fonctions actuelles_1",
"Adminstrator8_Name_1",
"Adminstrator8_Address_1",
"Adminstrator8_Fonctions actuelles_1",
"Adminstrator9_Name_1",
"Adminstrator9_Address_1",
"Adminstrator9_Fonctions actuelles_1",
"Adminstrator10_Name_1",
"Adminstrator10_Address_1",
"Adminstrator10_Fonctions actuelles_1",
"Associés1_Nom_1",
"Associés1_Type d'associé_1",
"Associés1_Adresse_1",
"Associés2_Nom_1",
"Associés2_Type d'associé_1",
"Associés2_Adresse_1",
"Associés3_Nom_1",
"Associés3_Type d'associé_1",
"Associés3_Adresse_1",
"Associés4_Nom_1",
"Associés4_Type d'associé_1",
"Associés4_Adresse_1",
"Associés5_Nom_1",
"Associés5_Type d'associé_1",
"Associés5_Adresse_1",
"Associés6_Nom_1",
"Associés6_Type d'associé_1",
"Associés6_Adresse_1",
"Associés7_Nom_1",
"Associés7_Type d'associé_1",
"Associés7_Adresse_1",
"Associés8_Nom_1",
"Associés8_Type d'associé_1",
"Associés8_Adresse_1",
"Associés9_Nom_1",
"Associés9_Type d'associé_1",
"Associés9_Adresse_1",
"Associés10_Nom_1",
"Associés10_Type d'associé_1",
"Associés10_Adresse_1",
"Code d'activité économique (CAE)_1_1",
"Activité_1_1",
"Précisions (facultatives)_1_1",
"Code d'activité économique (CAE)_2_1",
"Activité_2_1",
"Précisions (facultatives)_2_1",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_1",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_1",
"Dirigeants non membres du conseil d'administration _Name_1",
"Dirigeants non membres du conseil d'administration _Address_1",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_1",
"NOM_Registre_2",
"Address Registre_2",
"actionnaire1_Name_2",
"actionnaire1_Address_2",
"actionnaire2_Name_2",
"actionnaire2_Address_2",
"actionnaire3_Name_2",
"actionnaire3_Address_2",
"actionnaire4_Name_2",
"actionnaire4_Address_2",
"actionnaire5_Name_2",
"actionnaire5_Address_2",
"Adminstrator1_Name_2",
"Adminstrator1_Address_2",
"Adminstrator1_Fonctions actuelles_2",
"Adminstrator2_Name_2",
"Adminstrator2_Address_2",
"Adminstrator2_Fonctions actuelles_2",
"Adminstrator3_Name_2",
"Adminstrator3_Address_2",
"Adminstrator3_Fonctions actuelles_2",
"Adminstrator4_Name_2",
"Adminstrator4_Address_2",
"Adminstrator4_Fonctions actuelles_2",
"Adminstrator5_Name_2",
"Adminstrator5_Address_2",
"Adminstrator5_Fonctions actuelles_2",
"Adminstrator6_Name_2",
"Adminstrator6_Address_2",
"Adminstrator6_Fonctions actuelles_2",
"Adminstrator7_Name_2",
"Adminstrator7_Address_2",
"Adminstrator7_Fonctions actuelles_2",
"Adminstrator8_Name_2",
"Adminstrator8_Address_2",
"Adminstrator8_Fonctions actuelles_2",
"Adminstrator9_Name_2",
"Adminstrator9_Address_2",
"Adminstrator9_Fonctions actuelles_2",
"Adminstrator10_Name_2",
"Adminstrator10_Address_2",
"Adminstrator10_Fonctions actuelles_2",
"Associés1_Nom_2",
"Associés1_Type d'associé_2",
"Associés1_Adresse_2",
"Associés2_Nom_2",
"Associés2_Type d'associé_2",
"Associés2_Adresse_2",
"Associés3_Nom_2",
"Associés3_Type d'associé_2",
"Associés3_Adresse_2",
"Associés4_Nom_2",
"Associés4_Type d'associé_2",
"Associés4_Adresse_2",
"Associés5_Nom_2",
"Associés5_Type d'associé_2",
"Associés5_Adresse_2",
"Associés6_Nom_2",
"Associés6_Type d'associé_2",
"Associés6_Adresse_2",
"Associés7_Nom_2",
"Associés7_Type d'associé_2",
"Associés7_Adresse_2",
"Associés8_Nom_2",
"Associés8_Type d'associé_2",
"Associés8_Adresse_2",
"Associés9_Nom_2",
"Associés9_Type d'associé_2",
"Associés9_Adresse_2",
"Associés10_Nom_2",
"Associés10_Type d'associé_2",
"Associés10_Adresse_2",
"Code d'activité économique (CAE)_1_2",
"Activité_1_2",
"Précisions (facultatives)_1_2",
"Code d'activité économique (CAE)_2_2",
"Activité_2_2",
"Précisions (facultatives)_2_2",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_2",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_2",
"Dirigeants non membres du conseil d'administration _Name_2",
"Dirigeants non membres du conseil d'administration _Address_2",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_2",
"NOM_Registre_3",
"Address Registre_3",
"actionnaire1_Name_3",
"actionnaire1_Address_3",
"actionnaire2_Name_3",
"actionnaire2_Address_3",
"actionnaire3_Name_3",
"actionnaire3_Address_3",
"actionnaire4_Name_3",
"actionnaire4_Address_3",
"actionnaire5_Name_3",
"actionnaire5_Address_3",
"Adminstrator1_Name_3",
"Adminstrator1_Address_3",
"Adminstrator1_Fonctions actuelles_3",
"Adminstrator2_Name_3",
"Adminstrator2_Address_3",
"Adminstrator2_Fonctions actuelles_3",
"Adminstrator3_Name_3",
"Adminstrator3_Address_3",
"Adminstrator3_Fonctions actuelles_3",
"Adminstrator4_Name_3",
"Adminstrator4_Address_3",
"Adminstrator4_Fonctions actuelles_3",
"Adminstrator5_Name_3",
"Adminstrator5_Address_3",
"Adminstrator5_Fonctions actuelles_3",
"Adminstrator6_Name_3",
"Adminstrator6_Address_3",
"Adminstrator6_Fonctions actuelles_3",
"Adminstrator7_Name_3",
"Adminstrator7_Address_3",
"Adminstrator7_Fonctions actuelles_3",
"Adminstrator8_Name_3",
"Adminstrator8_Address_3",
"Adminstrator8_Fonctions actuelles_3",
"Adminstrator9_Name_3",
"Adminstrator9_Address_3",
"Adminstrator9_Fonctions actuelles_3",
"Adminstrator10_Name_3",
"Adminstrator10_Address_3",
"Adminstrator10_Fonctions actuelles_3",
"Associés1_Nom_3",
"Associés1_Type d'associé_3",
"Associés1_Adresse_3",
"Associés2_Nom_3",
"Associés2_Type d'associé_3",
"Associés2_Adresse_3",
"Associés3_Nom_3",
"Associés3_Type d'associé_3",
"Associés3_Adresse_3",
"Associés4_Nom_3",
"Associés4_Type d'associé_3",
"Associés4_Adresse_3",
"Associés5_Nom_3",
"Associés5_Type d'associé_3",
"Associés5_Adresse_3",
"Associés6_Nom_3",
"Associés6_Type d'associé_3",
"Associés6_Adresse_3",
"Associés7_Nom_3",
"Associés7_Type d'associé_3",
"Associés7_Adresse_3",
"Associés8_Nom_3",
"Associés8_Type d'associé_3",
"Associés8_Adresse_3",
"Associés9_Nom_3",
"Associés9_Type d'associé_3",
"Associés9_Adresse_3",
"Associés10_Nom_3",
"Associés10_Type d'associé_3",
"Associés10_Adresse_3",
"Code d'activité économique (CAE)_1_3",
"Activité_1_3",
"Précisions (facultatives)_1_3",
"Code d'activité économique (CAE)_2_3",
"Activité_2_3",
"Précisions (facultatives)_2_3",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_3",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_3",
"Dirigeants non membres du conseil d'administration _Name_3",
"Dirigeants non membres du conseil d'administration _Address_3",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_3",
"NOM_Registre_4",
"Address Registre_4",
"actionnaire1_Name_4",
"actionnaire1_Address_4",
"actionnaire2_Name_4",
"actionnaire2_Address_4",
"actionnaire3_Name_4",
"actionnaire3_Address_4",
"actionnaire4_Name_4",
"actionnaire4_Address_4",
"actionnaire5_Name_4",
"actionnaire5_Address_4",
"Adminstrator1_Name_4",
"Adminstrator1_Address_4",
"Adminstrator1_Fonctions actuelles_4",
"Adminstrator2_Name_4",
"Adminstrator2_Address_4",
"Adminstrator2_Fonctions actuelles_4",
"Adminstrator3_Name_4",
"Adminstrator3_Address_4",
"Adminstrator3_Fonctions actuelles_4",
"Adminstrator4_Name_4",
"Adminstrator4_Address_4",
"Adminstrator4_Fonctions actuelles_4",
"Adminstrator5_Name_4",
"Adminstrator5_Address_4",
"Adminstrator5_Fonctions actuelles_4",
"Adminstrator6_Name_4",
"Adminstrator6_Address_4",
"Adminstrator6_Fonctions actuelles_4",
"Adminstrator7_Name_4",
"Adminstrator7_Address_4",
"Adminstrator7_Fonctions actuelles_4",
"Adminstrator8_Name_4",
"Adminstrator8_Address_4",
"Adminstrator8_Fonctions actuelles_4",
"Adminstrator9_Name_4",
"Adminstrator9_Address_4",
"Adminstrator9_Fonctions actuelles_4",
"Adminstrator10_Name_4",
"Adminstrator10_Address_4",
"Adminstrator10_Fonctions actuelles_4",
"Associés1_Nom_4",
"Associés1_Type d'associé_4",
"Associés1_Adresse_4",
"Associés2_Nom_4",
"Associés2_Type d'associé_4",
"Associés2_Adresse_4",
"Associés3_Nom_4",
"Associés3_Type d'associé_4",
"Associés3_Adresse_4",
"Associés4_Nom_4",
"Associés4_Type d'associé_4",
"Associés4_Adresse_4",
"Associés5_Nom_4",
"Associés5_Type d'associé_4",
"Associés5_Adresse_4",
"Associés6_Nom_4",
"Associés6_Type d'associé_4",
"Associés6_Adresse_4",
"Associés7_Nom_4",
"Associés7_Type d'associé_4",
"Associés7_Adresse_4",
"Associés8_Nom_4",
"Associés8_Type d'associé_4",
"Associés8_Adresse_4",
"Associés9_Nom_4",
"Associés9_Type d'associé_4",
"Associés9_Adresse_4",
"Associés10_Nom_4",
"Associés10_Type d'associé_4",
"Associés10_Adresse_4",
"Code d'activité économique (CAE)_1_4",
"Activité_1_4",
"Précisions (facultatives)_1_4",
"Code d'activité économique (CAE)_2_4",
"Activité_2_4",
"Précisions (facultatives)_2_4",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_4",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_4",
"Dirigeants non membres du conseil d'administration _Name_4",
"Dirigeants non membres du conseil d'administration _Address_4",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_4",
"NOM_Registre_5",
"Address Registre_5",
"actionnaire1_Name_5",
"actionnaire1_Address_5",
"actionnaire2_Name_5",
"actionnaire2_Address_5",
"actionnaire3_Name_5",
"actionnaire3_Address_5",
"actionnaire4_Name_5",
"actionnaire4_Address_5",
"actionnaire5_Name_5",
"actionnaire5_Address_5",
"Adminstrator1_Name_5",
"Adminstrator1_Address_5",
"Adminstrator1_Fonctions actuelles_5",
"Adminstrator2_Name_5",
"Adminstrator2_Address_5",
"Adminstrator2_Fonctions actuelles_5",
"Adminstrator3_Name_5",
"Adminstrator3_Address_5",
"Adminstrator3_Fonctions actuelles_5",
"Adminstrator4_Name_5",
"Adminstrator4_Address_5",
"Adminstrator4_Fonctions actuelles_5",
"Adminstrator5_Name_5",
"Adminstrator5_Address_5",
"Adminstrator5_Fonctions actuelles_5",
"Adminstrator6_Name_5",
"Adminstrator6_Address_5",
"Adminstrator6_Fonctions actuelles_5",
"Adminstrator7_Name_5",
"Adminstrator7_Address_5",
"Adminstrator7_Fonctions actuelles_5",
"Adminstrator8_Name_5",
"Adminstrator8_Address_5",
"Adminstrator8_Fonctions actuelles_5",
"Adminstrator9_Name_5",
"Adminstrator9_Address_5",
"Adminstrator9_Fonctions actuelles_5",
"Adminstrator10_Name_5",
"Adminstrator10_Address_5",
"Adminstrator10_Fonctions actuelles_5",
"Associés1_Nom_5",
"Associés1_Type d'associé_5",
"Associés1_Adresse_5",
"Associés2_Nom_5",
"Associés2_Type d'associé_5",
"Associés2_Adresse_5",
"Associés3_Nom_5",
"Associés3_Type d'associé_5",
"Associés3_Adresse_5",
"Associés4_Nom_5",
"Associés4_Type d'associé_5",
"Associés4_Adresse_5",
"Associés5_Nom_5",
"Associés5_Type d'associé_5",
"Associés5_Adresse_5",
"Associés6_Nom_5",
"Associés6_Type d'associé_5",
"Associés6_Adresse_5",
"Associés7_Nom_5",
"Associés7_Type d'associé_5",
"Associés7_Adresse_5",
"Associés8_Nom_5",
"Associés8_Type d'associé_5",
"Associés8_Adresse_5",
"Associés9_Nom_5",
"Associés9_Type d'associé_5",
"Associés9_Adresse_5",
"Associés10_Nom_5",
"Associés10_Type d'associé_5",
"Associés10_Adresse_5",
"Code d'activité économique (CAE)_1_5",
"Activité_1_5",
"Précisions (facultatives)_1_5",
"Code d'activité économique (CAE)_2_5",
"Activité_2_5",
"Précisions (facultatives)_2_5",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_5",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_5",
"Dirigeants non membres du conseil d'administration _Name_5",
"Dirigeants non membres du conseil d'administration _Address_5",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_5",
"NOM_Registre_6",
"Address Registre_6",
"actionnaire1_Name_6",
"actionnaire1_Address_6",
"actionnaire2_Name_6",
"actionnaire2_Address_6",
"actionnaire3_Name_6",
"actionnaire3_Address_6",
"actionnaire4_Name_6",
"actionnaire4_Address_6",
"actionnaire5_Name_6",
"actionnaire5_Address_6",
"Adminstrator1_Name_6",
"Adminstrator1_Address_6",
"Adminstrator1_Fonctions actuelles_6",
"Adminstrator2_Name_6",
"Adminstrator2_Address_6",
"Adminstrator2_Fonctions actuelles_6",
"Adminstrator3_Name_6",
"Adminstrator3_Address_6",
"Adminstrator3_Fonctions actuelles_6",
"Adminstrator4_Name_6",
"Adminstrator4_Address_6",
"Adminstrator4_Fonctions actuelles_6",
"Adminstrator5_Name_6",
"Adminstrator5_Address_6",
"Adminstrator5_Fonctions actuelles_6",
"Adminstrator6_Name_6",
"Adminstrator6_Address_6",
"Adminstrator6_Fonctions actuelles_6",
"Adminstrator7_Name_6",
"Adminstrator7_Address_6",
"Adminstrator7_Fonctions actuelles_6",
"Adminstrator8_Name_6",
"Adminstrator8_Address_6",
"Adminstrator8_Fonctions actuelles_6",
"Adminstrator9_Name_6",
"Adminstrator9_Address_6",
"Adminstrator9_Fonctions actuelles_6",
"Adminstrator10_Name_6",
"Adminstrator10_Address_6",
"Adminstrator10_Fonctions actuelles_6",
"Associés1_Nom_6",
"Associés1_Type d'associé_6",
"Associés1_Adresse_6",
"Associés2_Nom_6",
"Associés2_Type d'associé_6",
"Associés2_Adresse_6",
"Associés3_Nom_6",
"Associés3_Type d'associé_6",
"Associés3_Adresse_6",
"Associés4_Nom_6",
"Associés4_Type d'associé_6",
"Associés4_Adresse_6",
"Associés5_Nom_6",
"Associés5_Type d'associé_6",
"Associés5_Adresse_6",
"Associés6_Nom_6",
"Associés6_Type d'associé_6",
"Associés6_Adresse_6",
"Associés7_Nom_6",
"Associés7_Type d'associé_6",
"Associés7_Adresse_6",
"Associés8_Nom_6",
"Associés8_Type d'associé_6",
"Associés8_Adresse_6",
"Associés9_Nom_6",
"Associés9_Type d'associé_6",
"Associés9_Adresse_6",
"Associés10_Nom_6",
"Associés10_Type d'associé_6",
"Associés10_Adresse_6",
"Code d'activité économique (CAE)_1_6",
"Activité_1_6",
"Précisions (facultatives)_1_6",
"Code d'activité économique (CAE)_2_6",
"Activité_2_6",
"Précisions (facultatives)_2_6",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_6",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_6",
"Dirigeants non membres du conseil d'administration _Name_6",
"Dirigeants non membres du conseil d'administration _Address_6",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_6",
"NOM_Registre_7",
"Address Registre_7",
"actionnaire1_Name_7",
"actionnaire1_Address_7",
"actionnaire2_Name_7",
"actionnaire2_Address_7",
"actionnaire3_Name_7",
"actionnaire3_Address_7",
"actionnaire4_Name_7",
"actionnaire4_Address_7",
"actionnaire5_Name_7",
"actionnaire5_Address_7",
"Adminstrator1_Name_7",
"Adminstrator1_Address_7",
"Adminstrator1_Fonctions actuelles_7",
"Adminstrator2_Name_7",
"Adminstrator2_Address_7",
"Adminstrator2_Fonctions actuelles_7",
"Adminstrator3_Name_7",
"Adminstrator3_Address_7",
"Adminstrator3_Fonctions actuelles_7",
"Adminstrator4_Name_7",
"Adminstrator4_Address_7",
"Adminstrator4_Fonctions actuelles_7",
"Adminstrator5_Name_7",
"Adminstrator5_Address_7",
"Adminstrator5_Fonctions actuelles_7",
"Adminstrator6_Name_7",
"Adminstrator6_Address_7",
"Adminstrator6_Fonctions actuelles_7",
"Adminstrator7_Name_7",
"Adminstrator7_Address_7",
"Adminstrator7_Fonctions actuelles_7",
"Adminstrator8_Name_7",
"Adminstrator8_Address_7",
"Adminstrator8_Fonctions actuelles_7",
"Adminstrator9_Name_7",
"Adminstrator9_Address_7",
"Adminstrator9_Fonctions actuelles_7",
"Adminstrator10_Name_7",
"Adminstrator10_Address_7",
"Adminstrator10_Fonctions actuelles_7",
"Associés1_Nom_7",
"Associés1_Type d'associé_7",
"Associés1_Adresse_7",
"Associés2_Nom_7",
"Associés2_Type d'associé_7",
"Associés2_Adresse_7",
"Associés3_Nom_7",
"Associés3_Type d'associé_7",
"Associés3_Adresse_7",
"Associés4_Nom_7",
"Associés4_Type d'associé_7",
"Associés4_Adresse_7",
"Associés5_Nom_7",
"Associés5_Type d'associé_7",
"Associés5_Adresse_7",
"Associés6_Nom_7",
"Associés6_Type d'associé_7",
"Associés6_Adresse_7",
"Associés7_Nom_7",
"Associés7_Type d'associé_7",
"Associés7_Adresse_7",
"Associés8_Nom_7",
"Associés8_Type d'associé_7",
"Associés8_Adresse_7",
"Associés9_Nom_7",
"Associés9_Type d'associé_7",
"Associés9_Adresse_7",
"Associés10_Nom_7",
"Associés10_Type d'associé_7",
"Associés10_Adresse_7",
"Code d'activité économique (CAE)_1_7",
"Activité_1_7",
"Précisions (facultatives)_1_7",
"Code d'activité économique (CAE)_2_7",
"Activité_2_7",
"Précisions (facultatives)_2_7",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_7",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_7",
"Dirigeants non membres du conseil d'administration _Name_7",
"Dirigeants non membres du conseil d'administration _Address_7",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_7",
"NOM_Registre_8",
"Address Registre_8",
"actionnaire1_Name_8",
"actionnaire1_Address_8",
"actionnaire2_Name_8",
"actionnaire2_Address_8",
"actionnaire3_Name_8",
"actionnaire3_Address_8",
"actionnaire4_Name_8",
"actionnaire4_Address_8",
"actionnaire5_Name_8",
"actionnaire5_Address_8",
"Adminstrator1_Name_8",
"Adminstrator1_Address_8",
"Adminstrator1_Fonctions actuelles_8",
"Adminstrator2_Name_8",
"Adminstrator2_Address_8",
"Adminstrator2_Fonctions actuelles_8",
"Adminstrator3_Name_8",
"Adminstrator3_Address_8",
"Adminstrator3_Fonctions actuelles_8",
"Adminstrator4_Name_8",
"Adminstrator4_Address_8",
"Adminstrator4_Fonctions actuelles_8",
"Adminstrator5_Name_8",
"Adminstrator5_Address_8",
"Adminstrator5_Fonctions actuelles_8",
"Adminstrator6_Name_8",
"Adminstrator6_Address_8",
"Adminstrator6_Fonctions actuelles_8",
"Adminstrator7_Name_8",
"Adminstrator7_Address_8",
"Adminstrator7_Fonctions actuelles_8",
"Adminstrator8_Name_8",
"Adminstrator8_Address_8",
"Adminstrator8_Fonctions actuelles_8",
"Adminstrator9_Name_8",
"Adminstrator9_Address_8",
"Adminstrator9_Fonctions actuelles_8",
"Adminstrator10_Name_8",
"Adminstrator10_Address_8",
"Adminstrator10_Fonctions actuelles_8",
"Associés1_Nom_8",
"Associés1_Type d'associé_8",
"Associés1_Adresse_8",
"Associés2_Nom_8",
"Associés2_Type d'associé_8",
"Associés2_Adresse_8",
"Associés3_Nom_8",
"Associés3_Type d'associé_8",
"Associés3_Adresse_8",
"Associés4_Nom_8",
"Associés4_Type d'associé_8",
"Associés4_Adresse_8",
"Associés5_Nom_8",
"Associés5_Type d'associé_8",
"Associés5_Adresse_8",
"Associés6_Nom_8",
"Associés6_Type d'associé_8",
"Associés6_Adresse_8",
"Associés7_Nom_8",
"Associés7_Type d'associé_8",
"Associés7_Adresse_8",
"Associés8_Nom_8",
"Associés8_Type d'associé_8",
"Associés8_Adresse_8",
"Associés9_Nom_8",
"Associés9_Type d'associé_8",
"Associés9_Adresse_8",
"Associés10_Nom_8",
"Associés10_Type d'associé_8",
"Associés10_Adresse_8",
"Code d'activité économique (CAE)_1_8",
"Activité_1_8",
"Précisions (facultatives)_1_8",
"Code d'activité économique (CAE)_2_8",
"Activité_2_8",
"Précisions (facultatives)_2_8",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_8",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_8",
"Dirigeants non membres du conseil d'administration _Name_8",
"Dirigeants non membres du conseil d'administration _Address_8",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_8",
"NOM_Registre_9",
"Address Registre_9",
"actionnaire1_Name_9",
"actionnaire1_Address_9",
"actionnaire2_Name_9",
"actionnaire2_Address_9",
"actionnaire3_Name_9",
"actionnaire3_Address_9",
"actionnaire4_Name_9",
"actionnaire4_Address_9",
"actionnaire5_Name_9",
"actionnaire5_Address_9",
"Adminstrator1_Name_9",
"Adminstrator1_Address_9",
"Adminstrator1_Fonctions actuelles_9",
"Adminstrator2_Name_9",
"Adminstrator2_Address_9",
"Adminstrator2_Fonctions actuelles_9",
"Adminstrator3_Name_9",
"Adminstrator3_Address_9",
"Adminstrator3_Fonctions actuelles_9",
"Adminstrator4_Name_9",
"Adminstrator4_Address_9",
"Adminstrator4_Fonctions actuelles_9",
"Adminstrator5_Name_9",
"Adminstrator5_Address_9",
"Adminstrator5_Fonctions actuelles_9",
"Adminstrator6_Name_9",
"Adminstrator6_Address_9",
"Adminstrator6_Fonctions actuelles_9",
"Adminstrator7_Name_9",
"Adminstrator7_Address_9",
"Adminstrator7_Fonctions actuelles_9",
"Adminstrator8_Name_9",
"Adminstrator8_Address_9",
"Adminstrator8_Fonctions actuelles_9",
"Adminstrator9_Name_9",
"Adminstrator9_Address_9",
"Adminstrator9_Fonctions actuelles_9",
"Adminstrator10_Name_9",
"Adminstrator10_Address_9",
"Adminstrator10_Fonctions actuelles_9",
"Associés1_Nom_9",
"Associés1_Type d'associé_9",
"Associés1_Adresse_9",
"Associés2_Nom_9",
"Associés2_Type d'associé_9",
"Associés2_Adresse_9",
"Associés3_Nom_9",
"Associés3_Type d'associé_9",
"Associés3_Adresse_9",
"Associés4_Nom_9",
"Associés4_Type d'associé_9",
"Associés4_Adresse_9",
"Associés5_Nom_9",
"Associés5_Type d'associé_9",
"Associés5_Adresse_9",
"Associés6_Nom_9",
"Associés6_Type d'associé_9",
"Associés6_Adresse_9",
"Associés7_Nom_9",
"Associés7_Type d'associé_9",
"Associés7_Adresse_9",
"Associés8_Nom_9",
"Associés8_Type d'associé_9",
"Associés8_Adresse_9",
"Associés9_Nom_9",
"Associés9_Type d'associé_9",
"Associés9_Adresse_9",
"Associés10_Nom_9",
"Associés10_Type d'associé_9",
"Associés10_Adresse_9",
"Code d'activité économique (CAE)_1_9",
"Activité_1_9",
"Précisions (facultatives)_1_9",
"Code d'activité économique (CAE)_2_9",
"Activité_2_9",
"Précisions (facultatives)_2_9",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_9",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_9",
"Dirigeants non membres du conseil d'administration _Name_9",
"Dirigeants non membres du conseil d'administration _Address_9",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_9",
"NOM_Registre_10",
"Address Registre_10",
"actionnaire1_Name_10",
"actionnaire1_Address_10",
"actionnaire2_Name_10",
"actionnaire2_Address_10",
"actionnaire3_Name_10",
"actionnaire3_Address_10",
"actionnaire4_Name_10",
"actionnaire4_Address_10",
"actionnaire5_Name_10",
"actionnaire5_Address_10",
"Adminstrator1_Name_10",
"Adminstrator1_Address_10",
"Adminstrator1_Fonctions actuelles_10",
"Adminstrator2_Name_10",
"Adminstrator2_Address_10",
"Adminstrator2_Fonctions actuelles_10",
"Adminstrator3_Name_10",
"Adminstrator3_Address_10",
"Adminstrator3_Fonctions actuelles_10",
"Adminstrator4_Name_10",
"Adminstrator4_Address_10",
"Adminstrator4_Fonctions actuelles_10",
"Adminstrator5_Name_10",
"Adminstrator5_Address_10",
"Adminstrator5_Fonctions actuelles_10",
"Adminstrator6_Name_10",
"Adminstrator6_Address_10",
"Adminstrator6_Fonctions actuelles_10",
"Adminstrator7_Name_10",
"Adminstrator7_Address_10",
"Adminstrator7_Fonctions actuelles_10",
"Adminstrator8_Name_10",
"Adminstrator8_Address_10",
"Adminstrator8_Fonctions actuelles_10",
"Adminstrator9_Name_10",
"Adminstrator9_Address_10",
"Adminstrator9_Fonctions actuelles_10",
"Adminstrator10_Name_10",
"Adminstrator10_Address_10",
"Adminstrator10_Fonctions actuelles_10",
"Associés1_Nom_10",
"Associés1_Type d'associé_10",
"Associés1_Adresse_10",
"Associés2_Nom_10",
"Associés2_Type d'associé_10",
"Associés2_Adresse_10",
"Associés3_Nom_10",
"Associés3_Type d'associé_10",
"Associés3_Adresse_10",
"Associés4_Nom_10",
"Associés4_Type d'associé_10",
"Associés4_Adresse_10",
"Associés5_Nom_10",
"Associés5_Type d'associé_10",
"Associés5_Adresse_10",
"Associés6_Nom_10",
"Associés6_Type d'associé_10",
"Associés6_Adresse_10",
"Associés7_Nom_10",
"Associés7_Type d'associé_10",
"Associés7_Adresse_10",
"Associés8_Nom_10",
"Associés8_Type d'associé_10",
"Associés8_Adresse_10",
"Associés9_Nom_10",
"Associés9_Type d'associé_10",
"Associés9_Adresse_10",
"Associés10_Nom_10",
"Associés10_Type d'associé_10",
"Associés10_Adresse_10",
"Code d'activité économique (CAE)_1_10",
"Activité_1_10",
"Précisions (facultatives)_1_10",
"Code d'activité économique (CAE)_2_10",
"Activité_2_10",
"Précisions (facultatives)_2_10",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_10",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_10",
"Dirigeants non membres du conseil d'administration _Name_10",
"Dirigeants non membres du conseil d'administration _Address_10",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_10",
"NOM_Registre_11",
"Address Registre_11",
"actionnaire1_Name_11",
"actionnaire1_Address_11",
"actionnaire2_Name_11",
"actionnaire2_Address_11",
"actionnaire3_Name_11",
"actionnaire3_Address_11",
"actionnaire4_Name_11",
"actionnaire4_Address_11",
"actionnaire5_Name_11",
"actionnaire5_Address_11",
"Adminstrator1_Name_11",
"Adminstrator1_Address_11",
"Adminstrator1_Fonctions actuelles_11",
"Adminstrator2_Name_11",
"Adminstrator2_Address_11",
"Adminstrator2_Fonctions actuelles_11",
"Adminstrator3_Name_11",
"Adminstrator3_Address_11",
"Adminstrator3_Fonctions actuelles_11",
"Adminstrator4_Name_11",
"Adminstrator4_Address_11",
"Adminstrator4_Fonctions actuelles_11",
"Adminstrator5_Name_11",
"Adminstrator5_Address_11",
"Adminstrator5_Fonctions actuelles_11",
"Adminstrator6_Name_11",
"Adminstrator6_Address_11",
"Adminstrator6_Fonctions actuelles_11",
"Adminstrator7_Name_11",
"Adminstrator7_Address_11",
"Adminstrator7_Fonctions actuelles_11",
"Adminstrator8_Name_11",
"Adminstrator8_Address_11",
"Adminstrator8_Fonctions actuelles_11",
"Adminstrator9_Name_11",
"Adminstrator9_Address_11",
"Adminstrator9_Fonctions actuelles_11",
"Adminstrator10_Name_11",
"Adminstrator10_Address_11",
"Adminstrator10_Fonctions actuelles_11",
"Associés1_Nom_11",
"Associés1_Type d'associé_11",
"Associés1_Adresse_11",
"Associés2_Nom_11",
"Associés2_Type d'associé_11",
"Associés2_Adresse_11",
"Associés3_Nom_11",
"Associés3_Type d'associé_11",
"Associés3_Adresse_11",
"Associés4_Nom_11",
"Associés4_Type d'associé_11",
"Associés4_Adresse_11",
"Associés5_Nom_11",
"Associés5_Type d'associé_11",
"Associés5_Adresse_11",
"Associés6_Nom_11",
"Associés6_Type d'associé_11",
"Associés6_Adresse_11",
"Associés7_Nom_11",
"Associés7_Type d'associé_11",
"Associés7_Adresse_11",
"Associés8_Nom_11",
"Associés8_Type d'associé_11",
"Associés8_Adresse_11",
"Associés9_Nom_11",
"Associés9_Type d'associé_11",
"Associés9_Adresse_11",
"Associés10_Nom_11",
"Associés10_Type d'associé_11",
"Associés10_Adresse_11",
"Code d'activité économique (CAE)_1_11",
"Activité_1_11",
"Précisions (facultatives)_1_11",
"Code d'activité économique (CAE)_2_11",
"Activité_2_11",
"Précisions (facultatives)_2_11",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_11",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_11",
"Dirigeants non membres du conseil d'administration _Name_11",
"Dirigeants non membres du conseil d'administration _Address_11",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_11",
"NOM_Registre_12",
"Address Registre_12",
"actionnaire1_Name_12",
"actionnaire1_Address_12",
"actionnaire2_Name_12",
"actionnaire2_Address_12",
"actionnaire3_Name_12",
"actionnaire3_Address_12",
"actionnaire4_Name_12",
"actionnaire4_Address_12",
"actionnaire5_Name_12",
"actionnaire5_Address_12",
"Adminstrator1_Name_12",
"Adminstrator1_Address_12",
"Adminstrator1_Fonctions actuelles_12",
"Adminstrator2_Name_12",
"Adminstrator2_Address_12",
"Adminstrator2_Fonctions actuelles_12",
"Adminstrator3_Name_12",
"Adminstrator3_Address_12",
"Adminstrator3_Fonctions actuelles_12",
"Adminstrator4_Name_12",
"Adminstrator4_Address_12",
"Adminstrator4_Fonctions actuelles_12",
"Adminstrator5_Name_12",
"Adminstrator5_Address_12",
"Adminstrator5_Fonctions actuelles_12",
"Adminstrator6_Name_12",
"Adminstrator6_Address_12",
"Adminstrator6_Fonctions actuelles_12",
"Adminstrator7_Name_12",
"Adminstrator7_Address_12",
"Adminstrator7_Fonctions actuelles_12",
"Adminstrator8_Name_12",
"Adminstrator8_Address_12",
"Adminstrator8_Fonctions actuelles_12",
"Adminstrator9_Name_12",
"Adminstrator9_Address_12",
"Adminstrator9_Fonctions actuelles_12",
"Adminstrator10_Name_12",
"Adminstrator10_Address_12",
"Adminstrator10_Fonctions actuelles_12",
"Associés1_Nom_12",
"Associés1_Type d'associé_12",
"Associés1_Adresse_12",
"Associés2_Nom_12",
"Associés2_Type d'associé_12",
"Associés2_Adresse_12",
"Associés3_Nom_12",
"Associés3_Type d'associé_12",
"Associés3_Adresse_12",
"Associés4_Nom_12",
"Associés4_Type d'associé_12",
"Associés4_Adresse_12",
"Associés5_Nom_12",
"Associés5_Type d'associé_12",
"Associés5_Adresse_12",
"Associés6_Nom_12",
"Associés6_Type d'associé_12",
"Associés6_Adresse_12",
"Associés7_Nom_12",
"Associés7_Type d'associé_12",
"Associés7_Adresse_12",
"Associés8_Nom_12",
"Associés8_Type d'associé_12",
"Associés8_Adresse_12",
"Associés9_Nom_12",
"Associés9_Type d'associé_12",
"Associés9_Adresse_12",
"Associés10_Nom_12",
"Associés10_Type d'associé_12",
"Associés10_Adresse_12",
"Code d'activité économique (CAE)_1_12",
"Activité_1_12",
"Précisions (facultatives)_1_12",
"Code d'activité économique (CAE)_2_12",
"Activité_2_12",
"Précisions (facultatives)_2_12",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_12",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_12",
"Dirigeants non membres du conseil d'administration _Name_12",
"Dirigeants non membres du conseil d'administration _Address_12",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_12",
"NOM_Registre_13",
"Address Registre_13",
"actionnaire1_Name_13",
"actionnaire1_Address_13",
"actionnaire2_Name_13",
"actionnaire2_Address_13",
"actionnaire3_Name_13",
"actionnaire3_Address_13",
"actionnaire4_Name_13",
"actionnaire4_Address_13",
"actionnaire5_Name_13",
"actionnaire5_Address_13",
"Adminstrator1_Name_13",
"Adminstrator1_Address_13",
"Adminstrator1_Fonctions actuelles_13",
"Adminstrator2_Name_13",
"Adminstrator2_Address_13",
"Adminstrator2_Fonctions actuelles_13",
"Adminstrator3_Name_13",
"Adminstrator3_Address_13",
"Adminstrator3_Fonctions actuelles_13",
"Adminstrator4_Name_13",
"Adminstrator4_Address_13",
"Adminstrator4_Fonctions actuelles_13",
"Adminstrator5_Name_13",
"Adminstrator5_Address_13",
"Adminstrator5_Fonctions actuelles_13",
"Adminstrator6_Name_13",
"Adminstrator6_Address_13",
"Adminstrator6_Fonctions actuelles_13",
"Adminstrator7_Name_13",
"Adminstrator7_Address_13",
"Adminstrator7_Fonctions actuelles_13",
"Adminstrator8_Name_13",
"Adminstrator8_Address_13",
"Adminstrator8_Fonctions actuelles_13",
"Adminstrator9_Name_13",
"Adminstrator9_Address_13",
"Adminstrator9_Fonctions actuelles_13",
"Adminstrator10_Name_13",
"Adminstrator10_Address_13",
"Adminstrator10_Fonctions actuelles_13",
"Associés1_Nom_13",
"Associés1_Type d'associé_13",
"Associés1_Adresse_13",
"Associés2_Nom_13",
"Associés2_Type d'associé_13",
"Associés2_Adresse_13",
"Associés3_Nom_13",
"Associés3_Type d'associé_13",
"Associés3_Adresse_13",
"Associés4_Nom_13",
"Associés4_Type d'associé_13",
"Associés4_Adresse_13",
"Associés5_Nom_13",
"Associés5_Type d'associé_13",
"Associés5_Adresse_13",
"Associés6_Nom_13",
"Associés6_Type d'associé_13",
"Associés6_Adresse_13",
"Associés7_Nom_13",
"Associés7_Type d'associé_13",
"Associés7_Adresse_13",
"Associés8_Nom_13",
"Associés8_Type d'associé_13",
"Associés8_Adresse_13",
"Associés9_Nom_13",
"Associés9_Type d'associé_13",
"Associés9_Adresse_13",
"Associés10_Nom_13",
"Associés10_Type d'associé_13",
"Associés10_Adresse_13",
"Code d'activité économique (CAE)_1_13",
"Activité_1_13",
"Précisions (facultatives)_1_13",
"Code d'activité économique (CAE)_2_13",
"Activité_2_13",
"Précisions (facultatives)_2_13",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise_13",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicil_13",
"Dirigeants non membres du conseil d'administration _Name_13",
"Dirigeants non membres du conseil d'administration _Address_13",
"Dirigeants non membres du conseil d'administration _Fonctions actuelles_13"

]

scrapesite2headers = [
"Number",

"Nom de l'entreprise",
"Numéro d'entreprise du Québec (NEQ)",
"Nom",
"Nom de famille",
"Prénom",
"Version du nom dans une autre langue",

"Adresse du domicile",
"Adresse du domicile élu_Nom de l'entreprise",
"Adresse du domicile élu_Nom de famille",
"Adresse du domicile élu_Prénom",

"Adresse du domicile élu",

"Adresse professionnelle",

"Date d'immatriculation",
"Statut",
"Date de mise à jour du statut",
"Date de fin d'existence prévue",

"Forme juridique",
"Date de la constitution",
"Régime constitutif",
"Régime courant",
"Précisions sur la forme juridique",
"Date à laquelle la société en nom collectif devient une société à responsabilité limitée",



"Date de mise à jour de l'état de renseignements",
"Date de la dernière déclaration de mise à jour annuelle",
"Date de fin de la période de production de la déclaration de mise à jour annuelle",
"Date de fin de la période de production de la déclaration de mise à jour annuelle de 2021",
"Date de fin de la période de production de la déclaration de mise à jour annuelle de 2022",
"Date de fin de la période de production de la déclaration de mise à jour annuelle de 2023",



"Faillite",
"Fusion, scission et conversion",
"Continuation et autre transformation",
"Liquidation ou dissolution",



"Code d'activité économique (CAE)_1",
"Activité_1",
"Précisions (facultatives)_1",

"Code d'activité économique (CAE)_2",
"Activité_2",
"Précisions (facultatives)_2",

"Nombre de salariés au Québec",
"Proportion de salariés qui ne sont pas en mesure de communiquer en français au travail",

"Premier actionnaire Nom",
"Premier actionnaire Nom de famille",
"Premier actionnaire Prénom",
"Premier actionnaire Adresse du domicile",
"Premier actionnaire Adresse professionnelle",

"Deuxième actionnaire Nom",
"Deuxième actionnaire Nom de famille",
"Deuxième actionnaire Prénom",
"Deuxième actionnaire Adresse du domicile",
"Deuxième actionnaire Adresse professionnelle",

"Troisième actionnaire Nom",
"Troisième actionnaire Nom de famille",
"Troisième actionnaire Prénom",
"Troisième actionnaire Adresse du domicile",
"Troisième actionnaire Adresse professionnelle",

"Quatrième actionnaire Nom",
"Quatrième actionnaire Nom de famille",
"Quatrième actionnaire Prénom",
"Quatrième actionnaire Adresse du domicile",
"Quatrième actionnaire Adresse professionnelle",

"Cinquième actionnaire Nom",
"Cinquième actionnaire Nom de famille",
"Cinquième actionnaire Prénom",
"Cinquième actionnaire Adresse du domicile",
"Cinquième actionnaire Adresse professionnelle",


"Convention unanime des actionnaires",

"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise",
"Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicile",



"Administrateurs Nom de famille  1 ",
"Administrateurs Prénom  1 ",
"Administrateurs Date du début de la charge  1 ",
"Administrateurs Date de fin de la charge  1 ",
"Administrateurs Fonctions actuelles  1 ",
"Administrateurs Adresse 1",
"Administrateurs Adresse du domicile  1 ",
"Administrateurs Adresse professionnelle  1 ",

"Administrateurs Nom de famille  2 ",
"Administrateurs Prénom  2 ",
"Administrateurs Date du début de la charge  2 ",
"Administrateurs Date de fin de la charge  2 ",
"Administrateurs Fonctions actuelles  2 ",
"Administrateurs Adresse 2",
"Administrateurs Adresse du domicile  2 ",
"Administrateurs Adresse professionnelle  2 ",

"Administrateurs Nom de famille  3 ",
"Administrateurs Prénom  3 ",
"Administrateurs Date du début de la charge  3 ",
"Administrateurs Date de fin de la charge  3 ",
"Administrateurs Fonctions actuelles  3 ",
"Administrateurs Adresse 3",
"Administrateurs Adresse du domicile  3 ",
"Administrateurs Adresse professionnelle  3 ",

"Administrateurs Nom de famille  4 ",
"Administrateurs Prénom  4 ",
"Administrateurs Date du début de la charge  4 ",
"Administrateurs Date de fin de la charge  4 ",
"Administrateurs Fonctions actuelles  4 ",
"Administrateurs Adresse 4",
"Administrateurs Adresse du domicile  4 ",
"Administrateurs Adresse professionnelle  4 ",

"Administrateurs Nom de famille  5 ",
"Administrateurs Prénom  5 ",
"Administrateurs Date du début de la charge  5 ",
"Administrateurs Date de fin de la charge  5 ",
"Administrateurs Fonctions actuelles  5 ",
"Administrateurs Adresse 5",
"Administrateurs Adresse du domicile  5 ",
"Administrateurs Adresse professionnelle  5 ",


"Administrateurs Nom de famille  6 ",
"Administrateurs Prénom  6 ",
"Administrateurs Date du début de la charge  6 ",
"Administrateurs Date de fin de la charge  6 ",
"Administrateurs Fonctions actuelles  6 ",
"Administrateurs Adresse 6",
"Administrateurs Adresse du domicile  6 ",
"Administrateurs Adresse professionnelle  6 ",

"Administrateurs Nom de famille  7 ",
"Administrateurs Prénom  7 ",
"Administrateurs Date du début de la charge  7 ",
"Administrateurs Date de fin de la charge  7 ",
"Administrateurs Fonctions actuelles  7 ",
"Administrateurs Adresse 7",
"Administrateurs Adresse du domicile  7 ",
"Administrateurs Adresse professionnelle  7 ",

"Administrateurs Nom de famille  8 ",
"Administrateurs Prénom  8 ",
"Administrateurs Date du début de la charge  8 ",
"Administrateurs Date de fin de la charge  8 ",
"Administrateurs Fonctions actuelles  8 ",
"Administrateurs Adresse 8",
"Administrateurs Adresse du domicile  8 ",
"Administrateurs Adresse professionnelle  8 ",

"Administrateurs Nom de famille  9 ",
"Administrateurs Prénom  9 ",
"Administrateurs Date du début de la charge  9 ",
"Administrateurs Date de fin de la charge  9 ",
"Administrateurs Fonctions actuelles  9 ",
"Administrateurs Adresse 9",
"Administrateurs Adresse du domicile  9 ",
"Administrateurs Adresse professionnelle  9 ",

"Administrateurs Nom de famille  10 ",
"Administrateurs Prénom  10 ",
"Administrateurs Date du début de la charge  10 ",
"Administrateurs Date de fin de la charge  10 ",
"Administrateurs Fonctions actuelles  10 ",
"Administrateurs Adresse 10",
"Administrateurs Adresse du domicile  10 ",
"Administrateurs Adresse professionnelle  10 ",

"Administrateurs Nom de famille  11 ",
"Administrateurs Prénom  11 ",
"Administrateurs Date du début de la charge  11 ",
"Administrateurs Date de fin de la charge  11 ",
"Administrateurs Fonctions actuelles  11 ",
"Administrateurs Adresse 11",
"Administrateurs Adresse du domicile  11 ",
"Administrateurs Adresse professionnelle  11 ",

"Administrateurs Nom de famille  12 ",
"Administrateurs Prénom  12 ",
"Administrateurs Date du début de la charge  12 ",
"Administrateurs Date de fin de la charge  12 ",
"Administrateurs Fonctions actuelles  12 ",
"Administrateurs Adresse 12",
"Administrateurs Adresse du domicile  12 ",
"Administrateurs Adresse professionnelle  12 ",

"Administrateurs Nom de famille  13 ",
"Administrateurs Prénom  13 ",
"Administrateurs Date du début de la charge  13 ",
"Administrateurs Date de fin de la charge  13 ",
"Administrateurs Fonctions actuelles  13 ",
"Administrateurs Adresse 13",
"Administrateurs Adresse du domicile  13 ",
"Administrateurs Adresse professionnelle  13 ",

"Administrateurs Nom de famille  14 ",
"Administrateurs Prénom  14 ",
"Administrateurs Date du début de la charge  14 ",
"Administrateurs Date de fin de la charge  14 ",
"Administrateurs Fonctions actuelles  14 ",
"Administrateurs Adresse 14",
"Administrateurs Adresse du domicile  14 ",
"Administrateurs Adresse professionnelle  14 ",

"Administrateurs Nom de famille  15 ",
"Administrateurs Prénom  15 ",
"Administrateurs Date du début de la charge  15 ",
"Administrateurs Date de fin de la charge  15 ",
"Administrateurs Fonctions actuelles  15 ",
"Administrateurs Adresse 15",
"Administrateurs Adresse du domicile  15 ",
"Administrateurs Adresse professionnelle  15 ",


"Administrateurs Nom de famille  16 ",
"Administrateurs Prénom  16 ",
"Administrateurs Date du début de la charge  16 ",
"Administrateurs Date de fin de la charge  16 ",
"Administrateurs Fonctions actuelles  16 ",
"Administrateurs Adresse 16",
"Administrateurs Adresse du domicile  16 ",
"Administrateurs Adresse professionnelle  16 ",

"Administrateurs Nom de famille  17 ",
"Administrateurs Prénom  17 ",
"Administrateurs Date du début de la charge  17 ",
"Administrateurs Date de fin de la charge  17 ",
"Administrateurs Fonctions actuelles  17 ",
"Administrateurs Adresse 17",
"Administrateurs Adresse du domicile  17 ",
"Administrateurs Adresse professionnelle  17 ",

"Administrateurs Nom de famille  18 ",
"Administrateurs Prénom  18 ",
"Administrateurs Date du début de la charge  18 ",
"Administrateurs Date de fin de la charge  18 ",
"Administrateurs Fonctions actuelles  18 ",
"Administrateurs Adresse 18",
"Administrateurs Adresse du domicile  18 ",
"Administrateurs Adresse professionnelle  18 ",

"Administrateurs Nom de famille  19 ",
"Administrateurs Prénom  19 ",
"Administrateurs Date du début de la charge  19 ",
"Administrateurs Date de fin de la charge  19 ",
"Administrateurs Fonctions actuelles  19 ",
"Administrateurs Adresse 19",
"Administrateurs Adresse du domicile  19 ",
"Administrateurs Adresse professionnelle  19 ",

"Administrateurs Nom de famille  20 ",
"Administrateurs Prénom  20 ",
"Administrateurs Date du début de la charge  20 ",
"Administrateurs Date de fin de la charge  20 ",
"Administrateurs Fonctions actuelles  20 ",
"Administrateurs Adresse 20",
"Administrateurs Adresse du domicile  20 ",
"Administrateurs Adresse professionnelle  20 ",

"Administrateurs Nom de famille  21 ",
"Administrateurs Prénom  21 ",
"Administrateurs Date du début de la charge  21 ",
"Administrateurs Date de fin de la charge  21 ",
"Administrateurs Fonctions actuelles  21 ",
"Administrateurs Adresse 21",
"Administrateurs Adresse du domicile  21 ",
"Administrateurs Adresse professionnelle  21 ",

"Administrateurs Nom de famille  22 ",
"Administrateurs Prénom  22 ",
"Administrateurs Date du début de la charge  22 ",
"Administrateurs Date de fin de la charge  22 ",
"Administrateurs Fonctions actuelles  22 ",
"Administrateurs Adresse 22",
"Administrateurs Adresse du domicile  22 ",
"Administrateurs Adresse professionnelle  22 ",

"Administrateurs Nom de famille  23 ",
"Administrateurs Prénom  23 ",
"Administrateurs Date du début de la charge  23 ",
"Administrateurs Date de fin de la charge  23 ",
"Administrateurs Fonctions actuelles  23 ",
"Administrateurs Adresse 23",
"Administrateurs Adresse du domicile  23 ",
"Administrateurs Adresse professionnelle  23 ",

"Administrateurs Nom de famille  24 ",
"Administrateurs Prénom  24 ",
"Administrateurs Date du début de la charge  24 ",
"Administrateurs Date de fin de la charge  24 ",
"Administrateurs Fonctions actuelles  24 ",
"Administrateurs Adresse 24",
"Administrateurs Adresse du domicile  24 ",
"Administrateurs Adresse professionnelle  24 ",

"Administrateurs Nom de famille  25 ",
"Administrateurs Prénom  25 ",
"Administrateurs Date du début de la charge  25 ",
"Administrateurs Date de fin de la charge  25 ",
"Administrateurs Fonctions actuelles  25 ",
"Administrateurs Adresse 25",
"Administrateurs Adresse du domicile  25 ",
"Administrateurs Adresse professionnelle  25 ",

"Administrateurs Nom de famille  26 ",
"Administrateurs Prénom  26 ",
"Administrateurs Date du début de la charge  26 ",
"Administrateurs Date de fin de la charge  26 ",
"Administrateurs Fonctions actuelles  26 ",
"Administrateurs Adresse 26",
"Administrateurs Adresse du domicile  26 ",
"Administrateurs Adresse professionnelle  26 ",


"Administrateurs Nom de famille  27 ",
"Administrateurs Prénom  27 ",
"Administrateurs Date du début de la charge  27 ",
"Administrateurs Date de fin de la charge  27 ",
"Administrateurs Fonctions actuelles  27 ",
"Administrateurs Adresse 27",
"Administrateurs Adresse du domicile  27 ",
"Administrateurs Adresse professionnelle  27 ",

"Administrateurs Nom de famille  28 ",
"Administrateurs Prénom  28 ",
"Administrateurs Date du début de la charge  28 ",
"Administrateurs Date de fin de la charge  28 ",
"Administrateurs Fonctions actuelles  28 ",
"Administrateurs Adresse 28",
"Administrateurs Adresse du domicile  28 ",
"Administrateurs Adresse professionnelle  28 ",

"Administrateurs Nom de famille  29 ",
"Administrateurs Prénom  29 ",
"Administrateurs Date du début de la charge  29 ",
"Administrateurs Date de fin de la charge  29 ",
"Administrateurs Fonctions actuelles  29 ",
"Administrateurs Adresse 29",
"Administrateurs Adresse du domicile  29 ",
"Administrateurs Adresse professionnelle  29 ",

"Administrateurs Nom de famille  30 ",
"Administrateurs Prénom  30 ",
"Administrateurs Date du début de la charge  30 ",
"Administrateurs Date de fin de la charge  30 ",
"Administrateurs Fonctions actuelles  30 ",
"Administrateurs Adresse 30",
"Administrateurs Adresse du domicile  30 ",
"Administrateurs Adresse professionnelle  30 ",




"Associés Nom 1",
"Associés Type d'associé 1",
"Associés Adresse 1",

"Associés Nom 2",
"Associés Type d'associé 2",
"Associés Adresse 2",

"Associés Nom 3",
"Associés Type d'associé 3",
"Associés Adresse 3",

"Associés Nom 4",
"Associés Type d'associé 4",
"Associés Adresse 4",

"Associés Nom 5",
"Associés Type d'associé 5",
"Associés Adresse 5",

"Associés Nom 6",
"Associés Type d'associé 6",
"Associés Adresse 6",

"Associés Nom 7",
"Associés Type d'associé 7",
"Associés Adresse 7",

"Associés Nom 8",
"Associés Type d'associé 8",
"Associés Adresse 8",

"Associés Nom 9",
"Associés Type d'associé 9",
"Associés Adresse 9",

"Associés Nom 10",
"Associés Type d'associé 10",
"Associés Adresse 10",

"Dirigeants non membres du conseil d'administration _ Nom de famille",
"Dirigeants non membres du conseil d'administration _ Prénom",
"Dirigeants non membres du conseil d'administration _ Fonctions actuelles",
"Dirigeants non membres du conseil d'administration _ Adresse du domicile",
"Dirigeants non membres du conseil d'administration _ Adresse professionnelle",



"Déclaration relative aux bénéficiaires ultimes",
"Fondé de pouvoir",
"Administrateurs du bien d'autrui _ Nom de famille",
"Administrateurs du bien d'autrui _ Prénom",
"Administrateurs du bien d'autrui _ Date du début de la charge",
"Administrateurs du bien d'autrui _ Date de fin de la charge",

"Administrateurs du bien d'autrui _ Fonction",
"Administrateurs du bien d'autrui _ Adresse du domicile",





"Établissements",
"Documents en traitement",
"Date de mise à jour de l'index des noms"
]

t = pd.DataFrame(columns=scrapesite2headers)
 
def scrapesite2(soup,exactname,funk):
    listings = []
    listings.append(exactname)

    #e = driver.find_elements(By.XPATH,"//span[@id='CPH_K1ZoneContenu1_Cadr_Section01_Section01_ctl04_aDivConsulNom']")[0]
    

    #allelements = driver.find_elements(By.XPATH,"//fieldset[@class='zonelibellechamp']")
    #allelements = soup.find_all('p')
    
    # Find the first <p> element with class "special"
    #allelements = soup
    #dataframes = getmefield(allelements[1])
    
    dataframes = pd.DataFrame()
    x = ""
    if "Nom de l'entreprise" in soup.text:
        print("s",exactname)
    #return

    e = getelementsbetweenstatic(soup,"Identification de l'entreprise", "zonelibellechamp", "fieldset")
    dataframes = getmefield(e)


    try:
        listings.append(dataframes[dataframes["Label"]=="Nom de l'entreprise"]["Value"].values[0])
    except:
        listings.append("")

    #print(listings)
    #return
    
    try:
        listings.append(dataframes[dataframes["Label"]=="Numéro d'entreprise du Québec (NEQ)"]["Value"].values[0])
    except:
        listings.append("")

    try:
        listings.append(dataframes[dataframes["Label"]=="Nom"]["Value"].values[0])
    except:
        listings.append("")

    try:
        listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
    except:
        listings.append("")

    try:
        listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
    except:
        listings.append("")

    try:
        listings.append(dataframes[dataframes["Label"]=="Version du nom dans une autre langue"]["Value"].values[0])
    except:
        listings.append("")
    
    


    dataframes = pd.DataFrame()
    x = ""
    
    try:
        e = getelementsbetweenstatic(soup,"Adresse du domicile", "zonelibellechamp", "fieldset")
        dataframes = getmefield(e)
        listings.append(dataframes["Value"].values[0].replace("\n"," "))
    except:
        listings.append("")
    


    
    dataframes = pd.DataFrame()
    x = ""
     
    try:
        e = getelementsbetweenstatic(soup,"Adresse du domicile élu", "zonelibellechamp", "fieldset")
        dataframes = getmefield(e)

        if len(dataframes)>1:
            try:
                listings.append(dataframes[dataframes["Label"]=="Nom de l'entreprise"]["Value"].values[0])
            except:
                listings.append("")
                    
            try:
                listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
            except:
                listings.append("")
            try:
                listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
            except:
                listings.append("")   
        else:
            for loop in range(0,3):
                listings.append("")


    except:
        for loop in range(0,3):
            listings.append("")


    dataframes = pd.DataFrame()
    x = ""

    try:
        e = getelementsbetweenstatic(soup,"Adresse du domicile élu", "textareavalidationvisuelle", "textarea")
        listings.append(e.text.replace("\n",""))
    except:
        listings.append("")


    dataframes = pd.DataFrame()
    x = ""
    
    
    try:
        for l in soup.find_all("h3"):
            if l.text == "Adresse professionnelle":
                x  = l.find_next("textarea", class_="textareavalidationvisuelle")
                #print(x.text)
        listings.append(x.text)
    except:
        listings.append("")




    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if l.text == "Immatriculation":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)
        
        try:
            listings.append(dataframes[dataframes["Label"]=="Date d'immatriculation"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Statut"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Date de mise à jour du statut"]["Value"].values[0])
        except:
            listings.append("") 

        try:
            listings.append(dataframes[dataframes["Label"]=="Date de fin d’existence prévue"]["Value"].values[0])
        except:
            listings.append("")  

    except:
        for loop in range(0,4):
            listings.append("")



    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if l.text == "Forme juridique":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)

        try:
            listings.append(dataframes[dataframes["Label"]=="Forme juridique"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Date de la constitution"]["Value"].values[0])
        except:
            listings.append("")
        try:
            listings.append(dataframes[dataframes["Label"]=="Régime constitutif"]["Value"].values[0])
        except:
            listings.append("")  
        try:
            listings.append(dataframes[dataframes["Label"]=="Régime courant"]["Value"].values[0])
        except:
            listings.append("")  

        try:
            listings.append(dataframes[dataframes["Label"]=="Précisions sur la forme juridique"]["Value"].values[0])
        except:
            listings.append("")  

        try:
            listings.append(dataframes[dataframes["Label"]=="Date à laquelle la société en nom collectif devient une société à responsabilité limitée"]["Value"].values[0])
        except:
            listings.append("")  

    except:
        for loop in range(0,6):
            listings.append("")


 
    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if l.text == "Dates des mises à jour":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)

        try:
            listings.append(dataframes[dataframes["Label"]=="Date de mise à jour de l'état de renseignements"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Date de la dernière déclaration de mise à jour annuelle"]["Value"].values[0])
        except:
            listings.append("")
        try:
            listings.append(dataframes[dataframes["Label"]=="Date de fin de la période de production de la déclaration de mise à jour annuelle"]["Value"].values[0])
        except:
            listings.append("")  
        try:
            listings.append(dataframes[dataframes["Label"]=="Date de fin de la période de production de la déclaration de mise à jour annuelle de 2021"]["Value"].values[0])
        except:
            listings.append("")  

        try:
            listings.append(dataframes[dataframes["Label"]=="Date de fin de la période de production de la déclaration de mise à jour annuelle de 2022"]["Value"].values[0])
        except:
            listings.append("")  

        try:
            listings.append(dataframes[dataframes["Label"]=="Date de fin de la période de production de la déclaration de mise à jour annuelle de 2023"]["Value"].values[0])
        except:
            listings.append("")  

    except:
        for loop in range(0,6):
            listings.append("")


    
  
    dataframes = pd.DataFrame()
    x = ""


    try:
        for l in soup.find_all("h3"):
            if l.text == "Faillite":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        listings.append(x.text.replace("Légende par défaut","").strip())

    except:
        for loop in range(0,1):
            listings.append("")

    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if l.text == "Fusion, scission et conversion":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        listings.append(x.text.replace("Légende par défaut","").strip())

    except:
        for loop in range(0,1):
            listings.append("")

    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if l.text == "Continuation et autre transformation":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        listings.append(x.text.replace("Légende par défaut","").strip())

    except:
        for loop in range(0,1):
            listings.append("")            

    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if l.text == "Liquidation ou dissolution":
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        listings.append(x.text.replace("Légende par défaut","").strip())

    except:
        for loop in range(0,1):
            listings.append("")




    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "1er secteur d'activité" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)
        if len(dataframes)>1:
            try:
                listings.append(dataframes[dataframes["Label"]=="Code d'activité économique (CAE)"]["Value"].values[0])
            except:
                listings.append("")
                    
            try:
                listings.append(dataframes[dataframes["Label"]=="Activité"]["Value"].values[0])
            except:
                listings.append("")
            try:
                listings.append(dataframes[dataframes["Label"]=="Précisions (facultatives)"]["Value"].values[0])
            except:
                listings.append("")  
        else:
            for loop in range(0,3):
                listings.append(x.text.replace("Légende par défaut","").strip())
            
        

    except:
        for loop in range(0,3):
            listings.append("")

    dataframes = pd.DataFrame()
    x = ""
    



    try:
        for l in soup.find_all("h3"):
            if "2e secteur d'activité" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)
        if len(dataframes)>1:
            try:
                listings.append(dataframes[dataframes["Label"]=="Code d'activité économique (CAE)"]["Value"].values[0])
            except:
                listings.append("")
                    
            try:
                listings.append(dataframes[dataframes["Label"]=="Activité"]["Value"].values[0])
            except:
                listings.append("")
            try:
                listings.append(dataframes[dataframes["Label"]=="Précisions (facultatives)"]["Value"].values[0])
            except:
                listings.append("")  
        else:
            for loop in range(0,3):
                listings.append(x.text.replace("Légende par défaut","").strip())
            
        

    except:
        for loop in range(0,3):
            listings.append("")


    dataframes = pd.DataFrame()
    x = ""

    
  


    try:
        for l in soup.find_all("h3"):
            if "Nombre de salariés" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)

        try:
            listings.append(dataframes[dataframes["Label"]=="Nombre de salariés au Québec"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Proportion de salariés qui ne sont pas en mesure de communiquer en français au travail"]["Value"].values[0])
        except:
            listings.append("")
        

    except:
        for loop in range(0,2):
            listings.append("")


   

    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Premier actionnaire" in l.text:
                #print(l)
                x  = l.find_previous("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse professionnelle"]["Value"].values[0])
        except:
            listings.append("")


    except:
        for loop in range(0,5):
            listings.append("")
    #print("listings")
    #print(listings)

    
    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Deuxième actionnaire" in l.text:
                #print(l)
                x  = l.find_previous("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse professionnelle"]["Value"].values[0])
        except:
            listings.append("")


    except:
        for loop in range(0,5):
            listings.append("")

    


    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Troisième actionnaire" in l.text:
                #print(l)
                x  = l.find_previous("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse professionnelle"]["Value"].values[0])
        except:
            listings.append("")


    except:
        for loop in range(0,5):
            listings.append("")

    try:
        for l in soup.find_all("h3"):
            if "Quatrième actionnaire" in l.text:
                #print(l)
                x  = l.find_previous("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse professionnelle"]["Value"].values[0])
        except:
            listings.append("")


    except:
        for loop in range(0,5):
            listings.append("")

    try:
        for l in soup.find_all("h3"):
            if "Cinquième actionnaire" in l.text:
                #print(l)
                x  = l.find_previous("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
        except:
            listings.append("")

        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse professionnelle"]["Value"].values[0])
        except:
            listings.append("")


    except:
        for loop in range(0,5):
            listings.append("")

    
    
    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Convention unanime des actionnaires" in l.text:
                #print(l)
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        
        try:
            listings.append(x.text.replace("Légende par défaut","").strip())
        except:
            listings.append("")
        
    except:
        for loop in range(0,1):
            listings.append("")
    

    try:
        for l in soup.find_all("h3"):
            if "Actionnaires ou tiers assumant les pouvoirs du conseil d'administration" in l.text:
                #print(l)
                x  = l.find_next("fieldset", class_="zonelibellechamp").find_next("fieldset", class_="zonelibellechamp")
                #print(x)
                break

        dataframes = getmefield(x)

        try:
            listings.append(dataframes[dataframes["Label"]=="Nom de l'entreprise"]["Value"].values[0])
        except:
            listings.append("")
                
        try:
            listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
        except:
            listings.append("")

    except:
        for loop in range(0,2):
            listings.append("")



    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Liste des administrateurs" in l.text:
                #print(l)
                x  = l.find_next("span", id="CPH_K1ZoneContenu1_Cadr_Section01_Section01_ctl39_divMembConsAdm")
                #print(x)
                break
        
        dataframes = getmefield(x)
        dataframes.rename(columns={'Label': 0}, inplace=True)
        dataframes.rename(columns={'Value': 1}, inplace=True)
        data = dataframes
        m = data[0].str.contains('Nom de famille').cumsum()
        d = {f'df{i}': g for i, g in data.groupby(m)}
        

        for k, v in d.items():
            try:
                #print(v[v['0'].str.contains("Nom")]['1'].values[0])
                listings.append(v[v[0]=="Nom de famille"][1].values[0])
            except:
                listings.append("")
                pass

            try:
                #print(v[v['0'].str.contains("Statut aux fins d'imposition scolaire")]['1'].values[0])
                listings.append(v[v[0]=="Prénom"][1].values[0])
            except:
                listings.append("")
                pass
            
            try:
                #print(v[v['0'].str.contains("Casier postal")]['1'].values[0])
                listings.append(v[v[0]=="Date du début de la charge"][1].values[0])
            except:
                listings.append("")
                pass
            
            try:
                #print(v[v['0'].str.contains("Adresse postale")]['1'].values[0])
                listings.append(v[v[0]=="Date de fin de la charge"][1].values[0])
            except:
                listings.append("")
                pass
            
            try:
                #print(v[v['0'].str.contains("Date d'inscription au rôle")]['1'].values[0])
                listings.append(v[v[0]=="Fonctions actuelles"][1].values[0])
            except:
                listings.append("")
                pass
            try:
                #print(v[v['0'].str.contains("Condition particulière d'inscription")]['1'].values[0])
                listings.append(v[v[0]=="Adresse"][1].values[0].replace("(Cliquer pour voir sur la carte)",""))
            except:
                listings.append("")
                pass


            try:
                #print(v[v['0'].str.contains("Condition particulière d'inscription")]['1'].values[0])
                listings.append(v[v[0]=="Adresse du domicile"][1].values[0])
            except:
                listings.append("")
                pass

            try:
                #print(v[v['0'].str.contains("Condition particulière d'inscription")]['1'].values[0])
                listings.append(v[v[0]=="Adresse professionnelle"][1].values[0])
            except:
                listings.append("")
                pass
            

        for tt in range(8*len(d),8*30):
            listings.append("") 
            

    except:
        for tt in range(0,8*30):
            listings.append("") 
            
    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Associés" == l.text and len(l.text)<9:
                #print(l)
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        
        if x=="":
            for tt in range(0,3*10):
                listings.append("")
        else: 
            for tt in range(1,11):
                try:
                    dataframes = getmefield(x)
                    #print(dataframes)
                    dataframes.rename(columns={'Label': 0}, inplace=True)
                    dataframes.rename(columns={'Value': 1}, inplace=True)
                except:
                    for loop in range(0,3):
                        listings.append("")    
                    continue
                if len(dataframes)==3 and "Adresse du domicile" in dataframes[0].values and "Nom" in dataframes[0].values and "Type d'associé" in dataframes[0].values:
                    try:
                        #print(v[v['0'].str.contains("Nom")]['1'].values[0])
                        listings.append(dataframes[dataframes[0]=="Nom"][1].values[0])
                    except:
                        listings.append("")
                        pass

                    try:
                        #print(v[v['0'].str.contains("Statut aux fins d'imposition scolaire")]['1'].values[0])
                        listings.append(dataframes[dataframes[0]=="Type d'associé"][1].values[0])
                    except:
                        listings.append("")
                        pass
                    
                    try:
                        #print(v[v['0'].str.contains("Casier postal")]['1'].values[0])
                        listings.append(dataframes[dataframes[0]=="Adresse du domicile"][1].values[0])
                    except:
                        listings.append("")
                        pass

                elif len(dataframes)==5 and "Adresse du domicile" in dataframes[0].values and "Nom de famille" in dataframes[0].values and "Type d'associé" in dataframes[0].values:
                    try:
                        #print(v[v['0'].str.contains("Nom")]['1'].values[0])
                        listings.append(dataframes[dataframes[0]=="Prénom"][1].values[0]+" "+dataframes[dataframes[0]=="Nom de famille"][1].values[0])
                    except:
                        listings.append("")
                        pass

                    try:
                        #print(v[v['0'].str.contains("Statut aux fins d'imposition scolaire")]['1'].values[0])
                        listings.append(dataframes[dataframes[0]=="Type d'associé"][1].values[0])
                    except:
                        listings.append("")
                        pass
                    
                    try:
                        #print(v[v['0'].str.contains("Casier postal")]['1'].values[0])
                        listings.append(dataframes[dataframes[0]=="Adresse du domicile"][1].values[0])
                    except:
                        listings.append("")
                        pass
                else:
                    for loop in range(0,3):
                        listings.append("")                
                x  = x.find_next("fieldset", class_="zonelibellechamp")
            
    except:
        pass


    dataframes = pd.DataFrame()
    x = ""

    try:
        for l in soup.find_all("h3"):
            if "Dirigeants non membres du conseil d'administration" in l.text:
                #print(l)
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        if len(dataframes)>1:
            try:
                listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
            except:
                listings.append("")
                    
            try:
                listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
            except:
                listings.append("")

            try:
                listings.append(dataframes[dataframes["Label"]=="Fonctions actuelles"]["Value"].values[0])
            except:
                listings.append("")

            try:
                listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
            except:
                listings.append("")

            try:
                listings.append(dataframes[dataframes["Label"]=="Adresse professionnelle"]["Value"].values[0])
            except:
                listings.append("")
        else:
            for loop in range(0,5):
                listings.append(x.text.replace("Légende par défaut","").strip().replace("\n"," "))

    except:
        for loop in range(0,5):
            listings.append("")



    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Déclaration relative aux bénéficiaires ultimes" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        
        try:
            listings.append(x.text.replace("Légende par défaut","").strip().replace("\n"," "))
        except:
            listings.append("")
        
    except:
        for loop in range(0,1):
            listings.append("")

    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Fondé de pouvoir" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        
        try:
            listings.append(x.text.replace("Légende par défaut","").strip().replace("\n"," "))
        except:
            listings.append("")
        
    except:
        for loop in range(0,1):
            listings.append("")




    dataframes = pd.DataFrame()
    x = ""

 
    try:
        for l in soup.find_all("h3"):
            if "Administrateurs du bien d'autrui" in l.text:
                #print(l)
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                #print(x)
                break
        dataframes = getmefield(x)

        if len(dataframes)>1:
            try:
                listings.append(dataframes[dataframes["Label"]=="Nom de famille"]["Value"].values[0])
            except:
                listings.append("")
                    
            try:
                listings.append(dataframes[dataframes["Label"]=="Prénom"]["Value"].values[0])
            except:
                listings.append("")

            try:
                listings.append(dataframes[dataframes["Label"]=="Date du début de la charge"]["Value"].values[0])
            except:
                listings.append("")

            try:
                listings.append(dataframes[dataframes["Label"]=="Date de fin de la charge"]["Value"].values[0])
            except:
                listings.append("")

            try:
                listings.append(dataframes[dataframes["Label"]=="Fonction"]["Value"].values[0])
            except:
                listings.append("")
            try:
                listings.append(dataframes[dataframes["Label"]=="Adresse du domicile"]["Value"].values[0])
            except:
                listings.append("")

        else:
            for loop in range(0,6):
                listings.append(x.text.replace("Légende par défaut","").strip().replace("\n"," "))

    except:
        for loop in range(0,6):
            listings.append("")

    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Établissements" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        
        try:
            listings.append(x.text.replace("Légende par défaut","").strip().replace("\n"," "))
        except:
            listings.append("")
        
    except:
        for loop in range(0,1):
            listings.append("")

    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Documents en traitement" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        
        try:
            listings.append(x.text.replace("Légende par défaut","").strip().replace("\n"," "))
        except:
            listings.append("")
        
    except:
        for loop in range(0,1):
            listings.append("")


    

    dataframes = pd.DataFrame()
    x = ""
    
    try:
        for l in soup.find_all("h3"):
            if "Index des noms" in l.text:
                x  = l.find_next("fieldset", class_="zonelibellechamp")
                break
        dataframes = getmefield(x)

        try:
            listings.append(dataframes[dataframes["Label"]=="Date de mise à jour de l'index des noms"]["Value"].values[0])
        except:
            listings.append("")
        
    except:
        for loop in range(0,1):
            listings.append("")

    #listings= []
    """
    t = pd.DataFrame(columns=scrapesite2headers)
    t.loc[len(t.index)] = listings
    listings= []
    
    if t["Nom"].values[0]=="":
        print(t["Prénom"].values[0]+" "+t["Nom de famille"].values[0])

        listings.append(t["Prénom"].values[0]+" "+t["Nom de famille"].values[0])

    else:
        
        listings.append(t["Nom"].values[0])
    
    listings.append(t["Adresse du domicile"].values[0])
    

    if t["Premier actionnaire Nom"].values[0]=="":
        print(t["Premier actionnaire Prénom"].values[0]+" "+t["Premier actionnaire Nom de famille"].values[0])
        listings.append(t["Premier actionnaire Prénom"].values[0]+" "+t["Premier actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Premier actionnaire Nom"].values[0])
    listings.append(t["Premier actionnaire Adresse du domicile"].values[0])

    if t["Deuxième actionnaire Nom"].values[0]=="":
        print(t["Deuxième actionnaire Prénom"].values[0]+" "+t["Deuxième actionnaire Nom de famille"].values[0])
        listings.append(t["Deuxième actionnaire Prénom"].values[0]+" "+t["Deuxième actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Deuxième actionnaire Nom"].values[0])
    listings.append(t["Deuxième actionnaire Adresse du domicile"].values[0])
    

    if t["Troisième actionnaire Nom"].values[0]=="":
        print(t["Troisième actionnaire Prénom"].values[0]+" "+t["Troisième actionnaire Nom de famille"].values[0])
        listings.append(t["Troisième actionnaire Prénom"].values[0]+" "+t["Troisième actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Troisième actionnaire Nom"].values[0])
    listings.append(t["Troisième actionnaire Adresse du domicile"].values[0])
     
    """
    t = pd.DataFrame(columns=scrapesite2headers)    
    # length_difference = len(scrapesite2headers) - len(listings)

    # # Append empty strings to listings if it's shorter than mirabelheaders2
    # if length_difference > 0:
    #     listings.extend([""] * length_difference)
    # elif length_difference < 0:
    #     listings = listings[:len(scrapesite2headers)]
    if len(listings)!=len(scrapesite2headers):
        fu = []
        for x in range(0,79):
            fu.append("Contains more values than expected!")
        return fu
    t.loc[len(t.index)] = listings
    listings= []
    
    if t["Nom"].values[0]=="":
        print(t["Prénom"].values[0]+" "+t["Nom de famille"].values[0])
        listings.append(t["Prénom"].values[0]+" "+t["Nom de famille"].values[0])
    else:
        listings.append(t["Nom"].values[0])
    
    listings.append(t["Adresse du domicile"].values[0])
    #2

    if t["Premier actionnaire Nom"].values[0]=="":
        #print(t["Premier actionnaire Prénom"].values[0]+" "+t["Premier actionnaire Nom de famille"].values[0])
        listings.append(t["Premier actionnaire Prénom"].values[0]+" "+t["Premier actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Premier actionnaire Nom"].values[0])
    listings.append(t["Premier actionnaire Adresse du domicile"].values[0])

    if t["Deuxième actionnaire Nom"].values[0]=="":
        #print(t["Deuxième actionnaire Prénom"].values[0]+" "+t["Deuxième actionnaire Nom de famille"].values[0])
        listings.append(t["Deuxième actionnaire Prénom"].values[0]+" "+t["Deuxième actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Deuxième actionnaire Nom"].values[0])
    listings.append(t["Deuxième actionnaire Adresse du domicile"].values[0])
    

    if t["Troisième actionnaire Nom"].values[0]=="":
        #print(t["Troisième actionnaire Prénom"].values[0]+" "+t["Troisième actionnaire Nom de famille"].values[0])
        listings.append(t["Troisième actionnaire Prénom"].values[0]+" "+t["Troisième actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Troisième actionnaire Nom"].values[0])

    listings.append(t["Troisième actionnaire Adresse du domicile"].values[0])

    if t["Quatrième actionnaire Nom"].values[0]=="":
        #print(t["Troisième actionnaire Prénom"].values[0]+" "+t["Troisième actionnaire Nom de famille"].values[0])
        listings.append(t["Quatrième actionnaire Prénom"].values[0]+" "+t["Quatrième actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Quatrième actionnaire Nom"].values[0])

    listings.append(t["Quatrième actionnaire Adresse du domicile"].values[0])
    
    if t["Cinquième actionnaire Nom"].values[0]=="":
        #print(t["Troisième actionnaire Prénom"].values[0]+" "+t["Troisième actionnaire Nom de famille"].values[0])
        listings.append(t["Cinquième actionnaire Prénom"].values[0]+" "+t["Cinquième actionnaire Nom de famille"].values[0])
    else:
        listings.append(t["Cinquième actionnaire Nom"].values[0])

    listings.append(t["Cinquième actionnaire Adresse du domicile"].values[0])
    
     
    #2+6
    #fix admin
    for loop in range(1,11):
        listings.append(t["Administrateurs Prénom  "+str(loop)+" "].values[0] + " "+t["Administrateurs Nom de famille  "+str(loop)+" "].values[0])
        listings.append(t["Administrateurs Adresse du domicile  "+str(loop)+" "].values[0])
        listings.append(t["Administrateurs Fonctions actuelles  "+str(loop)+" "].values[0])
    
    for loop in range(1,11):
        listings.append(t["Associés Nom "+str(loop)].values[0])
        listings.append(t["Associés Type d'associé "+str(loop)].values[0])
        listings.append(t["Associés Adresse "+str(loop)].values[0])

    #2+6+30    
    for loop in range(1,3):
        listings.append(t["Code d'activité économique (CAE)_"+str(loop)].values[0])
        listings.append(t["Activité_"+str(loop)].values[0])
        listings.append(t["Précisions (facultatives)_"+str(loop)].values[0])
    #2+6+30+6   
    for loop in range(1,2):
        listings.append(t["Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Nom de l'entreprise"].values[0])
        listings.append(t["Actionnaires ou tiers assumant les pouvoirs du conseil d'administration_Adresse du domicile"].values[0])
    #2+6+30+6+2
    for loop in range(1,2):
        listings.append(t["Dirigeants non membres du conseil d'administration _ Prénom"].values[0] + " "+t["Dirigeants non membres du conseil d'administration _ Nom de famille"].values[0])
        listings.append(t["Dirigeants non membres du conseil d'administration _ Adresse du domicile"].values[0])
        listings.append(t["Dirigeants non membres du conseil d'administration _ Fonctions actuelles"].values[0])
    #2+6+30+6+2+3

    #2+6+30+6+2+3+30
    #2+6+30+6+3

    #2+6+30+6+2+3

    #t.replace(u"\u2018", "'",inplace=True, regex=True)
    #t.replace(u"\u2019", "'",inplace=True, regex=True)

    #t =t[""]
    #print("XXXXXXXXX",len(listings))
    #t.to_csv("Input.csv",encoding="latin-1")
    return listings

 
def interme(funy,driver3):
    try:    
        tempcheck = 1
        while tempcheck:
            try:
                #Fix
                '''
                Massive optimization overhaul on the webdriver waits and the finally to close each web driver
                '''
                
                driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")
                ##Déconnexion du service
                time.sleep(3)
                WebDriverWait(driver3, timeout_duration).until(
                    EC.presence_of_element_located((By.XPATH, ".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']"))
                )
                element = driver3.find_element(By.XPATH, ".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
                tempcheck=0
                time.sleep(3)
                break
            except:
                print("exception in interme")
                safe_close_quit(driver3)
                time.sleep(600)
                driver3 = create_headless_driver3()
                time.sleep(1)
                driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")
                time.sleep(2)
                # try:
                #     #frame_element = driver3.find_element_by_id('cf-chl-widget-1ao4o')
                #     #driver3.switch_to.frame(frame_element)
                #     driver3.switch_to.frame(0)
                #     driver3.find_element(By.XPATH,".//input[@type='checkbox']").click()
                #     driver3.switch_to.default_content()
                #     time.sleep(5)
                #     element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
        
                #     tempcheck=0
                #     break
                # except:
                #     driver3.close();driver3.quit();
                #     #time.sleep(time)
                #     driver3 = create_headless_driver3
                #     driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")


        element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
        element.send_keys(str(funy))
        
        element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_CondUtil_CaseConditionsUtilisation_0']")
        is_checked = element.get_attribute("checked") is not None
        if not is_checked:
            element.click()

        element = driver3.find_element(By.XPATH,".//*[@name='ctl00$CPH_K1ZoneContenu1_Cadr$IdSectionRechSimple$IdSectionRechSimple$KRBTRechSimple$btnRechercher']")
        element.click()

        checknumber1 = 0
        checknumber2 = 0
        try:
            driver3.find_element(By.XPATH,".//*[@id='K1Acc_Contenu']").text 
        except:
            checknumber1 = 1

        try:
            table_html = driver3.find_elements(By.XPATH, "//table[@id='CPH_K1ZoneContenu1_Cadr_IdSectionResultat_IdSectionResultat_K1DetailsRecherche_K1GrilleDetail']")[0].get_attribute('outerHTML')
            # Now, use StringIO to create a file-like object from the HTML string
            html_io = StringIO(table_html)

            # Finally, use this file-like object with pd.read_html
            webtable_df = pd.read_html(html_io)[0]
        except:
            print("can't find Contenu1")
            return 0
        # if checknumber1==1 and checknumber2==1:
        #     print("Page is not loading!")
        #     driver3.close();driver3.quit();
        #     time.sleep(timefactorsimple)
        #     driver3 = create_headless_driver3()
        #     driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")
        #     time.sleep(timefactorsimple)
        
        #     tempcheck = 1

        #     while tempcheck:
        #         try:
        #             element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
        #             tempcheck=0
        #             break
        #         except:
        #             try:
        #                 #frame_element = driver3.find_element_by_id('cf-chl-widget-1ao4o')
        #                 #driver3.switch_to.frame(frame_element)
        #                 driver3.switch_to.frame(0)
        #                 driver3.find_element(By.XPATH,".//input[@type='checkbox']").click()
        #                 driver3.switch_to.default_content()
        #                 time.sleep(1)
        #                 element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
        
        #                 tempcheck=0
        #                 break
        #             except:
        #                 driver3.close();driver3.quit();
        #                 time.sleep(1)
        #                 driver3 = create_headless_driver3()
        #                 driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")
        
        #     element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
            
        #     element.send_keys(str(funy))
        #     #time.sleep(timefactorsimple)
            
        #     element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_CondUtil_CaseConditionsUtilisation_0']")
        #     element.click()
        #     #time.sleep(timefactorsimple)

        #     element = driver3.find_element(By.XPATH,".//*[@name='ctl00$CPH_K1ZoneContenu1_Cadr$IdSectionRechSimple$IdSectionRechSimple$KRBTRechSimple$btnRechercher']")
        #     element.click()
        #     #time.sleep(timefactorsimple)
        
        element = None
        element = driver3.find_element(By.XPATH,".//*[@id='K1Acc_Contenu']").text

        if "Aucun dossier n'a été retrouvé pour cette recherche" in element:
            """
            driver3.close();driver3.quit()
            time.sleep(10)

            driver3 = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
            driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")
            time.sleep(timefactorhard+20)
        
            try:
                element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
            except:
                try:
                    #frame_element = driver3.find_element_by_id('cf-chl-widget-1ao4o')
                    #driver3.switch_to.frame(frame_element)
                    driver3.switch_to.frame(0)
                    driver3.find_element(By.XPATH,".//input[@type='checkbox']").click()
                    driver3.switch_to.default_content()
                    time.sleep(60)
                except:
                    pass
            
            
            
            time.sleep(timefactorhard+10)
            
            element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
            
            element.send_keys(str(funy))
            time.sleep(timefactorhard)
            
            element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_CondUtil_CaseConditionsUtilisation_0']")
            element.click()
            time.sleep(timefactorsimple)

            element = driver3.find_element(By.XPATH,".//*[@name='ctl00$CPH_K1ZoneContenu1_Cadr$IdSectionRechSimple$IdSectionRechSimple$KRBTRechSimple$btnRechercher']")
            element.click()
            time.sleep(timefactorhard+10)

            element = driver3.find_element(By.XPATH,".//*[@id='K1Acc_Contenu']").text 
            time.sleep(timefactorsimple)
            """
            #if "Aucun dossier n'a été retrouvé pour cette recherche" in element:
            ################Fix
            #driver3.close()
            #driver3.quit()
            #time.sleep(2)

            return 0


        #time.sleep(timefactorsimple)
        #print("Waiting for execution!")
        #time.sleep(5)

        table = driver3.find_elements(By.XPATH, "//table[@id='CPH_K1ZoneContenu1_Cadr_IdSectionResultat_IdSectionResultat_K1DetailsRecherche_K1GrilleDetail']")[0].get_attribute('outerHTML')
        html_io = StringIO(table)
        # Now use this file-like object with pd.read_html
        webtable_df = pd.read_html(html_io)[0]
        webtable_df = webtable_df.dropna(how='all')
        data = webtable_df[webtable_df["Statut du nom"]=="En vigueur"]
        #FIX HAVE TO FIX THIS LOOP IF THERSE MORE PEOPLE. DATA COLLECTION NOT WORKING
        #try:
        # if len(data)>=1:
        #         #print("Data has multiple values!")
        #         data = data[data["Statut du nom"]=="En vigueur"]
        #         '''data['Similarity'] = data['Nom'].apply(lambda x: fuzz.ratio(funy, x))
        #         data = data.sort_values(by='Similarity', ascending=False)

        #         first_row_index = data.index[0]'''
        #         exactname = str(data.iloc[0]["Numéro de dossier"])
        #         #loop over table values and click on each
        #         #run in headless
        #         #if captcha then open in browser
        #         table_element = driver3.find_element(By.XPATH, "//table[@id='CPH_K1ZoneContenu1_Cadr_IdSectionResultat_IdSectionResultat_K1DetailsRecherche_K1GrilleDetail']")

        #         # Now find the link within this table. Adjust the XPath to point to the specific link.
        #         link_element = table_element.find_element(By.TAG_NAME, 'a')

        #         # Get the 'href' attribute from the link element
        #         href_attribute = link_element.get_attribute('href')
        #         print("issue")
        #         print(href_attribute)
        #         href_attribute = table.find_element(By.TAG_NAME, 'a').get_attribute('href')
        #         print("no issues")
        #         driver3.execute_script(href_attribute)
        #         time.sleep(1)
        #         #for loop to append all values




        #         '''element = driver3.find_elements(By.XPATH,"//table[@id = 'CPH_K1ZoneContenu1_Cadr_IdSectionResultat_IdSectionResultat_K1DetailsRecherche_K1GrilleDetail']//tr")[1:]
        #         link = element.find_element_by_tag_name('a')
        #         print(element)
        #         link.click()
                    
        #         elements = elements[first_row_index]

        #         time.sleep(1)
        #         link = elements.find_element_by_tag_name('a')
        #         link_text = link.text
                
        #         link_href = link.get_attribute('href')
        #         print(link)

        #         link.click()

        #         table = driver3.find_element_by_tag_name('table')
        #         print(table)
        #         link = table.find_element_by_tag_name('a')'''

        #         time.sleep(1)
        #         soup = BeautifulSoup(driver3.page_source, 'html.parser') 
        #         ############fix
        #         #driver3.close()
        #         #driver3.quit()

        #         return scrapesite2(soup,exactname,"")
                


        # else:
        data = data.copy()

        # Apply your fuzzy matching and add the 'Similarity' column
        data['Similarity'] = webtable_df['Nom'].apply(lambda x: fuzz.ratio(funy, x))
        data = data.sort_values(by='Similarity', ascending=False)
        
        first_row_index = data.index[0]
        exactname = str(data.iloc[0]["Numéro de dossier"])

        elements = driver3.find_elements(By.XPATH,"//table[@id = 'CPH_K1ZoneContenu1_Cadr_IdSectionResultat_IdSectionResultat_K1DetailsRecherche_K1GrilleDetail']//tr")[1:]

        try:

            elements = elements[first_row_index]
            link = elements.find_element(By.TAG_NAME,'a')
            link.click()
        except:
            first_row_index = data.index[0] #changed from 1 to 0
            exactname = str(data.iloc[1]["Numéro de dossier"])
            elements = elements[first_row_index]
            link = elements.find_element_by_tag_name('a')
            link.click()

        time.sleep(1)
        soup = BeautifulSoup(driver3.page_source, 'html.parser')
        #########fix
        #driver3.close();driver3.quit()

        return scrapesite2(soup,exactname,"")    
    except Exception as e:
        # Handle exceptions if needed
        print("error1")
        print(f"An error occurred: {e}")
        error_message = str(e)
        if "Max retries exceeded" in error_message:
            print("Max retries error detected. Shutting down.")
            safe_close_quit(driver)
            safe_close_quit(driver3)
            sys.exit(1)  # Exits the program with an error status
        safe_close_quit(driver)
        safe_close_quit(driver3)
        time.sleep(600)
        driver = create_headless_driver1()
        driver3 = create_headless_driver3()
        # Optionally return or handle the error
        return 2

def getmeaworkingproxy():
    file_path = 'Proxies.txt'  
    with open(file_path, 'r') as file:
        line = file.readline()
        return line.strip()

        while line:
            print(line.strip())
            print("Testing proxy!",line.strip())
            options2 = webdriver.ChromeOptions()
            options2.add_argument("--start-maximized")
            options2.add_argument('--user-agent='+line.strip())

            driver3 = webdriver.Chrome(2,executable_path=DRIVER_PATH)
            driver3.get("https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx?T1.CodeService=S00436&Clng=F&WT.co_f=2dbdfa4e917581b1bd01658768107903")
            time.sleep(timefactorhard)            
            line = file.readline()

            try:
                time.sleep(5)
                element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
                return line.strip()
            except:
                try:
                    time.sleep(10)
                    driver3.switch_to.frame(0)
                    driver3.find_element(By.XPATH,".//input[@type='checkbox']").click()
                    driver3.switch_to.default_content()
                    time.sleep(10)
                    element = driver3.find_element(By.XPATH,".//*[@id='CPH_K1ZoneContenu1_Cadr_IdSectionRechSimple_IdSectionRechSimple_K1Fieldset1_ChampRecherche__cs']")
                    time.sleep(10)
                    return line.strip()
                
                except:
                    driver3.close();driver3.quit();time.sleep(2)
                
line = 1
 
#driver = uc.Chrome() 
# options = uc.ChromeOptions() 
# options.add_argument("--start-maximized")
#options.add_argument("--headless")
#driver = uc.Chrome() 


mirabeldataframe = pd.DataFrame(columns=mirabelheaders)
mirabeldataframe2 = pd.DataFrame(columns=mirabelheaders2)

def mirabeltypescraper(driver,name,currFile,number,driver3,selected_type):
    import pandas as pd
    listings = []
    
    listings.append(number)
    
    table = WebDriverWait(driver, timeout_duration).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))[1].get_attribute('outerHTML')
    html_io = StringIO(table)
    webtable_list = pd.read_html(html_io)

    webtable_df1 = webtable_list[8]
    webtable_df2 = webtable_list[10].iloc[:-1]
    webtable_df3 = pd.concat([webtable_list[13], webtable_list[14]], ignore_index=True)
    webtable_df4 = webtable_list[18]

    webtable_df = pd.concat([webtable_df1, webtable_df2, webtable_df3, webtable_df4], ignore_index=True)

    # Drop rows in the DataFrame where all elements are NaN
    v = webtable_df.dropna(how='all')
    new_column_names = {0: 'A', 1: 'B'}
    v.rename(columns=new_column_names, inplace=True)
    isPhysique = False

    v["A"] = v["A"].str[:-2]
    print(v)
    ######VPN => if error 500 => either try again later or switch vpn locsation
    

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Adresse"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Arrondissement"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Cadastre(s) et numéro(s) de lot"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Numéro matricule"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Utilisation prédominante"]["B"].values[0])
    except:
        listings.append("")


    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Dossier no"]["B"].values[0])
    except:
        listings.append("")



    
    for i in range(5):
        try:
            #print(v[v[0].str.contains(Adresse")][1].values[0])
            
            listings.append(v[v["A"]=="Nom"]["B"].values[i])
        except:
            listings.append("")

        try:
            #print(v[v[0].str.contains(Adresse")][1].values[0])
            listings.append(v[v["A"]=="Statut aux fins d'imposition scolaire"]["B"].values[i])
        except:
            listings.append("")

        try:
            #print(v[v[0].str.contains(Adresse")][1].values[0])
            listings.append(v[v["A"]=="Casier postal"]["B"].values[i])
        except:
            listings.append("")

        try:
            #print(v[v[0].str.contains(Adresse")][1].values[0])
            listings.append(v[v["A"]=="Adresse postale"]["B"].values[i])
        except:
            listings.append("")

        try:
            #print(v[v[0].str.contains(Adresse")][1].values[0])
            listings.append(v[v["A"]=="Date d'inscription au rôle"]["B"].values[i])
        except:
            listings.append("")

        try:
            #print(v[v[0].str.contains(Adresse")][1].values[0])
            listings.append(v[v["A"]=="Condition particulière d'inscription"]["B"].values[i])
        except:
            listings.append("")


    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Mesure frontale"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Superficie"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Numéro de compte foncier"]["B"].values[0])
    except:
        listings.append("")




    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Zonage municipal"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Zonage agicole"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Nombre d'étages"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Année de construction"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v['0'].str.contains("Adresse postale")]['1'].values[0])
        listings.append(v[v["A"] == "Aire d'étages"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Genre de construction"]["B"].values[0])
    except:
        listings.append("")
    
    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Lien physique"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Nombre de logements"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Nombre de locaux non résidentiels"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Nombre de chambres locatives"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Numéro d'unité de voisinage"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Superficie totale"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Superficie en zone agricole"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v['0'].str.contains("Condition particulière d'inscription")]['1'].values[0])
        listings.append(v[v[0] == "Superficie visée par imposition maximale"]["B"].values[0])
    except:
        listings.append("")
    
    try:
        #print(v[v['0'].str.contains("Condition particulière d'inscription")]['1'].values[0])
        listings.append(v[v[0] == "Superficie totale"]["B"].values[1])
    except:
        listings.append("")

    







    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Date de référence au marché"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Valeur du terrain"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Valeur du bâtiment"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Valeur de l'immeuble"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Date de référence au marché"]["B"].values[1])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Valeur de l'immeuble au rôle antérieur"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Catégorie et classe d'immeuble à des fins d'application des taux variés de taxation"]["B"].values[0])
    except:
        listings.append("")
    
    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Valeur imposable de l'immeuble"]["B"].values[0])
    except:
        listings.append("")

    try:
        #print(v[v[0].str.contains(Adresse")][1].values[0])
        listings.append(v[v["A"]=="Valeur non imposable de l'immeuble"]["B"].values[0])
    except:
        listings.append("")


    '''#print(listings)
    try:
        v = v.iloc[v[v['A'] == "Numéro de dossier"].index[0] + 1:]
        v.reset_index(inplace=True)
        
        #for l in v["Propriétaire" in v['A']].index:
        #prop_list = [col for col in v['A'] if 'Propriétaire' in col]
        for l in v[v['A'] .str[:12] == 'Propriétaire'].index:
            listings.extend(v.iloc[l:l+6]["B"].values)
            
        if len(v[v['A'].str[:12] == 'Propriétaire'].index)==1:
            for loop in range(0,24):
                listings.append("")
        
        if len(v[v['A'].str[:12] == 'Propriétaire'].index)==2:
            for loop in range(0,18):
                listings.append("")
        if len(v[v['A'].str[:12] == 'Propriétaire'].index)==3:
            for loop in range(0,12):
                listings.append("")
        if len(v[v['A'].str[:12] == 'Propriétaire'].index)==4:
            for loop in range(0,6):
                listings.append("")
    except:
        for loop in range(0,30):
                listings.append("")

    try:
        start = v[v['A'].str[:26] == "Date d'inscription au rôle"].index[-1]+1
        end = v[v['A'] == "Valeur de l'immeuble au rôle antérieur"].index[0]
        listings.extend(v.iloc[start:end+1]["B"].values)
    except:
        listings = [listings[0]]
        for _ in range(1, 53):
            listings.append('Does not exist!')'''

    # Drop rows in the DataFrame where all elements are NaN
    #print(data)
    #print(data[1].values[0:8])
    
    numbers = 0
    cc = 0
    for loop in listings:
        if loop=="":
            cc=cc+1
    if cc>80:
        print("It is null")
        return False
    
    print(len(mirabelheaders))
    print(len(listings))
    if len(listings)!=len(mirabelheaders):
        listings = []
        listings.append(numbers)
        for loop in range(0,len(mirabelheaders)-1):
            listings.append("Contains more values than expected!")
        mirabeldataframe.loc[len(mirabeldataframe.index)] = listings
    else:
        mirabeldataframe.loc[len(mirabeldataframe.index)] = listings
    
    scrappednumbers = mirabeldataframe['Numbers'].values
    global originalnumberlist
    import os
    ###Fix
    originalnumberlist = pd.read_csv("DataAreaNumbers\\"+name+os.sep+name+".csv")["Numbers"].values
    
    duplia1 = list(set(originalnumberlist)-set(scrappednumbers))  
    global curr_datetime
    #mirabeldataframe.to_csv("C:\\Users\\kl\\Desktop\\Testing Airtasker\\Jonathan\\Websites list\\ResultsAreaNumbers\\"+name+"\\Data_latin_original_"+str(curr_datetime)+".csv",encoding = "latin-1")
    templaval = mirabeldataframe.copy()

    templaval["Superficie"] = templaval["Superficie"].apply(formatmeter)
    templaval["Mesure frontale"] = templaval["Mesure frontale"].apply(formatmeter)
    templaval["Aire d'étages"] = templaval["Aire d'étages"].apply(formatmeter)

    templaval["Valeur du terrain"] = templaval["Valeur du terrain"].apply(formatdollars)
    templaval["Valeur du bâtiment"] = templaval["Valeur du bâtiment"].apply(formatdollars)
    templaval["Valeur de l'immeuble"] = templaval["Valeur de l'immeuble"].apply(formatdollars)
    templaval["Valeur de l'immeuble au rôle antérieur"] = templaval["Valeur de l'immeuble au rôle antérieur"].apply(formatdollars)

    #templaval["Valeur imposable de l'immeuble"] = templaval["Valeur imposable de l'immeuble"].apply(formatdollars)
    #templaval["Valeur non imposable de l'immeuble"] = templaval["Valeur non imposable de l'immeuble"].apply(formatdollars)      
    #templaval["Date d'inscription au rôle"] = templaval["Date d'inscription au rôle"].apply(formatdate)
    #emplaval["Date de référence au marché"] = templaval["Date de référence au marché"].apply(formatdate)
    '''print(templaval)'''




    '''cleaned = templaval[~templaval["Adresse"].str.contains("Does not exist!")]'''
    cleaned = templaval
    #cleaned.to_csv("C:\\Users\\kl\\Desktop\\Testing Airtasker\\Jonathan\\Websites list\\ResultsAreaNumbers\\"+name+"\\Data_latin_processed_"+str(curr_datetime)+".csv",encoding = "latin-1")
    duplia2 = mirabeldataframe[mirabeldataframe["Adresse"].str.contains(r'^\s*$', na=False)]["Numbers"].values
    tempnumbers = pd.DataFrame()
    tempnumbers["Numbers"] = Union(duplia1, duplia2)
    #tempnumbers.to_csv("C:\\Users\\kl\\Desktop\\Testing Airtasker\\Jonathan\\Websites list\\DataAreaNumbers\\"+name+"\\NoResults_"+str(curr_datetime)+".csv",index=False)
    last_row = cleaned.tail(1)
        
    newcols = []
    for m in last_row.columns:
        try:
            if m.split("_")[0]=="Nom":
                newcols.append(m)
        except:
            pass

    newvalues = []
    ####TODO
    ####Fix
    isError = False
    tmp = 0
    for m in last_row[newcols].values:
        
        for mm in m:
            if len(mm)>5:
                newvalues.append(mm)
                if(selected_type) ==1 and not isPhysique:
                    tmp = interme(mm,driver3)
                else:
                    tmp =3
                try:
                    if isinstance(tmp, list):
                        listings.extend(tmp)
                    elif tmp==0:
                        for loop in range(0,79):
                            isError = True
                            listings.append("Does not exist!")
                    elif tmp==1:
                        for loop in range(0,79):
                            isError = True
                            listings.append("Does not contain En vigueur!")

                    elif tmp==2:
                        for loop in range(0,79):
                            listings.append("Unexpected error")
                    elif tmp==3:
                        for loop in range(0,79):
                            listings.append("")
                except:
                    for loop in range(0,79):
                        listings.append("Unexpected error")

            else:
                for loop in range(0,79):
                    listings.append("")


    global mirabeldataframe2
    print(len(mirabeldataframe2))
    # print(len(listings))
    # print(len(mirabelheaders2))
    print("Done!")
    length_difference = len(mirabelheaders2) - len(listings)

    # Append empty strings to listings if it's shorter than mirabelheaders2
    if length_difference > 0:
        listings.extend([""] * length_difference)
    elif length_difference < 0:
        listings = listings[:len(mirabelheaders2)]
        print(listings)

    # Now you can safely add the listings to your dataframe
    mirabeldataframe2.loc[len(mirabeldataframe2.index)] = listings
    #mirabeldataframe2.loc[len(mirabeldataframe2.index)] = listings

    scrappednumbers = mirabeldataframe2['Numbers'].values
    originalnumberlist = pd.read_csv("DataAreaNumbers\\"+currFile, encoding='ISO-8859-1')["Numbers"].values

    duplia1 = list(set(originalnumberlist)-set(scrappednumbers))  

    #global curr_datetime
    #def changecolumnorder(mirabeldataframe2):
    #    return mirabeldataframe2[newordermirabelheaders2]
    op = mirabeldataframe2[newordermirabelheaders2]  
    op.replace(u"\u2018", "'",inplace=True, regex=True)
    op.replace(u"\u2019", "'",inplace=True, regex=True)
    ###Fix
    # Splitting the string to remove the path ("Montreal/") and the extension (".csv")
    filename_str = str(currFile)
    required_string = filename_str.split('\\')[1].split('.')[0]

    #op.to_csv("ResultsAreaNumbers"+os.sep+name+os.sep+"Data_latin_original_"+str(curr_datetime)+".csv",encoding = "latin-1")
    op.to_csv("ResultsAreaNumbers"+os.sep+name+os.sep+"processed_"+required_string+"_"+str(curr_datetime)+".csv", encoding="latin-1", errors="replace")
    templaval = mirabeldataframe2.copy()
    templaval["Superficie"] = templaval["Superficie"].apply(formatmeter)
    templaval["Mesure frontale"] = templaval["Mesure frontale"].apply(formatmeter)
    templaval["Aire d'étages"] = templaval["Aire d'étages"].apply(formatmeter)
    templaval["Valeur du terrain"] = templaval["Valeur du terrain"].apply(formatdollars)
    templaval["Valeur du bâtiment"] = templaval["Valeur du bâtiment"].apply(formatdollars)
    templaval["Valeur de l'immeuble"] = templaval["Valeur de l'immeuble"].apply(formatdollars)
    templaval["Valeur de l'immeuble au rôle antérieur"] = templaval["Valeur de l'immeuble au rôle antérieur"].apply(formatdollars)

    #templaval["Valeur imposable de l'immeuble"] = templaval["Valeur imposable de l'immeuble"].apply(formatdollars)
    #templaval["Valeur non imposable de l'immeuble"] = templaval["Valeur non imposable de l'immeuble"].apply(formatdollars)

    '''templaval['Arrondissement'].replace('Arrondissement de','',inplace=True)
    templaval['Arrondissement'].replace('Arrondissement du','',inplace=True)
    cleaned = templaval[~templaval["Adresse"].str.contains("Does not exist!")]'''
    cleaned = templaval
    op = cleaned[newordermirabelheaders2] 
    op.replace(u"\u2018", "'",inplace=True, regex=True)
    op.replace(u"\u2019", "'",inplace=True, regex=True)
    ###Fix
    #op.to_csv("ResultsAreaNumbers"+os.sep+name+os.sep+"processed"+str(curr_datetime)+".csv",encoding = "latin-1")
    
    op.to_csv("ResultsAreaNumbers"+os.sep+name+os.sep+"processed_"+required_string+"_"+str(curr_datetime)+".csv", encoding="latin-1", errors="replace")
    duplia2 = mirabeldataframe2[mirabeldataframe2["Adresse"].str.contains(r'^\s*$', na=False)]["Numbers"].values
    tempnumbers = pd.DataFrame()
    tempnumbers["Numbers"] = Union(duplia1, duplia2)
    tempnumbers.replace(u"\u2018", "'",inplace=True, regex=True)
    tempnumbers.replace(u"\u2019", "'",inplace=True, regex=True)   
        # Define the file path
    file_path = os.path.join("DataAreaNumbers", name, "NoResults_" + str(required_string) + "_" + str(curr_datetime) + ".csv")
    # Write to the CSV file
    tempnumbers.to_csv(file_path, index=False)
    # Writing to files based on the condition
    if isError:
        # Define the file path
        file_path = os.path.join("DataAreaNumbers", name, "Doesnt Exist - " + str(required_string) + "_" + str(curr_datetime) + ".csv")
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the existing data
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
        else:
            # If the file doesn't exist, create a new DataFrame with the 'Numbers' column
            df = pd.DataFrame(columns=['Numbers'])


        # Create a new DataFrame from 'numbers'
        new_data = pd.DataFrame([{'Numbers': number}])

        # Append new data to the 'Numbers' column using pd.concat
        df = pd.concat([df, new_data], ignore_index=True)

        # Write the DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

    #tempnumbers.to_csv("DataAreaNumbersRegistration"+os.sep+name+os.sep+"NoResults_Montreal"+str(curr_datetime)+".csv",index=False)
    return True        
        
#from pywinauto import Application


def pdfscrapper(driver,name,currFile,number,driver3,selected_type):
    destination="ResultsAreaNumbers"+os.sep+name
    if not os.path.isdir(destination):
        os.mkdir(destination)

    if name=="Beauharnois":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Beloeil":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Blainville":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Boisbriand":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Bromont":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Candiac":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Chambly":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Chateauguay":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Farnham":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Joliette":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Lâile-Perrot":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Lachute":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Mirabel":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Mont-Saint-Hilaire":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Notre-Dame-de-Lâile-Perrrot":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Notre-Dame-des-Prairies":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Repentigny":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Saint-Basile-Le-Grand":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Saint-Jean-sur-Richelieu":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Saint-Jerome":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Sherbrooke":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    elif name=="Terrebonne":
        return mirabeltypescraper(driver,name,currFile,number,driver3,selected_type)
    




originalnumberlist = []

driver1Number = 0
def scraperbynumber(Name,filename,selected_type,manualnumber=""):
    try:
        data = pd.read_csv("FinalInfomationAboutAreasPDFtype2.csv",index_col=0, encoding='ISO-8859-1')
    except:
        print(os.getcwd)
        print("not right folder!")
    
    areaname = data[data["AreaName"]==Name]["AreaName"].values[0]
    link = data[data["AreaName"]==Name]["Links"].values[0]
    path_parts = filename.replace('\\', '/').split('/')
    
    # Find the index of the desired directory ('Montreal') in the path
    montreal_index = path_parts.index(optVariable.get())
    # Reconstruct the path from 'Montreal' onwards
    currFile = os.sep.join(path_parts[montreal_index:])
    filename_str = str(currFile)
    required_string = filename_str.split('\\')[1].split('.')[0]

    allfiles = [filename]

    driver = create_headless_driver1()
    driver3 = create_headless_driver3()

    global mirabeldataframe
    mirabeldataframe = pd.DataFrame(columns=mirabelheaders)
    num_tries = 9
    for funy in allfiles:

        numberslist = pd.read_csv(funy, encoding='ISO-8859-1')
        numberslist = numberslist['Numbers'].values
        originalnumberlist = numberslist

    
        label_6.config(text="Starting Scraper for : "+ areaname+" using Cadastre Number")

        tempcounter = 0
        directory = '..\\VPN'
        ip_list = []
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                ip_list.append(file)

        print('Connecting to IP', ip_list[0])
        VPN('connect', ip_list[0])
        for loop in range(0,len(numberslist)):

            try:
                singlenumber = str(numberslist[loop].replace(" ","").strip())
            except:
                singlenumber = str(numberslist[loop])

            link_num = 0
            singlenumber = numberslist[loop]
            singlename = random_char(10)+str(singlenumber).replace('-', '')
            singleserver = listofservers[loop%len(listofservers)]
            singleemail = singlename+"@"+singleserver
            itworked = True
            regenerateemail = False
            
            stepnumber = 0
            print("WORKING!!!!!!!")

            while itworked:
                if line==1:
                    try:
                        
                        #driver = Driver(uc=True)
                        ##FIX

                        #ADD PROXY WHEN MAX LIMIT REACHED
                        '''
                        Massive optimization overhaul on the webdriver waits and the finally to close each web driver
                        '''
                        if len(driver.window_handles) == 2:
                            before = driver.window_handles[0]
                            driver.close()
                            driver.switch_to.window(before)
                        driver.get(link)

                        WebDriverWait(driver, timefactorhard).until(
                            EC.presence_of_all_elements_located((By.XPATH, ".//a[@class='btn nav-btn']"))
                        )[1].click()

                        try:
                            #driver.find_element(By.XPATH,"//button[contains(@class,'cky-btn cky-btn-accept')]").click()
                            division = WebDriverWait(driver, timefactorhard).until(
                                EC.presence_of_element_located((By.XPATH, ".//input[@id='Division']"))
                                )
                            division.send_keys(str(singlenumber).split('-')[0])

                            section = WebDriverWait(driver, timefactorhard).until(
                                EC.presence_of_element_located((By.XPATH, ".//input[@id='Section']"))
                                )
                            section.send_keys(str(singlenumber).split('-')[1])

                            emplacement = WebDriverWait(driver, timefactorhard).until(
                                EC.presence_of_element_located((By.XPATH, ".//input[@id='Emplacement']"))
                                )
                            emplacement.send_keys(str(singlenumber).split('-')[2])

                            if len(str(singlenumber).split('-')) > 3:
                                cav = WebDriverWait(driver, timefactorhard).until(
                                    EC.presence_of_element_located((By.XPATH, ".//input[@id='CAV']"))
                                    )
                                cav.send_keys(str(singlenumber).split('-')[3])

                            if len(str(singlenumber).split('-')) > 4:
                                batiment = WebDriverWait(driver, timefactorhard).until(
                                    EC.presence_of_element_located((By.XPATH, ".//input[@id='Batiment']"))
                                    )
                                batiment.send_keys(str(singlenumber).split('-')[4])

                            if len(str(singlenumber).split('-')) > 5:
                                local = WebDriverWait(driver, timefactorhard).until(
                                    EC.presence_of_element_located((By.XPATH, ".//input[@id='Local']"))
                                    )
                                local.send_keys(str(singlenumber).split('-')[5])
                        except:
                            pass

                        WebDriverWait(driver, timeout_duration).until(
                            EC.presence_of_element_located((By.XPATH, ".//input[@id='ty_rapport_eval']"))
                        ).click()
                        
                        WebDriverWait(driver, timeout_duration).until(
                            EC.element_to_be_clickable((By.XPATH, ".//button[@id='btnSearch']"))
                        ).click()

                        time.sleep(5)
                        tmp = WebDriverWait(driver, timeout_duration).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
                        try:
                            link_list = WebDriverWait(tmp, timeout_duration).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
                        except:
                            print('Matricule does not exist!')
                            link_list = []
                        if len(link_list) > 0:
                            if len(link_list[link_num].text) == 0:
                                link_num += 1
                            link_list[link_num].click()
                            time.sleep(5)


                            try:
                                
                                WebDriverWait(driver, timeout_duration).until(
                                    EC.presence_of_element_located((By.XPATH, ".//input[@id='mail_usager']"))
                                ).send_keys(singleemail)

                                driver.find_elements(By.XPATH, ".//button[@class='btn btn-default btn-acceo']")[1].click()

                                driver2 = create_headless_driver2()
                                driver2.get('https://www.fakemailgenerator.com/#/' + singleserver + '/' + singlename + '/')

                                now = WebDriverWait(driver2, 120).until(
                                    EC.presence_of_element_located((By.XPATH, ".//iframe[@id='emailFrame']"))
                                ).get_attribute('src')

                                driver2.get(now)
                                elem = driver2.find_element(By.TAG_NAME, 'strong').text

                                driver2.close()
                                driver2.quit()

                                driver.find_element(By.XPATH, ".//input[@id='code']").send_keys(elem)
                                driver.find_elements(By.XPATH, ".//button[@class='btn btn-default btn-acceo']")[1].click()
                                
                            except:
                                pass

                            time.sleep(6)
                            researchButton = WebDriverWait(driver, timeout_duration).until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='btn btn-default btn-acceo']")))
                            researchButton.click()
                            time.sleep(7)

                            try:
                                before = driver.window_handles[0]
                                after = driver.window_handles[1]

                                driver.switch_to.window(after)

                                l = WebDriverWait(driver, timeout_duration).until(
                                    EC.presence_of_element_located((By.XPATH, ".//iframe[@name='Report_PDF_Zone']"))
                                ).get_attribute('src')

                                driver.get(l)
                                time.sleep(5)

                                table = WebDriverWait(driver, timeout_duration).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))[1].get_attribute('outerHTML')
                                html_io = StringIO(table)
                                webtable_list = pd.read_html(html_io)

                                webtable_df1 = webtable_list[8]
                                webtable_df2 = webtable_list[10].iloc[:-1]
                                webtable_df3 = pd.concat([webtable_list[13], webtable_list[14]], ignore_index=True)
                                webtable_df4 = webtable_list[18]

                                webtable_df = pd.concat([webtable_df1, webtable_df2, webtable_df3, webtable_df4], ignore_index=True)
                            except:
                                itworked=False
                                listings = []
                                try:
                                    listings.append(str(numberslist[loop]).replace(" ","").strip())
                                except:
                                    listings.append(str(numberslist[loop]))

                                for t in range(0,len(newordermirabelheaders2)-1):
                                    listings.append("Does not exist!")
                                continue

                                '''#mirabeldataframe2.loc[len(mirabeldataframe2.index)] = listings
                                #mirabeldataframe2.replace(u"\u2018", "'",inplace=True, regex=True)
                                #mirabeldataframe2.replace(u"\u2019", "'",inplace=True, regex=True)
                                #Fix
                                file_path = os.path.join("DataAreaNumbers", Name, "Doesnt Exist - " + +str(required_string) + "_" + str(curr_datetime) + ".csv")
                                # Check if the file exists
                                if os.path.exists(file_path):
                                    # Read the existing data
                                    df = pd.read_csv(file_path, encoding='ISO-8859-1')
                                else:
                                    # If the file doesn't exist, create a new DataFrame with the required column
                                    df = pd.DataFrame(columns=['Numbers'])  # Replace 'YourColumnName' with your actual column name
                                # Append new data to the specified column
                                # If the column doesn't exist, it will be created
                                first_column_name = df.columns[0] if not df.empty else 'DefaultColumn'
                                df.loc[len(df)] = {first_column_name: singlenumber}

                                # Write the DataFrame back to the CSV file
                                df.to_csv(file_path, index=False)


                                #mirabeldataframe2.to_csv("ResultsAreaNumbers"+os.sep+Name+os.sep+"Data_latin_original_"+str(curr_datetime)+".csv",encoding = "latin-1", errors="replace")
                                ###Fix
                                #driver.close()
                                #driver.quit();
                                continue'''
                            if pdfscrapper(driver,Name,currFile,numberslist[loop],driver3,selected_type):
                                #driver.close();
                                #driver.quit();
                                link_num += 1
                                if link_num < len(link_list):
                                    itworked=True
                                else:
                                    itworked=False
                                continue
                            else:
                                itworked=False
                                listings = []
                                try:
                                    listings.append(str(numberslist[loop]).replace(" ","").strip())
                                except:
                                    listings.append(str(numberslist[loop]))

                                for t in range(0,len(newordermirabelheaders2)-1):
                                    listings.append("Does not exist!")

                                continue
                        else:
                            itworked=False
                            listings = []
                            try:
                                listings.append(str(numberslist[loop]).replace(" ","").strip())
                            except:
                                listings.append(str(numberslist[loop]))

                            for t in range(0,len(newordermirabelheaders2)-1):
                                listings.append("Does not exist!")
                                
                    except Exception as e:
                        itworked = True
                        VPN('disconnect', ip_list[0])
                        ip_list = ip_list[1:]
                        print('Connecting to IP', ip_list[0])
                        VPN('connect', ip_list[0])
                        '''# Handle exceptions if needed
                        print("error2")
                        print(f"An error occurred: {e}")
                        # Optionally return or handle the error
                        itworked = False
                        safe_close_quit(driver)
                        safe_close_quit(driver3)
                        time.sleep(600)
                        driver = create_headless_driver1()
                        driver3 = create_headless_driver3()
                        #except:
                        #    pass
                        #itworked=False'''
    print("Were done scraping!")
    safe_close_quit(driver)
    safe_close_quit(driver3)



def scraperbylot(Name,filename,selected_type,manualnumber=""):
    data = pd.read_csv("FinalInfomationAboutAreasPDFtype2.csv",index_col=0, encoding='ISO-8859-1')
    areaname = data[data["AreaName"]==Name]["AreaName"].values[0]
    link = data[data["AreaName"]==Name]["Links"].values[0]
    path_parts = filename.replace('\\', '/').split('/')

    #if find cant access then call proxy, safe close and call continue 

    # Find the index of the desired directory ('Montreal') in the path
    montreal_index = path_parts.index(optVariable.get())
    # Reconstruct the path from 'Montreal' onwards
    currFile = os.sep.join(path_parts[montreal_index:])
    filename_str = str(currFile)
    required_string = filename_str.split('\\')[1].split('.')[0]

    allfiles = [filename]

    driver = create_headless_driver1()
    driver3 = create_headless_driver3()
    
    global mirabeldataframe
    mirabeldataframe = pd.DataFrame(columns=mirabelheaders)
    for funy in allfiles:

        numberslist = pd.read_csv(funy, encoding='ISO-8859-1')
        numberslist = numberslist['Numbers'].values
        originalnumberlist = numberslist

    
        label_6.config(text="Starting Scraper for : "+ areaname+" using Lot Number")

        tempcounter = 0
        directory = '..\\VPN'
        ip_list = []
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                ip_list.append(file)

        print('Connecting to IP', ip_list[0])
        VPN('connect', ip_list[0])
        for loop in range(0,len(numberslist)):
           
            try:
                singlenumber = str(numberslist[loop].replace(" ","").strip())
            except:
                singlenumber = str(numberslist[loop])


            link_num = 0
            singlenumber = numberslist[loop]
            singlename = random_char(10)+str(singlenumber)
            singleserver = listofservers[loop%len(listofservers)]
            singleemail = singlename+"@"+singleserver
            itworked = True
            regenerateemail = False
            print("WORKING!!!!!!!")

            while itworked:
                if line==1:
                    try:
                        
                        #driver = Driver(uc=True)
                        ##FIX

                        '''
                        Massive optimization overhaul on the webdriver waits and the finally to close each web driver
                        '''
                        if len(driver.window_handles) == 2:
                            before = driver.window_handles[0]
                            driver.close()
                            driver.switch_to.window(before)

                        driver.get(link)

                        WebDriverWait(driver, timefactorhard).until(
                            EC.presence_of_all_elements_located((By.XPATH, ".//a[@class='btn nav-btn']"))
                        )[2].click()

                        try:
                            #driver.find_element(By.XPATH,"//button[contains(@class,'cky-btn cky-btn-accept')]").click()
                            WebDriverWait(driver, timefactorhard).until(
                                EC.presence_of_element_located((By.XPATH, ".//input[@id='NoCadastre']"))
                                ).send_keys(str(singlenumber))
                        except:
                            pass

                        WebDriverWait(driver, timeout_duration).until(
                            EC.presence_of_element_located((By.XPATH, ".//input[@id='ty_rapport_eval']"))
                        ).click()
                        
                        WebDriverWait(driver, timeout_duration).until(
                            EC.element_to_be_clickable((By.XPATH, ".//button[@id='btnSearch']"))
                        ).click()

                        time.sleep(5)
                        tmp = WebDriverWait(driver, timeout_duration).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
                        try:
                            link_list = WebDriverWait(tmp, timeout_duration).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
                        except:
                            print('Lot Number does not exist!')
                            link_list = []
                        if len(link_list) > 0:
                            if len(link_list[link_num].text) == 0:
                                link_num += 1
                            link_list[link_num].click()
                            time.sleep(5)



                            try:
                                
                                WebDriverWait(driver, timeout_duration).until(
                                    EC.presence_of_element_located((By.XPATH, ".//input[@id='mail_usager']"))
                                ).send_keys(singleemail)

                                driver.find_elements(By.XPATH, ".//button[@class='btn btn-default btn-acceo']")[1].click()

                                driver2 = create_headless_driver2()
                                driver2.get('https://www.fakemailgenerator.com/#/' + singleserver + '/' + singlename + '/')

                                now = WebDriverWait(driver2, 60).until(
                                    EC.presence_of_element_located((By.XPATH, ".//iframe[@id='emailFrame']"))
                                ).get_attribute('src')

                                driver2.get(now)
                                elem = driver2.find_element(By.TAG_NAME, 'strong').text

                                driver2.close()
                                driver2.quit()

                                driver.find_element(By.XPATH, ".//input[@id='code']").send_keys(elem)
                                driver.find_elements(By.XPATH, ".//button[@class='btn btn-default btn-acceo']")[1].click()
                                
                            except:
                                pass
                            time.sleep(6)
                            researchButton = WebDriverWait(driver, timeout_duration).until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='btn btn-default btn-acceo']")))
                            researchButton.click()
                            time.sleep(7)

                            try:
                                before = driver.window_handles[0]
                                after = driver.window_handles[1]

                                driver.switch_to.window(after)

                                l = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((By.XPATH, ".//iframe[@name='Report_PDF_Zone']"))
                                ).get_attribute('src')

                                driver.get(l)
                                time.sleep(5)

                                table = WebDriverWait(driver, timeout_duration).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))[1].get_attribute('outerHTML')
                                html_io = StringIO(table)
                                webtable_list = pd.read_html(html_io)

                                webtable_df1 = webtable_list[8]
                                webtable_df2 = webtable_list[10].iloc[:-1]
                                webtable_df3 = pd.concat([webtable_list[13], webtable_list[14]], ignore_index=True)
                                webtable_df4 = webtable_list[18]

                                webtable_df = pd.concat([webtable_df1, webtable_df2, webtable_df3, webtable_df4], ignore_index=True)

                            except:
                                itworked=False
                                listings = []
                                try:
                                    listings.append(str(numberslist[loop]).replace(" ","").strip())
                                except:
                                    listings.append(str(numberslist[loop]))

                                for t in range(0,len(newordermirabelheaders2)-1):
                                    listings.append("Does not exist!")


                                #mirabeldataframe2.loc[len(mirabeldataframe2.index)] = listings

                                #mirabeldataframe2.replace(u"\u2018", "'",inplace=True, regex=True)
                                #mirabeldataframe2.replace(u"\u2019", "'",inplace=True, regex=True)
                                #Fix
                                #Added errors="replace"
                                #mirabeldataframe2.to_csv("ResultsAreaNumbers"+os.sep+Name+os.sep+"Data_latin_original_"+str(curr_datetime)+".csv",encoding = "latin-1", errors="replace")
                                ###Fix
                                #driver.close()
                                #driver.quit();
                                continue
                            if pdfscrapper(driver,Name,currFile,numberslist[loop],driver3,selected_type):
                                #driver.close();
                                #driver.quit();
                                link_num += 1
                                if link_num < len(link_list):
                                    itworked=True
                                else:
                                    itworked=False
                                continue
                            else:
                                itworked=False
                                listings = []
                                try:
                                    listings.append(str(numberslist[loop]).replace(" ","").strip())
                                except:
                                    listings.append(str(numberslist[loop]))

                                for t in range(0,len(newordermirabelheaders2)-1):
                                    listings.append("Does not exist!")


                                continue
                        else:
                            itworked=False
                            listings = []
                            try:
                                listings.append(str(numberslist[loop]).replace(" ","").strip())
                            except:
                                listings.append(str(numberslist[loop]))

                            for t in range(0,len(newordermirabelheaders2)-1):
                                listings.append("Does not exist!")

                    except Exception as e:
                        itworked = True
                        VPN('disconnect', ip_list[0])
                        ip_list = ip_list[1:]
                        print('Connecting to IP', ip_list[0])
                        VPN('connect', ip_list[0])
                        '''# Handle exceptions if needed
                        print("error3")
                        print(f"An error occurred: {e}")
                        # Optionally return or handle the error
                        itworked = False
                        safe_close_quit(driver)
                        safe_close_quit(driver3)
                        time.sleep(600)
                        driver = create_headless_driver1()
                        driver = create_headless_driver3()
                        time.sleep(300)
                        #except:
                        #    pass
                        #itworked=False'''
    print("Were done scraping!")
    safe_close_quit(driver)
    safe_close_quit(driver3)

# Check if we are running in a bundle or in a normal Python environment
if getattr(sys, 'frozen', False):
    # If the script is running in a PyInstaller bundle
    script_dir = sys._MEIPASS
else:
    # If the script is running in a normal Python environment
    script_dir = os.path.dirname(os.path.abspath(__file__))

print("Script directory:", script_dir)

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(script_dir, "FinalInfomationAboutAreasPDFtype2.csv")
data = pd.read_csv(csv_file_path, index_col=0, encoding='ISO-8859-1')

def open_file():
   file = filedialog.askopenfilename()
   if file is not None:
        label_4.config(text=file)

OPTIONS = list(data['AreaName'].values)
def submitForm():    
    strFile = optVariable.get()
    # Print the selected value from Option (Combo Box)    
    if (strFile !=''):        
        print('Selected File is : ' + label_4['text'])
        print("Selected Area is : " + strFile)
        global curr_datetime            
        curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        selected_type = type_variable.get()
        if radiobutton_variable.get()==1:
            scraperbylot(strFile,label_4['text'],selected_type)
            print("were done!")
        if radiobutton_variable.get()==2:
            #get_proxy(n)
            scraperbynumber(strFile,label_4['text'],selected_type)
            print("Were done!")

def changed(*args):
    print("You changed the selection. The new selection is %s." % optVariable.get())

root = Tk()
root.geometry('800x600')
root.title("Scraper-2 + Company Scraper")
label_1 = Label(root, text="General Scraper",width=50,font=("bold", 20))
label_1.pack()
label_2 = Label(root, text="Choose Files ",width=50,font=("bold", 20))
label_2.pack()
optVariable = StringVar(root)
optVariable.set("Select") # default value
optVariable.trace("w", changed)
optFiles = OptionMenu(root, optVariable,*OPTIONS)
optFiles.config(width=20)
optFiles.pack()
        

label_3 = Label(root, text="Click the Button to browse the Files",width=300)
label_3.pack()
scroll_v = Scrollbar(root)
scroll_v.pack(side= RIGHT,fill="y")
scroll_h = Scrollbar(root, orient= HORIZONTAL)
scroll_h.pack(side= BOTTOM, fill= "x")


label_4 = Label(root, text="You Selected: No File",width=300)
label_4.pack()

Button(root, text="Browse", command=open_file, width=20).pack()


label_5 = Label(root, text="Choose Cadastre or personnel number",width=50,font=("bold", 20))
label_5.pack()
radiobutton_variable = IntVar()
Radiobutton(root, text="Cadastre Number", variable = radiobutton_variable, value = 1).pack()
Radiobutton(root, text="Personnel/Registration number",  variable = radiobutton_variable, value = 2).pack()


label_6 = Label(root, text="",width=300,font=("bold", 20))
label_6.pack()

label_7 = Label(root, text="Choose Type", width=50, font=("bold", 20))
label_7.pack()

type_variable = IntVar()
Radiobutton(root, text="Type 2 + Company", variable=type_variable, value=1).pack()


Button(root, text='Submit', command=submitForm, width=20,bg='brown',fg='white').pack()
###FIX
#Implementing this fix as the resources of the selenium use up system resources. This allows to restart the program automatically if closes.
#TODO 
#Check if the second row firs tcolumn contains a -, if it does, its scraper by number else its scraper by lot
if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_file_path = sys.argv[1]  # The first argument after the script name
        print(f"CSV file path provided: {csv_file_path}")
        # Proceed with processing the CSV file
        # ...
    else:
        print("No CSV file path was provided as an argument.")
        # Handle the case where no CSV file path is provided
        # ...
    print("Usage: python script.py <path_to_csv_file>")
root.mainloop()

#add a way to change vpn => selenium on surfshark
#keep track of number of searches so far
#call surfshark when we get to 10
