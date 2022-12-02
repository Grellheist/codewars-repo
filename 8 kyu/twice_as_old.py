def twice_as_old(dad_years_old, son_years_old):
    years = 0
    if (dad_years_old == 2*son_years_old):
        return 0
    else:
        # loop that checks future years
        years = dad_years_old - son_years_old
        if son_years_old - years > 0:
            return son_years_old - years
        elif son_years_old - years < 0:
            return years - son_years_old