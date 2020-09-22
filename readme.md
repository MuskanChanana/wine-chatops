## Wine Q/A ChatOps

#### About
A simple bot that queries over the wine mag dataset, built using the RASA stack.

directory structure
```
.
+-- dialog_data               <--- contains data used for training dialogue
|   +-- domain.yml          
|   +-- wine_stories.md
+-- models                    <--- contains the trained models
|   +-- current      
|   +-- NLU
+-- nlu_data                  <--- config used for the intent classifier  
|   +-- config_spacy.yml
+-- actions.py                <--- Custom actions
+-- bot_glue.py
+-- index.html
+-- readme.md
+-- requirements.txt
+-- server.py
+-- winemag-data_first150k.csv
```

#### Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

To run locally
```bash
python bot-glue.py run
```
#### The bot
A simple bot, can handle fairly moderate queries, still a bit unrefined. I have used Chatito for generating some training examples.
I have modeled the bot to answer queries over mostly three fields in the dataset the price, the review score and the country.


 
 It can handle queries such as
```
can you find the wine whose reviews is greater than or equal to 85 in canada
suggest some wine whose price = 72 in czech
suggest some wine whose review greater than or equal to 99 in USA
find the wine where price is greater than or equal to 15 in australia
give me info on lowest priced wines in czech
worst 85 wines in nz
suggest some wine whose score greater than or equal to 8 in montenegro
```


#### Demo
Run server.py and head to http://localhost:8080/

Made with :love: by Sheryl
