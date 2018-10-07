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
    if intentName == "compfacts":
        return comp_facts(intent, session)
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
    speechOutput =  "Hello, Welcome to Computer Facts. " \
                    "You can ask me an interesting computer fact by saying Tell me a fact."
    repromptText =  "You can ask me an interesting computer fact by saying Tell me a fact."
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def comp_facts(intent, session):
    import random
    index = random.randint(0,len(facts)-1)
    cardTitle = "Computer Fact"
    sessionAttributes = {}
    speechOutput = facts[index]
    shouldEndSession = True
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Bye Bye"
    speechOutput = "Thank you for using Computer Facts Skill. Have a nice day ahead! "
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
    "The first electronic computer ENIAC weighed more than 27 tons and took up 1800 square feet.",
    "Only about 10% of the world’s currency is physical money, the rest only exists on computers.",
    "TYPEWRITER is the longest word that you can write using the letters only on one row of the keyboard of your computer.",
    "Doug Engelbart invented the first computer mouse in around 1964 which was made of wood.",
    "There are more than 5000 new computer viruses are released every month.",
    "Around 50% of all Wikipedia vandalism is caught by a single computer program with more than 90% accuracy.",
    "If there was a computer as powerful as the human brain, it would be able to do 38 thousand trillion operations per second and hold more than 3580 terabytes of memory.",
    "The password for the computer controls of nuclear tipped missiles of the U.S was 00000000 for eight years.",
    "Approximately 70% of virus writers are said to work under contract for organized crime syndicates.",
    "HP, Microsoft and Apple have one very interesting thing in common – they were all started in a garage.",
    "An average person normally blinks 20 times a minute, but when using a computer he/she blinks only 7 times a minute.",
    "The house where Bill Gates lives, was designed using a Macintosh computer.",
    "The first ever hard disk drive was made in 1979, and could hold only 5MB of data.",
    "The first 1GB hard disk drive was announced in 1980 which weighed about 550 pounds, and had a price tag of $40,000.",
    "More than 80% of the emails sent daily are spams.",
    "A group of 12 engineers designed IBM PC and they were called as “The Dirty Dozen”.",
    "The original name of windows was Interface Manager.",
    "The first microprocessor created by Intel was the 4004. It was designed for a calculator, and in that time nobody imagined where it would lead.",
    "IBM 5120 from 1980 was the heaviest desktop computer ever made. It weighed about 105 pounds, not including the 130 pounds external floppy drive.",
    "Genesis Device demonstration video in Star Trek II: The Wrath of Khan was the the first entirely computer generated movie sequence in the history of cinema. That studio later become Pixar."
    ]
