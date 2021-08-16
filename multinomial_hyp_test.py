import pandas as pd
import numpy as np
import scipy.stats as stats
import random

def get_frequencies(n_reps, p):
    '''make some dummy null data
       this data will really be the outcome proportion/class
       from experiments with the previous reco'''
    temp = stats.multinomial(n=10, p=p).rvs(n_reps)
    df = pd.DataFrame(temp).T
    df['proportion'] =temp.sum(axis=0)/temp.sum()
    return df.iloc[:,-1]

def get_observations(n_reps, p):
    '''make some dummy alt data
       this data will really be the outcomes
       from the L&S reco'''
    temp = stats.multinomial(n=10, p=p).rvs(n_reps)
    df = pd.DataFrame(temp).T
    df['observed'] =temp.sum(axis=0)
    return df.iloc[:,-1]

def get_expected_frequencies(data, p_null):
    '''new obsrvations as proportions based on null proportions
       data: array of k observations
       p_null: k null frequencies'''
    return np.sum(data)*p_null

def get_sqd_deviations(observed, expected):
    '''just for checking that results with stats fn are equal'''
    return (observed-expected)**2 

def results(observed, expected, alpha=0.05):
    '''test is just some evidence to add to evalution
       beware the hypothesis test :) '''
    t, p = stats.chisquare(observed, expected)
    if p <+ alpha:
        return f'At a significance level of {alpha},'\
    ' there IS statistical evidence that the observations'\
    ' are from a different distribution. pval:{p:2.4f}'
    else:
        return f'At a significance level of {alpha},'\
    ' there IS NOT statistical evidence that the observations'\
    ' are from a different distribution. pval:{p:2.4f}'

if __name__=="__main__":
    # GET SOME SIMULATED DATA FOR 
    # pk = class k probabilities
    # in real data the proportions for the test stat
    # will come from the previous recommender results

    # random seeds
    # number of trials (recommendations)
    n = 10
    # number of classes (categories)
    k = 20
    # random probability of being in each class
    random_probs = stats.uniform().rvs(k, random_state=1111)
    norm_denom = np.sum(random_probs)
    pks_jordan = random_probs/norm_denom

    random_probs = stats.uniform().rvs(k, random_state=42)
    norm_denom = np.sum(random_probs)
    pks_martha = random_probs/norm_denom

    # set "true" frequencies per class
    jordan = get_frequencies(1000, pks_jordan)

    # get observations from null distribution
    martha = get_observations(30, pks_jordan)

    # calculate expected frequencies
    exp_martha = get_expected_frequencies(martha, jordan)

    # multinomial hypothesis test
    # H_o: observed freq have the same distribution as null 
    # H_a: observed freq have a statistically difference distribution
    print(results(martha, exp_martha))

    #________________________________________________________________
    # get observations from DIFFERENT distribution
    martha = get_observations(30, pks_martha)

    # calculate expected frequencies
    exp_martha = get_expected_frequencies(martha, jordan)

    # multinomial hypothesis test
    # H_o: observed freq have the same distribution as null 
    # H_a: observed freq have a statistically difference distribution
    print(results(martha, exp_martha))