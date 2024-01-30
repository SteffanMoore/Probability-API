import math
import logging
from inspect import signature, getfullargspec
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from modules.poisson_distribution import poisson_find_successes, poisson_find_probability

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

def poisson_find_probability():
    pass

def poisson_find_mean():
    pass

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
            print("mean")

        case "success_number":

            success_number = poisson_find_successes(mean, probability)

        case "probability":

            success_number = int(success_number)
            probability = poisson_find_probability(mean, success_number)

    return {"mean": mean, "success_number": success_number, "probability": probability}
    """
    for argument in signature(poisson_probability).parameters:
        print(argument)

    print(signature(poisson_probability).parameters)

    for i in signature(poisson_probability).parameters:
        print(signature(poisson_probability).parameters[i].name)
        print(signature(poisson_probability).parameters[i].annotation)

    print(getfullargspec(poisson_probability))

    #print(signature(poisson_probability).parameters)
    #print(argument for argument in signature(poisson_probability).parameters.keys)
    """

"""
app = Flask(__name__)

api = Api(app)

class PoissonDistribution(Resource):

    def get(self):
        pass


if __name__ == "__main__":
    app.run(debug = False)

"""

print(poisson_probability(mean = 5.2, probability = 0.15))