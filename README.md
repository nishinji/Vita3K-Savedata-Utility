# Vita3K Savedata Utility

Vita3K用のセーブデータユーティリティ。実機とのセーブデータ形式の変換を行います。

# 要件

Python (古すぎない)

# 使い方
split_file.pyは同じディレクトリにあるVitaからインポートしたsdslot.datファイルを分割しVita3Kで用いられるSlotParam形式に分割します。
出力先はoutputディレクトリになります。

> [!NOTE]
> VItaのセーブデータは暗号化されているため、このツールを使うにはVitaShellやSavemgrなどで暗号化を解除する必要があります。

merge_file.pyはSlotParam形式のファイルを結合し、Vitaで用いられるsdslot.dat形式に変換します。
入力元はinputディレクトリになります。
