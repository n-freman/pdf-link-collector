import sys
import re
from pprint import pprint

from pypdf import PdfReader

from file_path_validators import FilePathValidationError, does_exist, is_pdf

try:
    file_path = sys.argv[1]
except IndexError:
    print('You should provide path to .pdf file as cli argument')
    exit()


validators = [does_exist, is_pdf]
for validator in validators:
    try:
        validator(file_path)
    except FilePathValidationError as e:
        print(e)
        exit()


reader = PdfReader(file_path)
number_of_pages = len(reader.pages)

pattern = r'\w+:/? /[\w\.\/\-]+'
urls = []
filename = file_path.split("/")[-1]

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    matches = re.findall(pattern, text)
    matches = list(map(lambda x: x.replace(' ', ''), matches))
    if len(matches) == 0:
        continue
    print(f'{i}: {len(page.extract_text())}')
    pprint(matches)
    urls.extend(matches)

print(f'Found {len(urls)} links in the [{filename}]')

with open(f'links_{filename}', 'w') as file:
    for url in urls:
        file.write(f'{url}\n')

