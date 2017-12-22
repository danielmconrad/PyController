import time
from invoke import task
from PyController import Dualshock4


@task
def tank(ctx):
    controller = Dualshock4.Dualshock4()

    previous = None

    for data_list in controller.yield_input():
        data_array = []

        for item in data_list:
            data_array.append(item)

        differences = []

        if previous != None:
            for i, val in enumerate(data_list):
                if previous[i] != data_array[i]:
                    differences.append(tuple((i, previous[i], data_array[i])))

        print(differences)

        previous = data_array
        time.sleep(1)
