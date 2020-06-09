def filter1(my_str):
    return my_str.upper()


def filter2(my_str):
    return my_str.lower()


def filter3(my_str):
    return my_str.capitalize()


class FilterModule(object):
    def filters(self):
        return {
            "filter1": filter1,
            "filter2": filter2,
            "filter3": filter3,
        }
