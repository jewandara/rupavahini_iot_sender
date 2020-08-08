######################################################################
######## vc_means_vision_carrier - python project import libs ########
######################################################################
import threading
import requests
import requests.auth
import json
from datetime import date, timedelta
import base64



#######################################################################################################################
### THIS FUNCTION IS USED FOR UPLOADING IMAGE FILE FROM RASBERY PY LOCATION (PATH="/home/y/nms/test_text_file.txt") ###
#######################################################################################################################
def CALLING_URL(DATA):
    try:
        print("CALLING_URL ...")
        print("PLEASE WAIT ...")
        JDATA = json.loads(DATA)
        success = requests.post(str(JDATA["URL"]), json=JDATA["JSON_DATA"])
        return [1, success]
    except Exception as error:
        return [0, error]



#######################################################################################################################
### THIS FUNCTION IS USED FOR UPLOADING IMAGE FILE FROM RASBERY PY LOCATION (PATH="/home/y/nms/test_image.png") ###
#######################################################################################################################
def UPLOADING_IMGE(PATH):
    try:
        print("UPLOADING_IMGE ...")
        with open(str(PATH), "rb") as imageFile:
            return [1, base64.b64encode(imageFile.read())]
    except Exception as error:
        return [0, error]



######################################################################################################################
### THIS FUNCTION IS USED FOR UPLOADING TEXT FILE FROM RASBERY PY LOCATION (PATH="/home/y/nms/test_text_file.txt") ###
######################################################################################################################
def UPLOADING_TEXT_FILE(PATH):
    try:
        print("UPLOADING_TEXT_FILE ...")
        with open(str(PATH), 'r') as file:
            return [1, str(file.read()).encode('utf-8')]
    except Exception as error:
        return [0, error]



############################################################
### THIS FUNCTION IS USED FOR VIEWING THE SERVER RESPOND ###
############################################################
def VIEW_RESPOND(DATA):
    print("READING RESPOND ...")
    JDATA = json.loads(DATA)
    print("SERVER ERRORS : " + str(JDATA["result"]["error"]))
    print("SERVER MESSAFE : " + str(JDATA["result"]["message"]))
    print("DATABASE ID : " + str(JDATA["result"]["result"]))
    print("TO VIEW IMAGE : 'https://api.maxford.lk/rupavahini/vc_means_vision_carrier/image.php?id=" + str(JDATA["result"]["result"]) + "' -> Link To Visit")
    print("TO READ FILE : 'https://api.maxford.lk/rupavahini/vc_means_vision_carrier/read/index.php?id=" + str(JDATA["result"]["result"]) + "' -> Link To Visit")



#####################
### MAIN FUNCTION ###
#####################
def main():
    try:
        print("STARTING MAIN FUNCTION ...")
        TODAY = date.today()
        ###----------------> RASBERY PI TXT FILE LOCATION -> METHANA TYPE KARPAN KAOOOOOOOOOOOOOOOOOOOOO
        TEXT_DATA = UPLOADING_TEXT_FILE("test_text_file.txt")
        if(TEXT_DATA[0]):
            ###----------------> RASBERY PI IMAGE FILE LOCATION -> METHANA TYPE KARPAN KAOOOOOOOOOOOOOOOOOOOOO
            IMGE_DATA = UPLOADING_IMGE("test_main.jpg")
            if(IMGE_DATA[0]):
                DATA = '''{
                    "URL": "https://api.maxford.lk/rupavahini/vc_means_vision_carrier/update/index.php?dev_mode=0",
                    "JSON_DATA":
                            {
                            "PROJECT" : "project_rupavahini",
                            "TEXT_FILE" : "'''+str(TEXT_DATA[1])+'''",
                            "IMAGE_FILE" : "'''+str(IMGE_DATA[1])+'''",
                            "DATE_TIME" : "'''+str(TODAY)+'''"
                            }
                    }'''
                URL_DATA = CALLING_URL(DATA)
                if(URL_DATA[0]):
                    VIEW_RESPOND(URL_DATA[1].text)
                    print("PROGRAM ENDED")
                else: print(URL_DATA[1])
            else: print(IMGE_DATA[1])
        else: print(TEXT_DATA[1])
    except Exception as error:
        print(error)



####################################
### STARTING PROGRAM IN A THREAD ###
####################################
if __name__ == '__main__':
     thread = threading.Thread(target=main())
     thread.start()
     thread.join()
