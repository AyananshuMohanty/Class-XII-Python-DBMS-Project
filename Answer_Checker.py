# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:46:11 2021

@author: Ayananshu Mohanty
"""
qpaper=open(r'C:\Users\Ayananshu Mohanty\Downloads\JEEMains4thAttemptResponseSheet.txt',"r")
anskey=open(r'C:\Users\Ayananshu Mohanty\Downloads\31SeptAnsKeys.txt',"r")
questionid=anskey.readlines()
response=qpaper.readlines()
physicscorrect=0
physicsincorrect=0
for i in range(1,21):
    qid=""
    ansid=""
    chosenanskey=""
    chosenans=""
    for j in range(11):
        qid=qid+questionid[i][j]
        ansid=ansid+questionid[i][j+12]
    for k in range(len(response)):
        if qid in response[k]:
            if ansid in response[k]:
                chosenans=response[k][169]
                print(chosenans)
                if chosenans=="1":
                    for l in range(11):
                        chosenanskey=chosenanskey+response[k][55+l]
                elif chosenans=="2":
                    for l in range(11):
                        chosenanskey=chosenanskey+response[k][79+l]
                elif chosenans=="3":
                    for l in range(11):
                        chosenanskey=chosenanskey+response[k][103+l]
                elif chosenans=="4":
                    for l in range(11):
                        chosenanskey=chosenanskey+response[k][127+l]
            elif "Chosen Option" in response[k+11]:
                chosenans=response[k+12]
                print(chosenans)
                if chosenans=="1":
                    choseanskey=response[k+2].rstrip
                if chosenans=="2":
                    choseanskey=response[k+4].rstrip
                if chosenans=="3":
                    choseanskey=response[k+6].rstrip
                if chosenans=="4":
                    choseanskey=response[k+8].rstrip
            print(qid)
            print(ansid)
            print(chosenanskey)
            if ansid==chosenanskey:
                physicscorrect=physicscorrect+1
            else:
                physicsincorrect=physicsincorrect+1

print()
print("physicscorrect=",physicscorrect)
print("physicsincorrect=",physicsincorrect)
                
                    
            
            
            