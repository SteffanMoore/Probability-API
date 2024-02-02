# Probability-API
## Intro
Having used APIs in a few previous projects, I thought it was about time that I had a crack at making one! I saw that there was a Flask add-on which promised a familiar approach to getting an API up and running quickly (excellent for me as I use Flask fairly regularly). So I got my venv set up with the neccesary packages and hit the usual conundrum of what to actually make - this time I opted for the boring route and decided that I would make an API to return probability values given specific inputs (I've decided just to stick to the Poisson distribution for the time being but might come back and add a couple of others if the mood takes me).

## Functionality
The Poisson distribution is used for discrete data and requires the expected value (mean) and actual number of successes to find a probability. However I didn't want the API to only be able to calculate probabilities. I wanted it to be able to return the mean given the probability and success number as well as return the success number given the probability and mean. The problem with this is that the equation for finding the probability is very nice and straightforward:

$$ P = {{\lambda}^k e^{-\lambda}} / k! $$

The equations for finding the mean and success number however aren't as nice and clean making life a little more difficult. This was easy enough to solve through isolating the unknown parameter to one side of the equation and slowly incrementing estimate values until within a certain accuracy but still added some complexity.

This at least gave me an opportunity to fiddle around with decorators to check the number of arguments used in the function (although this ended up being semi-redundant by the end as I hadn't considered that by using optional arguments in the function, I would either always have to supply three arguments, causing the decorator function to reject it, or use a match statement which got rid of the point of checking the number of arguments used).

In the end, the API now returns results in JSON format when one of the input arguments is missing. To query the API, the format is as follows:

http://whereveritishosted/Poisson/mean=5/successes=4/probability=None

This example would calculate a probability. The "None" should be placed in whichever argument the user would like the API to calculate. If the API can't calculate the answer due to an overflow error, it will return an error string in the JSON response but if the arguments are incorrectly entered (incorrect number of arguments or non-numerical arguments supplied) it will return a response with an error code 400.

