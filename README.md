# Kapuas

Kapuas is a small library utilizing pickle to make persistent, nameable, binary variables and alter or test
their states.

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
