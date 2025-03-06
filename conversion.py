ONE_DAY_IN_SECONDS = 86_400


def acre_feet_to_m3(volume_acre_feet):
    """Converts volume in US acre-feet to SI m³."""
    volume_m3 = volume_acre_feet * 1_233
    return volume_m3

def cms_to_cfs(flow_cms):
    """Converts flow rate in cubic feet per second to cubic metres per second."""
    flow_cfs = flow_cms * 35.3146662
    return flow_cfs
