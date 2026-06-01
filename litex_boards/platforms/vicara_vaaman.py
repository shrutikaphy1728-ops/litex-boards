#
# This file is part of LiteX-Boards.
#
# Master Platform Constraint File for the Vicara Vaaman Board (Rev 0.3)
# Base Pin Mappings compiled from official Vicharak Hardware Documentation.

from litex.build.generic_platform import *
from litex.build.efinix import EfinixPlatform

# I/O Pins -----------------------------------------------------------------------------------------

_io = [
    # --- Onboard FPGA Dedicated Clock Oscillators ---
    ("clk25",     0, Pins("F10"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("clk50",     0, Pins("U8"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("clk30",     0, Pins("L14"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("clk20",     0, Pins("D9"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("clk74_25",  0, Pins("C9"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("clk10",     0, Pins("R8"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")), 

    # --- Default Debug Serial Port ---
    ("serial", 0,
        Subsignal("tx", Pins("A10")), 
        Subsignal("rx", Pins("B10")), 
        IOStandard("3.3_V_LVTTL_/_LVCMOS")
    ),

    # --- Onboard FPGA Hardware Status/User LEDs ---
    ("user_led", 0, Pins("A12"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("user_led", 1, Pins("B12"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("user_led", 2, Pins("A11"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("user_led", 3, Pins("B11"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 

    # --- Complete FPGA 40-Pin GPIO Header Array ---
    ("fpga_header_gpio", 0,  Pins("H13"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), # Header Pin 07 
    ("fpga_header_gpio", 1,  Pins("G13"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), # Header Pin 08 
    
    # -----------------------------------------------------------------
    # DEDICATED SERIAL PROTOCOLS (Replacing generic GPIOs 2 through 7)
    # -----------------------------------------------------------------
    ("spi", 0,
        Subsignal("clk",  Pins("G5")), 
        Subsignal("mosi", Pins("H14")), 
        Subsignal("miso", Pins("G6")), 
        Subsignal("cs_n", Pins("H6")),  
        IOStandard("3.3_V_LVTTL_/_LVCMOS")
    ),
    
    ("i2c", 0,
        Subsignal("scl", Pins("K6")),  
        Subsignal("sda", Pins("K15")),  
        IOStandard("3.3_V_LVTTL_/_LVCMOS")
    ),
    # -----------------------------------------------------------------

    ("winbond_cs", 0, Pins("A9"), IOStandard("3.3_V_LVTTL_/_LVCMOS")),
    
    ("fpga_header_gpio", 9,  Pins("B9"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")),
    ("fpga_header_gpio", 10, Pins("L16"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("fpga_header_gpio", 11, Pins("E9"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("fpga_header_gpio", 12, Pins("T8"),  IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("fpga_header_gpio", 13, Pins("L15"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
    ("fpga_header_gpio", 14, Pins("L17"), IOStandard("3.3_V_LVTTL_/_LVCMOS")),  
    ("fpga_header_gpio", 15, Pins("L18"), IOStandard("3.3_V_LVTTL_/_LVCMOS")),
    ("fpga_header_gpio", 16, Pins("K17"), IOStandard("3.3_V_LVTTL_/_LVCMOS")),
    ("fpga_header_gpio", 17, Pins("M18"), IOStandard("3.3_V_LVTTL_/_LVCMOS")),
    ("fpga_header_gpio", 18, Pins("K16"), IOStandard("3.3_V_LVTTL_/_LVCMOS")), 
]

# Platform Configuration ---------------------------------------------------------------------------

class Platform(EfinixPlatform):
    default_clk_name   = "clk10"
    default_clk_period = 1e9 / 10e6 

    def __init__(self):
        EfinixPlatform.__init__(
            self,
            device      = "T120F324C3", 
            io          = _io,
            toolchain   = "efinity"
        )
        self.iobank_info = []
