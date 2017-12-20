import os
print(list(filter(lambda x: x and x[0] != '.', os.listdir(os.getcwd()))))