# Extract-data-from-xml
A Python script that fetches XML data from a remote URL, parses it, and calculates the sum of all <count> values found in the file.

**What It Does**

Takes a URL as input from the user
Fetches the XML file from that URL over the internet
Parses the XML and finds all <comment> tags
Extracts the <count> value from each comment
Prints the total sum of all count values


**Technologies Used**

xml.etree.ElementTree — to parse XML data
urllib.request — to fetch data from a URL
ssl — to handle HTTPS connections


**How to Run**

When prompted, enter the URL:
Enter url here: https://py4e-data.dr-chuck.net/comments_2203406.xml

**Example XML Structure**

xml<comments>
  <comment>
    <name>Romina</name>
    <count>97</count>
  </comment>
  <comment>
    <name>Laurie</name>
    <count>45</count>
  </comment>
</comments>
