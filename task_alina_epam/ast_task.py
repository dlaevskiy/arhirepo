import ast


def recurse(node):
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
            print('(')
        recurse(node.left)
        recurse(node.op)
        recurse(node.right)
        if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
            print(')')
    elif isinstance(node, ast.Add):
        print('+')
    elif isinstance(node, ast.Sub):
        print('-')
    elif isinstance(node, ast.Mult):
        print('*')
    elif isinstance(node, ast.Div):
        print('/')
    elif isinstance(node, ast.Num):
        print(node.n)
    elif isinstance(node, ast.Call):
        print(node.func.id)
    else:
        for child in ast.iter_child_nodes(node):
            recurse(child)


def search_expr(node):
    returns = []
    for child in ast.iter_child_nodes(node):
        if isinstance(child, ast.Expr):
            return child
        returns.append(search_expr(child))
    for ret in returns:
        if isinstance(ret, ast.Expr):
            return ret
    return None


formula = 'sin(7)'

a = ast.parse(formula)

expr = search_expr(a)

if expr is not None:
    recurse(expr)
