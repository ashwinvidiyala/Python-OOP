class Call(object):
    def __init__(self, id, name, phone_number, time_of_call, reason_for_call):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display(self):
        print "ID:", self.id
        print "Name:", self.name
        print "Phone Number:", self.phone_number
        print "Time of call (in HHMM format):", self.time_of_call
        print "Reason for call:", self.reason_for_call

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    # def add(self, id, name, phone_number, time_of_call, reason_for_call):
    #     self.calls.append(Call(id, name, phone_number, time_of_call, reason_for_call))

    def add(self, call):
        self.calls.append(call)

    def remove(self):
        self.calls.pop(0)

    def info(self):
        print 'Length of queue:', self.queue_size
        # for value in self.calls:
        #     print "Name:", value.name
        #     print "Phone Number:", value.phone_number

call1 = Call(1, 'Ash', 123, 1234, 'thanks')
# call1.display()
call_center = CallCenter()
call_center.add(call1)
call_center.info
# print call_center.calls
# print call_center.queue_size
