#import alfi4
import cv2
import numpy as np 
#import alfi
from datetime import datetime
import re
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
# src='/home/user/smartclaim/'
words_stored=[] #Define list
amount_list=[]
#amount_list.append(value)
y=[]
food_items=['bloody','mary','Coffee','Ckn','Dum','Biryani','Chicken','meals','Meals']
food_print=[]
time_value=0
date_value=0
#Extract text from image
def get_text(img_path):
	img=cv2.imread(img_path) #Read image
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	kernel=np.ones((1,1),np.uint8)
	img=cv2.dilate(img,kernel,iterations=1)
	img=cv2.erode(img,kernel,iterations=1)
	#cv2.imwrite(src+"removed_img.jpg",img)
	img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	#cv2.imwrite(src+"thresh.jpg",img)
	result=pytesseract.image_to_string(Image.open(img_path))#src+"thresh.jpg"))
	return result

# get_text(src+"snap.jpg").encode('utf-8')

def check_name():
	file_name='imgtext.txt'
	# a=get_text(img_path)
	# file_name='imgtext.txt'
	
	file2=open(file_name,"r")
	b=file2.read()
	hname=0
	for index,value in enumerate(b.split()):
		if index==0:
			hname=value
	 		"""print "Hotel Name: " + value"""

	return hname


def check_date():
	file_name='imgtext.txt'
	file2=open(file_name,"r")
	b=file2.read()
	date_value=0
	for index,value in enumerate(b.split()):
	
		p_date = re.compile(r'(\d{1,2})[/-](\d{1,2})[/-](\d{1,4})')

		if  bool(p_date.match(value)) is True:
			date_value=value
			# print "Date functn: " + value

	if date_value is 0:
		return "Enter Date"
	else:
		return date_value
	


def check_time():
	file_name='imgtext.txt'
	file2=open(file_name,"r")
	b=file2.read()
	ap=0
	time_value=0
	for index,value in enumerate(b.split()):
		time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
		time_re1 = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d):([0-5]\d)|24:00:00)$')
		if bool(time_re.match(value)) is True or bool(time_re1.match(value)) is True:
		#print index+1 
			time_value=value
			c=b.split()
		
			if c[index+1] == 'pm' or  c[index+1] == 'am':
				# print "Time: " + value + c[index+1]
				ap=c[index+1]
			"""else:
				print "Time: " + value #+ c[index+1]"""


	if time_value is 0:
		return "Enter Time"
	elif ap is 0:
		return time_value
	else:
		return time_value + ap


def check_food_items():
	file_name='imgtext.txt'
	file2=open(file_name,"r")
	b=file2.read()
	count=0
	for index,value in enumerate(b.split()):
		words_stored.append(value)
		for value2 in food_items:
			if value==value2:
				count+=1
				food_print.append(value2)	
	# print "Food items: " + str(food_print)
#	print "food = " + food_items
	return count,str(food_print)


def check_amount():
	file_name='imgtext.txt'
	file2=open(file_name,"r")
	b=file2.read()
	amount_set=0
	for index,value in enumerate(b.split()):
		amount_re=re.findall("\d+\.\d+",value)

		if bool(amount_re) is True:
			amount_set=1
			y.append(value)
	

	#print "amount_list" + amount_list
	#print "y" + y
	# print "Amount: " + amount

	if amount_set is 0:
		return "Enter Amount"
	else:
		amount_list=sorted(y)
		amount_list=sorted(y,key=float)
		length=len(amount_list)
		amount=str(amount_list[length-1])
		return amount



def main1(img_path):
	a=get_text(img_path).encode('utf-8')#Storing result into another variable
	print a
	file_name='imgtext.txt'
	file=open(file_name,"w")
	file.write(a)#.encode('utf-8')
	file.close()
	result_name=check_name()
	result_date=check_date()
	result_time=check_time()
	result_amount=check_amount()
	result_count,result_food=check_food_items()
#check_food_items()



	file_name='imgtext.txt'
	file2=open(file_name,"r")
	b=file2.read()
	for index,value in enumerate(b.split()):
		words_stored.append(value)
	print words_stored
	print '\n'
	print "Name   = " + result_name
	print "Date   = " + result_date
	print "Time   = " + result_time
	print "Amount = " + result_amount
	res = result_count
	print "food count = {0}".format(res)
	print "Food Items = " + result_food
	print '\n'



# a=get_text(img_path).encode('utf-8')#Storing result into another variable

"""print '\n'

file_name='imgtext.txt'
file2=open(file_name,"r")
b=file2.read()
for index,value in enumerate(b.split()):
	words_stored.append(value)
print words_stored


result_name=check_name()
result_date=check_date()
result_time=check_time()
result_amount=check_amount()
result_count,result_food=check_food_items()
#check_food_items()

print '\n'
print "Name   = " + result_name
print "Date   = " + result_date
print "Time   = " + result_time
print "Amount = " + result_amount
res = result_count
print "food count = {0}".format(res)
print "Food Items = " + result_food
print '\n'"""







