from ipaddress import summarize_address_range


def getMean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = { "Mary": 9.5, "Bob": 4.5, "John": 7.8, "K Dawg": 2.3}
print(getMean(student_grades))