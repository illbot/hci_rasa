# hci_rasa

workflow for modifing:
1. py -m rasa train
2. py -m rasa shell

data/stories.yml - where you can define stories, this tells the bot what to answer to intents

data/nlu.yml - here you can define intents (what the users say)

domain.yml - here you can define what the bot will answer

To use custom actions:
py -m rasa run actions

then start 
py -m rasa shell


- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy

- story: sad path 1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy

- story: sad path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: deny
  - action: utter_goodbye
