def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session): return welcomeuser(launchRequest, session)

def onIntent(intentRequest, session):
    intent = intentRequest['intent']
    intentName = intent['name']
    if intentName == "TableIntent":
        return table(intent, session)
    if intentName == "AMAZON.RepeatIntent":
        return repeat(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return helpuser(intent, session)
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser(launchRequest, session):
    num = 2
    table = out = ""
    for i in range(1,10): 
        table += str(num)+" times "+str(i)+" equals <emphasis level=\"strong\">" + str(num*i) + "</emphasis> <break time=\"1s\"/>\n"
        out += str(num)+" times "+str(i)+" equals " + str(num*i) + "\n"
    table += str(num)+" times "+str(10)+" equals <emphasis level=\"strong\">" + str(num*10) + "</emphasis>\n"
    out += str(num)+" times "+str(10)+" equals " + str(num*10) + "\n"
    sessionAttributes = {"last" : table, "out" : out, "num" : num}
    print(session)
    cardTitle = "Hello! Welcome my Friend!"
    speechOutput =  "Hello, Welcome to Multiplication Table Reciter. \
                    To recite multiplication table of a number, say table of any number. \nFor example, table of 2."
    repromptText =  "To recite multiplication table of a number, say table of any number. \nFor example, table of 2."
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, speechOutput, repromptText, shouldEndSession))

def helpuser(intent, session):
    sessionAttributes = session
    cardTitle = "HELP"
    speechOutput =  "To recite multiplication table of a number, say table of any number. \nFor example, table of 2."
    repromptText =  "To recite multiplication table of a number, say table of any number. \nFor example, table of 2."
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, speechOutput, repromptText, shouldEndSession))
    
def table(intent, session):
    num = int(intent['slots']['number']['value'])
    cardTitle = "TABLE OF "+str(num)
    table = out = ""
    for i in range(1,10): 
        table += str(num)+" times "+str(i)+" equals <emphasis level=\"strong\">" + str(num*i) + "</emphasis> <break time=\"1s\"/>\n"
        out += str(num)+" times "+str(i)+" equals " + str(num*i) + "\n"
    table += str(num)+" times "+str(10)+" equals <emphasis level=\"strong\">" + str(num*10) + "</emphasis>\n"
    out += str(num)+" times "+str(10)+" equals " + str(num*10) + "\n"
    sessionAttributes = {"last" : table, "out" : out, "num" : num}
    speechOutput = table
    repromptText =  "Say repeat to repeat the table or stop to close or say table of some other number like 4"
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, out, repromptText, shouldEndSession))

def repeat(intent, session):
    num = session['attributes']['num']
    cardTitle = "TABLE OF "+str(num)
    speechOutput = session['attributes']['last']
    out = session['attributes']['out']
    sessionAttributes = {"last" : speechOutput, "out" : out, "num" : num}
    repromptText =  "Say repeat to repeat the table or stop to close or say table of some other number like 4"
    shouldEndSession = False
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, out, repromptText, shouldEndSession))
    
def handleSessionEndRequest():
    cardTitle = "Bye Bye"
    speechOutput = "Goodbye my friend. Have a nice day ahead! And I hope you won't forget the tables you learnt today."
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, txt, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>"+output+"</speak>"
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': txt
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
