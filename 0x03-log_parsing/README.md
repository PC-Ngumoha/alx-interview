# Log Parsing (Mock Interview)

### My Thinking:

EXAMPLE:
```
127.0.0.1 - [2023-10-19 19:36:27.125550] "GET /projects/260 HTTP/1.1" 200 777
```

```

PSEUDOCODE:

NOTE:
	- PATTERN1 -> Regex pattern to match the entire line.
	- PATTERN2 -> Regex pattern to extract the status code and file size from the line.

main:
  count = 0
  total_size = 0
  s_codes = {}
  try:
    LOOP FOREVER:
		  line = stdin.readline()
			if line == EOF:
				print('File Size: {total_size}')
				for s_code in s_codes:
					print('{s_code}: {s_codes[s_code]}')	

	    if count % 10 == 0 and count != 0:
		    print('File Size: {total_size}')
		    for s_code in s_codes:
		    	print('{s_code}: {s_codes[s_code]}')	
	
	    line_match = MATCH(PATTERN1, line)
	    if line_match is false:
		    continue  # Read the next line in stdin
	    else:
		    s_code, file_size = MATCH(PATTERN2, line)
		    total_size += int(file_size)
		    if s_code in s_codes:
			    s_codes[s_code] += 1
		    else:
			    s_codes[s_code] = 1
	    count += 1
  except KeyboardInterrupt:
     print('File Size: {total_size}')
		    for s_code in s_codes:
		    	print('{s_code}: {s_codes[s_code]}')
      
	

```