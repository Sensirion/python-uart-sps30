Install the SPS30 Driver
------------------------

.. include:: driver-installation.rst

Run Usage-Example
-----------------

1. Connect the SPS30 sensor to your system with the serial USB cable.
2. Run the example script from the root of the repository.

   By default the script assumes the sensor is connected to COM1 serial port. If this is different on your system,
   pass the port in use with the :code:`--serial-port` parameter as outlined below.

   .. sourcecode:: bash

    python examples/example_usage_uart_sps30.py --serial-port <your COM port>

Example script
~~~~~~~~~~~~~~

.. literalinclude:: ../examples/example_usage_uart_sps30.py
    :language: python