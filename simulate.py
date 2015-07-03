
import numpy as np

# Use case: from a daily measure of something you need to know the future, lets say in 10 days.
# Get a vector of change per day, so every day calculate the change it had from previous day
# assuming the future will be like that past, sum up 10 days of sampling randomly from the change per day history 
# run that 10k times to make sure is stable and do an average.

# whats the value in X iterations, given the history of diferences?
def iterations_ahead (current, iterations, delta_ar):
    def sample_add (current, iterations, delta_ar):
        for i in range(iterations):
            current = current + float(np.random.choice(delta_ar))
        return current

    current = [sample_add(current, iterations, delta_ar) for i in range(10000)]
    return np.mean(current)
# print iterations_ahead(5, 1, ['1', '2', '3'])
# pd.DataFrame(value).hist()



# Use case: from a daily measure of something you need to know in how many days you will reach a desired value.
# Get a vector of change per day, and keep summing up random samples from that vector until reaching desired value.
# number of times needed to get there, is the number of days needed
# might never get there, so timeout after trying for 1.5 years worth of days (548) 
# Run that 10k times to make sure is stable and do an average.

# Simulate how many iterations needed to reach value
def iterations_to_value (current, target, delta_ar):
    def iter (current, target, delta_ar):
        iter = 0
        max = np.max([current, target])
        min = np.min([current, target])
        descending = (max == current)
        while max > min:
            if (descending):
                max = max + float(np.random.choice(delta_ar))
            else: # ascending
                min = min + float(np.random.choice(delta_ar))
            iter = iter + 1
            if (iter >= 548): # about 1.5 years worth of days
                return 0  # if value too crazy just interrupt the loop
        return(iter)

    value = [iter(current, target, delta_ar) for i in range(3000)]
    return np.mean(value)

# How it should work
def test_iterations_to_value():
    iterations_to_value(70, 80, [-0.2]) == 0.0 # never
    iterations_to_value(70, 80, [+0.2]) == 50
    iterations_to_value(80, 70, [+0.2]) == 0.0 # never
    iterations_to_value(80, 70, [-0.2]) == 50

if __name__ == "__main__":
    # run tests
    from subprocess import call
    call(["nosetests", "--verbose", __file__])
