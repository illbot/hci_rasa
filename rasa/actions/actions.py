# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import sys
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted
import pandas as pd


class GoodDay(Action):
    def name(self) -> Text:
        return "action_good_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("tempoMin", tracker.get_slot("tempoMin") + tracker.get_slot("changeAmount")),
                SlotSet("energyMin", tracker.get_slot("energyMin") + tracker.get_slot("changeAmount"))]


class BadDay(Action):
    def name(self) -> Text:
        return "action_bad_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("tempoMax", tracker.get_slot("tempoMax") - tracker.get_slot("changeAmount")),
                SlotSet("energyMax", tracker.get_slot("energyMax") - tracker.get_slot("changeAmount"))]


class CelebrateY(Action):
    def name(self) -> Text:
        return "action_celebrate_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("valenceMin", tracker.get_slot("valenceMin") + tracker.get_slot("changeAmount"))]


class CelebrateN(Action):
    def name(self) -> Text:
        return "action_celebrate_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("valenceMin", tracker.get_slot("valenceMin") - tracker.get_slot("changeAmount"))]


class DanceY(Action):
    def name(self) -> Text:
        return "action_dance_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("danceabilityMin", tracker.get_slot("danceabilityMin") + tracker.get_slot("changeAmount"))]


class DanceN(Action):
    def name(self) -> Text:
        return "action_dance_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("danceabilityMax", tracker.get_slot("danceabilityMax") - tracker.get_slot("changeAmount"))]


class SingY(Action):
    def name(self) -> Text:
        return "action_sing_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("instrumentalnessMin", tracker.get_slot("instrumentalnessMin") + tracker.get_slot("changeAmount")),
                SlotSet("acousticnessMin", tracker.get_slot("acousticnessMin") + tracker.get_slot("changeAmount"))]


class SingN(Action):
    def name(self) -> Text:
        return "action_sing_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("instrumentalnessMax", tracker.get_slot("instrumentalnessMax") - tracker.get_slot("changeAmount")),
                SlotSet("acousticnessMax", tracker.get_slot("acousticnessMax") - tracker.get_slot("changeAmount"))]


class CheerUpY(Action):
    def name(self) -> Text:
        return "action_cheer_up_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("valenceMin", tracker.get_slot("valenceMin") + tracker.get_slot("changeAmount"))]


class CheerUpN(Action):
    def name(self) -> Text:
        return "action_cheer_up_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("valenceMax", tracker.get_slot("valenceMax") - tracker.get_slot("changeAmount"))]


class SuggestSong(Action):
    def name(self) -> Text:
        return "action_suggest_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_csv('actions/data.csv')
        sd = SongData(df)
        result = sd.tempo(tracker.get_slot("tempoMin"), tracker.get_slot("tempoMax")
                    ).energy(tracker.get_slot("energyMin"), tracker.get_slot("energyMax")
                    ).valence(tracker.get_slot("valenceMin"), tracker.get_slot("valenceMax")
                    ).danceability(tracker.get_slot("danceabilityMin"), tracker.get_slot("danceabilityMax")
                    ).acousticness(tracker.get_slot("acousticnessMin"), tracker.get_slot("acousticnessMax")
                    ).instrumentalness(tracker.get_slot("instrumentalnessMin"), tracker.get_slot("instrumentalnessMax")
                    ).dataFrame

        suggested = result.sample()
        dispatcher.utter_message(suggested.iloc[0]['song_title'] + ", by: " + suggested.iloc[0]['artist'])

        return []


class Restart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Restarted!")
        return [Restarted()]


class SongData:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    def acousticness(self, minAcousticness, maxAcousticness):
        minData = self.dataFrame['acousticness'].min()
        maxData = self.dataFrame['acousticness'].max()
        if minAcousticness <= minData:
            minAcousticness = minData
        if maxAcousticness >= maxData:
            maxAcousticness = maxData
        if minAcousticness >= maxData:
            minAcousticness = maxData
        if maxAcousticness <= minData:
            maxAcousticness = minData
        if minAcousticness > maxAcousticness:
            temp = minAcousticness
            minAcousticness = maxAcousticness
            maxAcousticness = temp

        return SongData(self.dataFrame[
                            (self.dataFrame['acousticness'] <= maxAcousticness) &
                            (self.dataFrame['acousticness'] >= minAcousticness)])

    def danceability(self, minDanceability, maxDanceability):
        minData = self.dataFrame['danceability'].min()
        maxData = self.dataFrame['danceability'].max()
        if minDanceability <= minData:
            minDanceability = minData
        if maxDanceability >= maxData:
            maxDanceability = maxData
        if minDanceability >= maxData:
            minDanceability = maxData
        if maxDanceability <= minData:
            maxDanceability = minData
        if minDanceability > maxDanceability:
            temp = minDanceability
            minDanceability = maxDanceability
            maxDanceability = temp

        return SongData(self.dataFrame[
                            (self.dataFrame['danceability'] <= maxDanceability) &
                            (self.dataFrame['danceability'] >= minDanceability)])

    def energy(self, minEnergy, maxEnergy):
        minData = self.dataFrame['energy'].min()
        maxData = self.dataFrame['energy'].max()
        if minEnergy <= minData:
            minEnergy = minData
        if maxEnergy >= maxData:
            maxEnergy = maxData
        if minEnergy >= maxData:
            minEnergy = maxData
        if maxEnergy <= minData:
            maxEnergy = minData
        if minEnergy > maxEnergy:
            temp = minEnergy
            minEnergy = maxEnergy
            maxEnergy = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['energy'] <= maxEnergy) &
                            (self.dataFrame['energy'] >= minEnergy)])

    def instrumentalness(self, minInstrumentalness, maxInstrumentalness):
        minData = self.dataFrame['instrumentalness'].min()
        maxData = self.dataFrame['instrumentalness'].max()
        if minInstrumentalness <= minData:
            minInstrumentalness = minData
        if maxInstrumentalness >= maxData:
            maxInstrumentalness = maxData
        if minInstrumentalness >= maxData:
            minInstrumentalness = maxData
        if maxInstrumentalness <= minData:
            maxInstrumentalness = minData
        if minInstrumentalness > maxInstrumentalness:
            temp = minInstrumentalness
            minInstrumentalness = maxInstrumentalness
            maxInstrumentalness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['instrumentalness'] <= maxInstrumentalness) &
                            (self.dataFrame['instrumentalness'] >= minInstrumentalness)])


    def tempo(self, minTempoPercent, maxTempoPercent):
        minData = self.dataFrame['tempo'].min()
        maxData = self.dataFrame['tempo'].max()
        minTempo = minData + (maxData-minData)*minTempoPercent
        maxTempo = minData + (maxData - minData) * maxTempoPercent
        if minTempo <= minData:
            minTempo = minData
        if maxTempo >= maxData:
            maxTempo = maxData
        if minTempo >= maxData:
            minTempo = maxData
        if maxTempo <= minData:
            maxTempo = minData
        if minTempo > maxTempo:
            temp = minTempo
            minTempo = maxTempo
            maxTempo = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['tempo'] <= maxTempo) &
                            (self.dataFrame['tempo'] >= minTempo)])

    def valence(self, minValence, maxValence):
        minData = self.dataFrame['valence'].min()
        maxData = self.dataFrame['valence'].max()
        if minValence <= minData:
            minValence = minData
        if maxValence >= maxData:
            maxValence = maxData
        if minValence >= maxData:
            minValence = maxData
        if maxValence <= minData:
            maxValence = minData
        if minValence > maxValence:
            temp = minValence
            minValence = maxValence
            maxValence = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['valence'] <= maxValence) &
                            (self.dataFrame['valence'] >= minValence)])