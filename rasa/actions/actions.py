# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ReadCSV(Action):
    def name(self) -> Text:
        return "action_read_csv"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #with open('data.csv', 'r') as file:
        #    csv_content = csv.reader(file)
        #    data = []
        #    for row in csv_content:
        #        data.append(row)
        
        # Set a slot with the data
        dispatcher.utter_message("Hi there, I am a music quessing bot!")
        return [SlotSet("csv_data", "Lefutott")]


class RecommendMusic(Action):
    def name(self) -> Text:
        return "action_recommend_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #Get the user's mood from the "mood" entity
        performer = tracker.get_slot("performer")
        csv_data = tracker.get_slot("csv_data")
        dispatcher.utter_message("CSV_DATA: "+csv_data)

        # Your custom code to recommend music here, based on the mood
        if performer:
            # Respond to the user with the recommendation
            dispatcher.utter_message("Here is a music recommendation for you based on your mood: "+performer)
        else:
            dispatcher.utter_message("Sorry I didn't catch that")
        
        return []