from datetime import datetime

def fecha():
    ahora = datetime.now()
    return ahora.strftime("%Y/%m/%d  %H:%M:$S")