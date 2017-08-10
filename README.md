# Simple FAQ ChatBot

This example uses  [BotHub.Studio](https://bothub.studio/?utm_source=github&utm_medium=display&utm_campaign=faq_chatbot).

If this is your first time to use Bothub.Studio, please see [here.](https://medium.com/bothub-studio/build-a-telegram-chatbot-with-python-2dafd6c033bd)

## Installation

To install bothub-cli:

````
$ pip install bothub-cli
````

## Getting Started

Before using bothub-cli, you need to tell it about your [BotHub.Studio](https://bothub.studio/?utm_source=github&utm_medium=display&utm_campaign=faq_chatbot) credentials.

```
$ bothub configure
Username: myuser
Password: mysecret
```

Project Init & Deploy:

````
$ git clone https://github.com/MKtalk/simple_faq_bot.git
$ cd simple_faq_bot
$ bothub init
Project name: <your bot name>
$ bothub deploy
````

You also need to configure channel to use.

````
$ bothub channel add telegram --api-key=<my-api-key>
````

## Usage

Add property for keyboard usage:

ex)
````
$ bothub property set keyboard Question1,Question2,Question3,Question4
$ bothub property set Question1 "{'answer': 'Answer 1', 'title': 'Go Answer1', 'link': 'http://www.example.com/answer1'}"
$ bothub property set Question2 "{'answer': 'Answer 2', 'title': 'Go Answer2', 'link': 'http://www.example.com/answer2'}"
````


Finally, send a message to your bot.
