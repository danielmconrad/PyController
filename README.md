## Requirements

- [Python3](https://www.python.org/downloads/)


## Supported Controllers

- [PS4 Controller](https://www.playstation.com/en-us/explore/accessories/gaming-controllers/dualshock-4/) connected via the [USB Wireless Adapter](https://www.playstation.com/en-us/explore/accessories/gaming-controllers/dualshock-4-usb-wireless-adaptor/)


## Supported Operating Systems

- MacOS


## Installation

```bash
    pip install PyController
```


## Usage



## Development

**Requirements:**
- [Miniconda](https://conda.io/docs/user-guide/install/index.html), a package and environment manager.

- Linux
  - Follow the [hidapi](https://github.com/trezor/cython-hidapi#description) installation instructions.
  - Copy the udev rules file from the setup folder into your local udev rules

```
    sudo cp ./setup/81-pycontroller.rules /etc/udev/rules.d/81-pycontroller.rules
```

**Installation:**
  1. Fork this repository.
  2. Clone your fork.

```bash
  git clone git@github.com:YOURUSERNAME/PyController.git
  cd PyController
```

  3. Install the Conda named `PyController` that contains the necessary version of Python, as well as any dependencies, to develop against for this project:

```bash
  conda env create -f environment.yml
```


**Commands:**

When developing against this repo, make sure to always have the environment activated. Once activated, you can use `invoke` to run several tasks.

```bash
  ## Activate
  source activate PyController

  ## List what commands are available
  invoke -l

  ## Run tests
  invoke test

  ## Deactivate once done developing
  source deactivate

```
