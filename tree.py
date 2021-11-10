# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:25:14 2021

@author: Joyce
"""

def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)



def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left,right])
    
def count_leaf(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum(count_leaf(i) for i in branches(tree))
    
    
    
def increment_leaves(t):
    """Return a tree like t but with leaf labels inremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


def print_tree(t, indent = 0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)





def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def fact_times(n ,k):
    """Return k * n * (n-1) * ...* 1"""
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)

def fact_new(n):
    return fact_times(n, 1)



def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for branch in branches(t):
            print_sums(branch, so_far)
            

        