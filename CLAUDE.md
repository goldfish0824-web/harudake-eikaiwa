# ChatGPT英会話プロンプト

ChatGPT（無料版）に貼り付けるだけで英会話の練習ができる、プロンプト作成用のWebページ。
APIは使わない静的HTMLで、GitHub Pagesで公開する予定。画面は日本語、生成されるプロンプト本文は英語。

## フォルダ構成

```
chatgpt-eikaiwa-prompt/
├─ hs/index.html     高校生版（生徒にはこのURLだけを配る）
├─ adv/index.html    中〜上級版（自分用・一般の学習者向け）
└─ src/              編集用の元ファイル
   ├─ template.html  共通のHTML・CSS・JavaScript（プロンプト生成は buildPrompt()）
   ├─ data_hs.js     高校生版のデータ（トピック・場面・論題・面接・コマンド・注意書き）
   ├─ data_adv.js    中〜上級版のデータ（上に加え、英検1級トピック・IELTSカード）
   └─ build.py       src から hs/index.html と adv/index.html を作る
```

- `hs/index.html` と `adv/index.html` は生成物なので直接編集しない。`src/` を直してから `python src/build.py` を実行する。
- 色やフォントなど版ごとのテーマは `build.py` の `THEMES` にある。

## ページの中身（両版共通）

- 練習の種類：トピック別Q&A／ロールプレイ／ディスカッション（意見交換・ディベート）／面接練習
- 設定：レベル、音声で話すか文字で入力するか、訂正のタイミング（最後にまとめて／その場で短く／少なめ）、練習の長さ、フィードバックの言語、その他の希望（自由記述）
- 高校生版のみ：「困ったら日本語OK」。ディスカッションではOREO（Opinion→Reason→Example→Opinion）を促す
- 中〜上級版のみ：英語の種類（アメリカ／イギリス）、「Upgrade」コマンド。英検1級のトピックとIELTSのカードはランダムに入れ替わる
- 設定はブラウザの localStorage に保存（キーは `eikaiwa-prompt-v1-hs` と `eikaiwa-prompt-v1-adv`）
- Google Fonts を読み込む（高校生版：M PLUS Rounded 1c、中〜上級版：Zen Kaku Gothic New）

## 次にやること

1. GitHubに公開リポジトリを作り、このフォルダをpushする（リポジトリ名の候補：`chatgpt-eikaiwa-prompt`）
2. GitHub Pagesを有効にする（mainブランチ／ルート）
3. 公開後のURL（GitHubのユーザー名が goldfish0824-web の場合）
   - 高校生版：https://goldfish0824-web.github.io/chatgpt-eikaiwa-prompt/hs/
   - 中〜上級版：https://goldfish0824-web.github.io/chatgpt-eikaiwa-prompt/adv/
4. ルート（`/`）には2つの版へのリンクページを置かない（本人の判断）。ルートは404のままでよい
5. GoatCounter は今のところ入れない（本人の判断）

## メモ

- 高校生版の「知っておくこと」欄に、個人情報を入れないことと、OpenAIの利用規約（13歳以上、18歳未満は保護者の同意が必要）を書いてある
- 実際にChatGPTに貼り付けて会話するテストはまだしていない。気になる動きがあれば `template.html` の `buildPrompt()` か `data_*.js` の文言を調整する
- 同じページを claude.ai のアーティファクトとしても公開済み（非公開設定）
