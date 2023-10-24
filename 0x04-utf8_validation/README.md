# UTF-8 Validation (Mock Interview)

### Objective:
The objective of this mock interview question is to challenge you to write a method that determines if a given data set represents a valid UTF-8 encoding.

### What is UTF-8?
_UTF-8_ or _Unicode Transformation Format-8bits_ is an encoding system which is widely used on the web and other modern multimedia to encode characters. It is a system of encoding which uses anywhere from 1 to 4 bytes to encode all characters in existence. Below is a table that illustrates UTF-8:

**Code Point -> UTF-8 conversion:**
<table>
  <thead>
    <tr>
      <th>First code point</th>
      <th>Last code point</th>
      <th>Byte 1</th>
      <th>Byte 2</th>
      <th>Byte 3</th>
      <th>Byte 4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>U+0000</td>
      <td>U+007F</td>
      <td>0xxxxxxx</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>U+0080</td>
      <td>U+07FF</td>
      <td>110xxxxx</td>
      <td>10xxxxxx</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>U+0800</td>
      <td>U+FFFF</td>
      <td>1110xxxx</td>
      <td>10xxxxxx</td>
      <td>10xxxxxx</td>
      <td></td>
    </tr>
    <tr>
      <td>U+10000</td>
      <td>U+10FFFF</td>
      <td>11110xxx</td>
      <td>10xxxxxx</td>
      <td>10xxxxxx</td>
      <td>10xxxxxx</td>
    </tr>
  </tbody>
</table>

### My Thought Process