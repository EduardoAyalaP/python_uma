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


