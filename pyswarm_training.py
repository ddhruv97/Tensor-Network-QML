import numpy as np
import math
from pyswarm import pso
import utils
import model_refactored as model


def train():
    """
    """

    # Set hyperparameters:
    num_epochs = 20
    swarm_size = 10
    batch_size = 10
    lam = .33
    eta = 1.0


    train_data, train_labels, test_data, test_labels = utils.load_data(BLACK_AND_WHITE=True)
    n = len(train_data[0])
    # print("n: %d" % n)

    #Save parameters
    mod = model.Model(n=n, num_trials=100)
    params = list(2*math.pi*np.random.rand(mod.count))
    dim = len(params)
    print("Number of parameters in circuit: %d " % dim)

    bounds = (np.zeros(dim), 2*math.pi*np.ones(dim))

    xopt, fopt = pso(mod.get_loss, bounds[0], bounds[1], args=(train_data, train_labels, lam, eta, batch_size), swarmsize=swarm_size, maxiter=num_epochs)
    print(xopt, fopt)
    params = xopt
    np.savetxt("params/pyswarm_params_bw_v0.csv", params, delimiter = ",")
    num_correct = 0
    for i in range(len(test_data)):
        dist =  mod.get_distribution(params, test_data[i])
        if dist[math.floor(test_labels[i])] > 0.5:
            num_correct += 1
    print("test accuracy = ", num_correct/len(test_data))
    print("number of circuit runs = ", mod.num_runs)
if __name__ == '__main__':
    train()
