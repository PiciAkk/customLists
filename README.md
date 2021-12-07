# customLists
Python module for making lists with custom starting index

## Usage

```python
from customLists import *

myList = customList(["someElement", "anotherElement"], 1) # make a customList with the starting index `1`

len(myList) # ˙2˙
myList.elements() # `['someElement', 'anotherElement']`
type(myList) # `<class 'customLists.customList'>` 
myList[1] # `someElement`
myList[1] = 'newElement'
myList.toList() # `[None, 'newElement', 'anotherElement']`
```
