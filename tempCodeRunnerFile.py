def playResponce(self,responce):
        x=pyttsx3.init()
        #print(responce)
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')
                #print(b)
                 
        x.setProperty('rate',120)
        x.setProperty('volume',100)
        x.say(responce)
        x.runAndWait()