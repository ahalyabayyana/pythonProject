from datetime import datetime, timedelta

# to print the current date and time
def date_time_fn():

    cd = datetime.now()
    print("Current date and time is:", cd)
    date_object = datetime(2011, 8, 11, 16, 30, 9)
    print("Setting the date to certain date and time:", date_object)
    # we are formatting the date_object according to our convenience
    res = date_object.strftime("%y")
    print("Shorter of year:", res)
    res1 = date_object.strftime("%Y")
    print("Full form of year:", res1)
    res2 = date_object.strftime("%b")
    print("Short version of month:", res2)
    res3 = date_object.strftime("%B")
    print("Full form of month:", res3)
    res4 = date_object.strftime("%a")
    print("Short version of day:", res4)
    res5 = date_object.strftime("%A")
    print("Full version of day:", res5)
    res6 = date_object.strftime("%w")
    print("Number of weekday:", res6)
    res7 = date_object.strftime("%H")
    print("24 hour format:", res7)
    res8 = date_object.strftime("%I")
    print("12 hour format:", res8)
    res9 = date_object.strftime("%p")
    print("AM/PM:", res9)
    res10 = date_object.strftime("%M")
    print("Minutes:", res10)
    res11 = date_object.strftime("%S")
    print("Seconds:", res11)
    res12 = date_object.strftime("%f")
    print("Micro Seconds:", res12)
    res13 = date_object.strftime("%j")
    print("DAy number of year:", res13)
    res14 = date_object.strftime("%x")
    print("Local Version without time:", res14)
    res15 = date_object.strftime("%X")
    print("Local Version of time:", res15)

    # using timedelta function we can modify the existing time and date

    cd = datetime.now()
    print("current date and time is:", cd)

    new_date = cd + timedelta(weeks=2)
    print("Current date will be modified with added two weeks:", new_date)
    new_date1 = cd + timedelta(days=31)
    print("Current date will be modified with added 31days:", new_date1)
    new_date3 = cd - timedelta(weeks=5)
    print("we gave - subtraction so the 5 weeks will be deduced from current date:", new_date3)
    new_date4 = cd - timedelta(days=5)
    print("Current date will be modified subtracted with 5 days:", new_date4)

def CurrentTime():
    print("Current time at the execution is:",datetime.now())

def main():
    CurrentTime()
    date_time_fn()

if (__name__=="__main__"):  #we are doing this inorder to prevent the entire module to run when importing it into another
                             #module
    main()
