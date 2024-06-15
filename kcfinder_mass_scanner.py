#!/usr/bin/python
# -*- coding: utf-8 -*
# Scanner KCfinder Python2
# Youtube : Smile Of Beauty 
# Blog : https://www.blog-gan.org
#####################################

import requests
import os
import sys
import random
from multiprocessing.dummy import Pool
from time import time as timer
import time
from colorama import Fore, Style, init
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf8')
init(autoreset=True)

abang = Fore.RED
ijo = Fore.GREEN
putih = Fore.WHITE
biru = Fore.BLUE
kuning = Fore.YELLOW
mbohopo = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
              Mass Scanner KCfinder - Jamet31337
                  Ajibarang - 29 DECEMBER 2K20
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


cls()
print_logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")

try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
    pass

try:
    ooo = list((ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()

count = 0
with open(start_raw, 'r') as f:
    for line in f:
        count += 1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=', count


def kcfinder(url):
    try:
        head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'}
        ajg = [
            'ckeditor/kcfinder/upload.php', 
            'kcfinder/upload.php', 
            'assets/kcfinder/upload.php', 
            'webboard/plugins/editors/kcfinder/upload.php', 
            'admin/editor/kcfinder/upload.php', 
            'ckeditor/plugins/kcfinder/upload.php', 
            'admin-panel/vendor/kcfinder/upload.php', 
            'assets/plugin/kcfinder/upload.php', 
            'plugins/kcfinder/upload.php', 
            'admin/kcfinder/upload.php', 
            'vendor/kcfinder/upload.php', 
            'painel/kcfinder/upload.php', 
            'panel/kcfinder/upload.php', 
            'yonetim/engine/ckeditor/kcfinder/upload.php', 
            'assets/admin/js/kcfinder/upload.php', 
            'js/kcfinder/upload.php',
            'upload/kcfinder/upload.php',
            'site/plugins/kcfinder/upload.php',
            'assets/js/kcfinder/upload.php',
            'app/libraries/kcfinder/upload.php',
            'modules/kcfinder/upload.php',
            'lib/kcfinder/upload.php',
            'uploads/kcfinder/upload.php',
            'storage/app/kcfinder/upload.php',
            'inc/kcfinder/upload.php',
            'assets/ckeditor/kcfinder/upload.php',
            'resources/kcfinder/upload.php',
            'modules/admin/editor/kcfinder/upload.php',
            'system/kcfinder/upload.php',
            'assets/admin/plugins/kcfinder/upload.php',
            'en/kcfinder/upload.php',
            'plugin/ckeditor/kcfinder/upload.php',
            'data/kcfinder/upload.php',
            'core/kcfinder/upload.php',
            'files/kcfinder/upload.php',
            'admin/public/kcfinder/upload.php',
            'media/kcfinder/upload.php',
            'modules/ckeditor/kcfinder/upload.php',
            'plugin/kcfinder/upload.php',
            'system/libraries/kcfinder/upload.php',
            'foo/kcfinder/upload.php',
            'bar/kcfinder/upload.php',
            'test/kcfinder/upload.php',
            'tmp/kcfinder/upload.php',
            'secret/kcfinder/upload.php',
            'logs/kcfinder/upload.php',
            'config/kcfinder/upload.php',
            'private/kcfinder/upload.php',
            'data/uploads/kcfinder/upload.php',
            'images/kcfinder/upload.php',
            'uploads/cache/kcfinder/upload.php',
            'assets/css/kcfinder/upload.php',
            'upload/images/kcfinder/upload.php',
            'img/kcfinder/upload.php',
            'filemanager/kcfinder/upload.php',
            'storage/kcfinder/upload.php',
            'uploads/files/kcfinder/upload.php',
            'gallery/kcfinder/upload.php',
            'vendor/assets/kcfinder/upload.php',
            'uploads/images/kcfinder/upload.php',
            'files/docs/kcfinder/upload.php',
            'config/config.kcfinder/upload.php',
            'assets/kcfinder/src/',
            'data/files/kcfinder/upload.php',
            'includes/kcfinder/upload.php',
            'resources/views/kcfinder/upload.php',
            'upload/files/kcfinder/upload.php',
            'cache/kcfinder/upload.php',
            'uploads/uploadfiles/kcfinder/upload.php',
            'library/kcfinder/upload.php',
            'system/assets/kcfinder/upload.php',
            'js/ckeditor/kcfinder/upload.php',
            'data/upload/kcfinder/upload.php',
            'tmp/cache/kcfinder/upload.php',
            'lib/ckeditor/kcfinder/upload.php',
            'data/file/kcfinder/upload.php',
            'js/libs/kcfinder/upload.php',
            'files/data/kcfinder/upload.php',
            'css/kcfinder/upload.php',
            'plugins/ckeditor/kcfinder/upload.php',
            'upload/images/uploads/kcfinder/upload.php',
            'site/ckeditor/kcfinder/upload.php',
            'assets/css/admin/kcfinder/upload.php',
            'uploads/uploads/kcfinder/upload.php',
            'public/kcfinder/upload.php',
            'upload/uploads/kcfinder/upload.php',
            'cache/images/kcfinder/upload.php',
            'app/assets/kcfinder/upload.php',
            'assets/cms/kcfinder/upload.php',
            'uploads/uploads/uploads/kcfinder/upload.php',
            'css/admin/kcfinder/upload.php',
            'uploads/files/files/kcfinder/upload.php',
            'upload/images/images/kcfinder/upload.php',
            'uploads/data/kcfinder/upload.php',
            'uploads/images/upload/kcfinder/upload.php',
            'uploads/images/files/kcfinder/upload.php',
            'uploads/data/files/kcfinder/upload.php',
            'ckeditor/kcfinder/upload.phpkcfinder/upload.php',
            'assets/kcfinder/upload.phpckeditor/',
            'uploads/upload/kcfinder/upload.php',
            'fileuploads/kcfinder/upload.php',
            'uploads/images/images/uploads/kcfinder/upload.php',
            'uploads/upload/upload/kcfinder/upload.php',
            'uploads/files/uploads/kcfinder/upload.php',
            'assets/ckeditor/plugins/kcfinder/upload.php',
            'uploads/images/upload/images/kcfinder/upload.php',
            'uploads/images/files/uploads/kcfinder/upload.php',
            'uploads/images/uploadfiles/kcfinder/upload.php',
            'uploads/files/upload/images/kcfinder/upload.php',
            'uploads/images/files/upload/kcfinder/upload.php',
            '/admin/ckeditor/kcfinder-3.12/upload.php',
            '/admin/ckeditor/kcfinder/upload.php',
            '/admin/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/admin/ckeditor/plugins/kcfinder/upload.php',
            '/admin/core/kcfinder-3.12/upload.php',
            '/admin/core/kcfinder/upload.php',
            '/admin/js/kcfinder-3.12/upload.php',
            '/admin/js/kcfinder/upload.php',
            '/admin/plugin/kcfinder-3.12/upload.php',
            '/admin/plugin/kcfinder/upload.php',
            '/admin/plugins/kcfinder-3.12/upload.php',
            '/admin/plugins/kcfinder/upload.php',
            '/adminpanel/kcfinder-3.12/upload.php',
            '/adminpanel/kcfinder/upload.php',
            '/app/webroot/js/kcfinder-3.12/upload.php',
            '/app/webroot/js/kcfinder/upload.php',
            '/app/webroot/kcfinder-3.12/upload.php',
            '/app/webroot/kcfinder/upload.php',
            '/application/themes/admin/assets/js/kcfinder-3.12/upload.php',
            '/application/themes/admin/assets/js/kcfinder/upload.php',
            '/asset/js_ckeditor/kcfinder-3.12/upload.php',
            '/asset/js_ckeditor/kcfinder/upload.php',
            '/asset/kcfinder-3.12/upload.php',
            '/asset/kcfinder/upload.php',
            '/asset/webadmin/js/kcfinder-3.12/upload.php',
            '/asset/webadmin/js/kcfinder/upload.php',
            '/assets/admin/js/kcfinder-3.12/upload.php',
            '/assets/admin/js/kcfinder/upload.php',
            '/assets/admin/plugins/kcfinder-3.12/upload.php',
            '/assets/admin/plugins/kcfinder/upload.php',
            '/assets/bo/plugin/kcfinder-3.12/upload.php',
            '/assets/bo/plugin/kcfinder/upload.php',
            '/assets/ckeditor/kcfinder-3.12/upload.php',
            '/assets/ckeditor/kcfinder/upload.php',
            '/assets/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/assets/ckeditor/plugins/kcfinder/upload.php',
            '/assets/frontend/js/ckeditor/kcfinder-3.12/upload.php',
            '/assets/frontend/js/ckeditor/kcfinder/upload.php',
            '/assets/frontend/js/kcfinder-3.12/upload.php',
            '/assets/frontend/js/kcfinder/upload.php',
            '/assets/js/ckeditor/kcfinder-3.12/upload.php',
            '/assets/js/ckeditor/kcfinder/upload.php',
            '/assets/js/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/assets/js/ckeditor/plugins/kcfinder/upload.php',
            '/assets/js/kcfinder-3.12/upload.php',
            '/assets/js/kcfinder/upload.php',
            '/assets/js/mylibs/kcfinder-3.12/upload.php',
            '/assets/js/mylibs/kcfinder/upload.php',
            '/assets/js/plugins/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/assets/js/plugins/ckeditor/plugins/kcfinder/upload.php',
            '/assets/js/scripts/kcfinder-3.12/upload.php',
            '/assets/js/scripts/kcfinder/upload.php',
            '/assets/kcfinder-3.12/upload.php',
            '/assets/kcfinder/upload.php',
            '/assets/lib/kcfinder-3.12/upload.php',
            '/assets/lib/kcfinder/upload.php',
            '/assets/libs/kcfinder-3.12/upload.php',
            '/assets/libs/kcfinder/upload.php',
            '/assets/scripts/kcfinder-3.12/upload.php',
            '/assets/scripts/kcfinder/upload.php',
            '/assets/vendor/kcfinder-3.12/upload.php',
            '/assets/vendor/kcfinder/upload.php',
            '/assets/vendors/js/kcfinder-3.12/upload.php',
            '/assets/vendors/js/kcfinder/upload.php',
            '/assets/vendors/kcfinder-3.12/upload.php',
            '/assets/vendors/kcfinder/3.12/upload.php',
            '/assets/vendors/kcfinder/upload.php',
            '/assets/webadmin/js/kcfinder-3.12/upload.php',
            '/assets/webadmin/js/kcfinder/upload.php',
            '/backend/ckeditor/kcfinder-3.12/upload.php',
            '/backend/ckeditor/kcfinder/upload.php',
            '/backend/js/kcfinder-3.12/upload.php',
            '/backend/js/kcfinder/upload.php',
            '/backend/js/plugins/ckeditor/kcfinder-3.12/upload.php',
            '/backend/js/plugins/ckeditor/kcfinder/upload.php',
            '/backend/plugins/kcfinder-3.12/upload.php',
            '/backend/plugins/kcfinder/upload.php',
            '/ckeditor/kcfinder-3.12/upload.php',
            '/ckeditor/kcfinder/upload.php',
            '/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/ckeditor/plugins/kcfinder/upload.php',
            '/component/kcfinder-3.12/upload.php',
            '/components/kcfinder/upload.php',
            '/core/scripts/kcfinder-3.12/upload.php',
            '/core/scripts/kcfinder/upload.php',
            '/core/scripts/wysiwyg/kcfinder-3.12/upload.php',
            '/core/scripts/wysiwyg/kcfinder/upload.php',
            '/inc_admin/plugins/kcfinder-3.12/upload.php',
            '/inc_admin/plugins/kcfinder/upload.php',
            '/js/kcfinder-3.12/upload.php',
            '/js/kcfinder/upload.php',
            '/js/tinymce/kcfinder-3.12/upload.php',
            '/js/tinymce/kcfinder/upload.php',
            '/kcfinder-3.12/upload.php',
            '/kcfinder/upload.php',
            '/lib/kcfinder-3.12/upload.php',
            '/lib/kcfinder/upload.php',
            '/libs/kcfinder-3.12/upload.php',
            '/libs/kcfinder/upload.php',
            '/media/kcfinder-3.12/upload.php',
            '/media/kcfinder/upload.php',
            '/my_cms/public/assets/plugins/ckeditor/kcfinder-3.12/upload.php',
            '/my_cms/public/assets/plugins/ckeditor/kcfinder/upload.php',
            '/packages/assets/js/kcfinder-3.12/upload.php',
            '/packages/assets/js/kcfinder/upload.php',
            '/packages/ckeditor/kcfinder-3.12/upload.php',
            '/packages/ckeditor/kcfinder/upload.php',
            '/packages/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/packages/ckeditor/plugins/kcfinder/upload.php',
            '/packages/js/kcfinder-3.12/upload.php',
            '/packages/js/kcfinder/upload.php',
            '/packages/scripts/kcfinder-3.12/upload.php',
            '/packages/scripts/kcfinder/upload.php',
            '/packages/upload/kcfinder-3.12/upload.php',
            '/packages/upload/kcfinder/upload.php',
            '/panel/kcfinder-3.12/upload.php',
            '/panel/kcfinder/upload.php',
            '/public/ckeditor/kcfinder-3.12/upload.php',
            '/public/ckeditor/kcfinder/upload.php',
            '/public/ckeditor/plugins/kcfinder-3.12/upload.php',
            '/public/ckeditor/plugins/kcfinder/upload.php',
            '/public/js/kcfinder-3.12/upload.php',
            '/public/js/kcfinder/upload.php',
            '/resource/assets/kcfinder-3.12/upload.php',
            '/resource/js/kcfinder/upload.php',
            '/resource/kcfinder-3.12/upload.php',
            '/resource/kcfinder/upload.php',
            '/resources/assets/kcfinder-3.12/upload.php',
            '/resources/assets/kcfinder/upload.php',
            '/resources/js/kcfinder-3.12/upload.php',
            '/resources/js/kcfinder/upload.php',
            '/resources/kcfinder-3.12/upload.php',
            '/resources/kcfinder/upload.php',
            '/resources/vendor/kcfinder-3.12/upload.php',
            '/resources/vendor/kcfinder/upload.php',
            '/scripts/js/kcfinder-3.12/upload.php',
            '/scripts/js/kcfinder/upload.php',
            '/scripts/kcfinder-3.12/upload.php',
            '/scripts/kcfinder/upload.php',
            '/tinymce/kcfinder-3.12/upload.php',
            '/tinymce/kcfinder/upload.php',
            '/upload/kcfinder-3.12/upload.php',
            '/upload/kcfinder/upload.php',
            '/uploads/kcfinder-3.12/upload.php',
            '/uploads/kcfinder/upload.php',
            '/vendor/kcfinder-3.12/upload.php',
            '/vendor/kcfinder/upload.php',
            '/webassist/kcfinder-3.12/upload.php',
            '/webassist/kcfinder/upload.php',
            '/third_party/kcfinder/upload.php',
            '/third_party/kcfinder-3.12/upload.php',
            '/ard/assets/js/kcfinder/upload.php',
            '/editor/kcfinder/upload.php',
            '/assets/grocery_crud/texteditor/ckeditor/kcfinder/upload.php',
            '/assets/text_editor/kcfinder/upload.php',
            '/assets/js/ckeditor12/kcfinder/upload.php',
            '/apps/kcfinder/upload.php',
            '/apps/js/kcfinder/upload.php',
            '/include/libs/kcfinder-2.54/upload.php',
            '/vendors/kcfinder/upload.php',
            '/vendors/js/kcfinder/upload.php',
            '/ThirdParty/kcfinder/upload.php',
            '/assets/plugins/kcfinder/upload.php',
            '/admin/kcfinder/upload.php',
        ]
        
        for path in ajg:
            gasbro = 'http://' + url + '/' + path
            asu = requests.get(gasbro, headers=head, timeout=15)
            if "alert('Unknown error')" in asu.content:
                print(url + ijo + '[!] Vuln Kcfinder . . .')
                open('rzlt_kcf.txt', 'a').write(gasbro + '\n')
            else:
                print(url + abang + '[!] Not Vuln Kcfinder . . .')
    except:
        pass


def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pr = pp.map(kcfinder, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
