def tag(name, *content, cls=None, **attrs):
    """"Generation one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        result = '\n'.join('<%s %s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        result = '<%s%s />' % (name, attr_str)
    return result


print(tag('amt', '1.00', cur='RUB'))
print(tag.__defaults__)
print(tag.__kwdefaults__)
print(tag.__code__)
print(tag.__code__.co_varnames)
print(tag.__code__.co_argcount)  # count only name

