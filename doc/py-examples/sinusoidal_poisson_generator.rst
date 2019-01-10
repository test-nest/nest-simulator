.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_py-examples_sinusoidal_poisson_generator.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_py-examples_sinusoidal_poisson_generator.py:


Sinusoidal poisson generator example
------------------------------------

This script demonstrates the use of the `sinusoidal_poisson_generator`
and its different parameters and modes. The source code of the model
can be found in ``models/sinusoidal_poisson_generator.h``.

The script is structured into two parts and creates one common figure.
In Part 1, two instances of the `sinusoidal_poisson_generator` are
created with different parameters. Part 2 illustrates the effect of
the ``individual_spike_trains`` switch.

KEYWORDS:


We import the modules required to simulate, analyze and plot this example.



.. code-block:: python
   :lineno-start: 44



    import nest
    import matplotlib.pyplot as plt
    import numpy as np

    nest.ResetKernel()   # in case we run the script multiple times from iPython








We create two instances of the `sinusoidal_poisson_generator` with two
different parameter sets using `Create`. Moreover, we create devices to
record firing rates (`multimeter`) and spikes (`spike_detector`) and connect
them to the generators using `Connect`.



.. code-block:: python
   :lineno-start: 58



    nest.SetKernelStatus({'resolution': 0.01})

    g = nest.Create('sinusoidal_poisson_generator', n=2,
                    params=[{'rate': 10000.0,
                             'amplitude': 5000.0,
                             'frequency': 10.0,
                             'phase': 0.0},
                            {'rate': 0.0,
                             'amplitude': 10000.0,
                             'frequency': 5.0,
                             'phase': 90.0}])

    m = nest.Create('multimeter', n=2, params={'interval': 0.1, 'withgid': False,
                                               'record_from': ['rate']})
    s = nest.Create('spike_detector', n=2, params={'withgid': False})

    nest.Connect(m, g, 'one_to_one')
    nest.Connect(g, s, 'one_to_one')
    print(nest.GetStatus(m))
    nest.Simulate(200)






.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ({'thread_local_id': -1, 'withweight': False, 'interval': 0.1, 'scientific': False, 'thread': 0, 'withtime': True, 'global_id': 3, 'time_in_steps': False, 'vp': 0, 'close_on_reset': True, 'origin': 0.0, 'to_memory': True, 'offset': 0.0, 'to_file': False, 'events': {'rate': array([], dtype=float64), 'times': array([], dtype=float64)}, 'to_screen': False, 'use_gid_in_filename': True, 'withrport': False, 'binary': False, 'element_type': <SLILiteral: recorder>, 'model': <SLILiteral: multimeter>, 'close_after_simulate': False, 'file_extension': 'dat', 'record_to': (<SLILiteral: memory>,), 'flush_after_simulate': True, 'frozen': False, 'fbuffer_size': -1, 'parent': 0, 'local': True, 'to_accumulator': False, 'label': '', 'precision': 3, 'n_events': 0, 'withtargetgid': False, 'withgid': False, 'start': 0.0, 'record_from': (<SLILiteral: rate>,), 'node_uses_wfr': False, 'flush_records': False, 'stop': 1.7976931348623157e+308, 'withport': False, 'local_id': 3, 'supports_precise_spikes': False}, {'thread_local_id': -1, 'withweight': False, 'interval': 0.1, 'scientific': False, 'thread': 0, 'withtime': True, 'global_id': 4, 'time_in_steps': False, 'vp': 0, 'close_on_reset': True, 'origin': 0.0, 'to_memory': True, 'offset': 0.0, 'to_file': False, 'events': {'rate': array([], dtype=float64), 'times': array([], dtype=float64)}, 'to_screen': False, 'use_gid_in_filename': True, 'withrport': False, 'binary': False, 'element_type': <SLILiteral: recorder>, 'model': <SLILiteral: multimeter>, 'close_after_simulate': False, 'file_extension': 'dat', 'record_to': (<SLILiteral: memory>,), 'flush_after_simulate': True, 'frozen': False, 'fbuffer_size': -1, 'parent': 0, 'local': True, 'to_accumulator': False, 'label': '', 'precision': 3, 'n_events': 0, 'withtargetgid': False, 'withgid': False, 'start': 0.0, 'record_from': (<SLILiteral: rate>,), 'node_uses_wfr': False, 'flush_records': False, 'stop': 1.7976931348623157e+308, 'withport': False, 'local_id': 4, 'supports_precise_spikes': False})


After simulating, the spikes are extracted from the `spike_detector` using
`GetStatus` and plots are created with panels for the PST and ISI histograms.



.. code-block:: python
   :lineno-start: 85



    colors = ['b', 'g']

    for j in range(2):

        ev = nest.GetStatus([m[j]])[0]['events']
        t = ev['times']
        r = ev['rate']

        sp = nest.GetStatus([s[j]])[0]['events']['times']
        plt.subplot(221)
        h, e = np.histogram(sp, bins=np.arange(0., 201., 5.))
        plt.plot(t, r, color=colors[j])
        plt.step(e[:-1], h * 1000 / 5., color=colors[j], where='post')
        plt.title('PST histogram and firing rates')
        plt.ylabel('Spikes per second')

        plt.subplot(223)
        plt.hist(np.diff(sp), bins=np.arange(0., 1.005, 0.02),
                 histtype='step', color=colors[j])
        plt.title('ISI histogram')





.. image:: /py-examples/images/sphx_glr_sinusoidal_poisson_generator_001.png
    :class: sphx-glr-single-img




The kernel is reset and the number of threads set to 4.



.. code-block:: python
   :lineno-start: 111



    nest.ResetKernel()
    nest.SetKernelStatus({'local_num_threads': 4})








A `sinusoidal_poisson_generator` with  `individual_spike_trains` set to
``True`` is created and connected to 20 parrot neurons whose spikes are
recorded by a spike detector. After simulating, a raster plot of the spikes
is created.



.. code-block:: python
   :lineno-start: 122



    g = nest.Create('sinusoidal_poisson_generator',
                    params={'rate': 100.0, 'amplitude': 50.0,
                            'frequency': 10.0, 'phase': 0.0,
                            'individual_spike_trains': True})
    p = nest.Create('parrot_neuron', 20)
    s = nest.Create('spike_detector')

    nest.Connect(g, p, 'all_to_all')
    nest.Connect(p, s, 'all_to_all')

    nest.Simulate(200)
    ev = nest.GetStatus(s)[0]['events']
    plt.subplot(222)
    plt.plot(ev['times'], ev['senders'] - min(ev['senders']), 'o')
    plt.ylim([-0.5, 19.5])
    plt.yticks([])
    plt.title('Individual spike trains for each target')





.. image:: /py-examples/images/sphx_glr_sinusoidal_poisson_generator_002.png
    :class: sphx-glr-single-img




The kernel is reset again and the whole procedure is repeated for a
`sinusoidal_poisson_generator` with `individual_spike_trains` set to
``False``. The plot shows that in this case, all neurons receive the same
spike train from the `sinusoidal_poisson_generator`.



.. code-block:: python
   :lineno-start: 148



    nest.ResetKernel()
    nest.SetKernelStatus({'local_num_threads': 4})

    g = nest.Create('sinusoidal_poisson_generator',
                    params={'rate': 100.0, 'amplitude': 50.0,
                            'frequency': 10.0, 'phase': 0.0,
                            'individual_spike_trains': False})
    p = nest.Create('parrot_neuron', 20)
    s = nest.Create('spike_detector')

    nest.Connect(g, p, 'all_to_all')
    nest.Connect(p, s, 'all_to_all')

    nest.Simulate(200)
    ev = nest.GetStatus(s)[0]['events']
    plt.subplot(224)
    plt.plot(ev['times'], ev['senders'] - min(ev['senders']), 'o')
    plt.ylim([-0.5, 19.5])
    plt.yticks([])
    plt.title('One spike train for all targets')



.. image:: /py-examples/images/sphx_glr_sinusoidal_poisson_generator_003.png
    :class: sphx-glr-single-img




**Total running time of the script:** ( 0 minutes  0.250 seconds)


.. _sphx_glr_download_py-examples_sinusoidal_poisson_generator.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: sinusoidal_poisson_generator.py <sinusoidal_poisson_generator.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: sinusoidal_poisson_generator.ipynb <sinusoidal_poisson_generator.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_
