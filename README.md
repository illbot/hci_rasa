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


Step-by step deploy guide to VM:

- uncomment  endpoins.yml; url: "http://app:5055/webhook"
- after VM DNS:
  - frontend/index.html
    - "<div id="rasa-chat-widget" data-websocket-url="http://{VM_DNS_NAME}:5005/socket.io"></div>"
- git commit and push with the latest builded model under models/
- docker build -t illesbotond/personal:rasa_action_server .
- docker push

in VM:

// git install
- sudo apt update
- sudo apt install git

// docker install
- sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

- install docker
- git pull repo
- docker-compuse up -d

VM settings:
- open ports: 80, 5005
