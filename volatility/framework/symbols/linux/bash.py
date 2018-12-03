from volatility.framework.symbols import intermed
from volatility.framework.symbols.linux.extensions import bash

class BashIntermedSymbols(intermed.IntermediateSymbolTable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_type_class('_hist_entry', bash._hist_entry)

