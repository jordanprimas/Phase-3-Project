class Library:
    def __init__(self, name, address):
        self.name = name 
        self.address = address

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self):
        if isinstance(name, str) and len(name):
            self._name = name 
        else:
            raise ValueError(
                "Name must be a string with at least 1 character."
            )

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, (str, int)) and len(address):
            self._address = address
        else:
            raise ValueError(
                "Address must be a string or integer with at least 1 character."
            )
