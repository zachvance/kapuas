# Kapuas

Kapuas is a small library utilizing pickle to make persistent, nameable, boolean variables and alter or test their states.

The variable names and states are stored in a dictionary, which is saved and loaded as a .pickle file so they are callable on subsequent runs of the program.

#### Examples:

```
from kapuas import make, ison, on

switch = "S1"

# Create a switch named S1, with the default state as off (a value of 0).
make(switch)

# Test if the switch S1 is on, returns False.
ison(switch)

# Turn the switch S1 on.
on(switch)

# Test if the switch S1 is on again - this time returns True.
ison(switch)
```
