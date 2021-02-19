from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import AllSlotsReset, SlotSet, Restarted
from email.message import EmailMessage


import smtplib
import zomatopy
import json
import logging
import re

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain):
        restaurants_found = []
        response_message = ""
        email_message= ""
        global res
        config={'user_key':'065eb7b87d82ccabf5e8d8b6c4d4da0d'}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
       
        
        
        d = json.loads(results)
        response=""
        if d['results_found'] == 0:
            response= "no results"
        else:
            for restaurant in d['restaurants']:
                restaurants_found.append(
                        {
                            "name": restaurant["restaurant"]["name"],
                            "address": restaurant["restaurant"]["location"]["address"],
                            "avg_cost_for_2": restaurant["restaurant"]["average_cost_for_two"],
                            "rating": restaurant["restaurant"]["user_rating"]["aggregate_rating"],
                        }
                    )
                
        
        if len(restaurants_found) > 0:
            restaurant_filtered_budget = self.filter_restaurant_by_budget(budget, restaurants_found)
            number_of_records=len(restaurant_filtered_budget)
            if (number_of_records == 0):
                res='False'
            else:
                restaurant_filtered_budget =sorted(restaurant_filtered_budget, key = lambda i: i['rating'],reverse=True)
                for index in range(0, number_of_records):
                    restaurant = restaurant_filtered_budget[index]
                    if index < 5:
                        response_message = (
                            response_message
                            + "\n   "
                            + str(index + 1)
                            + ". "
                            + restaurant["name"]
                            + " in "
                            + restaurant["address"] 
                            + " has been rated "
                            + restaurant["rating"]
                            + " out of 5."
                            + "Average cost for 2 : "
                            + str(restaurant["avg_cost_for_2"])
                            + "\n"
                        )
                    if index < 10:
                        email_message = (
                                email_message
                                + "\n   "
                                + str(index + 1)
                                + ". "
                                + restaurant["name"]
                                + " in "
                                + restaurant["address"] 
                                + " has been rated "
                                + restaurant["rating"]
                                + " out of 5. "
                                + "Average cost for 2 : "
                                + str(restaurant["avg_cost_for_2"])
                                + "\n"
                        )      
                res='True'
                dispatcher.utter_message("-----"+response_message)   
        
        return [SlotSet('location',loc),SlotSet("email_message", email_message),SlotSet("results_found",res)]
    
    
    def filter_restaurant_by_budget(self, budget, restaurant_list):
        filtered_restaurant_list = []
       
        rangeMin = 0
        rangeMax = 999999
       
        if budget == "Low":
            rangeMax = 299
        elif budget == "Medium":
            rangeMin = 300
            rangeMax = 700
        elif budget == "High":
            rangeMin = 701
        else:
            rangeMin = 0
            rangeMax = 9999
        print(budget)
        print(rangeMax)
        print(rangeMin)
        for restaurant in restaurant_list:
            print(restaurant)
            print(restaurant["avg_cost_for_2"])
            avg_cost = int(restaurant["avg_cost_for_2"])

            if avg_cost >= rangeMin and avg_cost <= rangeMax:
                filtered_restaurant_list.append(restaurant)

        return filtered_restaurant_list 


class ActionSendEmail(Action):

    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        email_id = tracker.get_slot("email")
        email_message = tracker.get_slot("email_message")
        
        """
            Parse email id
            Required to handle email id sent from SLACK connector
        """
        str_email_id = str(email_id)
        if str_email_id.startswith("mailto"):
            separator_index = str_email_id.index("|")
            if separator_index > -1:
                emails = str_email_id.split("|")
                email_id = emails[1]

        """
            Create an email message
        """
        message = EmailMessage()

        message.set_content(email_message)
        message['Subject'] = "Restaurant Bot | List of {0} Restaurants in {1}".format(cuisine, location)

        """
            Read SMTP configuration
        """
                
        """
            Send email to the user
        """
        try:
            s = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
            s.login('abc@gmail.com', 'abc123')
        
            message['From'] = 'chatfoodie@gmail.com'
            message['To'] = email_id
           
            s.send_message(message)
            s.quit()
        except Exception as e:
            print("failed to send an email")
            print(e)

        return [SlotSet('email',email_id)]

class ActionEmailValidation(Action):
    def name(self):
        return "action_email_valid"

    def run(self, dispatcher, tracker, domain):
        global em
        email = tracker.get_slot("email")
        regex='([\w\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)'
        if(re.search(regex,email)):
            em='True'
        else:
            em='False'
        return [SlotSet('email_validity',em)]

        

class ActionValidateLocation(Action):
    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        location_validity = "valid"
        cities=["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Agra", "Ajmer", "Aligarh", "Allahabad", "Hubli-Dharwad", "Aurangabad", "Amravati", "Amritsar", "Asansol", "Ahmedabad", "Bareilly", "Belgaum", "Bhavnagar", "Bhiwandi", "Bhopal", "Bhilai", "Bilaspur", "Bhubaneswar", "Bikaner", "Chandigarh", "Coimbatore", "Nagpur", "Cuttack", "Bokaro Steel City", "Dehradun", "Dindigul", "Dhanbad", "Durgapur", "Erode", "Faridabad", "Firozabad", "Gulbarga", "Ghaziabad", "Guntur", "Gwalior", "Hamirpur", "Gorakhpur", "Gurgaon", "Guwahati", "Indore", "Jabalpur", "Jaipur", "Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Kakinada", "Karnal", "Kannur", "Kanpur", "Kochi", "Kottayam", "Kolhapur", "Kollam", "Kozhikode", "Kurnool", "Lucknow", "Ludhiana", "Madurai", "Malappuram", "Mathura", "Goa", "Mangalore", "Meerut", "Moradabad", "Mysore", "Nanded", "Nashik", "Nellore", "Noida", "Palakkad", "Patna", "Pondicherry", "Pune", "Raipur", "Purulia", "Prayagraj", "Rajkot", "Rajpur", "Rajahmundry", "Ranchi", "Rourkela", "Sangli", "Salem", "Shimla", "Siliguri", "Solapur", "Srinagar", "Surat", "Thiruvananthapuram", "Thrissur", "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Tiruvannamalai", "Ujjain", "Bijapur", "Vadodara", "Varanasi", "Vijayawada", "Visakhapatnam", "Vellore", "Warangal", "Vasai-Virar City"] 
        
        cities_lower = [city.lower() for city in cities]

        location_validity = (
            "invalid"
            if location.lower() not in cities_lower
            else "valid"
        )
            

        return [SlotSet("location_validity", location_validity)]


""" Custom action to validate input cuisine
"""
class ActionValidateCuisine(Action):
    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_validity = "valid"

        if not cuisine:
            cuisine_validity = "invalid"
        else:
            supported_cuisines = [
                "american",
                "chinese",
                "italian",
                "mexican",
                "north indian",
                "south indian",
            ]

            cuisine_validity = (
                "invalid" if cuisine.lower() not in supported_cuisines else "valid"
            )

        return [SlotSet("cuisine_validity", cuisine_validity)]

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 


class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 

	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]
