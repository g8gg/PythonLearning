import html2markdown
import html2text

text_maker = html2text.HTML2Text()

html = """
<table>
<thead>
<tr>
<th>#id</th>
<th>Type</th>
<th>Description</th>
<th>Java type</th>
<th>MinimumMaximum</th>
<th>Auto-conversion from/to</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>Boolean</td>
<td>Handles only the values <em>True</em> or <em>False</em></td>
<td><code>java.lang.Boolean</code> or <code>boolean</code></td>
<td>01</td>
<td>String</td>
</tr>
<tr>
<td>1</td>
<td>Integer</td>
<td>32-bit signed Integers</td>
<td><code>java.lang.Integer</code> or <code>int</code></td>
<td>-2,147,483,648+2,147,483,647</td>
<td>Any Number, String</td>
</tr>
<tr>
<td>2</td>
<td>Short</td>
<td>Small 16-bit signed integers</td>
<td><code>java.lang.Short</code> or <code>short</code></td>
<td>-32,76832,767</td>
<td>Any Number, String</td>
</tr>
<tr>
<td>3</td>
<td>Long</td>
<td>Big 64-bit signed integers</td>
<td><code>java.lang.Long</code> or <code>long</code></td>
<td>-2<sup>63</sup>+2<sup>63</sup>-1</td>
<td>Any Number, String</td>
</tr>
<tr>
<td>4</td>
<td>Float</td>
<td>Decimal numbers</td>
<td><code>java.lang.Float</code> or <code>float</code></td>
<td>2<sup>-149</sup>(2-2<sup>-23</sup>)*2<sup>127</sup></td>
<td>Any Number, String</td>
</tr>
<tr>
<td>5</td>
<td>Double</td>
<td>Decimal numbers with high precision</td>
<td><code>java.lang.Double</code> or <code>double</code></td>
<td>2<sup>-1074</sup>(2-2<sup>-52</sup>)*2<sup>1023</sup></td>
<td>Any Number, String</td>
</tr>
<tr>
<td>6</td>
<td>Datetime</td>
<td>Any date with the precision up to milliseconds. To know more about it, look at <a href="Managing-Dates.html">Managing Dates</a></td>
<td><code>java.util.Date</code></td>
<td>-1002020303</td>
<td>Date, Long, String</td>
</tr>
<tr>
<td>7</td>
<td>String</td>
<td>Any string as alphanumeric sequence of chars</td>
<td><code>java.lang.String</code></td>
<td>--</td>
<td>-</td>
</tr>
<tr>
<td>8</td>
<td>Binary</td>
<td>Can contain any value as byte array</td>
<td><code>byte[]</code></td>
<td>02,147,483,647</td>
<td>String</td>
</tr>
<tr>
<td>9</td>
<td>Embedded</td>
<td>The Record is contained inside the owner. The contained Record has no <a href="Concepts.html#recordid">RecordId</a></td>
<td><code>ORecord</code></td>
<td>--</td>
<td>ORecord</td>
</tr>
<tr>
<td>10</td>
<td>Embedded list</td>
<td>The Records are contained inside the owner. The contained records have no <a href="Concepts.html#recordid">RecordIds</a> and are reachable only by navigating the owner record</td>
<td><code>List&lt;Object&gt;</code></td>
<td>041,000,000 items</td>
<td>String</td>
</tr>
<tr>
<td>11</td>
<td>Embedded set</td>
<td>The Records are contained inside the owner. The contained Records have no <a href="Concepts.html#recordid">RecordId</a> and are reachable only by navigating the owner record</td>
<td><code>Set&lt;Object&gt;</code></td>
<td>041,000,000 items</td>
<td>String</td>
</tr>
<tr>
<td>12</td>
<td>Embedded map</td>
<td>The Records are contained inside the owner as values of the entries, while the keys can only be Strings. The contained ords e no <a href="Concepts.html#recordid">RecordId</a>s and are reachable only by navigating the owner Record</td>
<td><code>Map&lt;String, ORecord&gt;</code></td>
<td>041,000,000 items</td>
<td><code>Collection&lt;? extends ORecord&lt;?&gt;&gt;</code>, <code>String</code></td>
</tr>
<tr>
<td>13</td>
<td>Link</td>
<td>Link to another Record. It's a common <a href="Concepts.html#1-1-and-n-1-referenced-relationships">one-to-one relationship</a></td>
<td><code>ORID</code>, <code>&lt;? extends ORecord&gt;</code></td>
<td>1:-132767:2^63-1</td>
<td>String</td>
</tr>
<tr>
<td>14</td>
<td>Link list</td>
<td>Links to other Records. It's a common <a href="Concepts.html#1-n-and-n-m-embedded-relationships">one-to-many relationship</a> where only the <a href="Concepts.html#recordid">RecordId</a>s are stored</td>
<td><code>List&lt;? extends ORecord</code></td>
<td>041,000,000 items</td>
<td>String</td>
</tr>
<tr>
<td>15</td>
<td>Link set</td>
<td>Links to other Records. It's a common <a href="Concepts.html#1-n-and-n-m-embedded-relationships">one-to-many relationship</a></td>
<td><code>Set&lt;? extends ORecord&gt;</code></td>
<td>041,000,000 items</td>
<td><code>Collection&lt;? extends ORecord&gt;</code>, <code>String</code></td>
</tr>
<tr>
<td>16</td>
<td>Link map</td>
<td>Links to other Records as value of the entries, while keys can only be Strings. It's a common <a href="Concepts.html#1-n-and-n-m-embedded-relationships">One-to-Many Relationship</a>. Only the <a href="Concepts.html#recordid">RecordId</a>s are stored</td>
<td><code>Map&lt;String,&nbsp;&nbsp;&nbsp;&nbsp;? extends Record&gt;</code></td>
<td>041,000,000 items</td>
<td>String</td>
</tr>
<tr>
<td>17</td>
<td>Byte</td>
<td>Single byte. Useful to store small 8-bit signed integers</td>
<td><code>java.lang.Byte</code> or <code>byte</code></td>
<td>-128+127</td>
<td>Any Number, String</td>
</tr>
<tr>
<td>18</td>
<td>Transient</td>
<td>Any value not stored on database</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>Date</td>
<td>Any date as year, month and day. To know more about it, look at <a href="Managing-Dates.html">Managing Dates</a></td>
<td><code>java.util.Date</code></td>
<td>-<bonetomanyr>-</bonetomanyr></td>
<td>Date, Long, String</td>
</tr>
<tr>
<td>20</td>
<td>Custom</td>
<td>used to store a custom type providing the marshall and unmarshall methods</td>
<td><code>OSerializableStream</code></td>
<td>0X</td>
<td>-</td>
</tr>
<tr>
<td>21</td>
<td>Decimal</td>
<td>Decimal numbers without rounding</td>
<td><code>java.math.BigDecimal</code></td>
<td>??</td>
<td>Any Number, String</td>
</tr>
<tr>
<td>22</td>
<td>LinkBag</td>
<td>List of <a href="Concepts.html#recordid">RecordId</a>s as spec <a href="RidBag.html">RidBag</a></td>
<td><code>ORidBag</code></td>
<td>??</td>
<td>-</td>
</tr>
<tr>
<td>23</td>
<td>Any</td>
<td>Not determinated type, used to specify Collections of mixed type, and null</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>
"""
text = text_maker.handle(html)
print(text)
