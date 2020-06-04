def another_filter(my_string, arg1, arg2):
    return f"{my_string}...{arg1}...{arg2}"


class FilterModule(object):
    def filters(self):
        return {"another_filter": another_filter}
