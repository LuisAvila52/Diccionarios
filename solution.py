from typing import Tuple

db = set()
def almacenar_orden(orden: Tuple[str, ...]) -> bool:
    if orden in db:
        return False
    else:
        db.add(orden)
    return True