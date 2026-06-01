#!/usr/bin/env python3

from migen import *
from litex_boards.platforms import vicara_vaaman

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores.led import LedChaser

class BaseSoC(SoCCore):
    def __init__(self, sys_clk_freq=25e6, **kwargs):
        platform = vicara_vaaman.Platform()
        SoCCore.__init__(self, platform, sys_clk_freq,
            ident          = "LiteX SoC on Vicara Vaaman",
            ident_version  = True,
            **kwargs
        )
        self.submodules.leds = LedChaser(
            pads         = platform.request_all("user_led"),
            sys_clk_freq = sys_clk_freq
        )

def main():
    from litex.soc.integration.soc import litex_soc_args, litex_soc_argdict
    from litex.build.parser import LiteXArgumentParser
    
    parser = LiteXArgumentParser(description="LiteX SoC on Vicara Vaaman")
    target_group = parser.add_argument_group(title="Target options")
    target_group.add_argument("--build", action="store_true", help="Build bitstream")
    
    builder_args(parser)
    soc_core_args(parser)
    args = parser.parse_args()

    soc = BaseSoC(**soc_core_argdict(args))
    builder = Builder(soc, **builder_argdict(args))
    if args.build:
        builder.build(run=True)

if __name__ == "__main__":
    main()
