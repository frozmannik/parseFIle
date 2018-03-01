import os

file_name = 'a_example.in'  # name of file
file_path = os.path.abspath(os.path.join('data',file_name))

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

ride = {}
with open(file_path, 'r') as f:
    lines = f.readlines()
    rows, columns, vehicles, rides, bonus, steps = lines[0].split()
    start = Point(0, 0)
    finish = Point(0, 0)
    for i in xrange(1, len(lines)):
        line = lines[i].split()
        start = line[0], line[1]
        finish = line[2], line[3]
        early_start = line[4]
        latest_finish = line[5]
        ride[str(i)] = {'start': start, 'finish': finish, 'early_start': early_start, 'latest_finish': latest_finish}

#print ride['1']
assign = []



def find_closest():
    for coord in ride:
        #print ride[coord]['start'][0]
        distance = abs(car.x - int(ride[coord]['start'][0])) + abs(car.y - int(ride[coord]['start'][1]))

        print distance

class car:
    x = 0
    y = 0
    count = 0
    def step(self):
        if self.count == 0:
            find_closest()
            #assign new final
            print 'will be soon'
        else:
            self.x = self.x -1
            self.y = self.y -1


find_closest()