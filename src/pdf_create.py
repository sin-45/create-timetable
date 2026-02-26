from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def create_pdf(table_data, output_filename="timetable_with_teacher.pdf"):
    fontname = "HeiseiKakuGo-W5"
    pdfmetrics.registerFont(UnicodeCIDFont(fontname))

    doc = SimpleDocTemplate(output_filename, pagesize=A4)

    col_width = 90
    row_height = 70 
    max_text_width = col_width - 8

    # 科目名と教員名の基本フォントサイズ
    base_subject_size = 14
    base_teacher_size = 10  # ★ 教員名の基本サイズ（少し小さめ）

    # 表に渡すための新しいデータ（Paragraphオブジェクト）を格納するリスト
    formatted_table_data = []

    for row_idx, row in enumerate(table_data):
        formatted_row = []
        for col_idx, cell_text in enumerate(row):
            text = str(cell_text)
            if not text:
                formatted_row.append("")
                continue

            # 「\n」が含まれているか判定して、科目名と教員名に分ける
            if '\n' in text:
                parts = text.split('\n', 1)
                subject = parts[0]
                teacher = parts[1]
            else:
                subject = text
                teacher = ""

            # それぞれの文字の横幅を計算
            w_subj = pdfmetrics.stringWidth(subject, fontname, base_subject_size)
            w_teach = pdfmetrics.stringWidth(teacher, fontname, base_teacher_size) if teacher else 0
            
            # はみ出す場合は、科目と教員のバランスを保ったまま全体を縮小する割合(scale)を計算
            max_w = max(w_subj, w_teach)
            scale = 1.0
            if max_w > max_text_width:
                scale = max_text_width / max_w
            
            subj_size = base_subject_size * scale
            teach_size = base_teacher_size * scale
            
            # マスの中央揃えなどの基本スタイル
            p_style = ParagraphStyle(
                name=f'Cell_{row_idx}_{col_idx}',
                fontName=fontname,
                fontSize=subj_size,
                leading=subj_size * 1.2, # 行間
                alignment=TA_CENTER      # 中央揃え
            )
            
            # ★ HTMLタグを使って、教員名だけサイズと色を指定する
            if teacher:
                # color='#666666' で濃すぎないグレーに設定
                p_text = f"{subject}<br/><font size={teach_size} color='#666666'>{teacher}</font>"
            else:
                p_text = subject

            # Paragraphオブジェクトを作ってリストに追加
            formatted_row.append(Paragraph(p_text, p_style))
            
        formatted_table_data.append(formatted_row)

    # Paragraphを入れた新しいデータで表を作成
    pdf_table = Table(formatted_table_data, colWidths=col_width, rowHeights=row_height)

    # 全体の枠線や背景色の設定（文字の設定はParagraphで行うため削除）
    style_commands = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
    ]

    pdf_table.setStyle(TableStyle(style_commands))
    doc.build([pdf_table])
    print(f"「{output_filename}」が作成されました！教員名のスタイルを適用しました。")

# ==========================================
# 実行テスト用
# ==========================================
if __name__ == "__main__":
    my_table = [
        ["", "月", "火", "水", "木", "金"],
        ["1限", "プログラミング基礎\n田中先生", "数学\n佐藤", "英語", "理科", "社会"],
        ["2限", "数学", "英語コミュニケーション\nスミス先生", "理科", "社会\n山田", "国語"],
        ["3限", "英語", "理科", "社会", "国語", "データサイエンス演習\n鈴木教授"],
        ["4限", "体育\n高橋", "音楽", "美術\n伊藤", "技術", "家庭"],
        ["5限", "理科", "社会", "国語", "数学\n加藤", "英語"],
    ]

    create_pdf(my_table)