class Vector:
    def __init__(self, *components):
        self.components = components
 
    def __repr__(self):
        return f'Vector{self.components}'