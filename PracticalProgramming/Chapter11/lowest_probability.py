def lowest_probability(particles):
    '''
    (dict) -> string

    Returns the particle with the lowest probably in
    the dictionary particles.

    >>> lowest_probability({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03})
    meson
    '''

    return min(particles, key=particles.get)
