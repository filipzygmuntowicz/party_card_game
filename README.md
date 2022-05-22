# party_card_game
work in progress

Currently you can only use the api.

https://drinkixxy.herokuapp.com/api/categories returns all categories of cards 

https://drinkixxy.herokuapp.com/api/question returns a random question from random (by default) category, you can specify it more with:

- `?category=` - specifies the category of returned question, `?category=random` returns random question. You can input multiple categories and seperate them with "," and it will choose them randomly.
- `?count=` - specifies the amount of returned questions.
- `?nsfw=` - True or False, specifies if returned question is safe to work. Random by default.

You can mix these queries, for example:
https://drinkixxy.herokuapp.com/api/question?category=popular,random,kids&nsfw=False&count=10
will return 10 non-nsfw questionns of randomly chosen categories from [popular, random, kids].
