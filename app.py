import math
import logging
from inspect import signature, getfullargspec
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

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
            print("mean")

        case "success_number":
            print("success_number")

        case "probability":
            probability = ((mean ** success_number) * math.exp(-mean)) / math.factorial(success_number)
            print("probability")


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

print(poisson_probability(mean = "five", success_number = "less"))