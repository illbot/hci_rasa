# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class RecommendMusic(Action):
    def name(self) -> Text:
        return "action_recommend_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #Get the user's mood from the "mood" entity
        performer = tracker.get_slot("performer")
        # Your custom code to recommend music here, based on the mood
        if performer:
            # Respond to the user with the recommendation
            dispatcher.utter_message("Here is a music recommendation for you based on your mood: "+performer)
        else:
            dispatcher.utter_message("Sorry I didn't catch that")
        
        return []