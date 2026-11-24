# src/ の template.html と data_*.js から hs/index.html と adv/index.html を作る
# 使い方: python src/build.py
import pathlib
root = pathlib.Path(__file__).parent   # src/
proj = root.parent                     # プロジェクトのルート
tpl = (root/'template.html').read_text(encoding='utf-8')

# 版ごとのテーマ。色は light / dark の両方、フォントは本文(font)と見出し(display)。
#  band/hero : 上の濃い帯とその模様     hi    : 帯の上の差し色（「英会話」・版の名前）
#  acc       : 選択中・コピーボタン      accGrad: アクセントの塗り（高校生版はグラデーション）
#  stub      : チケットの半券            sh1〜3: 影
HS_HERO = ('radial-gradient(rgba(255,255,255,.13) 1px,transparent 1.4px) 0 0/20px 20px,'
           'radial-gradient(55% 120% at 88% -10%,rgba(139,92,246,.75),transparent 62%),'
           'radial-gradient(45% 100% at -5% 110%,rgba(59,91,255,.7),transparent 60%),'
           'radial-gradient(35% 70% at 62% 120%,rgba(255,95,162,.45),transparent 70%)')
ADV_HERO = ('linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px) 0 0/100% 36px,'
            'linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px) 0 0/36px 100%,'
            'radial-gradient(60% 130% at 100% 0%,rgba(224,72,45,.34),transparent 62%),'
            'radial-gradient(40% 90% at 0% 120%,rgba(64,140,130,.28),transparent 65%)')
TABS = dict(tabBg='rgba(255,255,255,.07)', tabHover='rgba(255,255,255,.13)', tabLine='rgba(255,255,255,.16)', tabNum='rgba(255,255,255,.12)')

THEMES = {
 'hs': dict(
   light=dict(bg='#f3f4fb', ink='#14163a', soft='#585b80', soft2='#b9bcd6', line='#e0e2ef', panel='#ffffff',
              band='#11133a', bandInk='#ffffff', bandSoft='#c9ccf2', hero=HS_HERO, decoLine='rgba(255,255,255,.16)',
              hi='#ffd84d', hiInk='#14163a', hiSoft='#fff5c7', **TABS,
              acc='#3b5bff', accInk='#ffffff', accSoft='#eef1ff', accGrad='linear-gradient(135deg,#3b5bff,#7c4dff)', accShadow='rgba(59,91,255,.75)',
              tk='#ffffff', stub='linear-gradient(160deg,#3b5bff,#7c4dff 65%,#b84fe0)', stubInk='#ffffff', stubLine='rgba(255,255,255,.55)',
              sh1='0 1px 2px rgba(20,22,58,.05)', sh2='0 12px 24px -14px rgba(20,22,58,.35)', sh3='0 28px 56px -30px rgba(20,22,58,.5),0 2px 6px rgba(20,22,58,.06)'),
   dark=dict(bg='#0c0e24', ink='#eef0ff', soft='#a8abd2', soft2='#4a4e85', line='#262a52', panel='#14173a',
             band='#090b1f', bandInk='#ffffff', bandSoft='#b9bce6', decoLine='rgba(255,255,255,.1)',
             hiSoft='#34301a', acc='#8aa0ff', accInk='#0c0e24', accSoft='#1d2252', accGrad='linear-gradient(135deg,#8aa0ff,#b69cff)', accShadow='rgba(0,0,0,.8)',
             tk='#14173a', stub='linear-gradient(160deg,#4a63ff,#7c4dff 65%,#a84ad6)',
             sh1='0 1px 2px rgba(0,0,0,.3)', sh2='0 12px 24px -14px rgba(0,0,0,.7)', sh3='0 28px 56px -30px rgba(0,0,0,.85)'),
   font='"M PLUS Rounded 1c","Hiragino Maru Gothic ProN","Hiragino Sans","Noto Sans JP","Yu Gothic",Meiryo,sans-serif',
   display='"Dela Gothic One","M PLUS Rounded 1c","Hiragino Sans","Noto Sans JP",sans-serif', dw='400',
   link='https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=M+PLUS+Rounded+1c:wght@400;700;800&display=swap',
   eyebrow='Speaking practice for high school students', deco='TALK!',
   out='hs/index.html'),
 'adv': dict(
   light=dict(bg='#f4f2ec', ink='#141618', soft='#5a5e62', soft2='#bdb8ad', line='#e3ded3', panel='#ffffff',
              band='#101315', bandInk='#f4f2ec', bandSoft='#b7bbb8', hero=ADV_HERO, decoLine='rgba(255,255,255,.13)',
              hi='#ff7657', hiInk='#141618', hiSoft='#fbe9e3', **TABS,
              acc='#d23e28', accInk='#ffffff', accSoft='#fbece7', accGrad='linear-gradient(135deg,#df4a2f,#c4351f)', accShadow='rgba(210,62,40,.75)',
              tk='#ffffff', stub='#101315', stubInk='#f4f2ec', stubLine='rgba(255,255,255,.3)',
              sh1='0 1px 2px rgba(30,24,15,.05)', sh2='0 12px 24px -14px rgba(30,24,15,.35)', sh3='0 28px 56px -30px rgba(30,24,15,.5),0 2px 6px rgba(30,24,15,.06)'),
   dark=dict(bg='#0e1113', ink='#ecebe5', soft='#a2a6a8', soft2='#3f4549', line='#262b2f', panel='#171b1e',
             band='#08090a', bandInk='#ecebe5', bandSoft='#a9adaa', decoLine='rgba(255,255,255,.1)',
             hiSoft='#2e1d18', acc='#ff6f52', accInk='#1a0905', accSoft='#2c1c18', accGrad='linear-gradient(135deg,#ff7a5e,#f0573a)', accShadow='rgba(0,0,0,.8)',
             tk='#171b1e', stub='#08090a', stubInk='#ecebe5', stubLine='rgba(255,255,255,.22)',
             sh1='0 1px 2px rgba(0,0,0,.3)', sh2='0 12px 24px -14px rgba(0,0,0,.7)', sh3='0 28px 56px -30px rgba(0,0,0,.85)'),
   font='"Zen Kaku Gothic New","Hiragino Sans","Noto Sans JP","Yu Gothic",Meiryo,sans-serif',
   display='"Zen Old Mincho","Hiragino Mincho ProN","Yu Mincho",serif', dw='900',
   link='https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;700;900&family=Zen+Old+Mincho:wght@700;900&display=swap',
   eyebrow='Speaking practice for intermediate & advanced learners', deco='Speak.',
   out='adv/index.html'),
}
def vars(d): return ''.join(f'--{k}:{v};' for k,v in d.items())
for vid, th in THEMES.items():
    data = (root/f'data_{vid}.js').read_text(encoding='utf-8')
    theme = (':root{color-scheme:light;' + vars(th['light']) + '--font:' + th['font'] + ';--display:' + th['display'] + ';--dw:' + th['dw'] + '}\n'
             '@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;' + vars(th['dark']) + '}}\n'
             ':root[data-theme=dark]{color-scheme:dark;' + vars(th['dark']) + '}')
    ver = '高校生版' if vid=='hs' else '中〜上級版'
    title = '貼るだけ英会話 ' + ver
    html = (tpl.replace('{{TITLE}}', title).replace('{{VER}}', ver).replace('{{FONTLINK}}', th['link'])
               .replace('{{EYEBROW}}', th['eyebrow']).replace('{{DECO}}', th['deco'])
               .replace('{{THEME}}', theme).replace('{{DATA}}', data))
    if vid=='adv':
        html = html.replace('font-weight:800', 'font-weight:900')
    dest = proj/th['out']
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(html.encode('utf-8'))  # 改行をLFのまま書く（WindowsでもCRLFにしない）
    print(th['out'], len(html))
