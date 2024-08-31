# ics-automation
This script created from python, Helps in managing events by puting them in calendar, to do that The Internet Calendaring and Scheduling (ICS) file  is created with the help of this script. This script was designed for more specific usage, so if you are to use this, are suggested to modify for your specific need.

## Files-used
in, `cleaned_schedule-2a.csv` I have these columns Day, Date, Time, Session, Type, Location.


| Day   | Date       | Time    | Session | Type                  | Location               |
|-------|------------|---------|---------|-----------------------|------------------------|
| DAY 1 | 2024-08-28 | Morning | T1      | Technical Training     | 3rd Floor CSE LAB     |
| DAY 1 | 2024-08-28 | Morning | T2      | Technical Training.1   | Ground Floor CAED LAB  |
| DAY 1 | 2024-08-28 | Morning | T3      | Technical Training.2   | Innovation Centre       |

## Usage
usual download the script file into your linux machine, and modify accordingly.

### Creating Project via conda
Download and install conda. I suggest using this script in Linux machines, and for those who cant may use the other method.
##### LINUX way
```bash
conda env create -f environment.yml
```
##### OTHER way (not recommended)
```bash
conda env create -f environment-no-builds.yml
```
after installing environment, run `conda activate ics-calendar` This should take care of project environment. Now, run the script
```bash
python create_ics.py
```
After this upon executing properly should create .ics files in the ./files folder of the repo. Share the file and happy Eventing..
