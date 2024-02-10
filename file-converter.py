import markdown
import sys

l = sys.argv
md_text = l[2]
html_output = l[3]

if len(l) != 4 or md_text[-3:] != ".md" or html_output[-5:] != ".html" or l[1] != "markdown":
   print("Error! Please input your command in the right way referencing README.md.")

def contents(pathname):
    with open(pathname) as f:
        contents =f.read()
    return contents

content = contents(md_text)
html = markdown.markdown(content)

with open(html_output, "w") as f:
    f.write(html)