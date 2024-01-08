# work in progress

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/6f6c72c3-e357-4116-b191-6b647edfa518)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/1116ff88-59f6-4291-b046-e8c483decc93)


# dummy train data

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/9ae3c456-5f57-4909-b83e-356f71d4d3b6)
created by signals.py

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/14ed53ea-bea3-4ee6-869d-9e6d3ede1635)

# dummy station data::

### populating from excel to postgres via python script; in build django file:: myapp/management/commands/populate_myapp_station.py 
python manage.py populate_myapp_station (django automatically created it)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/3f26c01a-b359-421f-b1dc-5e6dd134019f)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/5c0feaa4-537c-4319-885e-e9475fe1f462)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/aff43a63-26e7-47c1-8dc7-5f69569a177a)

admin can add stations and then select trainnumber via one to many relationship; many station one train
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/1f68c193-90a3-4d2a-a5fe-836e1a767a66)

# search for train from train number and it will display list of multiple stations

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/8954a9a3-6b9d-44a9-884c-8bc24cc9c1f4)


## implemented From-to destination.

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ef56cc52-64de-43be-a68a-bad26ded0f79)

## User registeration and login

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/b3549459-974a-4eb5-9470-7ed30dd67904)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/73924ff4-ffc1-4d3b-a20d-27643b5e3783)

## profile and wallet system added
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/5a174301-5c60-4673-8a24-2815704c030d)

## Booking models (was a challenging one for me)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/b96ba347-9bcd-4bed-bad1-0962ddf20f62)

let say we will book 2AC 37 available

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/aba1b221-4b37-4481-9918-49a0af2c2f1e)

used atomicity (all or nothing); django built in function
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/e98b312e-746e-40ca-945a-fdf1331fbad2)

currently basic css 
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/7389e2b4-8436-4617-b5f3-56c0e86e9e0c)

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/740ba715-9acf-4b42-9e31-8aeffd25deae)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ad49beca-f8c8-4bd9-9579-33b0584e927a)

after successfull payment user redirected to myticket page, wallet money deducted, seats updated in our case subtracted by 2 for train 1010 Ac

![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/ed67f764-3b14-4acb-915d-07bb3dcc3cc7)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/d11530d6-a98a-4b82-80f1-114a2f082502)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/dd4821b6-cd81-49c6-b8e4-64ff88813880)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/2efd5594-dbf7-4c6c-b4b4-632e426eaec7)

==== 

As of 8 jan  [4jan to 8jan ] ; Deadline approached :( will add more in future, for the task judgement i have included most of the functionality

==
<br>
Todos: (out of time :{ ) *cry*
1. now we can  mail this by retreiving data from Passenger model and mail to request.user
2. can edit data say name in myticket by introducing edit button and  edit button will make a post request function in a view
3. can add more complexity that is search trains by date can introduce calender feature in frontend which will then check corresponding day for date and further filter down relevant trains in frontend
4. talking about cancellation and refund, admin can change cancel_status from dashboard and in frontend we can update it
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/c19685b5-43c3-4887-b598-26e52f2a777a)
in def self im taking instance as passenger-name-createdby
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/81df86dc-ea7b-4139-85d5-843da78cc4b0)
if admin wants to cancel a ticket he check the checkbox
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/4836aebe-fe5c-4dab-94e9-f6c2e8ceb241)
![image](https://github.com/Ayush-gupta-dev/RAILWAY-ROUND2/assets/137040550/04c3f7aa-bbc2-4b58-84ae-4fe0b74dc0da)

## Yeah waant to add more but i should also respect the deadline so now i will dockerise it and deploy. (i feel i have something to show probably 70/100). #trains
