# PC_Dataset
## Description
PC dataset from https://www.kaggle.com/datasets/sudhanshuy17/pccomponents.
Use Pandas to section data from components into different categories.

## Example
```
data = "amd Ryzen 9 5900X 3.7 GHz Upto 4.8 GHz AM4 Socket 12 Cores 24 Threads Desktop Processor"
cpu_categories = {
    "name": "amd Ryzen 9 5900X",
    "ghz": (3.7,4.8),
    "socket": "AM4"
    "cores": "12"
    "threads": "24"
    "processor": "Desktop"
}
```
## Pip install instructions
Please run the following:
```
pip install -r requirements.txt
```
## How to run
In a terminal window, please type the following:
```
python main.py
```