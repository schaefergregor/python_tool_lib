import htmlmin
import sys

html_file = open(sys.argv[1],"r")
html_content_arr = html_file.readlines()
html_content = "".join(html_content_arr)
print(html_content)

minified_html = htmlmin.minify(html_content, remove_empty_space=True)

print(minified_html)