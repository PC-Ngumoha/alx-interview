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

U+00E5 = 0 0 E 5 = 0 0 14 5 

```
229 => 1110 0101 
80 => 0101 0000
121 => 0111 1001
116 => 0111 0100
104 => 0110 1000
111 => 0110 1111
110 => 0110 1110
32 =>  0010 0000
105 => 0110 1001
115 => 0111 0011
99  => 0110 0011
108 => 0110 1100
33 =>  0010 0001
65 =>  0100 0001
127 => 0111 1111
256 => 1000 0000 0

[65] => [0100 0001]

[80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33] =>

[0101 0000, 0111 1001, 0111 0100, 0110 1000, 0110 1111, 0110 1110, 0010 0000, 0110 1001, 0111 0011, 0010 0000, 0110 0011, 0110 1111, 0110 1111, 0110 1100, 0010 0001]
```

I observed that in all cases the dataset that seemed to pass was the one which incorporated numbers whose binary pattern seemed to be eight characters in length and in which the _Most Significant Bit_ or _M.S.B_ was always zero in compliance with the unicode specification for single-byte characters as demonstrated in the table above. So, with that in mind, I've come to the conclusion that UTF-8 validator will have to check the binary bit patterns of the characters it wants to validate to decipher the following:

- That the length of the bit pattern is not greater than eight **i.e** _len(bin(char)) <= 8_
- That the first bit or _M.S.B_ has a bit value set to zero **i.e** _bin(char).toString()[0] == '0'_


**Pseudocode:**

```
function valid_utf(data):
	for elem in data:
		elem = BINARY(elem).toString().padWithZeroToEightPlaces()
		if elem.length() > 8 || elem[0] != '0' :
			return FALSE
	return TRUE
```


