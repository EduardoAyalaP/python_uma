# Módulo de matemáticas financieras

def accum_value(c, irate, periods, yearly_payoff=1, itype="compound"):
    """
    Calcula el valor acumulado de una inversión inicial 'C'
    considerando una tasa anual 'irate' pagadera `yearly_payoff`
    veces al año y considerando una tasa de interés `itype`

    Parámetros
    ----------
    c: float
        inversión inicial
    irate: float
        tasa de interés anual
    periods: float
        número de períodos a considerar. Nota: si itype == 'simple',
        se considera periods como el tiempo de la inversión
    yearly_payoff: float
        número de veces de reinversión en un año
    itype: str ("compound" o "simple")
        tipo de inversión a considerar 


    Returns
    -------
    float:
        valor de la inversión acumulado después de `periods` períodos
    """
    if itype == "compound":
        return c * (1 + irate / yearly_payoff) ** (yearly_payoff * periods)
    elif itype == "simple":
        return c * (1 + irate * periods)

def present_value(c, irate, periods, yearly_payoff=1, itype="compound"):
    """
    Calcula el valor presente de una inversión inicial 'C'
    considerando una tasa anual 'irate' pagadera `yearly_payoff`
    veces al año y considerando una tasa de interés `itype`

    Parámetros
    ----------
    c: float
        inversión inicial
    irate: float
        tasa de interés anual
    periods: float
        número de períodos a considerar. Nota: si itype == 'simple',
        se considera periods como el tiempo de la inversión
    yearly_payoff: float
        número de veces de reinversión en un año
    itype: str ("compound" o "simple")
        tipo de inversión a considerar 


    Returns
    -------
    float:
        valor de la inversión presente después de `periods` períodos
    """
    if itype == "compound":
        return c / (1 + irate / yearly_payoff) ** (yearly_payoff * periods)
    elif itype == "simple":
        return c / (1 + irate * periods)


def rate_converter(rate, yearly_payoff, base):
    """
    Convierte una tasa nominal pagadera 'yearly_payoff'
    al año, por una tasa anual efectiva

    Parameters
    ----------
    rate: Una tasa convertir
    yearly_payoff: el número de veces en el que se reinvierte la tasa nominal
    base: str ("nominal" ^ "effective")
        La base 

    Returns
    -------
    Una tasa convertida
    """
    if base == "nominal":
        return (1 + rate) ** yearly_payoff - 1
    elif base == "effective":
        return yearly_payoff * ((1 + rate) ** (1 / yearly_payoff) - 1)
