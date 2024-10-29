from characters.models.table import Table  
from designs_patterns.factory.interfaces.i_factory import IFactory

class TableFactory(IFactory):
    def create(self) -> Table:
        """Cria uma instância de Table."""
        return Table()
