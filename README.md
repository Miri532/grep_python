# grep_python
an application that searches for a specific text through a list of files and URLs (Similar to Unix GREP)  
•	Input:  
o	A list that includes both files names, folders and web URLS.  For instance:  
	C:\test.txt  
  http://www.lipsum.com/  

o	A word to search for.  
o	A flag that indicates whether the search is case sensitive or case insensitive.  
o	A flag that indicates whether it’s a regular search (search for lines that include the word) or a reverse search (for lines that do not include the word)  
•	Output:  
o	For each file, folder or URL, The application shows all the lines that match (or do not match, depending on the setting) the word.  
o	Output format is <File full path or url>: <line text>    
•	UI:   
o	this a console application. the input received from command line. For example:  
grep –v –i hello file:file.txt,url:http://www.lipsum.com/  
-v stands for reverse search  
-i stands for case insensitive search.  
