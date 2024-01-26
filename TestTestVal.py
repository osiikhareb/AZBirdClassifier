# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:59:47 2024

@author: Osi
"""

import os
import math
import shutil
import random
import numpy as np
import pandas as pd



speciesCode_list ='A:/Documents/Python Scripts/BirdBot2.0/Scraper/_output/species_info_111.csv'
speciesCodelist = pd.read_csv(speciesCode_list)
speciesCodelist = speciesCodelist['speciesCode']
speciesCodelist = speciesCodelist[68:111]

# Create new folders to move preprocessed images
#def TrainTestFolder():
for x in ('train', 'validation', 'test'):
    folder_name = x
    path = 'A:\Documents\Python Scripts\BirdBot2.0\Training\_images'
    os.chdir(path)
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
        
    for y in speciesCodelist:
        folder_name = y
        path = f'A:\Documents\Python Scripts\BirdBot2.0\Training\_images\{x}'
        os.chdir(path)
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)

#def EmptyFolderCheck():
empty_folder = []
for z in speciesCodelist:
    folder = f'A:\Documents\Python Scripts\BirdBot2.0\Preprocessing\_images\{z}'#current working dir of preprocessed images
    file_count = sum(len(files) for _, _, files in os.walk(folder)) #no. of files in dir
    print(f'There are no images in the {z} preprocessing folder')
    empty_folder.append(z)
# If no images in the preprocessing folder, we can either skip that speciesCode in the next loop or pop out of the list


# Randomly move preprocessed images to train, validation, and Test folders
#def TrainTestSplit():
for n in speciesCodelist:
    folder = f'A:\Documents\Python Scripts\BirdBot2.0\Preprocessing\_images\{n}'#current working dir of preprocessed images
    file_count = sum(len(files) for _, _, files in os.walk(folder)) #no. of files in dir
    dest = f'A:\Documents\Python Scripts\BirdBot2.0\Training\_images\{n}'
    
    try:
        
        if file_count % 2 > 0:
            train_count = round(file_count*.4)
            validation_count = round(file_count*.2)
            test_count = round(file_count*.4)
            
        
        elif file_count % 2 == 0:
            train_count = round(file_count*.4)
            validation_count = round(file_count*.2)
            test_count = round(file_count*.4)
            
        elif file_count == 0:
            print('The folder corresponding to {n} is empty')
            continue
    
        else:
            pass
    
    except IndexError:
        print('The folder corresponding to {n} is empty') #IndexError: Cannot choose from an empty sequence
        continue
    
    except Exception as e:
        print(e)
        #Error: Destination path 'A:\Documents\Python Scripts\BirdBot2.0\Training\_images\train\{n}\{n}_#_pad.jpg' already exists
        continue
    
    if file_count != train_count + validation_count + test_count:
        train_count = round(file_count*.4) + 1
        validation_count = round(file_count*.2)
        test_count = round(file_count*.4)
    

    
    
    #random shuffle and move to new dir        
    for i in range(1, train_count + 1):
        try:
            #Variable random_file stores the name of the random file chosen
            m = 'train'
            random_file = random.choice(os.listdir(folder))
            source_file = f'{folder}\{random_file}'
            dest = f'A:\Documents\Python Scripts\BirdBot2.0\Training\_images\{m}\{n}'
            dest_file = dest
            #"shutil.move" function moves file from one directory to another
            shutil.move(source_file, dest_file)
        except IndexError:
            print(f'The folder corresponding to {n} is empty') #IndexError: Cannot choose from an empty sequence
            break
    
    for j in range(1, validation_count + 1):
        try:           
            #Variable random_file stores the name of the random file chosen
            m = 'validation'
            random_file = random.choice(os.listdir(folder))
            source_file = f'{folder}\{random_file}'
            dest = f'A:\Documents\Python Scripts\BirdBot2.0\Training\_images\{m}\{n}'
            dest_file = dest
            #"shutil.move" function moves file from one directory to another
            shutil.move(source_file, dest_file)
        except IndexError:
            print(f'The folder corresponding to {n} is empty') #IndexError: Cannot choose from an empty sequence
            break
            
            
    for k in range(1, test_count + 1):
        try:
            #Variable random_file stores the name of the random file chosen
            m = 'test'
            random_file = random.choice(os.listdir(folder))
            source_file = f'{folder}\{random_file}'
            dest = f'A:\Documents\Python Scripts\BirdBot2.0\Training\_images\{m}\{n}'
            dest_file = dest
            #"shutil.move" function moves file from one directory to another
            shutil.move(source_file, dest_file)
        except IndexError:
            print(f'The folder corresponding to {n} is empty') #IndexError: Cannot choose from an empty sequence
            break 