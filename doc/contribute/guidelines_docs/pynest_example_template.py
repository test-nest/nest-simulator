# -*- coding: utf-8 -*-
#
# pynest_example_template.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""This template demonstrates how to create an example python script.

   It is based on the NumPy style docstring and uses reStructured text mark
   up. Extra annotations that explain each section are marked with brackets like this
   [[ remove this content ]].

   You can copy this file and replace the text to fit
   your example, but keep the names of section headings in the order you see here. The
   bracketed sections should be removed completely from the final version.

   Your script should contain a complete code-block that begins with all
   necessary imports and ends with code that displays the output.

   Text explanations within the code-block need to begin with a line of hashes.
"""

# [[Titles should begin with a verb and include type of model and/or method]]

""" Simulate a balanced neuron with the bisection method
----------------------------------------------------------------
[[What does this script do?]]

This script simulates a neuron by an excitatory and an inhibitory
population of neurons firing a Poisson spike train.
Optimization is performed using the `bisection` method from Scipy,
which simulates the network repeatedly.

[[Why? What is the purpose or aim of this example?]]

The aim  of this example script is to find a firing rate for the inhibitory
population that will make the neuron fire at the same rate as the excitatory
population.

[[who would benefit from this example?]]

People interested in x research may find this useful. The example here may be 
useful  to learn how to apply method Y in NEST.

[[What kind of output is expected?]]

The output shows the target neuron's membrane potential as a function of time.

[[(If applicable) where is this example referenced in the literature?]]

This example is also shown in Sander et al. [1]_.



[[ Include a couple of related examples, models, or functions in the see also section]]

See Also
---------
intrinisic_current_spiking
intrisic_current_subthreshold


Notes
------
[[Additional information can be included here regarding background theory, relevant mathetmatical equations etc.]]

The value of :math:`\omega` is X.
For the population and time-averaged from the spiking simulation:
[[Note the syntax used for displaying equations uses reStructured text with LaTeX ]]

.. math::

    X(e^{j\omega } ) = x(n)e^{ - j\omega n}

 * use the asterisk for bullet items
 * second item

References
------------
    [[ Note the format of the reference. No bold nor italics is used. Last name
       of author(s) followed by year, title in sentence case and full name of
       journal followed by volume and page range. Include the doi if
       applicable.]]

.. [1] Sander M., et al. 2011. Biology of the sauropod dinosaurs: The
       evolution of gigantism. Biological Reviews. 86(1):117-155.
       https://doi.org/10.111/j.1469-185x.2010.00137.x

.. [2] Francillon-Vieillot H, et al. 1990. Microstructure and mineralization of
       vertebrate skeletal tissues. In: Carter J ed. Skeletal Biomineralization
       Patterns, Processes and Evolutionary Trends. New York: Van Nostrand
       Reinhold, 471–530.

:Authors:
    D Adams, N Gaiman

    [[ Include a couple of comma-separated keywords - this will help us increase 
       discoverability of related documents ]]

KEYWORDS: scipy, poisson spike train, precise
"""

import nest  # begin with imports

###############################################################################
# [[After the initial docstring, all following comment blocks must begin with a 
# a line of hashes and each line of a block must begin with a hash. This will 
# allow us to generate nice looking examples for the website! ]] 
# The excitatory `poisson_generator` (`noise[0]`) and the voltmeter are
# configured using `SetStatus`, which expects a list of node handles and
# a list of parameter dictionaries.
# The rate of the inhibitory Poisson generator is set later.
# Note that we do not need to set parameters for the neuron and the
# spike detector, since they have satisfactory defaults.

nest.SetStatus(noise, [{"rate": n_ex * r_ex}, {"rate": n_in * r_in}])
nest.SetStatus(voltmeter, {"withgid": True, "withtime": True})

##############################################################################
# Finally, we plot the target neuron's membrane potential as a function of time

nest.voltage_trace.from_device(voltmeter)  # end with output
