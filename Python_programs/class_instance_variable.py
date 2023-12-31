# This code shows that an Instance can access it's own
# attributes as well as Class attributes.

# We have a class attribute named 'count', and we add 1 to
# it each time we create an instance. This can help count the
# number of instances at the time of instantiation.


class InstanceCounter:
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1


    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print("value of obj: {}".format(obj.get_val()))
    print("Count : {}".format(obj.get_count())) #3
    







