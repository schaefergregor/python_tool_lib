import markdownify
import sys

html_file = open(sys.argv[1],"r")
html_content_arr = html_file.readlines()
html_content = "".join(html_content_arr)
print(html_content)

markdown_content = markdownify.markdownify(html_content, heading_style="ATX")
print(markdown_content)