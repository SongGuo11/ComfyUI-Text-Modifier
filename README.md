# ComfyUI 文本修改器节点 (SG11)

这是一个 ComfyUI 自定义节点，用于修改文本内容。你可以替换或删除特定文本，并支持区分大小写选项。

## 功能特点

- 替换文本内容
- 删除特定文本
- 支持区分大小写选项
- 显示修改次数

## 安装方法

1. 解压缩 ComfyUI-Text-Modifier 
2. 进入你的 ComfyUI 的 custom_nodes 文件夹
3. 将ComfyUI-Text-Modifier复制到该文件夹中
4. 重启 ComfyUI

## 使用方法

1. 在节点搜索中找到 "Text Modifier (SG11)" 节点
2. 输入参数说明：
   - text: 要修改的原始文本
   - find_text: 要查找的文本
   - replace_text: 要替换成的新文本（替换操作时使用）
   - operation: 选择 "replace"（替换）或 "delete"（删除）
   - case_sensitive: 是否区分大小写

## 输出说明

- text: 修改后的文本内容
- count: 修改的次数

## 使用示例

如果你想把 "Long hair" 替换成 "Short hair"：
1. 在 text 中输入你的提示词文本
2. 在 find_text 中输入 "Long hair"
3. 在 replace_text 中输入 "Short hair"
4. operation 选择 "replace"
5. 根据需要设置 case_sensitive

## 联系微信：NFTNiuTouRen666

## 许可证

MIT 许可证
