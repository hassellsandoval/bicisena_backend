from enum import Enum as PyEnum

class Metodo_Pago(PyEnum):
    BILLETERA_DIGITAL = "BILLETERA_DIGITAL"
    TARJETA_CREDITO = "TARJETA_CREDITO"
    TARJETA_DEBITO = "TARJETA_DEBITO"
    CONSIGNACION = "CONSIGNACION"
    EFECTIVO = "EFECTIVO"  
