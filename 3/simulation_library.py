def run_simulation():
    parameters = read_parameters()
    import time; time.sleep(1) # takes a while to compute!
    return int(parameters) * 5


def read_parameters():
    with open("parameters.txt", "r") as parameterFile:
        return parameterFile.read()
