from os import system
from time import sleep
from random import randint

def module_checker():
	try:
		import requests
		from bs4 import BeautifulSoup
	except ImportError:
		system("pip install bs4")
		system("pip install requests")
		
module_checker()

for _ in range(100):
	rand_int = randint(1111111111111,9999999999999)
	f = open(f"{rand_int}.py", "w+")
	k = open(f"{rand_int}.js", "w+")
	
system("clear")
print("     SCRIPT HACKER FACEBOOK V.999")
print()
target = input("  Enter the URL FB : ").lower()
print()
if ("https://www.facebook.com" or "https://facebook.com" or "https://w.facebook.com" in target):
	status = True
	sleep(2)
	while status:
		print(f"    [+] USERNANE (split) : {target}", end="\r")
		print(f"    [+] PASSWORD : {randint(9999999999,1111111111)}", end="\r")
else:
	print("แม่มึงตายไอสัสกูบอกให้ใส่ลิงก์ FB ละมึงมาใส่เหี้ยไรปัญญอ่อน")