<!--- Story 1 -->
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "valid"}
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!---  Story 2 -->	
## complete path with location first
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 3 -->	
## complete path with location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 4 -->	
## complete path with cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export
	
<!--- Location Invalidity -->	

<!--- Story 5 -->
## complete path with location invalid
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 6 -->	
## complete path with invalid location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"cuisine": "chinese"}
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 7 -->	
## happy_path with location invalid
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "invalid"}
	- slot{"cuisine_validity" : "valid"}
	- utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- With No Email -->

<!--- Story 8 -->
## happy_path with deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "valid"}
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 9 -->	
## complete path with location first with deny email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 10 -->	
## complete path with location specified with deny email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 11 -->	
## complete path with cuisine specified with deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 12 -->
## complete path with location invalid with deny email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* deny
    - utter_goodbye
    - export
	
<!--- With Location Invalid And Denied Email -->	

<!--- Story 13 -->
## complete path with invalid location specified with deny email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* deny
    - utter_goodbye
    - export

<!--- Story 14 -->	
## happy_path with location invalid with deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "invalid"}
	- slot{"cuisine_validity" : "valid"}
	- utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_location_valid
    - slot{"location_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "goa"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export


<!--- With Location Invalid And no Retry Location --->	

<!--- Story 15 -->	
## complete path with location invalid with notry
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* deny
    - utter_did_that_help
* deny
    - utter_goodbye
    - export

## complete path with invalid location  with notry
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 16 -->	
## happy_path with location invalid  with notry
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "invalid"}
	- slot{"cuisine_validity" : "valid"}
	- utter_location_invalid
    - utter_ask_location_retry
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Invalid Cusine -->

<!--- Story 17 -->	
## complete path with  invalid cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "invalid"}
	- utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}	
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "delhi"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 18 -->		
## happy_path with invalid cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "italian"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "valid"}
	- slot{"cuisine_validity" : "invalid"}
	- utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}	
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

	
<!--- Story 19 -->			
## when budget,cuisine and location are already specified.
* greet
    - utter_greet
* restaurant_search{"budget": "Low", "cuisine": "chinese", "location": "Bangalore"}
    - slot{"budget": "Low"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - action_cuisine_valid
    - slot{"location_validity": "valid"}
    - slot{"cuisine_validity" : "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"email_message": ""}
    - slot{"results_found": "False"}
    - utter_noresults
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"email_message": "\n   1. Hae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6 out of 5. Average cost for 2 : 1100\n\n   2. The Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1200\n\n   3. China Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1100\n\n   4. High Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4 out of 5. Average cost for 2 : 2600\n\n   5. Mamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.4 out of 5. Average cost for 2 : 2000\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye


<!--- Story 19 -->			
## when budget,cuisine and location are already specified, but no results found, so increasig budget
* greet
    - utter_greet
* restaurant_search{"budget": "Low", "cuisine": "chinese", "location": "Delhi"}
    - slot{"budget": "Low"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"email_message": ""}
    - slot{"results_found": "False"}
    - utter_noresults
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"email_message": "\n   1. Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.9 out of 5. Average cost for 2 : 2500\n\n   2. Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6 out of 5. Average cost for 2 : 2200\n\n   3. Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6 out of 5. Average cost for 2 : 2500\n\n   4. Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.5 out of 5. Average cost for 2 : 1500\n\n   5. You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5 out of 5. Average cost for 2 : 1000\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "shubhashri.rane@gmail.com"}
    - slot{"email": "shubhashri.rane@gmail.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "shubhashri.rane@gmail.com"}
    - utter_confirm_email
* goodbye
    - utter_goodbye

<!--- Story 20 -->		
## happy_path with low budget, no results then high budget
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"email_message": ""}
    - slot{"results_found": "False"}
    - utter_noresults
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"email_message": "\n   1. Hae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6 out of 5. Average cost for 2 : 1100\n\n   2. The Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1200\n\n   3. China Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1100\n\n   4. High Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4 out of 5. Average cost for 2 : 2600\n\n   5. Mamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.4 out of 5. Average cost for 2 : 2000\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye

<!--- Story 21 -->		
## complete path with missplet location,then correct location. First the user denies for email, then says "send"
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_ask_location_retry
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"email_message": ""}
    - slot{"results_found": "False"}
    - utter_noresults
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"email_message": "\n   1. Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9 out of 5. Average cost for 2 : 1800\n\n   2. Bastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8 out of 5. Average cost for 2 : 4200\n\n   3. Gallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   4. The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   5. Aer - Four Seasons in 1/136, E Moses Road, Worli, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 4500\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
* ask_email{"email": "shubhashri.rane@gmail.com"}
    - slot{"email": "shubhashri.rane@gmail.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "shubhashri.rane@gmail.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye

<!--- Story 22 -->		
## Happy path , checking email validity. After goodbye, checking if it takes another request.
* restaurant_search{"budget": "High", "cuisine": "mexican", "location": "Bangalore"}
    - slot{"budget": "High"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"email_message": "\n   1. Truffles in 28, 4th B Cross, Koramangala 5th Block, Bangalore has been rated 4.8 out of 5. Average cost for 2 : 900\n\n   2. Windmills Craftworks in 331, EPIP Area, Road 5B, Near KTPO, Whitefield, Bangalore has been rated 4.7 out of 5. Average cost for 2 : 2500\n\n   3. Brahma Brews in Opposite Brigade Palm Springs, 24th Main, 7th Phase, JP Nagar, Bangalore has been rated 4.6 out of 5. Average cost for 2 : 1900\n\n   4. Byg Brewski Brewing Company in Opposite MK Retail, Sarjapur Road, Bangalore has been rated 4.4 out of 5. Average cost for 2 : 1600\n\n   5. Toit in 298, 100 Feet Road, Namma Metro Pillar 62, Indiranagar, Bangalore has been rated 4.4 out of 5. Average cost for 2 : 2000\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "shubhashri.rane"}
    - slot{"email": "shubhashri.rane"}
    - action_email_valid
    - slot{"email_validity": "False"}
    - utter_emailerror
* ask_email{"email": "shubhashri.rane@gmail.com"}
    - slot{"email": "shubhashri.rane@gmail.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "shubhashri.rane@gmail.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
* restaurant_search{"cuisine": "italian", "location": "Bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Bangalore"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"email_message": "\n   1. Olive Bar And Kitchen in 16, Wood Street, Ashok Nagar, Richmond Road, Bangalore has been rated 4.6 out of 5. Average cost for 2 : 1800\n\n   2. Fenny's Lounge And Kitchen in 115, 3rd Floor, Opposite Raheja Arcade, Koramangala 7th Block, Bangalore has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   3. Smoke House Deli in Plot 1209, Ward 72, HAL 2nd Stage, Doopanahalli, Indiranagar, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1600\n\n   4. Pasta Street in 2022, 100 Feet Road,HAL 2nd Stage, Indiranagar, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1500\n\n   5. Pasta Street in 751, 80 Feet Road, Opposite SBI Bank, Koramangala 4th Block, Bangalore has been rated 4.5 out of 5. Average cost for 2 : 1500\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye

<!--- Story 23 -->		
## Happy path with location and budget, checking response of deny on asking "did that help"
    - utter_greet
* restaurant_search{"budget": "High", "location": "mumbai"}
    - slot{"budget": "High"}
    - slot{"location": "mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"email_message": "\n   1. Hard Rock Cafe in Sharyans Audeu, Fun Cinema Lane, Veera Desai Industrial Estate, Near Balaji Telefilms, Veera Desai Area, Mumbai has been rated 4.5 out of 5. Average cost for 2 : 2500\n\n   2. The Bandra Project by PizzaExpress in 534A, Ground Floor, HSBC Building, Dr. Ambedkar Road, Pali Hill, Bandra West, Mumbai has been rated 4.4 out of 5. Average cost for 2 : 2200\n\n   3. Smoke House Deli in 462, High Street Phoenix, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.4 out of 5. Average cost for 2 : 2500\n\n   4. Tipsy Gypsy in Level One, Fun Republic Mall, Off New Link Road, Near Veera Desai Area, Mumbai has been rated 4.3 out of 5. Average cost for 2 : 1800\n\n   5. Doolally Taproom in C18-21, Dalia Industrial Estate, Near Fun Republic, Veera Desai Area, Mumbai has been rated 4.3 out of 5. Average cost for 2 : 1800\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc.rdg"}
    - slot{"email": "abc.rdg"}
    - action_email_valid
    - slot{"email_validity": "False"}
    - utter_emailerror
* deny
    - utter_did_that_help
* deny
    - utter_goodbye
* goodbye
    - utter_goodbye

<!--- Story 24 -->		
## complete path , deny send email, but again ask to send email.
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Vellore"}
    - slot{"location": "Vellore"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_search_restaurants
    - slot{"location": "Vellore"}
    - slot{"email_message": "\n   1. Madurai Pandiyan Hotel in 104, Thiru.Vi.Ka Nagar, Main Road, Thottapalayam, Vellore has been rated 4.0 out of 5. Average cost for 2 : 300\n\n   2. Hotel Sangamam in Chittoor Main Road, Near Indian Bank, Katpadi, Gandhi Nagar, Vellore has been rated 3.1 out of 5. Average cost for 2 : 300\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* ask_email{"email": "shubhashri.rane@gmail.com"}
    - slot{"email": "shubhashri.rane@gmail.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "shubhashri.rane@gmail.com"}
    - utter_confirm_email
* goodbye{"goodbye": "byw"}
    - utter_goodbye

<!--- Story 25 -->		
## Happy path , checkign deny after ask email
* greet
    - utter_greet
* restaurant_search{"budget": "High", "cuisine": "mexican", "location": "mumbai"}
    - slot{"budget": "High"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"email_message": "\n   1. Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9 out of 5. Average cost for 2 : 1800\n\n   2. Bastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8 out of 5. Average cost for 2 : 4200\n\n   3. Gallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   4. The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   5. Aer - Four Seasons in 1/136, E Moses Road, Worli, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 4500\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 26 -->		
## Happy path , testing deny email, then affirm email 
* restaurant_search{"budget": "High", "cuisine": "north indian", "location": "Vellore"}
    - slot{"budget": "High"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Vellore"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "Vellore"}
    - slot{"email_message": "\n   1. Hundreds Heritage in 10, 14th East Cross Road, Gandhi Nagar, Vellore has been rated 4.5 out of 5. Average cost for 2 : 1500\n\n   2. Earth Plate in Hotel Aavanaa Inn, 144, Arcot Road, Opposite to CMC Hospital, Thottapalayam, Vellore has been rated 4.0 out of 5. Average cost for 2 : 1000\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
* ask_email{"email": "shubhashri.rane@gmail.com"}
    - slot{"email": "shubhashri.rane@gmail.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - export

<!--- Story 27 -->		
## complete path  , testing deny email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"email_message": "\n   1. Hakkasan in 206, 2nd Floor, Krystal, Waterfield Road, Linking Road, Bandra West, Mumbai has been rated 4.7 out of 5. Average cost for 2 : 2600\n\n   2. Pa Pa Ya in G-2, Ground Floor, North Avenue, Maker Maxity, Bandra Kurla Complex, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   3. Yazu - Pan Asian Supper Club in 9, Ground Floor, Raheja Classic Complex, Near Infinity Mall, Phase D, Shastri Nagar, Oshiwara, Andheri West, Mumbai has been rated 4.5 out of 5. Average cost for 2 : 2200\n\n   4. All Stir Fry - Gordon House Hotel in 5 Battery Street, Opposite Regal Cinema, Apollo Bunder, Near Colaba, Mumbai has been rated 4.5 out of 5. Average cost for 2 : 2300\n\n   5. By the Mekong - The St. Regis Mumbai in The St. Regis, 462, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.5 out of 5. Average cost for 2 : 4000\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 28 -->		
## complete path  , testing intuition
* greet
    - utter_greet
* restaurant_search{"budget": "High", "cuisine": "mexican", "location": "Mumbai"}
    - slot{"budget": "High"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"email_message": "\n   1. Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9 out of 5. Average cost for 2 : 1800\n\n   2. Bastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8 out of 5. Average cost for 2 : 4200\n\n   3. Gallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   4. The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   5. Sammy Sosa in Shop 18, Meera CHS, Near Mega Mall, Oshiwara Link Road, Oshiwara, Andheri West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n"}
    - slot{"results_found": "True"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 29 -->		
## complete path  , input invalid cuisine on prompt
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
    - slot{"location": "delhi"}
    - slot{"email_message": "\n   1. Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9 out of 5. Average cost for 2 : 1800\n\n   2. Bastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8 out of 5. Average cost for 2 : 4200\n\n   3. Gallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   4. The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   5. Sammy Sosa in Shop 18, Meera CHS, Near Mega Mall, Oshiwara Link Road, Oshiwara, Andheri West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n"}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 30 -->		
## happy path  , input invalid cuisine on prompt
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "mumbai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "valid"}
	- slot{"cuisine_validity" : "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants	
    - slot{"location": "Mumbai"}
    - slot{"email_message": "\n   1. Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9 out of 5. Average cost for 2 : 1800\n\n   2. Bastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8 out of 5. Average cost for 2 : 4200\n\n   3. Gallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   4. The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   5. Sammy Sosa in Shop 18, Meera CHS, Near Mega Mall, Oshiwara Link Road, Oshiwara, Andheri West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n"}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 31 -->		
## complete path  , input invalid cuisine on prompt
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "mumbai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "valid"}
	- slot{"cuisine_validity" : "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants	
    - slot{"location": "mumbai"}
    - slot{"email_message": "\n   1. Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9 out of 5. Average cost for 2 : 1800\n\n   2. Bastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8 out of 5. Average cost for 2 : 4200\n\n   3. Gallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 2600\n\n   4. The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n\n   5. Sammy Sosa in Shop 18, Meera CHS, Near Mega Mall, Oshiwara Link Road, Oshiwara, Andheri West, Mumbai has been rated 4.6 out of 5. Average cost for 2 : 1600\n"}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "abc@abc.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 31 -->		
## happy path with invalid location
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Rishikesh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Rishikesh"}
	- action_location_valid
	- action_cuisine_valid
	- slot{"location_validity" : "invalid"}
	- slot{"cuisine_validity" : "valid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_location_valid
    - slot{"location_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "goa"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 32 -->
## complete path with valid email
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export

<!--- Story 32 -->		
## complete path  , testing intuition
* greet
    - utter_greet
* restaurant_search{"budget": "Low", "location": "Vellore"}
    - slot{"budget": "Low"}
    - slot{"location": "Vellore"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - action_search_restaurants	
	- slot{"location": "Vellore"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export


<!--- Story 33 -->		
## happy path with synonym , testing intuition
* greet
    - utter_greet
* restaurant_search{"budget": "Low", "cuisine": "mexican", "location": "Vellore"}
    - slot{"budget": "Low"}
    - slot{"location": "Vellore"}
    - slot{"cuisine": "mexican"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - action_search_restaurants	
	- slot{"location": "Vellore"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 34 -->
## complete path with location first
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_location_valid
	- slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_location_valid
    - slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "goa"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_goodbye
    - export

<!--- Story 34 -->
## complete path with location first
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_location_valid
	- slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "mumbai"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
	- action_location_valid
	- slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_location_valid
    - slot{"location_validity" : "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
	- slot{"cuisine_validity" : "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants	
	- slot{"location": "goa"}
    - slot{"email_message":""}
    - slot{"results_found": "True"}
	- utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_email_valid
    - slot{"email_validity": "True"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_confirm_email
* affirm
    - utter_goodbye
    - export