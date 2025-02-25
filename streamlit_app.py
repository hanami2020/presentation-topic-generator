import random
import streamlit as st

# カテゴリーごとの単語リスト
category_A = ["保険", "歯医者", "車のブランド", "ファッションブランド", "広告代理店", "デジタルメディア"]
category_B = ["HR", "営業", "カスタマーサポート", "経理", "マネジメント", "開発"]
category_C = ["会社紹介", "月次報告", "企業向け営業", "決算", "人事評価", "研修", "イベント企画書"]

def generate_presentation_topic():
    A = random.choice(category_A)
    B = random.choice(category_B)
    C = random.choice(category_C)
    return f"{A}の、{B}が{C}の時に使うプレゼンテーション"

# Streamlitアプリのレイアウト
st.title("Canvaプレゼンお題ジェネレーター 🎨📊")
st.write("ボタンを押すとランダムなプレゼンテーションのトピックが生成されます！")

if st.button("お題を生成する 🎲"):
    topic = generate_presentation_topic()
    st.success(topic)

