from .root import app

@app.handle(intent='greet')
def welcome(request, responder):
    """
    When the user starts a conversation, say hi and give some wellness center suggestions to explore.
    """
    try:
        # Get user's name from session information in a request to personalize the greeting.
        responder.slots['name'] = request.context['name']
        prefix = 'Hello, {name}. '
    except KeyError:
        prefix = 'Hello. '

    places = app.question_answerer.get(index='wellness')
    suggestions = ', '.join([r['name'] for r in places[0:3]])

    # Build up the final natural language response and reply to the user.
    responder.reply(prefix + 'Some nearby that may intrest you '
                    + suggestions)

@app.handle(intent='exit')
def say_goodbye(request, responder):
    responder.reply(['Bye', 'Goodbye', 'Have a nice day.','peace out'])