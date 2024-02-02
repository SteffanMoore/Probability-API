import math

def poisson_find_mean(success_number, probability):
    """
    Uses the Poisson distribution to estimate possible values of the mean given the number of successes and
    the probability of that success number. This returns a high and a low value as it isn't known which side of
    the mean the number of successes is.
    """

    try:
        step_size = 1
        target_value = probability * math.factorial(success_number)
        closest_target_distance = None
        temp_mean_value = success_number

        # Runs through mean values, decreasing step size when close until max resolution is reached
        while True:

            estimate = math.exp(-temp_mean_value) * (temp_mean_value ** success_number)
            estimate_to_target_distance = abs(estimate - target_value)

            # Either increases the mean value if getting closer to the value or changes step and tracks back
            if closest_target_distance == None or estimate_to_target_distance < closest_target_distance:
                closest_target_distance = estimate_to_target_distance
            elif step_size == 0.01:
                temp_mean_value -= step_size
                break
            else:
                temp_mean_value -= step_size
                step_size /= 10

            temp_mean_value += step_size

        # The mean could either be above or below the success no so there are two possible values
        higher_mean_value = temp_mean_value
        lower_mean_value = (2 * success_number) - temp_mean_value
        
        # Both values of the mean are only returned if they're both over zero
        if lower_mean_value < 0:
            mean = [higher_mean_value]
        else:
            mean = [higher_mean_value, lower_mean_value]

        return mean
    
    except OverflowError:
        return "Could not calculate due to overflow error"


def poisson_find_successes(mean, probability):
    """
    Uses the Poisson distribution to find an estimate of successful outcomes given the probablity and mean of the
    distribution. This can either return a single value or two values (depending on whether the mean is close to
    zero) as the distribution is symettrical.
    """

    try:
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
    
    except OverflowError:
        return "Could not calculate due to overflow error"


def poisson_find_probability(mean, success_number):
    """
    Uses the Poisson distribution to return the probability of there being a certain number of successes given
    a mean value.
    """

    try:
        probability = ((mean ** success_number) * math.exp(-mean)) / math.factorial(success_number)
    except OverflowError:
        return "Could not calculate due to overflow error"
        

    return probability
