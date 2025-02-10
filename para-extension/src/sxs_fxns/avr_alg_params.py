"""AVR Task Demand algorithm parameters"""

class AvrAlgParams:

    """Generic interface for AVR Task Demand algorithm parameters"""

    def __init__(self,precision,memoize,give_sln_seq,trace_memory,apx_params,n_cores,parallelization_type):

        self.update_params(precision,memoize,give_sln_seq,trace_memory,apx_params,n_cores,parallelization_type)

    def update_params(self,precision,memoize,give_sln_seq,trace_memory,apx_params,n_cores,parallelization_type):

        """Update algorithm parameters"""

        self.precision = precision
        self.memoize = memoize
        self.give_sln_seq = give_sln_seq
        self.trace_memory = trace_memory
        self.apx_params = apx_params
        self.n_cores = n_cores
        self.parallelization_type = parallelization_type
