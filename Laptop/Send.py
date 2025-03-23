from Firebase import db

# initialize the action variable
action = ""

# if statement checking if it is time to start hw
action = "homework time" 

# if statement checking if the model sent arrive
action = "arrive"

# if statement checking if the model sent depart
action = "depart"

# if statement checking if the model sent procrastinate
action = "screenager"


# set the data library to the correct action
data = {"action": action}
