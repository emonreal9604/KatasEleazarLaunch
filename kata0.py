
from sys import displayhook
from ipywidgets import IntSlider
import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
data = np.random.default_rng(12345)
oxy_nums = data.integers(low=0, high=10, size=10)

plt.bar(range(len(oxy_nums)), oxy_nums)
plt.show()
endVelocity = 11200
startVelocity = 0
acceleration = 9.8

time = (endVelocity - startVelocity) / acceleration
print("Tiempo para alcanzar la velocidad deseada = ", time)

ignition = widgets.ToggleButton(
    value=False,
    description='Iniciar Launch',
    button_style='success',
    tooltip='Engage your Launch',
    icon='rocket'
)

output = widgets.Output()

displayhook(ignition, output)


def on_value_change(change):
    with output:
        if change['new'] == True:
            print("Nave Iniciada!")
        else:
            print("Nave Detenida")


ignition.observe(on_value_change, names='value')
