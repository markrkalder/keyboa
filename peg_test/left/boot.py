from kmk.bootcfg import bootcfg

bootcfg(
    # required:
    sense: [microcontroller.Pin, digitalio.DigitalInOut],
    # optional:
    source: Optional[microcontroller.Pin, digitalio.DigitalInOut] = None,
    boot_device: int = 0,
    cdc_console: bool = True,
    cdc_data: bool = False,
    consumer_control: bool = True,
    keyboard: bool = True,
    midi: bool = False,
    mouse: bool = False,
    nkro: bool = False,
    pan: bool = False,
    storage: bool = True,
    usb_id: Optional[tuple[str, str]] = None,
    **kwargs,
) -> bool