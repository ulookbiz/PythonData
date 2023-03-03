# Класс "Sound"
#  выполняет различные звуковые сигналы
import winsound

class Sound():

# --------------------------------
#   Инициализатор
    def __init__(self):

        return

# --------------------------------
#   Сигнал окончания работы
    def finish(self):
    
        frequency = 2000  # Set Frequency To 2500 Hertz
        duration = 100  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        frequency = 1000  # Set Frequency To 2500 Hertz
        duration = 300  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        return

# --------------------------------
#   Сигнал о событии
    def event(self):
    
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 300  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        frequency = 2000  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 100  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        return