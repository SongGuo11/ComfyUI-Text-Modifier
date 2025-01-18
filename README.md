# ComfyUI Text Modifier Node (SG11)

A ComfyUI custom node for modifying text content. You can replace or delete specific text with case-sensitive options.

## Features

- Replace text with new content
- Delete specific text
- Case-sensitive/insensitive options
- Shows modification count

## Installation

1. Navigate to your ComfyUI's custom_nodes folder
2. Create a new folder named `SG11_nodes`
3. Copy the files into the folder
4. Restart ComfyUI

## Usage

1. Find the node under "SG11/text" category named "Text Modifier (SG11)"
2. Input parameters:
   - text: The original text to modify
   - find_text: The text you want to find
   - replace_text: The new text to replace with (for replace operation)
   - operation: Choose between "replace" or "delete"
   - case_sensitive: Whether to match case exactly

## Outputs

- text: Modified text content
- count: Number of modifications made

## Example

If you want to replace "Long hair" with "Short hair":
1. Set text to your prompt text
2. Set find_text to "Long hair"
3. Set replace_text to "Short hair"
4. Choose "replace" operation
5. Set case_sensitive as needed

## License

MIT License
