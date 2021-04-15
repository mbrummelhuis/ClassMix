"""
This file was added by Martijn Brummelhuis as part of the reproducibility project of the CS4240 - Deep Learning course at TU Delft, faculty EEMCS
It automatically performs hyperparameter analysis of the network by changing the configSSL.json file, training and gathering results. This script is supposed
to be run from the terminal in a (virtual) environment with all requirements met.
"""
import os
import json
import subprocess
import tempfile
import time
from pathlib import Path

Run = "python3 trainSSL.py --config ./configs/configSSL.json --name SSL"
pth = str(Path(__file__).parent.absolute()) + "/configs/configSSL.json"

learningRates = [1.5e-4, 2.0e-4, 2.5e-4, 3.0e-4, 3.5e-4]
iterations = [10000, 20000, 30000, 40000] 

print("Starting loop")
for iteration_size in iterations:
    iteration_size = 40000
    print("NEW ITERATION SIZE ITERATION")
    json_file = open(pth,"r+")
    config = json.load(json_file)
    json_file.close()

    config["training"]["num_iterations"] = iteration_size

    json_file = open(pth,"w")
    json.dump(config, json_file)
    json_file.close()
    time.sleep(10)

    for learningRate in learningRates:
        print("NEW LEARNING RATE ITERATION")
        # Change learning rate in config file
        json_file = open(pth,"r+")
        config = json.load(json_file)
        json_file.close()

        config["training"]["learning_rate"] = learningRate
        print(config)

        json_file = open(pth,"w")
        json.dump(config, json_file)
        json_file.close()
        time.sleep(10)

        os.system(Run) #Runs the code
        # Results are automatically saved by original code

