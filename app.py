import math
from inspect import signature, getfullargspec
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

def ensure_start_conditions(function):
    """
    Decorator function to ensure that there is no more and no less that one function argument which has no value.
    """

    def wrapper(*args, **kwargs):

        if len(args) > 0:
            print("Only keyword arguments should be handled by this function")
            return False
        
        min_args = len(signature(function).parameters) - 1

        if len(kwargs) < min_args:
            print(f"This function requires at least {min_args} arguments.")
            return False
        
        function(*args, **kwargs)

    return wrapper


@ensure_start_conditions
def poisson_probability(mean = None, success_number = None, failure_number = None, probability = None):
    
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
app = Flask(__name__)

api = Api(app)

class PoissonDistribution(Resource):

    def get(self):
        pass


if __name__ == "__main__":
    app.run(debug = False)

"""

poisson_probability(mean="five")