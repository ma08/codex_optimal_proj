def time_conversion(time_str):
    h1, m1 = time_str.split(':')


    h1 = int(h1)
    m1 = int(m1)

    if m1 == 0:
        return str(h1).zfill(2) + ':' + str(m1).zfill(2)
    elif h1 == 23:
        return '00:' + str(m1).zfill(2)
    else:
        return str(h1 + 1).zfill(2) + ':' + str(m1).zfill(2)


if __name__ == '__main__':
    print(time_conversion('00:00'))
    print(time_conversion('01:30'))
    print(time_conversion('12:05'))
    print(time_conversion('14:01'))
    print(time_conversion('20:29'))
    print(time_conversion('21:00'))
