
# Somadhan

Somadhan is a simple web application developed using the Flask framework of python. It starts a dynamic website which solves mathematical problems within a few seconds. It uses the Wolframalpha API to solve problems and show outputs. Currently it can only provide one-line solution and some basic plotting features.

![A screenshot of Somadhan web-interface](https://images2.imgbox.com/41/87/0V4d4lb2_o.png)


## Prerequisites

- **Python** interpreter must be installed and Linux systems might need to install python-venv for using  it.
- Active internet connection is mandatory.

## Installation

- The installation is very simple and fast. Download and extract the zip file of this repository or clone it using:<br>
`$ git clone https://github.com/sakmus/somadhan`

- Activate the virtual environment in Linux and MacOS:<br>`$ source env/bin/activate`

- Install the required packages with pip (Windows):<br>`$ pip install flask wolframalpha python-dotenv`

- Get your own API key or AppID from [Wolfram Alpha developer portal](https://developer.wolframalpha.com/) and set it as the value of 'APP_ID' in '.env' file.


## Usage

Using the program is also pretty straight forward and easy. Navigate to the main branch and run the following command<br>
`$ python3 main.py` *or,*<br> `$ python main.py`

You will see some texts in the terminal showing the the adress of the website. Click on it or copy and paste it in the browser address bar to visit the website. It is a development server which runs on local machine but you can deploy it with servers like [Nginx](https://nginx.org/). For more details about deployment, read [Flask deployment manual](https://flask.palletsprojects.com/en/3.0.x/deploying/).

## Licensing

This work is published under [GPL-3](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text) License.
