from alfred_utils.feedback import Feedback
import urllib
import json
import sys

query = sys.argv[1]
url = 'http://sunrinwiki.layer7.kr/api.php?action=opensearch&search=%s' % query
response = json.load(urllib.urlopen(url))

fb = Feedback()
for title in response[1]:
    url = 'sunrinwiki.layer7.kr/index.php/%s' % title
    url.replace(' ', '_')
    fb.add_item(title,
        subtitle="Read sunrinwiki article on %s" % title,
        arg=title.replace(" ", "_"))
print fb