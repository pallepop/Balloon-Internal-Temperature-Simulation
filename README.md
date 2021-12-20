# Balloon-Internal-Temperature-Simulation
Program used to find out what thickness is needed to keep the internal temperature of the basket above a temperature of your choice

IMPORTANT: 

Matplotlib is necessary to run this program, otherwise it won't work. Go on Youtube or somewhere else to see how to install it.
Templib (homemade) is also a necessary library, make sure to download it aswell

HOW TO USE: 

In order to match this program to your needs, you need to know the following caracteristics of your insulation:

cp # Specific Heat in J/kg*K
, rho # Density in kg/m^3
, k # Thermal Conductivity in W/m*K

These will be used to calculate the Thermal diffusion coefficient of your insulation.

Moreover, you'll need to know the average ascension speed of your balloon. 

Run and enjoy

This program is based on the simplified version of the heat equation (1 dimension) https://en.wikipedia.org/wiki/Heat_equation#Derivation_in_one_dimension
Three assumptions are made:
-the temperature at the edge of the basket insulation (outside) is the same as the air outside (which does not take into account the boundary layer).
-the temperature inside the backet is the same as the temperature at the edge of the basket insulation (inside) (which should be enough because you don't put your experiments in "mid air").
-The heat produced from the electical components (arduino, raspberry pi for example) is neglected.
