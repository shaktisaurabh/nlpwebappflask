import json 
def uniquer(email,name,password):
    with open('mandala.json') as wf1:
        a1=json.load(wf1) 
        if email in a1:
            return 0 
        else:
            a1[email]=[name,password] 
    with open('mandala.json','w') as wf2:
        json.dump(a1,wf2) 
        return 1 
def checkinglogin(email,password):
    with open('mandala.json') as wf2:
        a3=json.load(wf2) 
        if email in a3:
            if a3[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0
        