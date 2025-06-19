def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''
    Output a list of BMIs
    '''
    try:
        if len(height) != len(weight):
            raise ValueError("ValueError: both lists aren't the same size")
        bmi = []
        for i in range(len(height)):
            bmi.append((float(weight[i]) / (float(height[i]) ** 2)))
        return bmi
    except ValueError as e:
        print(e)
    return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    Output a list of boolean
    '''
    try:
        return list(float(b) > int(limit) for b in bmi)
    except ValueError as e:
        print(e)
    return None
