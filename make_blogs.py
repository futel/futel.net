
import os
import re
from datetime import datetime

# util to convert the old _archive from tumblr into markdown

def write_md_header(filename, file):
  file.write('---\n')
  file.write('layout: post\n')
  file.write(f"permalink: /posts/{filename}\n")
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
        

def parse_title(lines):
  head_lines = list(filter(lambda x: '<h1>' in x, lines))
  if len(head_lines):
    line = head_lines[0]
    if line == '<h1></h1>':
      return ''
    return re.sub(r'.*<h1>(.*)</h1>', r'\1', head_lines[0])
  return '' # no headings

def convert_header(lines):
  def mangle(line):
    return re.sub(r'.*<h1>(.*)</h1>', r'# \1\n', line)
  return filter(lambda x: x != '# \n', map(mangle, lines))

def convert_paragraphs(content):
  content = re.sub(r'</p>', '\n\n', content)
  return re.sub(r'<p>', '', content)

def swizzle_images(lines):
  def mangle(line):
    return re.sub(r'img (alt="image" )?src="\.\./\.\./media', 'img src="/posts/images', line)
  return [mangle(line) for line in lines]

def find_date(lines):
  # <span id="timestamp"> December 11th, 2023 10:31pm </span>
  dateline = list(filter(lambda x: '<span id="timestamp"' in x, lines))[0]
  raw = re.sub(r'.*>(.*)</span>', r'\1', dateline).strip()
  raw = re.sub(r'(st|nd|th|rd), ', ', ', raw)
  print(f'  {raw}')
  return datetime.strptime(raw, '%B %d, %Y %I:%M%p')

def convert(src):
  with open(f'_archive/html/{src}', "rt") as file:
    lines = file.readlines()
  lines = get_body_content(lines)
  date = find_date(lines)
  lines = [x.strip() for x in lines]
  title = parse_title(lines)
  lines = convert_header(lines)
  lines = swizzle_images(lines)
  content = '\n'.join(lines)
  content = re.sub(r'^\n+', '\n', content)
  content = re.sub(r'\n\n+', '\n\n', content)
  content = convert_paragraphs(content)
  datestr = f"{datetime.strftime(date, '%Y%m%d%H%M')}"
  perma_filename = datestr
  print(f'  {datestr}.md')
  outfile = f'posts/{datestr}.md'
  if len(title):
    print(f'  title: {title}')
    title = re.sub(r"[ :?!|']", '_', title).lower()
    title = re.sub(r'_+', '_', title)
    perma_filename = f'{datestr}_{title}'
    outfile = f'posts/{perma_filename}.md'

  print(f'  -> {outfile}')
  with open(outfile, "wt") as out:
    write_md_header(perma_filename, out)
    out.write(content)
    out.write('\n')
    

files = [f for f in os.listdir('_archive/html') if os.path.isfile(f'_archive/html/{f}')]
# files = [f for f in files if os.path.isfile(f)]
for f in files:
  print(f"Converting {f}...")
  convert(f)
