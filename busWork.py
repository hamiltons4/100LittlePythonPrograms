Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> 
============ RESTART: C:/Users/Owner/Desktop/PyStuff/idlesave.py ============
0
1
2
3
4
5
6
7
>>> import urllib
>>> u = urllib.urlopen('http://ctabustracker.com/bustime/map/getbusesforRoute.jsp?route=22')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getbusesforRoute.jsp?route=22')
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> urllib
<module 'urllib' from 'C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\urllib\\__init__.py'>
>>> urllib.urlopen
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    urllib.urlopen
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> urllib.urlopen()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    urllib.urlopen()
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
AttributeError: module 'urllib' has no attribute 'request'
>>> urllib.request
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    urllib.request
AttributeError: module 'urllib' has no attribute 'request'
>>> import requests
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
>>> import urllib.requests
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import urllib.requests
ModuleNotFoundError: No module named 'urllib.requests'
>>> urllib.request.urlopen()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    urllib.request.urlopen()
AttributeError: module 'urllib' has no attribute 'request'
>>> import urllib.request
>>> urllib.request.urlopen
<function urlopen at 0x02D3CD68>
>>> urlib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    urlib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
NameError: name 'urlib' is not defined
>>> urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
<http.client.HTTPResponse object at 0x02ED21F0>
>>> u =  urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
>>> data = u.read()
>>> f = open('rt22.xml', 'wb')
>>> f.write(data)
8638
>>> f.close()
>>> b = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
>>> data2 = b.read()
>>> f = open('rt222.xml','wb')
>>> f.write(data2)
8654
>>> f.close()
>>> data2
b'<?xml version="1.0"?>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\t<buses rt="22" rtRtpiFeedName="" rtdd="22"> <!-- @11 @16 -->\r\n\r\n\t\t<time>10:58 AM</time>\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1781</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>S</dn> \r\n\t\t\t<lat>41.9997755686442</lat>\r\n\t\t\t<lon>-87.67123413085938</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P206</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>36799</op>\r\n\t\t\t<dip>8423</dip>\r\n\t\t\t<bid>1052</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>206</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1895</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>N</dn> \r\n\t\t\t<lat>41.89442443847656</lat>\r\n\t\t\t<lon>-87.62964630126953</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P221</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>45133</op>\r\n\t\t\t<dip>9113</dip>\r\n\t\t\t<bid>965</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>221</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1388</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>N</dn> \r\n\t\t\t<lat>41.905750162461224</lat>\r\n\t\t\t<lon>-87.63144818474265</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P228</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>50198</op>\r\n\t\t\t<dip>13640</dip>\r\n\t\t\t<bid>860</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>228</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1921</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>S</dn> \r\n\t\t\t<lat>41.98182184188092</lat>\r\n\t\t\t<lon>-87.66845427966508</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P609</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>29697</op>\r\n\t\t\t<dip>14998</dip>\r\n\t\t\t<bid>902</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>609</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1886</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North West Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>NNW</dn> \r\n\t\t\t<lat>41.92032587528229</lat>\r\n\t\t\t<lon>-87.63752615451813</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P227</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>45355</op>\r\n\t\t\t<dip>19362</dip>\r\n\t\t\t<bid>862</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>227</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1786</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South East Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>SSE</dn> \r\n\t\t\t<lat>41.95436878204346</lat>\r\n\t\t\t<lon>-87.6622142791748</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P202</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>40848</op>\r\n\t\t\t<dip>25121</dip>\r\n\t\t\t<bid>850</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>202</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1904</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South East Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>SSE</dn> \r\n\t\t\t<lat>41.93049716949463</lat>\r\n\t\t\t<lon>-87.6438217163086</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P216</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>42849</op>\r\n\t\t\t<dip>35219</dip>\r\n\t\t\t<bid>901</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>216</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1915</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>NNW</dn> \r\n\t\t\t<lat>41.95998372787084</lat>\r\n\t\t\t<lon>-87.66531411195413</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P223</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>54256</op>\r\n\t\t\t<dip>36049</dip>\r\n\t\t\t<bid>1042</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>223</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1789</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>NNW</dn> \r\n\t\t\t<lat>41.961207894717944</lat>\r\n\t\t\t<lon>-87.66578337725471</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P224</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>54585</op>\r\n\t\t\t<dip>36516</dip>\r\n\t\t\t<bid>1041</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>224</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1860</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South East Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>SSE</dn> \r\n\t\t\t<lat>41.913292978324144</lat>\r\n\t\t\t<lon>-87.63289477778416</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P231</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>34147</op>\r\n\t\t\t<dip>42139</dip>\r\n\t\t\t<bid>962</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>231</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1846</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>S</dn> \r\n\t\t\t<lat>41.885474586486815</lat>\r\n\t\t\t<lon>-87.63102722167969</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P226</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>50040</op>\r\n\t\t\t<dip>52437</dip>\r\n\t\t\t<bid>963</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>226</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1713</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>South Bound</d>\r\n\t\t\t<dd>Southbound</dd> \r\n\t\t\t<dn>SSE</dn> \r\n\t\t\t<lat>41.883998453617096</lat>\r\n\t\t\t<lon>-87.6310703754425</lon>\r\n\t\t\t<pid>3936</pid>\r\n\t\t\t<pd>Southbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P219</run>\r\n\t\t\t<fs>Harrison</fs>\r\n\t\t\t<op>49780</op>\r\n\t\t\t<dip>53048</dip>\r\n\t\t\t<bid>964</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>219</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1762</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>N</dn> \r\n\t\t\t<lat>42.01186429950553</lat>\r\n\t\t\t<lon>-87.67445932307713</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P211</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>36747</op>\r\n\t\t\t<dip>55050</dip>\r\n\t\t\t<bid>904</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>211</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t\t<bus>\r\n\t\t\t<id>1919</id>    \r\n\t\t\t<consist></consist>    \r\n\t\t\t<cars></cars>    \r\n\t\t\t<rtpiFeedName></rtpiFeedName>\r\n\t\t\t<m>1</m>\t  \t\r\n\t\t\t<rt>22</rt>\r\n\t\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t\t<rtdd>22</rtdd>  \r\n\t\t\t\r\n\t\t\t<d>North Bound</d>\r\n\t\t\t<dd>Northbound</dd> \r\n\t\t\t<dn>N</dn> \r\n\t\t\t<lat>42.01831287448689</lat>\r\n\t\t\t<lon>-87.67296509823557</lon>\r\n\t\t\t<pid>3932</pid>\r\n\t\t\t<pd>Northbound</pd> \r\n\t\t\t<pdRtpiFeedName></pdRtpiFeedName>\r\n\t\t\t<run>P218</run>\r\n\t\t\t<fs>Howard</fs>\r\n\t\t\t<op>45491</op>\r\n\t\t\t<dip>57795</dip>\r\n\t\t\t<bid>842</bid>\t\t\t\t\r\n\t\t\t<wid1>0P</wid1>\r\n\t\t\t<wid2>218</wid2>            \t\r\n\t\t</bus>\r\n\r\n\r\n\r\n\t</buses>\r\n'
>>> f = open('rt222.xml','wb')
>>> f.write(data2)
8654
>>> f.close()
>>> f = open('rt222.xml', 'w')
>>> f.write(data2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f.write(data2)
TypeError: write() argument must be str, not bytes
>>> c = str(data2)
>>> f.write(c)
10725
>>> from xml.etree.ElementTree import parse
>>> doc parse('rt22.xml')
SyntaxError: invalid syntax
>>> doc = parse('rt22.xml')
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x02EE0BF0>
>>> 
