# 貼るだけ英会話

ChatGPT（無料版）に貼り付けるだけで英会話の練習ができる、プロンプト作成用のWebページ。
APIは使わない静的HTMLで、GitHub Pagesで公開している。画面は日本語、生成されるプロンプト本文は英語。
旧名は「ChatGPT英会話プロンプト」。2026年11月24日に「貼るだけ英会話」に改名し、リポジトリ名も `chatgpt-eikaiwa-prompt` から `harudake-eikaiwa` に変えた。

## フォルダ構成

```
harudake-eikaiwa/    （手元のフォルダ名は chatgpt-eikaiwa-prompt のまま）
├─ hs/index.html     高校生版（生徒にはこのURLだけを配る）
├─ hs/apple-touch-icon.png   高校生版のホーム画面アイコン（180×180、タブのアイコンも兼ねる）
├─ adv/index.html    中〜上級版（自分用・一般の学習者向け）
├─ adv/apple-touch-icon.png  中〜上級版のホーム画面アイコン
└─ src/              編集用の元ファイル
   ├─ template.html  共通のHTML・CSS・JavaScript（練習のプロンプトは buildPrompt()、添削・評価は buildReview()）
   ├─ data_hs.js     高校生版のデータ（トピック・場面・論題・面接・コマンド・注意書き）
   ├─ data_adv.js    中〜上級版のデータ（上に加え、英検1級トピック・IELTSカード）
   ├─ build.py       src から hs/index.html と adv/index.html を作る
   └─ icon.html      ホーム画面アイコンの元（?v=hs / ?v=adv で版を切り替える）
```

- `hs/index.html` と `adv/index.html` は生成物なので直接編集しない。`src/` を直してから `python src/build.py` を実行する。
- `build.py` は改行をLFのまま書き出す（WindowsでビルドしてもCRLFにならない）。
- 色やフォントなど版ごとのテーマは `build.py` の `THEMES` にある（light/dark の色、本文フォント、見出しフォント、ヘッダーの英語の一行と飾り文字）。
- ルートの `.nojekyll` は消さない。これが無いと GitHub Pages が Jekyll を通し、README.md がルートのトップページとして表示されてしまう。

## ページの中身（両版共通）

ページは2ステップ。ヘッダーのタブで切り替える。

- **STEP 1 練習する**：練習のプロンプトを作る
  - 練習の種類：トピック別Q&A／ロールプレイ／ディスカッション（意見交換・ディベート）／面接練習
  - 設定：レベル、音声で話すか文字で入力するか、訂正のタイミング（会話のあとでまとめて／その場で短く）、練習の長さ、その他の希望（自由記述）
  - 練習のプロンプトでは、終わったときにフィードバックや評価を出さず、短いあいさつだけにさせている（高校生版の文字入力では、STEP 2へ進むよう日本語で一言添えさせる）
- **STEP 2 添削・評価をもらう**：会話が終わったあと、同じチャットに貼るプロンプトを作る
  - 添削・評価は会話のあとに別のメッセージで頼む方式（本人の経験から。会話全体を見直してもらえ、基準を変えて何度でも頼める）
  - 評価の基準（複数選べる、選ばなくてもよい）：英検（二次試験＝面接の観点、級を選べる）／TOEICスピーキング（0〜200点・レベル1〜8）／CEFR／高校生版は「5段階でざっくり」、中〜上級版は IELTS スピーキングと「ネイティブ目線」
  - 英検の級：高校生版は3級・準2級・準2級プラス・2級・準1級、中〜上級版は2級・準1級・1級。初期値はレベル設定から決まる（`data_*.js` の levels の `eg`）
  - 返してほしい内容：よかった点／添削（3つまで・5つまで・できるだけ全部）／ワンランク上の言い方（中〜上級版はネイティブらしい言い換え）／模範解答／練習に合わせたチェック（ミッション・OREO・面接など）／次へのアドバイス／もう一度チャレンジ
  - 添削・評価は両版とも日本語だけ（本人の希望で、日本語／英語の選択肢はなくした）。英語のまま書かせるのは、自分の発言と英語の例（直した文・言い換え・模範解答）だけ。評価の基準の説明は英語でも、評価そのものは日本語で書くよう指示している
  - その他の希望（自由記述）もここで書ける
  - 声の文字起こしの可能性があるので、つづりや句読点は無視し、発音は評価しないよう指示している。評価は非公式の目安だと一言添えさせる
- 高校生版のみ：「困ったら日本語OK」。ディスカッションではOREO（Opinion→Reason→Example→Opinion）を促す
- 中〜上級版のみ：英語の種類（アメリカ／イギリス）、「Upgrade」コマンド。英検1級のトピックとIELTSのカードはランダムに入れ替わる（IELTS面接の目安バンドは STEP 2 で「IELTS」を選んで出す）
- 設定はブラウザの localStorage に保存（キーは `eikaiwa-prompt-v1-hs` と `eikaiwa-prompt-v1-adv`。改名のときも変えていない）。どちらのステップを開いていたかも保存する
- 見た目：濃い色のヘッダー（STEP 1／2のタブつき）、カード型の選択肢、右側に「チケット」（選んだ練習・添削の内容）とコピーボタン。スマホでは下にコピーバーが出る。ダークモード対応
  - 高校生版：紺のヘッダーに青〜紫のグラデーション、差し色は黄色。見出しは Dela Gothic One、本文は M PLUS Rounded 1c
  - 中〜上級版：黒に近いヘッダーに細い方眼、差し色は朱色。見出しは Zen Old Mincho、本文は Zen Kaku Gothic New
- ホーム画面アイコン：ふきだしに「英会話」、角にマスキングテープ（「貼る」の意味）。地の色・模様・フォントは各版のヘッダーと同じ（高校生版は黄色のふきだし、中〜上級版は朱色のふきだしに明朝）
  - ホーム画面での名前は `apple-mobile-web-app-title` の「貼るだけ英会話」（両版とも同じ）
  - `apple-touch-icon.png` は `build.py` では作らない。`src/icon.html` を直したら、Chrome のヘッドレスで書き出して `hs/`・`adv/` に置く：
    `chrome --headless=new --hide-scrollbars --force-device-scale-factor=1 --window-size=180,180 --virtual-time-budget=10000 --screenshot=<出力先.png> "file:///<srcの絶対パス>/icon.html?v=hs"`（adv は `?v=adv`）
  - iPhone が角を丸めるので、アイコンは四角いまま・透明なしで作る

## 公開

- リポジトリ：https://github.com/goldfish0824-web/harudake-eikaiwa （公開、mainブランチ）
- GitHub Pages：mainブランチ／ルートから配信（2026年11月24日に公開）
  - 高校生版：https://goldfish0824-web.github.io/harudake-eikaiwa/hs/
  - 中〜上級版：https://goldfish0824-web.github.io/harudake-eikaiwa/adv/
  - 旧URL（`/chatgpt-eikaiwa-prompt/`）は改名で404になった。改名前にURLを配った相手はいない
- 更新するときは、`src/` を直す → `python src/build.py` → コミットして `git push`。1〜2分で公開ページに反映される
- コミットのメールアドレスは、このリポジトリだけ GitHub の noreply アドレスにしてある（`git config` のローカル設定）
- リポジトリは公開なので、CLAUDE.md や README.md も誰でも読める（Pages上の `/CLAUDE.md` などでも見える）
- ルート（`/`）には2つの版へのリンクページを置かない（本人の判断）。ルートは404のままでよい
- GoatCounter は今のところ入れない（本人の判断）

## メモ

- 高校生版の「知っておくこと」欄に、個人情報を入れないことと、OpenAIの利用規約（13歳以上、18歳未満は保護者の同意が必要）を書いてある
- 実際にChatGPTに貼り付けて会話するテストはまだしていない（STEP 2 の添削・評価も同じ）。気になる動きがあれば `template.html` の `buildPrompt()`・`buildReview()` か `data_*.js` の文言を調整する
- 同じページを claude.ai のアーティファクトとしても公開済み（非公開設定）。2026年11月24日に2ステップ化・新デザインの版に更新した
  - `src/` を直してもアーティファクトは自動では変わらない。更新するときは、ビルドした `index.html` から DOCTYPE・html・head・body のタグを外し（title・フォントのlink・styleは残す）、`<script>document.documentElement.lang="ja"</script>` を足したものを公開する。アイコン（apple-touch-icon・icon・apple-mobile-web-app-title）の行はアーティファクトでは要らないので外す
