# Multinomial-hypothesis-test

### GOAL: Compare recommender results to confirm consistent results

I can't stop thinking about how you could do this well. Good hard question!

## The Idea

**IF** we assume that the category distribution in a 10-set of recommendations contains information about the behavior of the recommender, then this may be helpful.

Translate problem in to multinomial distribution:

If, 

* Let n = the number of recommendations (trials)

* Let k = the number of categories (classes)

* Let (p_1, ..., p_k) be the probabilities of being in the 1-kth category

* Let (y_1, ..., y_k) be the number of outcomes that ended up in the 1-kth category

Then, y_i ~ Multinomial(n, **p**)

So, we can do a multinomial hypothesis test, using frequencies for each category over X(30+) experiements (so, X 10-set reco results for a given customer). 

> H_o: There is no difference between the distribution of the original recommender category frequency distribution and the new recommender category frequency distribution.

> H_a: There is a difference.

## How to Use the Idea

Ideally, you would grab a small subset of M customers so you could do a bunch of experiments quickly.

For each of the M customers, 

1. Collect the null frequency data

    From the previous reco, for customer m_i, keeping as much constant as possible (date, input history, idk what else), get customer m_i's 10 recommendations as many times (n_reps) as you reasonably can. Record the proportions of recommendations for each category over all n_reps. These are the **null frequencies**.
    
    THOUGHTS:
    - if you the same customer gets the exact same reco every time, then no randomness, and easy to tell the L&S is different.
    - if the frequencies never settle down, then we can't really test that the new observations are different.

2. Collect the new frequency data

    a. From the new reco, for customer m_i, keeping as much constant as possible (date, input history, idk what else), get customer m_i's 10 recommendations 30+ times. Record the COUNTS of recommendations for each category over all n_reps. These are the **observations**.

    b. Multiply the **null frequency** by the new COUNTS to get the **expected observations**.

3. Run and interpret the chi-square test:

    test-stat, pval = stats.chisquare(**observed**, **expected**)


*multinomial_hyp_test.py* has a dummy data version with functions you can use.

<br> 

### WARNING: this may be completely useless when we see the actual data. Just the first idea...