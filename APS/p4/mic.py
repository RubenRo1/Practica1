import time
import math

from ulab import numpy as np
from ulab import utils
from machine import I2S

import net
import profiler

# wifi 
SSID = b'CONFIGURAR'
PWD = b'CONFIGURAR'

net = net.Net(SSID, '', PWD)
profiler = profiler.Profiler()

# bucle principal
while True:
    # queda en espera de los parámetros de captura a través de la red
    sample_rate, bsize, duration, h = net.get_mic_params()
    print(f'Solicitud: {sample_rate=} Hz; {bsize=} samples; {duration=} s, h=[{h[0]}...] ({len(h)} taps)')

    # inicializa I2S
    # ... COMPLETAR ...
    
    # descarta los primeros instantes (ruido)
    time.sleep(1)

    print("==========  COMENZANDO GRABACIÓN ==========")
    
    # bucle de lectura y procesado
    # ... COMPLETAR ...

    print("==========  GRABACIÓN FINALIZADA ==========")
    profiler.print_average()
    
    net.close()

