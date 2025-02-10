"""Time conversions"""

def fxn_min_to_us(minutes):

    """Get equivalent microseconds given minutes"""

    assert minutes >= 0

    #us = min * 60s/min * 1000 ms / s * 1000us/ms = 60*1000*1000 us
    us = minutes * 60 * 1000 * 1000

    return us