
import os
import re

def write_md_header(src, file):
  file.write('---\n')
  file.write('layout: blog\n')
  file.write(f"permalink: /blog/{src.replace('.html', '')}\n")
  file.write('---\n')

def get_body_content(lines):
  in_body = False
  out = []
  for line in lines:
    if in_body:
      if re.match(r'\s*</body>', line):
        in_body = False
      else:
        out.append(line)
    else:
      if re.match(r'\s*<body>', line):
        in_body = True
  return out
        

def convert_header(lines):
  def mangle(line):
    return re.sub(r'<h1>(.*)</h1>', r'# \1\n', line)
  return filter(lambda x: x != '# \n', map(mangle, lines))

def parse_date(lines):
  pass

def convert_paragraphs(content):
  content = re.sub(r'</p>', '\n\n', content)
  return re.sub(r'<p>', '', content)

def convert(src):
  with open(f'_archive/html/{src}', "rt") as file:
    lines = file.readlines()
  outfile = f"blog/{src.replace('html', 'md')}"
  with open(outfile, "wt") as out:
    write_md_header(src, out)
    lines = get_body_content(lines)
    lines = [x.strip() for x in lines]
    lines = convert_header(lines)
    content = '\n'.join(lines)
    content = re.sub(r'^\n+', '\n', content)
    content = re.sub(r'\n\n+', '\n\n', content)
    content = convert_paragraphs(content)
    out.write(content)
    out.write('\n')
    

files = [f for f in os.listdir('_archive/html') if os.path.isfile(f'_archive/html/{f}')]
# files = [f for f in files if os.path.isfile(f)]
for f in files:
  print(f"Converting {f}...")
  convert(f)
