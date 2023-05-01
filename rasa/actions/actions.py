# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import sys
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd


class GoodDay(Action):
    def name(self) -> Text:
        return "action_good_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("tempoMin", tracker.get_slot("tempoMin") + tracker.get_slot("changeAmount"))]


class BadDay(Action):
    def name(self) -> Text:
        return "action_bad_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("tempoMax", tracker.get_slot("tempoMax") - tracker.get_slot("changeAmount"))]


class CelebrateY(Action):
    def name(self) -> Text:
        return "action_celebrate_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("valenceMin", tracker.get_slot("valenceMin")+tracker.get_slot("changeAmount"))]


class CelebrateN(Action):
    def name(self) -> Text:
        return "action_celebrate_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("valenceMax", tracker.get_slot("valenceMax")-tracker.get_slot("changeAmount"))]


class DanceY(Action):
    def name(self) -> Text:
        return "action_dance_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("danceabilityMin", tracker.get_slot("danceabilityMin")+tracker.get_slot("changeAmount"))]


class DanceN(Action):
    def name(self) -> Text:
        return "action_dance_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("danceabilityMax", tracker.get_slot("danceabilityMax")-tracker.get_slot("changeAmount"))]


class SingY(Action):
    def name(self) -> Text:
        return "action_sing_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("speechinessMin", tracker.get_slot("speechinessMin")+tracker.get_slot("changeAmount"))]


class SingN(Action):
    def name(self) -> Text:
        return "action_sing_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("speechinessMax", tracker.get_slot("speechinessMax")-tracker.get_slot("changeAmount"))]


class CheerUpY(Action):
    def name(self) -> Text:
        return "action_cheer_up_y"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("valenceMin", tracker.get_slot("valenceMin")+tracker.get_slot("changeAmount"))]


class CheerUpN(Action):
    def name(self) -> Text:
        return "action_cheer_up_n"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("valenceMax", tracker.get_slot("valenceMax")-tracker.get_slot("changeAmount"))]


class SuggestSong(Action):
    def name(self) -> Text:
        return "action_suggest_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_csv('actions/data.csv')
        sd = SongData(df)
        result = sd.acousticness(tracker.get_slot("tempoMin"), tracker.get_slot("tempoMax")
                    ).danceability(tracker.get_slot("danceabilityMin"), tracker.get_slot("danceabilityMax")
                    ).energy(tracker.get_slot("energyMin"), tracker.get_slot("energyMax")
                    ).instrumentalness(tracker.get_slot("instrumentalnessMin"), tracker.get_slot("instrumentalnessMax")
                    ).liveness(tracker.get_slot("livenessMin"), tracker.get_slot("livenessMax")
                    ).speechiness(tracker.get_slot("speechinessMin"), tracker.get_slot("speechinessMax")
                    ).valence(tracker.get_slot("valenceMin"), tracker.get_slot("valenceMax")
                    ).dataFrame

        suggested = result.sample()
        dispatcher.utter_message(
            "Suggested song: " + suggested.iloc[0]['song_title'] + ", by: " + suggested.iloc[0]['artist'])

        return []


class SongData:
    def __init__(self, dataframe):
        self.dataFrame = dataframe

    def acousticness(self, minAcousticness, maxAcousticness):
        if minAcousticness <= self.dataFrame['acousticness'].min():
            minAcousticness = self.dataFrame['acousticness'].min()
        if maxAcousticness >= self.dataFrame['acousticness'].max():
            maxAcousticness = self.dataFrame['acousticness'].max()
        if minAcousticness >= self.dataFrame['acousticness'].max():
            minAcousticness = self.dataFrame['acousticness'].max()
        if maxAcousticness <= self.dataFrame['acousticness'].min():
            maxAcousticness = self.dataFrame['acousticness'].min()
        if minAcousticness > maxAcousticness:
            temp = minAcousticness
            minAcousticness = maxAcousticness
            maxAcousticness = temp

        return SongData(self.dataFrame[
                            (self.dataFrame['acousticness'] <= maxAcousticness) &
                            (self.dataFrame['acousticness'] >= minAcousticness)])

    def danceability(self, minDanceability, maxDanceability):
        if minDanceability <= self.dataFrame['danceability'].min():
            minDanceability = self.dataFrame['danceability'].min()
        if maxDanceability >= self.dataFrame['danceability'].max():
            maxDanceability = self.dataFrame['danceability'].max()
        if minDanceability >= self.dataFrame['danceability'].max():
            minDanceability = self.dataFrame['danceability'].max()
        if maxDanceability <= self.dataFrame['danceability'].min():
            maxDanceability = self.dataFrame['danceability'].min()
        if minDanceability > maxDanceability:
            temp = minDanceability
            minDanceability = maxDanceability
            maxDanceability = temp

        return SongData(self.dataFrame[
                            (self.dataFrame['danceability'] <= maxDanceability) &
                            (self.dataFrame['danceability'] >= minDanceability)])

    def energy(self, minEnergy, maxEnergy):
        if minEnergy <= self.dataFrame['energy'].min():
            minEnergy = self.dataFrame['energy'].min()
        if maxEnergy >= self.dataFrame['energy'].max():
            maxEnergy = self.dataFrame['energy'].max()
        if minEnergy >= self.dataFrame['energy'].max():
            minEnergy = self.dataFrame['energy'].max()
        if maxEnergy <= self.dataFrame['energy'].min():
            maxEnergy = self.dataFrame['energy'].min()
        if minEnergy > maxEnergy:
            temp = minEnergy
            minEnergy = maxEnergy
            maxEnergy = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['energy'] <= maxEnergy) &
                            (self.dataFrame['energy'] >= minEnergy)])

    def instrumentalness(self, minInstrumentalness, maxInstrumentalness):
        if minInstrumentalness <= self.dataFrame['instrumentalness'].min():
            minInstrumentalness = self.dataFrame['instrumentalness'].min()
        if maxInstrumentalness >= self.dataFrame['instrumentalness'].max():
            maxInstrumentalness = self.dataFrame['instrumentalness'].max()
        if minInstrumentalness >= self.dataFrame['instrumentalness'].max():
            minInstrumentalness = self.dataFrame['instrumentalness'].max()
        if maxInstrumentalness <= self.dataFrame['instrumentalness'].min():
            maxInstrumentalness = self.dataFrame['instrumentalness'].min()
        if minInstrumentalness > maxInstrumentalness:
            temp = minInstrumentalness
            minInstrumentalness = maxInstrumentalness
            maxInstrumentalness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['instrumentalness'] <= maxInstrumentalness) &
                            (self.dataFrame['instrumentalness'] >= minInstrumentalness)])

    def liveness(self, minLiveness, maxLiveness):
        if minLiveness <= self.dataFrame['liveness'].min():
            minLiveness = self.dataFrame['liveness'].min()
        if maxLiveness >= self.dataFrame['liveness'].max():
            maxLiveness = self.dataFrame['liveness'].max()
        if minLiveness >= self.dataFrame['liveness'].max():
            minLiveness = self.dataFrame['liveness'].max()
        if maxLiveness <= self.dataFrame['liveness'].min():
            maxLiveness = self.dataFrame['liveness'].min()
        if minLiveness > maxLiveness:
            temp = minLiveness
            minLiveness = maxLiveness
            maxLiveness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['liveness'] <= maxLiveness) &
                            (self.dataFrame['liveness'] >= minLiveness)])

    def speechiness(self, minSpeechiness, maxSpeechiness):
        if minSpeechiness <= self.dataFrame['speechiness'].min():
            minSpeechiness = self.dataFrame['speechiness'].min()
        if maxSpeechiness >= self.dataFrame['speechiness'].max():
            maxSpeechiness = self.dataFrame['speechiness'].max()
        if minSpeechiness >= self.dataFrame['speechiness'].max():
            minSpeechiness = self.dataFrame['speechiness'].max()
        if maxSpeechiness <= self.dataFrame['speechiness'].min():
            maxSpeechiness = self.dataFrame['speechiness'].min()
        if minSpeechiness > maxSpeechiness:
            temp = minSpeechiness
            minSpeechiness = maxSpeechiness
            maxSpeechiness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['speechiness'] <= maxSpeechiness) &
                            (self.dataFrame['speechiness'] >= minSpeechiness)])

    def valence(self, minValence, maxValence):
        if minValence <= self.dataFrame['valence'].min():
            minValence = self.dataFrame['valence'].min()
        if maxValence >= self.dataFrame['valence'].max():
            maxValence = self.dataFrame['valence'].max()
        if minValence >= self.dataFrame['valence'].max():
            minValence = self.dataFrame['valence'].max()
        if maxValence <= self.dataFrame['valence'].min():
            maxValence = self.dataFrame['valence'].min()
        if minValence > maxValence:
            temp = minValence
            minValence = maxValence
            maxValence = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['valence'] <= maxValence) &
                            (self.dataFrame['valence'] >= minValence)])

    def tempo(self, minTempo, maxTempo):
        if minTempo <= self.dataFrame['tempo'].min():
            minTempo = self.dataFrame['tempo'].min()
        if maxTempo >= self.dataFrame['tempo'].max():
            maxTempo = self.dataFrame['tempo'].max()
        if minTempo >= self.dataFrame['tempo'].max():
            minTempo = self.dataFrame['tempo'].max()
        if maxTempo <= self.dataFrame['tempo'].min():
            maxTempo = self.dataFrame['tempo'].min()
        if minTempo > maxTempo:
            temp = minTempo
            minTempo = maxTempo
            maxTempo = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['tempo'] <= maxTempo) &
                            (self.dataFrame['tempo'] >= minTempo)])
