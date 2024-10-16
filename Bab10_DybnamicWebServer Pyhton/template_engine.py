import re

def parse_template(text):
    delimiter = re.compile(r'{%(.*?)%}', re.DOTALL)
    tokens = []

    for index, token in enumerate(delimiter.split(text)):
        if index % 2 == 0:
            # Bagian bukan kode program, masukkan sebagai teks biasa
            if token:
                tokens.append((False, token))
        else:
            # Bagian kode program (Python)
            lines = token.splitlines()

            # Tentukan indentasi minimum dengan mengabaikan baris kosong
            indent = None
            for line in lines:
                if line.strip():
                    current_indent = len(line) - len(line.lstrip())
                    if indent is None or current_indent < indent:
                        indent = current_indent

            # Jika indentasi ditemukan, hilangkan indentasi
            realigned_lines = []
            for line in lines:
                if indent is not None and line.strip():
                    realigned_lines.append(line[indent:])
                else:
                    realigned_lines.append(line)

            realigned = '\n'.join(realigned_lines).strip()  # Hapus spasi kosong di awal dan akhir
            tokens.append((True, compile(realigned, '<template>', 'exec')))
    
    return tokens


def compile_template(tokens, context=None, **keyword_args):
    global_context = {}
    if context:
        global_context.update(context)
    if keyword_args:
        global_context.update(keyword_args)

    result = []

    def echo(*args):
        result.extend([str(arg) for arg in args])

    def echo_fmt(fmt, *args):
        result.append(fmt % args)

    global_context['echo'] = echo
    global_context['echo_fmt'] = echo_fmt

    for is_code, token in tokens:
        if is_code:
            exec(token, global_context)
        else:
            result.append(token)

    return ''.join(result)
