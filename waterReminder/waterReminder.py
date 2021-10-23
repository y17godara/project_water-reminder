import time
from plyer import notification
if __name__ =='__main__':
 	while True:
 		notification.notify(
 			title = "**Please Drink Water Now!!",
 			message =" About 15.5 cups (3.7 liters) Required Daily",
 			app_icon = "img.ico",
 			timeout= 10
 			)
 		#time.sleep(6)
 		time.sleep(60*60)
		 


