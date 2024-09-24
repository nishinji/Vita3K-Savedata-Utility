import os

file_path = "./input/"
output_file = 'sdslot.dat'
max_slots = 255
header = b'\x53\x44\x53\x4C'  # 'SDSL'
padding_size = 0x200  # 512バイト
slot_start_address = 0x200  # スロットの開始アドレス
data_start_address = 0x400  # データの開始アドレス
block_size = 0x400 # ブロックサイズ (1024バイト)
data_block_size = 844  # 各ファイルデータブロックサイズ
zero_padding_size = 180  # 180バイトの0パディング

# 入力ディレクトリが存在しなければ作成
if not os.path.exists(file_path):
    os.makedirs(file_path)

# 先頭に'SDSL'を入れ、残りを0で埋める初期データを作成
content = header + b'\x00' * (padding_size - len(header))

# ファイルの存在に基づいて、0x20xのアドレスに1をセット
for i in range(max_slots + 1):
    slot_filename = f"SlotParam_{i}.bin"
    slot_file_path = os.path.join(file_path, slot_filename)
    
    # スロットが存在すれば、該当するアドレスに1をセット
    if os.path.exists(slot_file_path):
        # アドレスの位置を計算
        address = slot_start_address + i
        if len(content) <= address:
            content += b'\x00' * (address + 1 - len(content))
        content = content[:address] + b'\x01' + content[address+1:]

# 0x400まで0で埋める
if len(content) < data_start_address:
    content += b'\x00' * (data_start_address - len(content))

# SlotParam_x.bin のデータを追加、存在しない場合は0で埋める
for i in range(max_slots + 1):
    slot_filename = f"SlotParam_{i}.bin"
    slot_file_path = os.path.join(file_path, slot_filename)
    
    # データブロックの開始アドレスを計算
    block_address = data_start_address + i * block_size
    
    if os.path.exists(slot_file_path):
        # ファイルが存在する場合、そのデータを読み込む
        with open(slot_file_path, 'rb') as slot_file:
            slot_data = slot_file.read(data_block_size)
            slot_data += b'\x00' * zero_padding_size  # 最後の180バイト分を0で埋める
    else:
        # ファイルが存在しない場合は全て0で埋める
        slot_data = b'\x00' * block_size
    
    # データブロックをコンテンツに追加
    content += slot_data

# 結果を'sdslot.dat'に書き込む
with open(output_file, 'wb') as f:
    f.write(content)

print(f"ファイル '{output_file}' が作成されました。")
