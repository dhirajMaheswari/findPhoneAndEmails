'''this code makes use of the command line to find emails and/or phones from supplied text file
	or text using regular expressions.
'''

import argparse, re

def extractEmailAddressesOrPhones(text, kKhojne = "email"):
    ''' this function uses the regular expressions to extract emails from the 
        supplied text
        import re '''

    if kKhojne.lower() == "email":
    	Pattern = re.compile(r'[a-zA-Z0-9_.]+@[a-zA-Z0-9.]+[a-zA-Z]+') # pattern for email
    elif kKhojne.lower() == "phone":
    	Pattern = re.compile(r'(\d{3}-\d{3}-\d{4})|(\d{10})|(\d{3}\.\d{3}\.\d{4})') # pattern for phone
 
    emailPhoneLists = Pattern.findall(text)
    return emailPhoneLists



ap = argparse.ArgumentParser()
ap.add_argument("-p", "--filePath",required = True, help = "path to file.")
ap.add_argument("-f", "--find", required = True, help = "What to find? options are phone and email.")

args = vars(ap.parse_args())

n = len(args)

filep = args["filePath"]
findwhat = args["find"]

sourceText = []
fp = open(filep, 'r')
for l in fp:
	sourceText.append(l)
fp.close()

sourceText = ' '.join(sourceText)
	
if findwhat.lower() == "email":
	tt = extractEmailAddressesOrPhones(sourceText)

	print("I found {} email addresses in the file {}" .format(len(tt), args["filePath"]))
	print("**************")

	for w in range(len(tt)):
		print("Email address {}: {}".format(w+1, tt[w]))
		
elif findwhat.lower() == "phone":
	tt = extractEmailAddressesOrPhones(sourceText, kKhojne = "phone")

	print("I found {}  phone numbers in the file {}" .format(len(tt), args["filePath"]))
	print("**************")
	for w in range(len(tt)):
		print("Phone number {}: {}".format(w+1, tt[w]))
else:
	print("Invalid request made.")
	print("Correct Usage: findPhonesAndEmails.py --filePath fileName --find phone/email.")
