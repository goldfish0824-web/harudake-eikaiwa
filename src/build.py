# src/ の template.html と data_*.js から hs/index.html と adv/index.html を作る
# 使い方: python src/build.py
import pathlib
root = pathlib.Path(__file__).parent   # src/
proj = root.parent                     # プロジェクトのルート
tpl = (root/'template.html').read_text(encoding='utf-8')
THEMES = {
 'hs': dict(
   light=dict(bg='#ffffff',ink='#1c1d3a',soft='#55587a',line='#dcdcea',panel='#f5f5fa',band='#ffd23f',bandInk='#1c1d3a',acc='#2b54f0',accInk='#ffffff',accSoft='#eef2ff',sup='#ff6b5e',tk='#ffffff'),
   dark=dict(bg='#15162b',ink='#f3f2ec',soft='#b7b9d2',line='#30325a',panel='#1d1f3a',band='#3d3413',bandInk='#ffe28a',acc='#8aa2ff',accInk='#0f1433',accSoft='#232a55',sup='#c4544a',tk='#1d1f3a'),
   font='"M PLUS Rounded 1c","Hiragino Maru Gothic ProN","Hiragino Sans","Noto Sans JP","Yu Gothic",Meiryo,sans-serif',
   link='https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@400;700;800&display=swap',
   out='hs/index.html'),
 'adv': dict(
   light=dict(bg='#ffffff',ink='#0f262b',soft='#4b6266',line='#d4e0de',panel='#f1f6f5',band='#0e3b43',bandInk='#eef8f5',acc='#d13a22',accInk='#ffffff',accSoft='#fdf0ed',sup='#7fd1c0',tk='#ffffff'),
   dark=dict(bg='#0a1d21',ink='#e8f2f0',soft='#a3bab8',line='#24404a',panel='#102a30',band='#0e3b43',bandInk='#eef8f5',acc='#ff7a5f',accInk='#1b0a06',accSoft='#2a2322',sup='#1f6b5f',tk='#102a30'),
   font='"Zen Kaku Gothic New","Hiragino Sans","Noto Sans JP","Yu Gothic",Meiryo,sans-serif',
   link='https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap',
   out='adv/index.html'),
}
def vars(d): return ''.join(f'--{k}:{v};' for k,v in d.items())
for vid, th in THEMES.items():
    data = (root/f'data_{vid}.js').read_text(encoding='utf-8')
    theme = (':root{color-scheme:light;' + vars(th['light']) + '--font:' + th['font'] + '}\n'
             '@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;' + vars(th['dark']) + '}}\n'
             ':root[data-theme=dark]{color-scheme:dark;' + vars(th['dark']) + '}')
    ver = '高校生版' if vid=='hs' else '中〜上級版'
    title = 'ChatGPT英会話プロンプト ' + ver
    html = (tpl.replace('{{TITLE}}', title).replace('{{VER}}', ver).replace('{{FONTLINK}}', th['link'])
               .replace('{{THEME}}', theme).replace('{{DATA}}', data))
    if vid=='adv':
        html = html.replace('font-weight:800', 'font-weight:900')
    dest = proj/th['out']
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(html.encode('utf-8'))  # 改行をLFのまま書く（WindowsでもCRLFにしない）
    print(th['out'], len(html))
