def most_covered(bdm):
    """bdm is a birthday months calendar with at least one key in it. Return
    the name of the month (a str) that is most "covered" in the dictionary.
    i.e., the month with the most days on which someone has a birthday. If
    there is a tie, return any month with that maximum coverage.
    """
    # {"February": {13: ["Catherine"]},
    #   "May": {3: ["Katie"], 8: ["Peter", "Ed", "Ali"]},
    #   "August": {20: ["Katie"], 15: ["Alex", "David", "Veli", "Maria", "Sebastian"]},
    #   "December": {1: ["Atalay Samet Ergen"]}}

    max_people = -1
    max_month = ''
    for month in bdm:
        count_people = 0
        for day in bdm[month]:
            count_people += len(bdm[month][day])
        if count_people > max_people:
            max_people = count_people
            max_month = month  # August

    return max_month


bdm = {"February": {13: ["Catherine"]},
       "May": {3: ["Katie"], 8: ["Peter", "Ed", "Ali"]},
       "August": {20: ["Katie"], 15: ["Alex", "David", "Veli", "Maria", "Sebastian"]},
       "December": {1: ["Atalay Samet Ergen"]}}

print(most_covered(bdm))
