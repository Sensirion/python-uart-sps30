# Python UART Driver for Sensirion SPS30

This repository contains the Python driver to communicate with a Sensirion SPS30 sensor over UART using the SHDLC protocol.

<img src="https://raw.githubusercontent.com/Sensirion/python-uart-sps30/master/images/product-image-sps30.png"
    width="300px" alt="SPS30 picture">

Click [here](https://sensirion.com/products/catalog/SPS30) to learn more about the Sensirion SPS30 sensor.





## Connect the sensor

You can connect your sensor over the provided USB cable.
For special setups check out the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-uart-sps30/master/images/product-pinout-sps30.jpg"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red | VDD | Supply Voltage | 5V
| 2 | green | RX | UART: Transmission pin for communication |
| 3 | yellow | TX | UART: Receiving pin for communication |
| 4 |  | SEL | Interface select | Leave floating to select SHDLC
| 5 | black | GND | Ground |


</p>
</details>

## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-uart-sps30) for an API description and a
[quickstart](https://sensirion.github.io/python-uart-sps30/execute-measurements.html) example.


## Contributing

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).