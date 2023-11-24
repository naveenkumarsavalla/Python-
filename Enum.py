# Enum
from enum import Enum
class weekday(Enum):
    Monday=1
    Tuesday=2
    Wednesday=3
    Thursday=4
    Friday=5
    Saturday=6
    Sunday=7
def checkday(value):
    result:str=""
    match(value):
        case weekday.Monday.value:
            result="Weekday"
        case weekday.Tuesday.value:
            result="Weekday"
        case weekday.Wednesday.value:
            result="Weekday"
        case weekday.Thursday.value:
            result="Weekday"
        case weekday.Friday.value:
            result="Weekday"
        case weekday.Saturday.value:
            result="Weekend"
        case weekday.Sunday.value:
            result="Weekend"
    return result
day=int(input("Enter day value:"))
print(checkday(day))
print(type(weekday))
print(weekday.Monday)
print(weekday.Monday.value)
print(weekday.Monday.name)

#Exception Handling
try:
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    print(a*b)
except:
    print("Execption Occur.")
else:
    print("Program excuted Successfully.")
finally:
    print("program completed.")



