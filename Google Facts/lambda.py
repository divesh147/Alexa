def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session): return welcomeuser()

def onIntent(intentRequest, session):
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "googlefacts":
        return google_facts(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello! Namaste!"
    speechOutput =  "Hello, Welcome to Google Facts. " \
                    "You can ask me interesting google facts by saying Tell me google facts."
    repromptText =  "You can ask me interesting google facts by saying Tell me google facts."
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def google_facts(intent, session):
    import random
    index = random.randint(0,len(facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = facts[index]
    shouldEndSession = True
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Bye Bye"
    speechOutput = "Thank you for using Google Facts Skill. Have a nice day ahead! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }


facts = [
    "The name 'Google' is actually derived from the mathematical term 'googol' which is basically 1 with a 100 zeros following it.",
    "Co-founders Larry Page and Sergey Brin originally named Google 'Backrub'.",
    "As part of their green initiative, Google regularly rents goats to mow the lawns of their mountain view HQ.",
    "Thanks to Google Instant, you can't actually use the 'I'm Feeling Lucky' button anymore.",
    "Since 2010, Google has been acquiring an average of one company every week.",
    "Google uses a web tool called foo.bar to recruit new employees based on what they search for online.",
    "The first ever Google Doodle was a Burning Man stick figure that came out on August 30, 1998.",
    "Larry and Sergey's private planes have runways in NASA, where no other planes are allowed to land.",
    "Google owns common misspellings of its own name as well, such as www.gooogle.com, www.gogle.com, and www.googlr.com.",
    "The first Google computer storage was built with Legos.",
    "Google employees in the US get death benefits which guarantee that the surviving spouse will receive 50% of their salary every year for the next decade.",
    "No part of a Google office is allowed to be more than 150 feet away from some kind of food.",
    "Google helps pronounce massive numbers if you type '=english' after searching for a number.",
    "There's a rotated version of Google known as 'Google Mirror', which shows everything in a mirrored avatar.",
    "Google wanted to sell itself to online company Excite in 1999 for 1 million dollar, but the Excite CEO rejected the offer."
    ]
