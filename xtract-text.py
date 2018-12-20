import sys
import textract
import re
import codecs
query = sys.argv[1]
data = str(textract.process(f'./{query}/docs/{query}.pdf'))[2:-1]
# codecs.decode(data, 'unicode_escape')
data = re.compile(r'\\x..').sub(r'', data).replace("\\n", "\n").replace('\\t', '\t')
# data = re.sub(r"\\", "", data)
# data = ''.join(data.split('\\'))
f = open(f'./{query}/docs/{query}.html', 'w')
f.write(data)
f.close()