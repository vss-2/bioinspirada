import numpy as np

GENE_SIZE = 30
TAU = 1 / np.sqrt(GENE_SIZE)
TAU2 = 1 / np.sqrt(2 * GENE_SIZE)
TAU3 = 1 / np.sqrt(2 * np.sqrt(GENE_SIZE))
MIN_PACE = 1e-2

MAX_GERACAO = 10000