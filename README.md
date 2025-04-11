# Notes

> To check the datatype of the variable we below method.
```
var = 10.5
if isinstance(var, float):
    print(f"{var} is a float")
else:
    print(f"{var} is not a float")

```

> How to take the numbers as input seperated as space

```
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Sorted list: {numbers}")
```