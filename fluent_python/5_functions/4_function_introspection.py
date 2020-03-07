def upper_case_name(obj):
    return ('%s %s' % (obj.first_name, obj.last_name)).upper()


upper_case_name.short_description = 'Customer name'

print(dir(upper_case_name))


class C(object):
    pass


objC = C()


def func():
    pass


diff = sorted(set(dir(func)) - set(dir(objC)))
print(diff)
