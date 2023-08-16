
import glob
import subprocess
from pathlib import Path
import os
lang_root = './third_party/langs/Strings'
config_root = './third_party/langs/config'

makepri = os.path.abspath('./third_party/langs/makepri.cmd')
resws = glob.glob(f'{lang_root}/**/*.resw', recursive=False)

print('prepare....')

for resw in resws:
    path = Path(resw)

    lang = path.parent.name
    print('# ', lang)

    if not os.path.exists(f"{config_root}\\{lang}\\priconfig.xml"):
        output = subprocess.check_output([makepri, 'createconfig', '/cf', f'{config_root}\\{lang}\\priconfig.xml',
                                         '/dq', f'lang-{lang}', '/o', '/pv', '10.0.0'], cwd='.', universal_newlines=True)
        print(output)

    output = subprocess.check_output([makepri, 'new', '/pr', f'{lang_root}\\{lang}', '/cf',
                                     f'{config_root}\\{lang}\\priconfig.xml', '/o', '/of', f'./Translations/{lang}'], cwd='.', shell=True, universal_newlines=True)

    print(output)
