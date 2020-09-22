## story_01
* greet
    - utter_greet
* quant_price{"quality": "best"}
    - utter_on_it
    - action_general_query 
    - action_restarted
    
## story_002
* greet
    - utter_greet
* greet
    - utter_greet
* quant_price{"quality": "best"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_003
* greet
    - utter_greet
* quant_price{"quality": "worst"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_004
* greet
    - utter_greet
* quant_price{"quality": "worst"}
    - utter_on_it
    - action_general_query
    - action_restarted
    
## story_005
* greet
    - utter_greet
* quant_price{"quality": "best"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_006
* quant_price{"quality": "best"}
    - utter_on_it
    - action_general_query
    - action_restarted
    
## story_007
* specific{"field": "price", "quantifier": "gt", "quantity": "72"}
   - utter_on_it
   - action_specific_query
   - action_restarted

## story_008
* greet
    - utter_greet
* specific{"field": "score", "quantifier": "lte", "quantity": "20"}
    - utter_on_it
    - action_specific_query
    - action_restarted
    
## story_009
* greet
    - utter_greet
* specific{"quantifier": "lte", "quantity": "20"}
    - utter_field
* inform{"field" : "price"}
    - utter_on_it
    - action_specific_query
    - action_restarted
    
## story_010
* greet
    - utter_greet
* specific{"quantifier": "gt", "quantity": "34"}
    - utter_field
* inform{"field": "score"}
    - utter_on_it
    - action_specific_query
    - action_restarted
    
## story_011
* specific{"quantifier": "lt", "quantity": "21"}
    - utter_field
* inform{"field": "score"}
    - action_specific_query
    - action_restarted

## story_919
* specific{"quantifier": "lte", "quantity": "32"}
    - utter_field
* inform{"field": "score"}
    - action_specific_query
    - action_restarted
    
## story_012
* specific{"field": "score", "quantifier": "gt", "quantity": "30"}
    - utter_on_it
    - action_specific_query
    - action_restarted
    
## story_013
* specific{"field": "score", "quantifier": "gt", "quantity": "40", "country": "india"}
    - utter_on_it
    - action_specific_query
    - action_restarted
    
## story_014
* greet
    - utter_greet
* specific{"field": "score", "quantifier": "lte", "quantity": "20", "country": "us"}
    - utter_on_it
    - action_specific_query
    - action_restarted

## story_015
* greet
    - utter_greet
* quant_price{"quality": "best", "quantity": "6"}
    - utter_cocky
    - action_general_query
    - action_restarted

## story_016
* greet
    - utter_greet
* quant_price{"quality": "best", "quantity": "6", "howmuch": "most"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_017
* greet
    - utter_greet
* quant_price{"quality": "best", "quantity": "6", "howmuch": "most", "country": "switzerland"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_018
* quant_price{"quality": "best", "quantity": "6", "howmuch": "most", "country": "france"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_019
* quant_price{"quality": "best", "quantity": "6", "howmuch": "least"}
    - utter_cocky
    - action_general_query
    - action_restarted
    
## story_20
* quant_price{"quality": "best", "quantity": "6"}
    - utter_cocky
    - action_general_query
    - action_restarted