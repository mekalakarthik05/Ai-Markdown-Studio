import re


class MarkdownConverter:
    def __init__(self, markdown_text: str):
        self.markdown_text = markdown_text

    def convert_code_blocks(self, text: str) -> str:
        return re.sub(
            r'```(.*?)```',
            r'<pre><code>\1</code></pre>',
            text,
            flags=re.DOTALL
        )

    # 2️⃣ Headers (# to ######)
    def convert_headers(self, text: str) -> str:
        patterns = [
            (r'^###### (.*)', r'<h6>\1</h6>'),
            (r'^##### (.*)', r'<h5>\1</h5>'),
            (r'^#### (.*)', r'<h4>\1</h4>'),
            (r'^### (.*)', r'<h3>\1</h3>'),
            (r'^## (.*)', r'<h2>\1</h2>'),
            (r'^# (.*)', r'<h1>\1</h1>')
        ]

        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text, flags=re.MULTILINE)

        return text

    def convert_inline(self, text: str) -> str:
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
        text = re.sub(
            r'\[(.*?)\]\((.*?)\)',
            r'<a href="\2">\1</a>',
            text
        )
        return text


    def convert_lists(self, text: str) -> str:
        lines = text.split('\n')
        html_lines = []
        in_list = False

        for line in lines:
            if line.startswith('- '):
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                html_lines.append(f'<li>{line[2:]}</li>')
            else:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                if line.strip():
                    html_lines.append(f'<p>{line}</p>')

        if in_list:
            html_lines.append('</ul>')

        return '\n'.join(html_lines)

    def convert(self) -> str:
        text = self.markdown_text
        text = self.convert_code_blocks(text)
        text = self.convert_headers(text)
        text = self.convert_inline(text)
        text = self.convert_lists(text)
        return text
