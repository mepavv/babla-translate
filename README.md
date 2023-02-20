# babla-translate
A Python module for translating words and generating examples using [Bab.la](https://bab.la) dictionary.

## Installation
```pip install babla_translate```

## Functions

Module contains class `Babla` with two functions:
```python
babla.translation(word, exact_word = 1)
babla.example(word, exact_word = 1)
```

`word`, accepts string, which you'd like to translate.\
`exact_word`, optional argument which takes int (1 by default), defining if function has to use the exact word; for example if for word 'used' translation of 'use' should also be shown.



## Entry point
All operations are implemented in class `Babla`.     
It takes source and target languages ("english", "polish", "german", "spanish"...) as required arguments.

```python
from babla_translate import Babla

babla = Babla("english", "polish")
```
All usable languages can be found [here](https://bab.la/dictionary/).


## Usage
* Getting translations:
```python
>>> list(babla.translation("use"))
['użyć', 'używać', 'wykorzystać', 'wykorzystywać', 'zastosować', 'skorzystać', 'zażyć',...]
```
* Getting examples:
```python
>>> for context in babla.example("use"):
...     print(context)
'This use of turmeric leaves usually takes place in areas where turmeric is grown locally, since the leaves used are freshly picked.'
```
All the functions return iterators to not request more results than needed.