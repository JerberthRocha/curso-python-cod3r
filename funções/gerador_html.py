# def tag_bloco(texto, classe='success'):
#     return f'<div class="{classe}">{texto}</div>'

# if __name__ == '__main__':
#     print(tag_bloco('Bloco'))

# def tag_bloco(texto, classe='success', inline=False):
#     tag = 'span' if inline else 'div'
#     return f'<{tag} class="{classe}">{texto}</{tag}>'

# if __name__ == '__main__':
#     print(tag_bloco('Bloco'))
#     print(tag_bloco('Inline e classe', 'Info', True))

def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'

def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco('Bloco'))
    print(tag_bloco('Inline e classe', 'Info', True))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='Info'))