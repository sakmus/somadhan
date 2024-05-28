
# Somadhan

Somadhan is a simple web application developed using the Flask framework of python. It starts a dynamic website which solves mathematical problems within a few seconds. It uses the Wolframalpha API to solve problems and show outputs. Currently it can only provide one-line solution and some basic plotting features.


## Prerequisites

- **Python** interpreter must be installed and Linux systems might need to install python-venv for using  it.
- Active internet connection is mandatory.

## Installation

- The installation is very simple and fast. Download and extract the zip file of this repository or clone it using:<br>
`$ git clone https://github.com/sakmus/somadhan`

- Install the required packages using pip:<br>`$ pip install flask wolframalpha`

- Get your own API key or AppID from [Wolfram Alpha developer portal](https://developer.wolframalpha.com/) and paste it in 'api.key' file.

*Note:* For installing the additional packages using pip in Linux, you might need to to use virtual environment for the program.


## Usage

Using the program is also pretty straight forward and easy. Navigate to the main branch and run the following command<br>
`$ python3 main.py` *or,*<br> `$ python main.py`

You will see some texts in the terminal where it will show the the adress of the website that's running. Click on it or copy and paste it in the browser adress bar to visit the website. It is a development server which runs on local machine but you can deploy it and use it with Nginx and other servers. For more details about deployment, read [Flask deployment manual](https://flask.palletsprojects.com/en/3.0.x/deploying/).

## Warning!!

This project is licensed under the GNU General Pulic License (GPL) and so you can use it for any purpose and I'll not be responsible for them and you'll have to give credits for this program. Happy coding!
