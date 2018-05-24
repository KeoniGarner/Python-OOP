import random
class Call(object):
    def __init__(self, unique_id=None, caller_name=None, caller_number=None, time_of_call=None, reason_for_call=None):
        self.id = unique_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    
    def display(self):
        print ("ID: {}".format(self.id))
        print ("Name: {}".format(self.caller_name))
        print ("Number: {}".format(self.caller_number))
        print ("Time: {}".format(self.time_of_call))
        print ("Reason: {}".format(self.reason_for_call))

class CallCenter(object):
    def __init__(self,calls = []):
        self.calls = calls
        self.size = len(calls)

    def add(self, call):
        self.calls.append(call)
        self.size += 1
        return self

    def remove(self):
        self.calls.remove(self.calls[0])
        self.size -= 1
        return self
    
    def info(self):
        for entry in self.calls:
            print ("Name: {}".format(entry.caller_name))
            print ("Number: {}".format(entry.caller_number))
            print ("----------------")
        print ("Queue Length: {}".format(self.size))
        return self

    def remove_call(self, number):
        for entry in self.calls:
            if entry.caller_number == number:
                self.calls.remove(entry)
        return self

    def sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for index in range(0, len(self.calls)-1):
                if self.calls[index].time_of_call > self.calls[index+1].time_of_call:
                    temp = self.calls[index]
                    self.calls[index] = self.calls[index+1]
                    self.calls[index+1] = temp
                    is_sorted = False
        return self

call_list = []
for num in range(0,10):
    call_list.append(Call(num, "Caller Number {}".format(num), random.randint(1000000000, 10000000000), random.randint(0, 25), "Testing"))

call_center = CallCenter(call_list)
add_call = Call(10, "Caller Number 11", 6618588470, 0, "Adding a Call")
call_center.info().remove().info().add(add_call).info().remove_call(add_call.caller_number).info().sort().info()
