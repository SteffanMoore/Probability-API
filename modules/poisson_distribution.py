import math

def poisson_find_mean():
    pass


def poisson_find_successes(mean, probability):
    """
    Uses the Poisson distribution to find an estimate of successful outcomes given the probablity and mean of the
    distribution. This can either return a single value or two values (depending on whether the mean is close to
    zero) as the distribution is symettrical.
    """

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

    return success_number


def poisson_find_probability(mean, success_number):
    """
    Uses the Poisson distribution to return the probability of there being a certain number of successes given
    a mean value.
    """

    probability = ((mean ** success_number) * math.exp(-mean)) / math.factorial(success_number)

    return probability