try:
    import egttools
except ImportError as e:
    print('egttools is not installed')
else:
    print('found egttools')
    print('Numerical module in: {}'.format(egttools.numerical))
