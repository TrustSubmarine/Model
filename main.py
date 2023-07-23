import joblib

class Model:
    def __init__(self, dir):
        self.model = joblib.load(dir)

    def __call__(self, inputs):
        return self.model.predict(inputs)
    
    def predict(self, inputs):
        return self(inputs)
    

def get_predictions(event, context):
    event_body = event['body']
    inputs = event_body['inputs']

    predictions = Model('model.pkl')(inputs)

    return get_score(predictions)

def get_score(predictions):
    num_of_OR = len(list(filter(lambda x: x == 'OR', predictions)))
    num_of_elements = len(predictions)
    percentage_OR = num_of_OR / num_of_elements
    score = round(percentage_OR * 5, 1)
    return score