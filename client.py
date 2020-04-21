import requests
url="http://127.0.0.1:5000/"
while(True):
    print("Menu")
    print("1.Get all data")
    print("2.Get a student data")
    print("3.exit")
    n=int(input())
    if n==3:
        break
    if n==1:
        
        jsondata=requests.get(url)
        data=jsondata.json()
        print()
        print("contacts")
        for x in data['contacts']:
            print()
            print("Name\t:"+x)
            print("github\t:"+data['contacts'][x]['github'])
            print("Phone\t:"+data['contacts'][x]['phone'])
            print("github\t:"+data['contacts'][x]['instagram'])
            print()
    else:

        try:
            print("enter student name")
            strr=input()
            url1=url+strr
            jsondata=requests.get(url1)
            data=jsondata.json()
            print(data)
            print("contacts")
            for x in data:
                print()
                print("Name\t:"+strr)
                print("github\t:"+data['contacts']['github'])
                print("Phone\t:"+data['contacts']['phone'])
                print("github\t:"+data['contacts']['instagram'])
                print() 
        except:
            print()
            print("Sorry we dont have their data")
            print("press 1 and check the entire data we have")
            print()