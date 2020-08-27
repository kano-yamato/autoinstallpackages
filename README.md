# 複数package自動installツール
## Tool概要
任意のフォルダ内に格納したpackageのzipファイルを任意の環境に自動でinstallできるツール。
## 事前準備
### Python3インストール方法
1. https://www.python.org/downloads/windows/ &gt; Latest Python 3 Release - Python 3.x.x をクリック
1. Windows x86-64 web-based installer をクリックし、インストーラをダウンロードする
1. インストール完了後、以下のコマンドをコマンドプロンプトで実行し、バージョンが表示されていることを確認する
```
$ python --version
$ pip --version
```

### セットアップ
1. autoinstallpackageリポジトリに移動
2. コマンドプロンプトで以下を実行

```
$ pip install -e ./
```

### 実行手順
1. autoinstallpackageリポジトリに `env.json` というファイルを作成
2. 以下のような内容に編集(環境によって内容は変動)

```
{
    "domain": "http://localhost:4504",
    "user": "admin",
    "pass": "admin",
    "path": "C:\\Users\\kano\\Downloads\\author200820"
}
```

各項目の意味は

- domain: アップロード先のドメイン
- user: ユーザー
- pass: ユーザーのログインパスワード
- path: packageを保存している場所

3. autoinstallpackageリポジトリ内で `packins` コマンドを実行

### 注意事項
packageインストールの順番についてはファイル名アルファベット順となるため、依存関係等が存在して順番通りにインストールしたい場合は

- 依存関係があるpackageを分けてツール実行する
- ファイル名を変更し順番通りのインストールになるように調整する

以上のどちらかで調整をお願いします。
