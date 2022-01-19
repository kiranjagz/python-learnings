from ipaddress import summarize_address_range


def getMean(myList):
    the_mean = sum(myList) / len(myList)
    return the_mean

result = getMean([10,10,50])
print(result)