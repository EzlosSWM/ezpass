# EzPass

EzPass is an intuitive password generator. 

***I've been learning Python for about a year but never really did anything with it. My biggest struggle was to actually come up with project ideas but never wanted to do something as simple as a generic password generator. So I came up with the idea of taking it to the next level and this is where I came up with the idea for EzPass.***

Going through with EzPass I forced myself to learn, understand and implement simple Python concepts rather than just knowing the theory. This is just the beginning with limited features but my end goal is a password generator that: 

1. Is fully compatible with Windows, Mac, and Linux. *(Only works on Linux machines for the time being)*

2. Be able to access your passwords easily from the command line rather than going to search on the output/ folder. 

3. Simple copy and paste. 

Because I'm still learning about how to implement what and when, it might take some time, however, I'm hoping you all enjoy it. 

# Installation

Basic Usage: 

```bash
cd ~/Documents/ # Could be any folder.

git clone https://github.com/EzlosSWM/ezpass.git
```

To have it run from any directory.

```bash
# (Optional) Create a directory for your scripts, in your home folder.
mkdir ~/.scripts
# (Optional) Add folder to your PATH variable
export PATH=$PATH:"~/.scripts"
cd ~/.scripts
# Download EzPass
git clone https://github.com/EzlosSWM/ezpass.git
# (Optional) Remove the .py extension. 
mv ezpass.py ezpass 
# Make ezpass executable
chmod +x ezpass
```

After following the above instructions, you can run `ezpass` as a regular command. 

# Usage

If you chose not to make a dedicated folder for your scripts go to the installed path and enter: 

```python
python3 ezpass.py <length-of-password>
```

If you chose to run it as a script: 

```python
ezpass <length-of-password>
```

There are two options for output, **-o / --output** and **-s / --silent**.

- *-o / --ouput*: will present the generated password on the command line and save it the the json file in the output/ folder. 

- *-s / --silent*: wil not show you the passsword in the command line. The password is still saved within the json file. *(This is the default)* 

## Features

Even though, these are optional, I highly recommend using them for organization's sake. You don't want to generate different passwords for *abc.com* and *xyz.com* and don't know which password is for which website or username. 

- *-h / --help*: is a generic help menu for usage.

- *-u / --username*: the username attached to the generated password.

- *-t / title*: the name of the website for the generated password.

- *-o / --ouput*: will present the generated password on the command line and save it the the json file in the output/ folder.

- *-s / --silent*: wil not show you the passsword in the command line. The password is still saved within the json file. *(This is the default)*

### Example:

```python
python3 ezpass.py 16 -t www.test.com -u ezlosswm -o
```

### Output:

> The generated password for ['www.test.com'] is KElQ9iFiMBcXwUlR.

# Contact

I'm always learning, so if you have any tips to improve the code or any tips in general feel free to message me directly on: 

- [Github](www.github.com/EzlosSWM)

- [Twitter](www.twitter.com/EzlosSWM)
