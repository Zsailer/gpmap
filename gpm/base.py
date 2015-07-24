# Base class for all maps in this a genotype-phenotype map.
#
# Author: Zach Sailer
#
# -------------------------------------
# Outside imports
# -------------------------------------
import numpy as np
from collections import OrderedDict

# -------------------------------------
# Main class for building epistasis map
# -------------------------------------

class BaseMap:
    """
        Base class for all maps in this file. 
    """
    def _map(self, keys, values):
        """ Return ordered dictionary mapping two properties in self. """
        return OrderedDict([(keys[i], values[i]) for i in range(len(keys))])
        
    def _if_dict(self, dictionary):
        """ If setter method is passed a dictionary with genotypes as keys, 
            use those keys to populate array of elements in order
        """
        elements = np.empty(self._n, dtype=float)
        for i in range(self._n):
            elements[i] = dictionary[self._genotypes[i]]
        return elements