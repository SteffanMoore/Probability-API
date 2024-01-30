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
            
            closest_to_target_value = None
            temp_success_value = int(mean)
            value_to_find = math.exp(-mean) / probability

            # Increases the number of successes until both sides of the equation match
            while True:
                current_value = (math.factorial(temp_success_value) / (mean ** temp_success_value))
                value_difference = abs(value_to_find - current_value)

                if closest_to_target_value == None or closest_to_target_value > value_difference:
                    closest_to_target_value = value_difference
                elif closest_to_target_value <= value_difference:
                    break

                temp_success_value += 1

            # Due to symettry, the distribution has an upper and lower possible value
            closest_upper_success_number = (temp_success_value - 1)
            closest_lower_success_number = 2 * int(mean) - (temp_success_value - 1)

            # Number of successes has to be positive so the lower bracket can be discounted in some cases.
            if closest_lower_success_number < 0:
                success_number = [closest_upper_success_number]
            else:
                success_number = [closest_lower_success_number, closest_upper_success_number]

        case "probability":

            success_number = int(success_number)
            probability = ((mean ** success_number) * math.exp(-mean)) / math.factorial(success_number)

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