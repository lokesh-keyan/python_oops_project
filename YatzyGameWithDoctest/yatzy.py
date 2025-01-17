def small_straight(dice):
    """Score the given roll in the 'Small Straight' Yatzy category.
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([2,2,3,4,5])
    0
    >>> small_straight([1,2,3,4,6])
    0

    It should handle unsorted dice and duplicates
    >>> small_straight([5,4,3,2,1])
    15
    """
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    return 0

#for unique values that generate randomly, we can use elipsis that is use thre dots ...