# LLM Backend

日本語ログ要約システム / Japanese Log Summarization System

## 概要 / Overview

このプロジェクトは、Ollama と FAISS を使用してログデータを処理し、日本語で要約するバックエンドシステムです。

This project is a backend system that processes log data and summarizes it in Japanese using Ollama and FAISS.

## 機能 / Features

- **ログインデックス作成**: FAISSを使用してログデータのベクトルインデックスを作成
- **ログ要約**: Ollamaを使用してログを日本語で要約
- **類似検索**: ベクトル検索を使用して関連するログを検索
- **リアルタイム更新**: 新しいログでインデックスを更新

- **Log Indexing**: Create vector indexes of log data using FAISS
- **Log Summarization**: Summarize logs in Japanese using Ollama
- **Similarity Search**: Find relevant logs using vector search
- **Real-time Updates**: Update indexes with new logs

## 必要な環境 / Requirements

- Python 3.7+
- Ollama (with llama3 model)
- Dependencies listed in `requirements.txt`

## セットアップ / Setup

1. リポジトリをクローン / Clone the repository:
```bash
git clone https://github.com/Moge800/llm_backend.git
cd llm_backend
```

2. 依存関係をインストール / Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ollamaをインストールし、llama3モデルをダウンロード / Install Ollama and download llama3 model:
```bash
# Ollamaのインストール方法は公式サイトを参照
# Follow Ollama's official installation guide
ollama pull llama3
```

4. 設定ファイルを作成 / Create configuration file:
```python
# hidden_key.py
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer('your-embedding-model')
FAISS_INDEX = "index_latest.faiss"
```

## 使用方法 / Usage

```python
import backend_with_ollama as backend

# ログの要約
summary = backend.summarize_logs("ログテキスト")

# 最近のログを要約
recent_summary = backend.summarize_recent()

# インデックスの更新
backend.update_index(["新しいログ1", "新しいログ2"])
```

## 主な関数 / Main Functions

- `summarize_logs(log_texts, model="llama3")`: ログテキストを要約
- `summarize_recent(model="llama3")`: 最近のログを検索して要約
- `update_index(new_logs)`: メインインデックスを新しいログで更新
- `update_today_index(log_texts)`: 今日のログ用インデックスを作成

## ライセンス / License

MIT License - 詳細は [LICENSE](LICENSE) を参照