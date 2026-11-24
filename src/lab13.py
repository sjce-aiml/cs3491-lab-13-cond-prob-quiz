"""Lab 13 starter code: conditional probability quiz application.

P(A | B) = P(A and B) / P(B)       Bayes: P(H | E) = P(E | H) P(H) / P(E)
"""
import random

def conditional_probability(joint, a, b):
    """joint: {(a_value, b_value): probability} over two boolean events A and B.
Return P(A=a | B=b)."""
    raise NotImplementedError('TODO: implement this')

def bayes_posterior(prior, sensitivity, false_positive_rate):
    """P(H | positive evidence) given P(H), P(E|H) and P(E|not H)."""
    raise NotImplementedError('TODO: implement this')
SCENARIOS = ['A disease affects {prior:.0%} of people. A test detects it {sens:.0%} of the time and gives a false positive {fpr:.0%} of the time. A person tests positive. What is P(disease | positive)?', "{prior:.0%} of emails are spam. The word 'offer' appears in {sens:.0%} of spam and {fpr:.0%} of normal emails. An email contains 'offer'. What is P(spam | 'offer')?", 'A machine is faulty {prior:.0%} of the time. The alarm rings {sens:.0%} of the time when faulty and {fpr:.0%} of the time when fine. The alarm rings. What is P(faulty | alarm)?']

def make_question(seed):
    """Return {'question', 'options' (4 strings), 'answer' (index), 'value' (float)}.
Exactly one option equals the correct posterior rounded to 3 decimals."""
    raise NotImplementedError('TODO: implement this')

def grade(question, choice):
    """Return True if `choice` (index) is the correct option."""
    raise NotImplementedError('TODO: implement this')

def run_quiz(n=5, seed=0, answers=None):
    """Run an n-question quiz. If `answers` (list of indices) is given, use them instead of input().
Return the score (number correct)."""
    raise NotImplementedError('TODO: implement this')
if __name__ == '__main__':
    run_quiz()
