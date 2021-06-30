from pathlib import Path
import json
import re
import os
import telegram_send


class Device: 
    def __init__(self):
        self._deviceConfig = ""
        self._deviceType = ""
        self._deviceName = ""
        self._deviceVersion = ""

    def __init__(self, filePath, baselinePath):
        self._deviceConfig = ""
        self._deviceType = ""
        self._deviceName = ""
        self._deviceVersion = ""
        self._baselinePath = Path(baselinePath)
        deviceConfigurationFile = Path(filePath)
        if os.path.exists(deviceConfigurationFile):
            with open(deviceConfigurationFile, 'r') as f:
                for line in f.readlines():
                    self._deviceConfig += line
            
            if self._deviceConfig:
                self.extractConfigurationDetails()
            else:
                print("can't find file?")

        else:
            #TODO: Replace this with some sort of PYthon logging/actual error handling
            print("[**] Location error configfile \"%s\" not found. Empty performing!" % deviceConfigurationFile)

    def output(self):
        print("Device Hostname: %s\nDevice Version: %s" % (self._deviceName, self._deviceVersion))


    def extractConfigurationDetails(self):
        searchString = "hostname"

        self._deviceName = self._deviceConfig[self._deviceConfig.find(searchString) + len(searchString):].split('\n')[0]
        searchString = "version"
        self._deviceVersion = self._deviceConfig[self._deviceConfig.find(searchString) + len(searchString):].split('\n')[0]

    def performAudit(self):
        numTests = 0
        numCorrect = 0
        #Load baselines into memory
        with open(self._baselinePath, 'r') as f:
            data = json.load(f)
        

        print("Start Basline check of config!")
        #Loop through each baseline
        for baseline in data['baseline']:
            numTests += 1
            print("#" * 10)
            print(baseline['name'])
            print("Description: " + baseline['description'])


            #Check all search strings from the baselines json
            anyMatch = False
            for searchstring in baseline['searchstring']:
                if searchstring in self._deviceConfig:
                    anyMatch = True
                    break
            
            if anyMatch:
                numCorrect += 1
                print(self._deviceName + " Passes!")
            else:
                print(self._deviceName + " Fails!")
                telegram_send.send(messages=["Error found in the configuration of the device with the name:" + self._deviceName + " with the version:" + self._deviceVersion + ". Device fails on the following baseline:" + baseline['description']+". Please check the report for more details."])

            print("#" * 10 + "\n")

        print(self._deviceName + " Result Audit:")
        print((("#") * 10))
        print("Passed: " + str(numCorrect))
        print("Failed: " + str(numTests - numCorrect))
            

        










											
