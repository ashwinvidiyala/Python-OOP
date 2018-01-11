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
        self.queue_size = 0

    # def add(self, id, name, phone_number, time_of_call, reason_for_call):
    #     self.calls.append(Call(id, name, phone_number, time_of_call, reason_for_call))

    def add(self, call):
        call_list = []
        call_list.append(call.id)
        call_list.append(call.name)
        call_list.append(call.phone_number)
        call_list.append(call.time_of_call)
        call_list.append(call.reason_for_call)

        self.calls.append(call_list)

        self.queue_size += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def info(self):
        print 'Length of queue:', self.queue_size
        for value in self.calls:
            print "Name:", value[1]
            print "Phone Number:", value[2]

call1 = Call(1, 'Ash', 123, 1234, 'thanks')
# call1.display()
call_center = CallCenter()
call_center.add(call1)
call_center.info()
# print call_center.calls
