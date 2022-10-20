import schedule
import time
import datetime
import requests
import json
from playsound import playsound

print("-----------------Script Started-------------------")

def send_linkTo_telegram(subject,Name,links):
	token= '' #your telegram channel api keys
	chat_id = '-100+ Your chat_id'
	url = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text="+subject+Name+links

	try:
		response=requests.get(url)
		telegram_data = json.loads(response.text) #converts the text response to a JSON object and stores it in telegram_data.
		return telegram_data["ok"]  #The status of the request is stored in the "ok" field .True if the message has been sent.
	
	except Exception as e:
		print("An error occurred in sending the message via Telegram")
		print(e)
		return False


def getTodayClass():
    TodayTime = datetime.datetime.now()
    Current_Day=TodayTime.strftime("%A")
    CurrentTime=float(TodayTime.strftime("%H.%M"))
    Days={
    "Monday":   {09.10:"PANLAB", 10.10:"PANLAB", 11.10:"SLS", 12.10:"JTS", 13.50:"PAN", 14.40:"VNT",15.30:"JTS"},
    "Tuesday":  {09.10:"VNT",    10.10:"JTS",    11.10:"PHK", 12.10:"PRP", 13.50:"FLV", 14.40:"PAN",15.30:"PGA"},
    "Wednesday":{09.10:"VNT",    10.10:"VNT",    11.10:"PHK", 12.10:"PRP", 13.50:"FLV", 14.40:"JYS",15.30:"SLS"},
    "Thursday": {09.10:"MTK",    10.10:"MTK",    11.10:"PAN", 12.10:"PHK", 13.50:"VNT", 14.40:"RJR",15.30:"RJR"},
    "Friday":   {09.10:"PAN",    10.10:"JTS",    11.10:"PGA", 12.10:"PRP", 13.50:"FLV", 14.40:"JTS",15.30:"JTS"}
    }
    
    ##Teacher's Name, Subject Name And Meeting links
    teachersNameAndSubject={
    "JTS":["Jeetu Singh","Artificial intelligence","kgi-djtq-xhy"],
    "JYS":["Jaya Sharma","Comprehension","vnt-xkyy-mps"],
    "MTK":["Muthumum M","MOOC-II","nkr-yibe-hrh"],
    "PAN":["Pramod Nagar","Compiler Design","xhm-nzjw-ocv"],
    "PANLAB":["Pramod Nagar","Compiler Design-Lab","daa-mwys-pei"],
    "PGA":["Parag Assht","Employability Skills And Practices","aqv-ycyt-ruy"],
    "PHK":["Piyush Kaala","Energy Conservation","hsw-qoqq-unn"],
    "RJR":["Rajesh Rathnam","Competitive Professional Skills-III","rae-dspp-wft"],
    "SLS":["Shalini Sharma","Indian Art Form","qum-sgyp-art"],
    "FLV":["Franklin Vinod","Network Security","dcx-pcry-mso"],
    "PRP":["Pritee Parwekar","Wireless Sensor Networks","qaw-jnph-qis"],
    "VNT":["Vinam Tomar","Database Management System","pzg-edui-wti"]
    }
    
    if Current_Day=="Sunday" or Current_Day=="Saturday":
        print("No Class Today")
        
    else:
        print(CurrentTime)
        Todayclass=Days[Current_Day].get(CurrentTime) ## getting current class teacher name  
        Name=teachersNameAndSubject[Todayclass][0].upper() ## getting teacherfull name 
        Subject=teachersNameAndSubject[Todayclass][1].upper()##getting Subject name
        links=teachersNameAndSubject[Todayclass][2]  ## getting current class meeting link
        print(Subject)
        print(Name)
        target = "https://meet.google.com/"+links
        print(target)
        telegram_status =send_linkTo_telegram(Subject,"\n"+Name,"\n"+target) ## sending link to telegram bot
        print("Telegram status: ", telegram_status)   ## if message sent successfully print ok 
        playsound("") # Enter the absolute path of the audio file
	
    
scheduler1 = schedule.Scheduler()
scheduler2 = schedule.Scheduler()
scheduler3 = schedule.Scheduler()
scheduler4 = schedule.Scheduler()
scheduler5 = schedule.Scheduler()
scheduler6 = schedule.Scheduler()
scheduler7 = schedule.Scheduler()

def classScheduler():
    while True:
        AltTime = datetime.datetime.now()
        CheckTime=float(AltTime.strftime("%H.%M"))
        if CheckTime<=09.10:
            scheduler1.run_pending()
        elif CheckTime<=10.10:    
            scheduler2.run_pending()
        elif CheckTime<=11.10:
            scheduler3.run_pending()
        elif CheckTime<=12.10:
            scheduler4.run_pending()
        elif CheckTime<=13.50:
            scheduler5.run_pending()
        elif CheckTime<=14.40:
            scheduler6.run_pending()
        elif CheckTime<=15.30:
            scheduler7.run_pending()
        time.sleep(1)

scheduler1.every().day.at("09:10").do(getTodayClass)
scheduler2.every().day.at("10:10").do(getTodayClass)
scheduler3.every().day.at("11:10").do(getTodayClass)
scheduler4.every().day.at("12:10").do(getTodayClass)
scheduler5.every().day.at("13:50").do(getTodayClass)
scheduler6.every().day.at("14:40").do(getTodayClass)
scheduler7.every().day.at("15:30").do(getTodayClass)

classScheduler()
