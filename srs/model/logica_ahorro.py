class MetaInvalida(Exception):
    """ Se dispara cuando la meta de ahorro es menor o igual a cero """

class PlazoInvalido(Exception):
    """ Se dispara cuando el plazo es cero o negativo """

class InteresInvalido(Exception):
    """ Se dispara cuando la tasa de interés es negativa """

class MesAbonoInvalido(Exception):
    """ Se dispara cuando el mes del abono está fuera del rango del plazo """

def calcular_cuota(meta, interes, plazo, abono=0, mes_abono=None):
    """
    Calcula la cuota periódica necesaria para alcanzar una meta de ahorro.
    Utiliza la fórmula de anualidad ordinaria para determinar el pago regular
    requerido. Permite aplicar un abono adicional en un mes específico.
    
    Args:
        meta (float): Cantidad objetivo a ahorrar.
        interes (float): Tasa de interés periódica en decimal.
        plazo (int): Número de períodos en meses.
        abono (float, optional): Abono adicional. Por defecto es 0.
        mes_abono (int, optional): Mes del abono. Por defecto es None.
    
    Returns:
        float: Cuota periódica necesaria para alcanzar la meta.

    Raises:
        Exception: Si meta es menor o igual a cero.
        Exception: Si plazo es cero.
        Exception: Si interes es negativa.
        Exception: Si plazo es negativo.
    
    """
    #### RETORNAR UN ERROR
    if meta <= 0:
        raise MetaInvalida(f"ERROR: La meta debe ser mayor que cero. Se recibió meta={meta}. Ingrese un valor positivo.")
    
    if  plazo == 0:
        raise PlazoInvalido(f"ERROR: El plazo no puede ser cero. Se recibió plazo={plazo}. Ingrese un plazo de al menos 1 mes.")
    
    if  interes < 0:
        raise InteresInvalido(f"ERROR: La tasa de interés no puede ser negativa. Se recibió interes={interes}. Ingrese una tasa mayor o igual a cero.")

    if plazo < 0:
        raise PlazoInvalido(f"ERROR: El plazo no puede ser negativo. Se recibió plazo={plazo}. Ingrese un plazo de al menos 1 mes.")

    if interes == 0:
        if abono > 0 and mes_abono is not None:
            meta = meta - abono
        return meta / plazo

    
    if abono > 0 and mes_abono is not None:
        if mes_abono < 1 or mes_abono > plazo:
            raise MesAbonoInvalido(f"ERROR: El mes del abono no es válido. Se recibió mes_abono={mes_abono} con plazo={plazo}. El mes debe estar entre 1 y {plazo}.")
        meta = meta - abono

    return meta * (interes / ((1 + interes) ** plazo - 1))

def calcular_total_interes(meta, interes, plazo, abono=0, mes_abono=None):
    cuota = calcular_cuota(meta, interes, plazo, abono, mes_abono)
    if abono > 0 and mes_abono is not None:
        return (meta - abono) - cuota * plazo
    return meta - cuota * plazo

