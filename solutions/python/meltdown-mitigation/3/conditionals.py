"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    # Insert guard statement to check for false conditions first
    if temperature >= 800 or neutrons_emitted <=500:
        return False
    # assess if product is < 500000
    return (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    # define generated power
    generated_power = voltage * current

    # set up guard rail case
    if ((generated_power / theoretical_max_power) * 100) < 30:
        return 'black'
    # set up loop for other values
    if 30 <= ((generated_power / theoretical_max_power) * 100) < 60:
        return 'red'
    if 60 <= ((generated_power / theoretical_max_power) * 100) < 80:
        return 'orange'
    else :
        return 'green'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    # set up reactor criticality variable?
    reactor_criticality = neutrons_produced_per_second * temperature

    # max criticality
    max_criticality = threshold * 1.10

    #mix criticality
    min_criticality = threshold * .90

    # set up danger check - check that neutrons*temp is > 90% of threshold (product/threshold)*100
    if reactor_criticality > max_criticality:
        return 'DANGER'
    if min_criticality <= reactor_criticality <= max_criticality:
        return 'NORMAL'
    else:
        return 'LOW'
