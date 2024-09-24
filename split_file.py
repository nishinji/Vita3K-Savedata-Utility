import os

file_path = "sdslot.dat"  # 分割するファイルのパス
output_dir = "./output/"  # 出力ディレクトリのパス

# 出力ディレクトリが存在しなければ作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# バイナリが全て0のファイルを削除する関数
def delete_empty_files():
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        if os.path.getsize(file_path) == 0:
            os.remove(file_path)
            # print(f"File '{filename}' has been deleted as it contains only zero bytes.")

# ファイルの読み込みと分割
with open(file_path, "rb") as file:
    chunk_number = -1
    while True:
        chunk = file.read(1024)
        if not chunk:
            break

        # バイナリが全て0の場合はスキップ
        if chunk == b'\x00' * len(chunk):
            # print(f"Skipping chunk {chunk_number:>{len(str(chunk_number))}} as it contains only zero bytes.")
            chunk_number += 1
            continue

        # チャンク番号が-1の場合はスキップ
        if chunk_number == -1:
            # print(f"Skipping chunk {chunk_number:>{len(str(chunk_number))}} as it is invalid.")
            chunk_number += 1
            continue

        # 末尾の180バイトを削除
        chunk = chunk[:-180]

        # ファイルを書き出す
        output_path = os.path.join(output_dir, f"SlotParam_{chunk_number:>{len(str(chunk_number))}}.bin")
        with open(output_path, "wb") as output_file:
            output_file.write(chunk)
        #print(f"Chunk {chunk_number:>{len(str(chunk_number))}} has been created.")
        chunk_number += 1

# バイナリが全て0のファイルを削除
delete_empty_files()
