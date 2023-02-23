"""
Write a function called collectStrings which accepts an object 
and returns an array of all the values in the object that have a typeof string.
Examples
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
collectStrings(obj) # ['foo', 'bar', 'baz']
"""
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
def collectStrings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is dict:
            result.extend(collectStrings(obj[key]))
        elif type(obj[key]) is str:
            result.append(obj[key])
    return result 
print(collectStrings(obj))