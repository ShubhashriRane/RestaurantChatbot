Problem Statement:
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help
users discover restaurants across several Indian cities. 
The main purpose of the bot is to help users discover restaurants quickly and efficiently and
to provide a good restaurant discovery experience.

Requirements:

1. All the updated versions used for the chatbot project have been mentioned in the Requirements.txt file.
2. Also since we were encountering timeout issue, 
   we had set the value of DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS = 30 in anaconda3\Lib\site-packages\rasa\core\channels\console.py 
3. To run the model, please run the following
	- cd to ShubhashriRane
	- run rasa shell --model ./models/20201123-175328.tar.gz in one terminal
	- run rasa actions in another terminal

