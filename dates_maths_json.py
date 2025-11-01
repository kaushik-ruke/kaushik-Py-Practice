import datetime

x = datetime.datetime.now()
print(x)

#----------------------------------------------------------------#

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))     # full form of Weekday

#---------------------------------------------------------------#

import datetime
y = datetime.datetime(2020, 5, 17)

print(y)


import datetime
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#-----------------------------------------------------------------#
'''
%a	Weekday, short version	                        Wed	
%A	Weekday, full version	                        Wednesday	
%w	Weekday as a number 0-6, 0 is                   Sunday	3	
%d	Day of month                                    01-31	31	
%b	Month name, short version	                    Dec	
%B	Month name, full version	                    December	
%m	Month as a number                               01-12	12	
%y	Year, short version, without century	        18	
%Y	Year, full version	                            2018	
%H	Hour                                            00-23	17	
%I	Hour                                            00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	                                41	
%S	Second 00-59	                                08	
%f	Microsecond                                     000000-999999	548513	
%z	UTC offset	                                    +0100	
%Z	Timezone	                                    CST	
%j	Day number of year                              001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	++++++++++
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	                        12/31/18	
%X	Local version of time	                        17:41:00	
%%	A % character	                                %	
%G	ISO 8601 year	                                2018	
%u	ISO 8601 weekday (1-7)	                        1	
%V	ISO 8601 weeknumber (01-53) 	                01	
'''


# Math Function 

import math

x = math.sqrt(6)
print(x)

#---------------------------------------------#

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#-----------------------------------------------#

import math
x = math.pi

print(x)                    # gives the Value of pi

#---------------------------------------------------------------------#

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])


import json
a={
    "name":"Kaushik",
    "age":21,
    "city":"Mumbai"
}

b = json.dumps(a)
print(b)

#----------------------------------------------------------------------#


import json

x = {
  "name": "JOHN",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": [{"Dog": "Scout"}],
  "friends": ("Harry", "Randy"),
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1},
    {"model": "Toyota", "mpg": 30.2},
    {"model": "Suzuki", "mpg": 32.4}
  ]
}
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))


#----------------------------------------------------------------------#

# Python Regular expression :

import re

txt = " there is Rain in Mumbai"
x = re.search("^The.*Mumbai$", txt)       # this will print else Condi
y = re.search("Mumbai$", txt)      # this will print IF condition

if(y):
    print("Yes! Its raining Heavily In Bombay")
if(x):
    print("its less rain")
else:
    print("No its Not")
    
#-------------------------------------------------------------------------------------#

import re

txt = "The cloudy in Spain"
x = re.findall("ai", txt)
print(x)


import re

txt1 = " Spain is the Euro Winner "
x = re.findall("in", txt1)
y = re.findall("Portugal", txt1 )
print(y)
print (x)
if(y):
    print("Portugal is Euro Winner")
if(x):
    print("Yes! Spain are also playing Finalisma against Argentina")
else:
    print("No they Are Not")
    
    
#----------------------------------------------------------------------------------#

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 


# here the white Spacing is seen
#eg : T  h  e     r  a  i  n     i  n     S  p  a  i  n
#     0  1  2  3  4  5  6  7  8  9 10  11 12 13 14 15 16

# therefore here the white spacing is in number '3','8','11'


#----------------------------------------------------------------------------#

import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)    #\s is important for this Func to work
print(x)

