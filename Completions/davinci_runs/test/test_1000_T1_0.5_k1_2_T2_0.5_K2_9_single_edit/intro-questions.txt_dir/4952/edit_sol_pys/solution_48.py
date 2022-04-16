#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:53:44 2019

@author: hannaholdorf
"""

import sys
import collections 


def main():
    """
    Main function that prints the winner of the voting election.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    # read in votes
    votes = [line.strip() for line in sys.stdin]
    
    # count votes
    # find most common vote
    
    # check if there is a runoff

    votes = collections.Counter(votes)
    max_votes = votes.most_common(1)[0][1]
    if votes.most_common(2)[0][1] == votes.most_common(2)[1][1]:
    # print the winner
        print('Runoff!')
        return
    else:
        for name, num in votes.most_common():
            if num == max_votes:
                print(name)
                return

if __name__ == '__main__':
    main()
