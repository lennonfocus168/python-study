<<<<<<< HEAD
=======
from optparse import OptionParser

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Referer', 'http//acm.fzu.edu.cn/login.php?dir=L2luZGV4LnBocA=='),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'acm.fzu.edu.cn'), ('Origin', 'http//acm.fzu.edu.cn'), ('Upgrade-Insecure-Requests', ' 1'),
           ('Cookie', 'FASAST=7vbtpgjviv872vsg60me6n8086')]

import re

text = "iioodffeeeeris"
m = re.search(r'(..)*', text)

from optparse import OptionParser


def main():
    p = OptionParser()
    p.add_option('-n', '--name', dest='person_name', help='person\'s name', default='person1')
    p.add_option('-a', '--age', default=30, help='person\'s age')
    p.add_option('-j', '--job', default='software engineer', help='person\'s job')
    options, args = p.parse_args()
    print('Hello %s' % options.person_name, ', age is %d' % int(options.age), ',job is %s' % options.job)
    print(args)
    print(p.print_help())


if __name__ == '__main__':
    main()
>>>>>>> master
