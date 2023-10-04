import pandas as pd

# Initialize empty lists for each category
names = []
integrated_graphics_list = []
coolers = []
ghz_values = []
sockets = []
cores = []
threads = []
processors = []

# Given data
data = [
    "amd Ryzen 5 3600 with Wraith Stealth Cooler (100-000000031) 3.6 GHz Upto 4.2 GHz AM4 Socket 6 Cores 12 Threads 3 MB L2 32 MB L3 Desktop Processor",
    "amd Ryzen 9 5900X 3.7 GHz Upto 4.8 GHz AM4 Socket 12 Cores 24 Threads Desktop Processor",
    "amd Ryzen 5 5600G 3.9 GHz Upto 4.4 GHz AM4 Socket 6 Cores 12 Threads 3 kB L2 16 kB L3 Desktop Processor"
    #"GIGASTAR 3.4 GHz LGA 1155 Intel i5-3570K For H61 Motherboard 3rd Generation Processor",
    #"Intel i5-12400F 4.4 GHz Upto 4.4 GHz LGA1700 Socket 6 Cores 12 Threads Desktop Processor"
]

# Iterate through the data and split into categories
for item in data:
    components = item.split()

    # if "width" found, either cooler or integrated graphics
    try:
        names.append(" ".join(components[:components.index("with"):1]))
        extra_component = " ".join(components[components.index("with") + 1: components.index("GHz") - 1:1])
        # Decide whether extra_component is a cooler or integrated graphics
        if extra_component.find("Graphics") != -1:
            integrated_graphics_list.append(extra_component)
            coolers.append("None")
        else:
            coolers.append(extra_component)
            integrated_graphics_list.append("None")
    except ValueError:
        names.append(" ".join(components[:components.index("GHz") - 1:1]))
        integrated_graphics_list.append("None")
        coolers.append("None")

    # Get "# GHz Upto # GHz", remove "GHz", replace "Upto" with "-"
    ghz_values.append((" ".join(components[components.index("GHz") - 1: components.index("Socket") - 1:1])
           .replace("GHz", "")).replace("Upto", "-"))

    sockets.append(components[components.index("Socket") - 1])
    cores.append(components[components.index("Cores") - 1])
    threads.append(components[components.index("Threads") - 1])
    processors.append(components[-2])

# Create a DataFrame
df = pd.DataFrame({
    'Name': names,
    'Integrated Graphics': integrated_graphics_list,
    'Cooler': coolers,
    'GHz': ghz_values,
    'Socket': sockets,
    'Cores': cores,
    'Threads': threads,
    'Processor': processors
})

# Display the DataFrame
print(df)
