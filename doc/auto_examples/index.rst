:orphan:

This directory contains example networks  using PyNEST.

Some of the examples have corresponding SLI versions (e.g. brunel-alpha-nest.py) and it is instructive to compare them.

Here is a list of all examples:

LeNovere_2012/  Directory with examples from the NEST Tutorial chapter in Le Novere (2012)
LeNovere_2012/brunel2000_classes.py
LeNovere_2012/brunel2000_interactive.py
LeNovere_2012/brunel2000_rand.py
LeNovere_2012/brunel2000_rand_plastic.py
LeNovere_2012/one_neuron_with_sine_wave.py

BrodyHopfield.py
CampbellSiegert.py
balancedneuron.py
brette-gerstner-fig-2c.py 
brette-gerstner-fig-3d.py
brunel-alpha-nest.py
brunel-alpha-numpy.py
brunel-delta-nest.py
csa_example.py
gif_population.py
if_curve.py
mc_neuron.py
multimeter.py
multimeter_file.py
one-neuron-with-noise.py
one-neuron.py
pulsepacket.py
repeated_stimulation.py
test_tsodyks2_synapse.py
testiaf.py
tsodyks_depressing.py
tsodyks_facilitating.py
twoneurons.py
vinit_example.py



.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates a neuron driven by a constant external current and records its membrane p...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_one_neuron_thumb.png

        :ref:`sphx_glr_auto_examples_one_neuron.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/one_neuron

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="References ~~~~~~~~~~~~">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_twoneurons_thumb.png

        :ref:`sphx_glr_auto_examples_twoneurons.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/twoneurons

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates a neuron with input from the Poisson generator, and records the neuron&#x27;s ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_one_neuron_with_noise_thumb.png

        :ref:`sphx_glr_auto_examples_one_neuron_with_noise.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/one_neuron_with_noise

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot several runs of the `iaf_cond_exp_sfa_rr` neuron without input for various initial values ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_vinit_example_thumb.png

        :ref:`sphx_glr_auto_examples_vinit_example.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/vinit_example

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example tests the adaptive integrate and fire model (AdEx) according to Brette and Gerstne...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brette_gerstner_fig_3d_thumb.png

        :ref:`sphx_glr_auto_examples_brette_gerstner_fig_3d.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brette_gerstner_fig_3d

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example tests the adaptive integrate and fire model (AdEx) according to Brette and Gerstne...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brette_gerstner_fig_2c_thumb.png

        :ref:`sphx_glr_auto_examples_brette_gerstner_fig_2c.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brette_gerstner_fig_2c

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Simple example for how to repeat a stimulation protocol using the &#x27;origin&#x27; property of devices.">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_repeated_stimulation_thumb.png

        :ref:`sphx_glr_auto_examples_repeated_stimulation.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/repeated_stimulation

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example sets up a simple network in NEST using the Connection Set Algebra (CSA) instead of...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_csa_example_thumb.png

        :ref:`sphx_glr_auto_examples_csa_example.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/csa_example

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates two Hodgkin-Huxley neurons of type `hh_psc_alpha_gap` connected by a gap ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_gap_junctions_two_neurons_thumb.png

        :ref:`sphx_glr_auto_examples_gap_junctions_two_neurons.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/gap_junctions_two_neurons

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example produces a rate-response (FI) curve of the Hodgkin-Huxley neuron  in response to a...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_hh_psc_alpha_thumb.png

        :ref:`sphx_glr_auto_examples_hh_psc_alpha.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/hh_psc_alpha

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This synapse model implements synaptic short-term depression and short-term f according to [1] ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_evaluate_tsodyks2_synapse_thumb.png

        :ref:`sphx_glr_auto_examples_evaluate_tsodyks2_synapse.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/evaluate_tsodyks2_synapse

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows a brute-force way of specifying connections between NEST Topology layers usi...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_csa_topology_example_thumb.png

        :ref:`sphx_glr_auto_examples_csa_topology_example.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/csa_topology_example

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This file demonstrates recording from an `iaf_cond_alpha` neuron using a multimeter and writing...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_multimeter_file_thumb.png

        :ref:`sphx_glr_auto_examples_multimeter_file.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/multimeter_file

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script reproduces the spike synchronization behavior of integrate-and-fire neurons in resp...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_BrodyHopfield_thumb.png

        :ref:`sphx_glr_auto_examples_BrodyHopfield.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/BrodyHopfield

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This scripts simulates two connected binary neurons, similar as in [1]. It measures and plots t...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_correlospinmatrix_detector_two_neuron_thumb.png

        :ref:`sphx_glr_auto_examples_correlospinmatrix_detector_two_neuron.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/correlospinmatrix_detector_two_neuron

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates a population of generalized integrate-and-fire (GIF) model neurons driven...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_gif_population_thumb.png

        :ref:`sphx_glr_auto_examples_gif_population.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/gif_population

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In traditional time-driven simulations, spikes are constrained to the time grid at a user-defin...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_precise_spiking_thumb.png

        :ref:`sphx_glr_auto_examples_precise_spiking.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/precise_spiking

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates a neuron driven by an excitatory and an inhibitory population of neurons ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_balancedneuron_thumb.png

        :ref:`sphx_glr_auto_examples_balancedneuron.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/balancedneuron

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The quantal_stp_synapse is a stochastic version of the Tsodys-Markram model for synaptic short ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_evaluate_quantal_stp_synapse_thumb.png

        :ref:`sphx_glr_auto_examples_evaluate_quantal_stp_synapse.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/evaluate_quantal_stp_synapse

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This scripts simulates two neurons. One is driven with dc-input and connected to the other one ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_tsodyks_depressing_thumb.png

        :ref:`sphx_glr_auto_examples_tsodyks_depressing.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/tsodyks_depressing

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This scripts simulates two neurons. One is driven with dc-input and connected to the other one ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_tsodyks_facilitating_thumb.png

        :ref:`sphx_glr_auto_examples_tsodyks_facilitating.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/tsodyks_facilitating

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A DC current is injected into the neuron using a current generator device. The membrane potenti...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_testiaf_thumb.png

        :ref:`sphx_glr_auto_examples_testiaf.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/testiaf

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A time bin of size tbin is centered around the time difference it represents. If the correlatio...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_cross_check_mip_corrdet_thumb.png

        :ref:`sphx_glr_auto_examples_cross_check_mip_corrdet.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/cross_check_mip_corrdet

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates a neuron receiving spiking input through several different receptors (...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_intrinsic_currents_spiking_thumb.png

        :ref:`sphx_glr_auto_examples_intrinsic_currents_spiking.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/intrinsic_currents_spiking

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A binary decision is implemented in the form of two rate neurons engaging in mutual inhibition.">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_rate_neuron_dm_thumb.png

        :ref:`sphx_glr_auto_examples_rate_neuron_dm.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/rate_neuron_dm

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates an inhibitory network of 500 Hodgkin-Huxley neurons. Without the gap junc...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_gap_junctions_inhibitory_network_thumb.png

        :ref:`sphx_glr_auto_examples_gap_junctions_inhibitory_network.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/gap_junctions_inhibitory_network

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates how to extract the connection strength for all the synapses among two...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_plot_weight_matrices_thumb.png

        :ref:`sphx_glr_auto_examples_plot_weight_matrices.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/plot_weight_matrices

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates how to record from a model with multiple intrinsic currents and visual...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_intrinsic_currents_subthreshold_thumb.png

        :ref:`sphx_glr_auto_examples_intrinsic_currents_subthreshold.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/intrinsic_currents_subthreshold

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates an excitatory and an inhibitory population of lin_rate_ipn neurons with d...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_lin_rate_ipn_network_thumb.png

        :ref:`sphx_glr_auto_examples_lin_rate_ipn_network.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/lin_rate_ipn_network

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script demonstrates the use of the `sinusoidal_poisson_generator` and its different parame...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_sinusoidal_poisson_generator_thumb.png

        :ref:`sphx_glr_auto_examples_sinusoidal_poisson_generator.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/sinusoidal_poisson_generator

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script performs a mean-field analysis of the spiking network of excitatory and an inhibito...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brunel_siegert_nest_thumb.png

        :ref:`sphx_glr_auto_examples_brunel_siegert_nest.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brunel_siegert_nest

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Simple example of how to use the three-compartment ``iaf_cond_alpha_mc`` neuron model.">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_mc_neuron_thumb.png

        :ref:`sphx_glr_auto_examples_mc_neuron.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/mc_neuron

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates a network in two successive trials, which are identical except for one ex...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_sensitivity_to_perturbation_thumb.png

        :ref:`sphx_glr_auto_examples_sensitivity_to_perturbation.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/sensitivity_to_perturbation

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates how to measure the I-F curve of a neuron. The program creates a small ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_if_curve_thumb.png

        :ref:`sphx_glr_auto_examples_if_curve.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/if_curve

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates an excitatory and an inhibitory population on the basis of the network us...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brunel_delta_nest_thumb.png

        :ref:`sphx_glr_auto_examples_brunel_delta_nest.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brunel_delta_nest

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="hh_phaseplane makes a numerical phase-plane analysis of the Hodgkin-Huxley neuron (iaf_psc_alph...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_hh_phaseplane_thumb.png

        :ref:`sphx_glr_auto_examples_hh_phaseplane.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/hh_phaseplane

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Example script that applies Campbell&#x27;s theorem and Siegert&#x27;s rate approximation to and integrat...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_CampbellSiegert_thumb.png

        :ref:`sphx_glr_auto_examples_CampbellSiegert.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/CampbellSiegert

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script compares the average and individual membrane potential excursions in response to a ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_pulsepacket_thumb.png

        :ref:`sphx_glr_auto_examples_pulsepacket.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/pulsepacket

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates an excitatory and an inhibitory population on the basis of the network us...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brunel_exp_multisynapse_nest_thumb.png

        :ref:`sphx_glr_auto_examples_brunel_exp_multisynapse_nest.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brunel_exp_multisynapse_nest

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates an excitatory and an inhibitory population on the basis of the network us...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brunel_alpha_nest_thumb.png

        :ref:`sphx_glr_auto_examples_brunel_alpha_nest.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brunel_alpha_nest

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates an excitatory and an inhibitory population on the basis of the network us...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brunel_alpha_numpy_thumb.png

        :ref:`sphx_glr_auto_examples_brunel_alpha_numpy.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brunel_alpha_numpy

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Example script with invalid Python syntax ">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_sinusoidal_gamma_generator_thumb.png

        :ref:`sphx_glr_auto_examples_sinusoidal_gamma_generator.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/sinusoidal_gamma_generator

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script simulates a finite network of generalized integrate-and-fire (GIF) neurons directly...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_gif_pop_psc_exp_thumb.png

        :ref:`sphx_glr_auto_examples_gif_pop_psc_exp.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/gif_pop_psc_exp

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="References ~~~~~~~~~~~~ .. [1] Butz M,and van Ooyen A. 201). A simple rule for dendritic spine ...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_structural_plasticity_thumb.png

        :ref:`sphx_glr_auto_examples_structural_plasticity.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/structural_plasticity

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script produces a balanced random network of scale*11250 neurons in which the excitatory-e...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_hpc_benchmark_thumb.png

        :ref:`sphx_glr_auto_examples_hpc_benchmark.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/hpc_benchmark

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This script uses an optimization algorithm to find the appropriate parameter values for the ext...">

.. only:: html

    .. figure:: /auto_examples/images/thumb/sphx_glr_brunel_alpha_evolution_strategies_thumb.png

        :ref:`sphx_glr_auto_examples_brunel_alpha_evolution_strategies.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/brunel_alpha_evolution_strategies
.. raw:: html

    <div style='clear:both'></div>


The example scripts presented in the "NEST by Example" chapter in
Le Novere (2012) are now maintained in directory

	doc/nest_by_example/scripts
	
Hans E Plesser, 2014-12-12


.. raw:: html

    <div style='clear:both'></div>



.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-gallery


  .. container:: sphx-glr-download

    :download:`Download all examples in Python source code: auto_examples_python.zip <//home/graber/work-nest/nest-git/nest-simulator/doc/auto_examples/auto_examples_python.zip>`



  .. container:: sphx-glr-download

    :download:`Download all examples in Jupyter notebooks: auto_examples_jupyter.zip <//home/graber/work-nest/nest-git/nest-simulator/doc/auto_examples/auto_examples_jupyter.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_
