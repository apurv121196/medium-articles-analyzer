import sys
import textract
import re
query = sys.argv[1]
data = str(textract.process(f'./{query}/docs/{query}.pdf')[2:-1])
data = re.compile(r'\x..').sub(r'', data)
f = open(f'./{query}/docs/{query}.html', 'w')
f.write(data)
f.close()