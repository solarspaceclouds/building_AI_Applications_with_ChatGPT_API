# Overview
This is the updated code for the projects from Building AI Applications with ChatGPT APIs book by Martin Yanev after the openai library revamp in Oct/Nov 2023. 
This code works as of 23 February 2024.

(https://github.com/PacktPublishing/Building-AI-Applications-with-ChatGPT-APIs)

Within each folder,
Step 1: 
Install required dependencies with
```
pip install requirements.txt
```

Step 2:Run the app with 
```
python3 app.py
```
Sample results for the relevant projects can be found within the respective folders

## 2 ChatGPT CLone

![chatgpt_clone](https://github.com/solarspaceclouds/building_AI_Applications_with_ChatGPT_API/assets/65459827/778af075-612d-4362-83a6-6853094f9c57)

## 5 Quiz Generator App with Django
```
python3 manage.py runserver
```

![chatgpt_quiz_generator](https://github.com/solarspaceclouds/building_AI_Applications_with_ChatGPT_API/assets/65459827/35657435-0ac1-46d7-a9e0-c604378ec813)
![chatgpt_quiz_generator_download](https://github.com/solarspaceclouds/building_AI_Applications_with_ChatGPT_API/assets/65459827/bb40d646-127e-4f53-8447-ed9ce4f3660e)

## 6 Language Translator App

![chatgpt_language_translator](https://github.com/solarspaceclouds/building_AI_Applications_with_ChatGPT_API/assets/65459827/460f1732-f972-4025-a723-944d65eed1ef)

## 8 Powerpoint Generator with ChatGPT and DALLE API
- 1 slide generated per paragraph;
- paragraphs to be separated by '\n\n'

## 11 Models Cost Estimation and Performance Analysis 
- jupyter notebook
  
## 12 Fine Tuning
- jupyter notebooks
  
Chapter12_helper.ipynb has helper functions to convert train_data.json into train_data_prepared.jsonl;
training file required to be in the format as specified in train_data_prepared.jsonl for fine-tuning

Chapter12_fine_tune.ipynb uses train_data_prepared.jsonl for fine-tuning.


### Helpful resource for openai API migrations
https://github.com/openai/openai-python/discussions/742  
