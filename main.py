
#SES KAYIT
import numpy as np
from recorder import Recorder

r = Recorder()
r.record(15, output='Out.wav')

Recorder.play("Out.wav")
r.close()
