from converter.markdown_converter import MarkdownConverter

md = """
# Hello World

This is **bold** and *italic* text.

## List
- Item one
- Item two

```python
print("Hello")

"""

converter = MarkdownConverter(md)
html = converter.convert()

print(html)