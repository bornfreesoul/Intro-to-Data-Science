import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def update_thetas(features, values, theta, alpha):

    """

    :rtype numpy array
    """
    difference = values - numpy.dot(features, theta)
    # print "differences", difference
    new_thetas = theta + (alpha/len(values)) * numpy.dot(difference.T, features)
    return new_thetas

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it
    # to cost_history.
    # See the Instructor notes for hints.

    cost_history = [compute_cost(features, values, theta)]
    thetas = [[theta]]
    # print cost_history
    # print theta
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    i = 1
    thetas_prev = theta
    while i <= num_iterations:

        new_thetas = update_thetas(features, values, thetas_prev, alpha)
        thetas_prev = new_thetas
        # print "new_thetas", new_thetas
        thetas.append(new_thetas)
        cost_history.append(compute_cost(features, values, new_thetas))
        i += 1

    theta = thetas[cost_history.index(min(cost_history))]
    return theta, pandas.Series(cost_history) # leave this line for the grader
