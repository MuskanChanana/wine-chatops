from rasa_core.actions import Action
import pandas as pd
from rasa_core.events import Restarted


df = pd.read_csv('winemag-data_first150k.csv', index_col=0)

def db_specific(store):
    quantity = int(store['quantity'])
    result = []
    if store['field'] == 'price':
        print("here2")
        if store['quantifier'] == 'gt':
            result = df[df['price'] > quantity].iloc[:5]
        elif store['quantifier'] == 'lt':
            result = df[df['price'] < quantity].iloc[:5]
        elif store['quantifier'] == 'lte':
            result = df[df['price'] <= quantity].iloc[:5]
        elif store['quantifier'] == 'gte':
            result = df[df['price'] >= quantity].iloc[:5]
        elif store['quantifier'] == 'eq':
            result = df[df['price'] == quantity].iloc[:5]
    elif store['field'] == 'score':
        if store['quantifier'] == 'gt':
            result = df[df['points'] > quantity].iloc[:5]
        elif store['quantifier'] == 'lt':
            result = df[df['points'] < quantity].iloc[:5]
        elif store['quantifier'] == 'lte':
            result = df[df['points'] <= quantity].iloc[:5]
        elif store['quantifier'] == 'gte':
            result = df[df['points'] >= quantity].iloc[:5]
        elif store['quantifier'] == 'eq':
            result = df[df['points'] == quantity].iloc[:5]
    if len(result) == 0:
        return False
    else:
        return result.sample(len(result))


def dbq(kwargs):
    if kwargs['quantity'] == None:
        quantity = 5
    else:
        quantity = int(kwargs['quantity'])
    # base branch
    if not kwargs['howmuch']:
        if not kwargs['country']:
            result = df[df['points'] >= 94].iloc[:quantity]
            if kwargs['quality'] == 'worst':
                result = df[(df['points'] <= 88) & (df['points'] <= 88)].iloc[:quantity]
        # quality country branch
        else:
            result = df[(df['points'] >= 94) & (df['country'] == kwargs['country'])].iloc[:quantity]
            if kwargs['quality'] == 'worst':
                result = df[(df['points'] >= 80) & (df['points'] <= 88) & (df['country'] ==
                                                                           kwargs['country'])].iloc[:quantity]
    # price branch
    else:
        # most price branch
        if kwargs['howmuch'] == 'most':
            if not kwargs['country']:
                result = df[df['price'] > 300].iloc[:quantity]
                if kwargs['quality'] == 'worst':
                    result = df[(df['points'] >= 80) & (df['points'] <= 88) & (df['price'] > 300)].iloc[:quantity]
                elif kwargs['quality'] == 'best':
                    result = df[(df['points'] >= 94) & (df['price'] > 300)].iloc[:quantity]
            else:
                result = df[(df['price'] > 300) & (df['country'] == kwargs['country'])].iloc[:quantity]
                if kwargs['quality'] == 'worst':
                    result = df[(df['points'] >= 80) & (df['points'] <= 88) &
                                (df['country'] == kwargs['country'])].iloc[:quantity]
                elif kwargs['quality'] == 'best':
                    result = df[(df['points'] >= 94) & (df['price'] > 300) & (df['country'] == kwargs['country'])].iloc[
                             :quantity]

        else:
            if 'country' not in kwargs:
                if 'quality' not in kwargs:
                    result = df[df['price'] < 150].iloc[:quantity]
                else:
                    if kwargs['quality'] == 'worst':
                        result = df[(df['points'] >= 80) & (df['points'] <= 88)
                                    & (df['price'] < 150)].iloc[:quantity]
                    else:
                        result = df[(df['points'] >= 94) & (df['price'] < 150)].iloc[:quantity]
            else:
                if 'quality' in kwargs:
                    if kwargs['quality'] == 'worst':
                        result = df[(df['points'] >= 80) & (df['points'] <= 88) &
                                    (df['country'] == kwargs['country'])].iloc[:quantity]
                    else:
                        result = df[(df['points'] >= 94) & (df['price'] > 150)].iloc[:quantity]
                else:
                    result = df[(df['points'] >= 80) & (df['points'] <= 88) & (df['price'] < 150) & (df['country'] ==
                                                                                     kwargs['country'])].iloc[:quantity]
    if len(result) == 0:
        return False
    else:
        return result.sample(len(result))


def make_message(answer):
    template_list = list()
    template = """<br>
    variety: {variety}<br>
    winery: {winery}<br>
    points: {points}<br>
    price: $ {price}<br>
    country: {country}<br>
    designation: {designation}<br>
    description: {description}<br>
    """
    for i in range(len(answer)):
        temp = template
        zen = answer.iloc[[i, ]]
        for key in zen.to_dict().keys():
            temp = temp.replace('{' + key + '}', str(zen[key].item()))
        template_list.append(temp)

    return template_list


class ActionGeneralQuery(Action):

    def name(self):
        return "action_general_query"

    def run(self, dispatcher, tracker, domain):
        print("action general")
        current_store = tracker.current_slot_values()
        print(current_store)
        if current_store['country'] is not None:
            current_store['country'] = current_store['country'][0].upper() + current_store['country'][1:]
        answer = dbq(current_store)
        if answer is False:
            dispatcher.utter_message("Sorry couldn't find anything relevant :(")
            return []
            # return [SlotSet("country", None), SlotSet("quantity", None), SlotSet("quality", None),
            #         SlotSet("howmuch", None)]
        dispatcher.utter_message("Here's what i found: ")
        for st in make_message(answer):
            dispatcher.utter_message(st)
        dispatcher.utter_message(answer)

        return []
        # return [SlotSet("country", None), SlotSet("quantity", None), SlotSet("quality", None),
        #         SlotSet("howmuch", None)]


class ActionSpecificQuery(Action):

    def name(self):
        return "action_specific_query"

    def run(self, dispatcher, tracker, domain):
        print("Action Specific")
        current_store = tracker.current_slot_values()
        print(current_store)
        if current_store['country'] is not None:
            current_store['country'] = current_store['country'][0].upper() + current_store['country'][1:]
        answer = db_specific(current_store)
        if answer is False:
            dispatcher.utter_message("Sorry couldn't find anything relevant :(")
            return []
        dispatcher.utter_message("Here's what i found: ")
        for st in make_message(answer):
            dispatcher.utter_message(st)
        dispatcher.utter_message(answer)
        return []
        # return [SlotSet("country", None), SlotSet("quantity", None), SlotSet("quality", None),
        #         SlotSet("howmuch", None), SlotSet("quantifier", None), SlotSet("field", None)]

class ActionRestartedQuery(Action):
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return[Restarted()]





