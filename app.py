import logging
from inspect import signature
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from modules.poisson_distribution import poisson_find_mean, poisson_find_successes, poisson_find_probability

logging.basicConfig(level = logging.INFO)

def ensure_start_conditions(function):
    """
    Decorator function to ensure that there is no more and no less that one function argument which has no value.
    """

    def wrapper(**kwargs):

        arg_no = len(signature(function).parameters) - 1

        if len(kwargs) != arg_no:
            logging.info(f"This function requires {arg_no} arguments.")
            return False
        
        return function(**kwargs)

    return wrapper

@ensure_start_conditions
def poisson_probability(mean = None, success_number = None, probability = None):
    """
    Uses three of its arguments to find the value for the other according to the Poisson distribution and returns
    them all as a dictionary. Mean is the number of expected successes, success_number is the actual number of
    successes and probability is the likelyhood of there being that many successes given the expected number. This
    is used for a discrete data set so doesn't work on continuous data.
    """
    
    arguments = {"mean": mean, "success_number": success_number, "probability": probability}
    
    # Finds the argument left as default and checks that the correct data types are used.
    for arg in arguments:

        if arguments[arg] == None:
            missing_arg = arg

        elif not isinstance(arguments[arg], (int, float)):
            logging.info(f"""Provided argument - "{arguments[arg]}" for {arg} is not the correct data type. It """
                         f"""is currently a {type(arguments[arg])}.""")
            return False

    # Function changes depending on which argument is missing.
    match missing_arg:

        case "mean":
            success_number = int(success_number)
            mean = poisson_find_mean(success_number, probability)
            
        case "success_number":
            success_number = poisson_find_successes(mean, probability)

        case "probability":
            success_number = int(success_number)
            probability = poisson_find_probability(mean, success_number)

    return {"mean": mean, "success_number": success_number, "probability": probability}



app = Flask(__name__)

api = Api(app)

class PoissonDistribution(Resource):

    def get(self, mean, successes, probability):

        arguments = signature(PoissonDistribution.get).parameters
        for arg in arguments:
            arg_name = arguments[arg].name

            if arg_name in locals() and arg_name != "self":
                print(f"{arg_name} - {locals()[arg_name]}")
                value = locals()[arg_name]

                if value == "None":
                    continue

                match arg_name:
                    
                    case "mean":
                        mean = float(mean)
                    
                    case "probability":
                        probability = float(probability)

                    case "successes":
                        successes = int(successes)
                
                

api.add_resource(PoissonDistribution, '/Poisson/mean=<string:mean>/successes=<string:successes>/probability=<string:probability>')

if __name__ == "__main__":
    app.run(debug = False)
