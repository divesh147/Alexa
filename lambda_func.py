def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "amazingworldfacts":
        return world_facts(intent, session)
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
    speechOutput =  "Hello, Welcome to Amazing World Facts. " \
                    "You can ask me amazing world facts by saying Tell me amazing facts"
    repromptText =  "You can ask me amazing world facts by saying Tell me amazing facts"
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def world_facts(intent, session):
    import random
    index = random.randint(0,len(facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = facts[index] 
    repromptText = "You can ask me amazing world facts by saying Tell me amazing facts"
    shouldEndSession = False                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Amazing World Facts Alexa Skills Kit. Have a great day! "
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


facts = ["In 1948, before Pakistan had the facilities, The Reserve Bank of India issued provisional notes for the Pakistani Rupee.",
         "In 2011, a woman named Aimee Davison purchased a \'non visible\' piece of art for $10,000.",
         "In 2006, a woman lit matches in a flight to cover her fart smell. That forced an emergency landing",
         "Saddam Hussein was the author of a romantic novel called Zabiba and the King.",
         "In Taiwan, there is a restaurant that serves food on miniature toilets.",
         "Prince Charles & Prince William always travel in separate planes in case there is a crash, one needs to survive.",
         "Las Vegas casinos have no clocks. That way, customers tend to spend more time.",
         "Everyday, 20 banks are robbed. The average amount stolen is 1,72,100 rupees.",
         "Cockroaches were there 120 million years before dinosaurs roamed the earth. And they survived!",
         "As a kid, Adolf Hitler wanted to be a priest.",
         "He also suffered from Ailurophobia, which is a fear of cats. Alexander the Great, Napoleon and Mussolini had the same phobia.",
         "Global Warming helped settle a land dispute between India and Bangladesh. The area in question was New Moore, or South Talpatti. But the island drowned because of global warming in 2010.",
         "Butterflies were originally called flutterflies.",
         "Once, carrots were purple. Until late in the 16th century Dutch growers took mutant strains of the purple carrot and gradually developed them into the sweet, plump, orange variety we have today.",
         "Millions of crabs migrate on the Christmas Islands towards the shore to mate and populate. There are around 43.2 million crabs on the island in the Indian Ocean.",
         "The 110-acre \'Snake Island\' in Sao Paulo has 4,000 snakes. Which is one snake for every 6 square yards. It is one of the world's deadliest islands.",
         "Worldwide, women earn US$18 trillion but spend US$28 trillion.",
         "Charles Darwin ate almost every animal he discovered.",
         "Russia has a larger surface area than Pluto. However, it has less population than the small country of Bangladesh.",
         "Two actors have died while playing Judas in live Biblical plays by accidentally hanging themselves for real during the death scene.",
         "For every human, there are 1.6 million ants in the world. However, the weight of all ants combined is almost equal to the weight of all humans combined.",
         "The world's largest family stays in India. Man named Ziona Chana has 39 wives and 94 children.",
         "Amazon holds a patent on 1-click buying; Apple pays them licensing fees.",
         "Microsoft has a patent, for opening a new window when you click a hyperlink. It expires in 2021.",
         "Speaking of patents, Halliburton Company once tried to patent patenting.",
         "Brad Pitt was banned from entering China for his role in the movie Seven Years in Tibet (1997), for portraying the Dalai Lama in positive light.",
         "A man planted 7,000 trees to make a guitar shaped forest as tribute to his wife."]
