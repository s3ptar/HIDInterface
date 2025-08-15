########################################################################
#! \file:                   application.c
#  \projekt:                openbot
#  \created on:             2025 03 01
#  \author:                 R. Gräber
#  \version:                0
#  \history:                -
#  \brief
########################################################################


########################################################################
# Includes
########################################################################
import neopixel
import machine
import time
import ujson
import logging
########################################################################
# Informations
########################################################################
##https:##os.mbed.com#platforms#FRDM-K64F##board-pinout
########################################################################
# Declarations
########################################################################
np = neopixel.NeoPixel(machine.Pin(39), 1)
np_power = machine.Pin(38, machine.Pin.OUT)
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)  # DEBUG, INFO, WARNING, ERROR
########################################################################
# Constant
########################################################################


########################################################################
# Global Variable
########################################################################


########################################################################
# local Variable
########################################################################


########################################################################
# Constant
########################################################################

########################################################################
# Local Funtions
########################################################################
def log(level_name, msg):
    # level_name: "INFO", "ERROR", ...
    getattr(logger, level_name.lower())(f"{ts()} [{level_name}] {msg}")

    
# Optional: eigenes Format (einfach gehalten)
def ts():
    # Falls keine RTC-Zeit vorhanden ist, notfalls ticks_ms nutzen
    try:
        y, m, d, hh, mm, ss, *_ = time.localtime()
        return f"{y:04d}-{m:02d}-{d:02d} {hh:02d}:{mm:02d}:{ss:02d}"
    except:
        return f"t+{time.ticks_ms()}ms"

########################################################################
#! \fn          int main(){
#  \brief       start up function
#  \param       none
#  \exception   none
#  \return      none
########################################################################
if __name__ == "__main__":
    log("DEBUG", "Programm start")
    np_power.value(1)
    var = "bla"
    print(f"lets go: {var}")

    configfile = open("config.json", "r")
    configfile_content = configfile.read()
    configfile.close()
    configfile_dict = ujson.loads(configfile_content)    
    
    while True:
        np[0] = (255, 0, 0, 128) # Orange in an RGBY Setup
        np.write()
        time.sleep(1)
        np[0] = (0, 0, 0, 0) # Orange in an RGBY Setup
        np.write()
        time.sleep(1)

    
