# СТАВКИ
desired_rate = None  # желаемая ставка (руб/рейс)
proposed_rate = None  # предлагаемая ставка (руб/рейс)
desired_rate_RK = None  # желаемая ставка (руб/км)
proposed_rate_RK = None  # предлагаемая ставка (руб/км)

# РАСХОДНИКИ
# шины
tire_mileage = int()  # пробег шин (км)
tire_price = int()  # цена одной покрышки (руб)
tire_size = int()  # кол-во шин в комплекте на машину с прицепом (шт)


def tire_consumption(a=250000, b=20000, c=16):
    '''Возвращает амортизацию шин в рублях.
    a - tire_mileage
    b - tire_price
    c - tire_size
    '''
    result = b * c / a
    return result


# топливо
fuel_price = float()  # цена на дизель (руб/литр)
fuel_intake = float()  # расход топлива (литр/100км)


def fuel_consum(a=49, b=38):
    '''Возвращает расход топлива на км в рублях.
    a - fuel_price
    b - fuel_intake'''
    result = a * b / 100
    return result


# масло
motor_oil_price = float()  # цена моторного масла (руб/литр)
motor_oil_consum = float()  # расход масла (литр/100км)
motor_oil_mileage = int()  # пробег до смены масла (км)
motor_pil_space = float()  # ёмкость


def oil_consumption(a=500, b=0.05, c=100000, d=25):
    '''Возвращает расход масла на километр в рублях.
    a - motor_oil_price
    b - motor_oil_consum
    c - motor_oil_mileage
    d - motor_pil_space'''
    b += (d / c)
    e = b * a
    return e


# ЗАРПЛАТА
driver_salary = None  # заработная плата водителя (руб/км)
daily_allowance = None  # суточные (руб/сутки)

# НАЛОГИ
nds_rate = int(20)  # ставка НДС (%)
toll_roads = None  # ПЛАТОН, платные дороги (руб/км)

# ПРОЧЕЕ
other_expenses = None  # прочие расходы (руб)
daily_mileage = None  # суточный пробег input(км/сут)
