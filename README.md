# Soft for a Raspberry's CPU fan

## About
It's a simple soft with **Python**, that controls the **CPU fan** on **Raspberry Pi 3B**. It turns the fan on if the set temperature was achieved. And turns it off when the CPU cools down
Soft also saves the **logs of temperature** with the preset frequency.


## Dependencies
`Python 3.10.0`
Some python `modules`:
    - RPi.GPIO
    - time
    - os
    - datetime
    - logging


## Electric Circuit
All you need are:
    - `Raspberry Pi`
    - `Fan 5v DC`
    - `NPN transistor` (e.g. BC337, but analogs are possible) 
    - `Resistor 1k Ohm`

The **electric circuit** is attached below

![electric circuit](/materials/circuit.png)
