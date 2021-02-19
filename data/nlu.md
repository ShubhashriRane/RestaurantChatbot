## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Okay
- okay
- yes, thanks
- yes, please
- yes, thank you
- thank you

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- thanks, bye
- exit
- Exit

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hola
- hola
- hi there
- hows it going
- Hellow

## intent:ask_budget
- I want to eat at a place between 300 and 700
- I am fine with an expensive place
- I am looking for a dinner place at less than 300
- [Low](budget)
- [Medium](budget)
- [High](budget)
- [>700](budget)

## intent:ask_email
- can u mail me the information to [abc@abc.com](email)?
- can u mail to [test@tes.com](email)?
- can u mail me at [test-123.456@dom.123.co.in](email)?
- email address - [test.some@gmail.co.in](email). Mail this list.
- email me at [email-123@domina.com](email)
- mail me [emial@domain.io](email)
- my email address [email.123-abc@domain.123.com](email)
- please mail me the list to [123-email@domain.co.in](email)
- please send me the list to [123@domain.net](email)
- please send this to [email.123@123.456.com](email)
- send this to [abc-email@abc.com](email)
- send to [abc_123-email@abc123.com](email)
- this is my email address - [email-abc_123@abc.com.edu](email). send me an email.
- [email1_34-ret@host-name.123.com](email)
- can u share this information over email?
- can u send me an email?
- mail me the list
- [jddk.2jmd@kdl.co.in](email)
- email me a list of top 10 restaurants
- mail me the names of restaurants
- please send me an email
- please share this with me
- send me an email
- share some more restaurant names with me
- share this over mail
- share this information with me over email
- [shubhashri.rane@gmail.com](email)
- wait, send me mail to [shubhashri.rane@gmail.com](email)
- [shubhashri.rane](email)
- [shubhashri.rane@gmail.com](email)
- yes. please send it to [ahbcdj@dkj.com](email)
- yes. Please send it to [xyz@sth.edu](email)
- [jddk.2jmd@kdl.co.in](email)
- yes. Please send it to [shubhashri.rane@gmail.com](email)
- yes, Please send it to [shubhashri.rane@gmail.com](email)
- Yes, send it to [shubhashri.rane@gmail.com](email)

## intent:deny
- no
- nope
- definitely not
- never
- absolutely not
- i don't think so
- i'm afraid not
- no sir
- no ma'am
- no way
- no sorry
- No, not really.
- nah not for me
- nah
- no and no again
- no go
- no thanks
- never mind
- nevermind
- I'm not giving you my email address
- I don't want to give it to you
- I'm not going to give it to you
- no!!!!
- no you did it wrong
- no i can't
- not really
- i guess it means - no
- i don't want to
- i don't want either of those
- nah thanks
- neither of these
- suggest some other option
- no, thanks

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [cheap]{"entity": "budget", "value": "Low"}
- [expensive]{"entity": "budget", "value": "High"}
- [moderate]{"entity": "budget", "value": "Medium"}
- find me [expensive]{"entity": "budget", "value": "High"} [mexican](cuisine) restaurants in [delhi](location)
- find me a [cheap]{"entity": "budget", "value": "Low"} restaurant
- find me a [cheap]{"entity": "budget", "value": "Low"} [chinese](cuisine) restuarant in [bangalore]{"entity": "location", "value": "Bangalore"}
- find me a restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- find me a [cheap]{"entity": "budget", "value": "Low"} [chinese](cuisine) restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- i'm hungry. Looking out for some good restaurants
- [bengaluru]{"entity": "location", "value": "Bangalore"}
- I'm hungry. lookig out for some good restaurants
- hey, please find me cheap restaurants in [Vellore](location)
- in [mubaim](location)
- in [mumbai](location)
- [American](cuisine)
- I'll prefer [Thai](cuisine)
- [thai](cuisine)
- please find me [expensive]{"entity": "budget", "value": "High"} [mexican](cuisine) restaurants in [mumbai]{"entity": "location", "value": "Mumbai"}
- please find me a [expensive]{"entity": "budget", "value": "High"} [mexican](cuisine) restaurant in [bangalore]{"entity": "location", "value": "Bangalore"}
- Hello Please find me some [italian](cuisine) restaurants in [bangalore]{"entity": "location", "value": "Bangalore"}

## synonym:4
- four

## synonym:Bangalore
- bangalore
- bengaluru
- Bengaluru
- blore

## synonym:Delhi
- New Delhi
- delhi
- Dilli
- dilli
- nayi dilli

## synonym:Goa
- goa
- goi

## synonym:High
- expensive
- >700
- > 700
- Expensive
- more than Rs. 700
- costly

## synonym:Hubli-Dharwad
- Hubli
- hubballi
- dharwad
- hubli-dharwad

## synonym:Kolkata
- calcutta
- Calcutta

## synonym:Low
- cheap
- Cheap
- less than Rs. 300
- lower
- <300
- < 300

## synonym:Medium
- moderate
- medium
- mid range
- in range of Rs. 300 to Rs. 700
- 300-700
- between 300 to 700

## synonym:Thiruvananthapuram
- trivandrum
- Trivandrum

## synonym:Hubli-Dharwad
- hubli-dharwad
- hubli
- Hubli
- Dharwad
- dharwad

## synonym:Vellore
- vellore

## synonym:Vasai-Virar City
- Vasai
- vasai
- virar
- Virar
- vasai-virar

## synonym:Belgaum
- belgaum
- belagavi
- Belagavi

## synonym:Mumbai
- mumbai
- bombay
- Bombay

## synonym:Chandigarh
- chandigarh

## synonym:chinese
- chines
- Chinese
- Chines
- chinese

## synonym:italian
- Italian
- pizza

## synonym:mexican
- Mexican
- spanish
- taco

## synonym:north indian
- northindian
- northie
- North Indian

## synonym:south indian
- southindian
- andhra
- South Indian

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:email
- ([\w\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
- Bangalore
- Chennai
- Delhi
- Hyderabad
- Kolkata
- Mumbai
- Agra
- Pune
- Ajmer
- Aligarh
- Allahabad
- Amravati
- Amritsar
- Asansol
- Ahmedabad
- Bareilly
- Belgaum
- Bhavnagar
- Bhiwandi
- Bhopal
- Bhubaneswar
- Bikaner
- Chandigarh
- Coimbatore
- Nagpur
- Cuttack
- Dehradun
- Dhanbad
- Durgapur
- Erode
- Faridabad
- Firozabad
- Gulbarga
- Guntur
- Gwalior
- Gurgaon
- Guwahati
- Indore
- Jabalpur
- Jaipur
- Jalandhar
- Jammu
- Jamnagar
- Jamshedpur
- Jhansi
- Jodhpur
- Kakinada
- Kannur
- Kanpur
- Kochi
- Kottayam
- Kolhapur
- Kollam
- Kozhikode
- Kurnool
- Lucknow
- Ludhiana
- Madurai
- Malappuram
- Mathura
- Goa
- Mangalore
- Meerut
- Moradabad
- Mysore
- Nanded
- Nashik
- Nellore
- Noida
- Palakkad
- Patna
- Pondicherry
- Raipur
- Rajkot
- Rajahmundry
- Ranchi
- Rourkela
- Sangli
- Siliguri
- Solapur
- Srinagar
- Surat
- Thiruvananthapuram
- Thrissur
- Tiruchirappalli
- Tirunelveli
- Tiruppur
- Tiruvannamalai
- Ujjain
- Bijapur
- Vadodara
- Varanasi
- Vijayawada
- Visakhapatnam
- Vellore
- Warangal
- Hubli-Dharwad
- Vasai-Virar City

## lookup:cuisine
- american
- chinese
- italian
- mexican
- north indian
- south indian
