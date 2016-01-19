# encoding = utf-8

class HtmlOuter(object):
	def __init__(self):
		self.datas = []
	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output(self):
		fwriter = open('gansu.html', 'w')
		fwriter.write("<html>")
		fwriter.write("<body>")
		fwriter.write("<table>")
		for data in self.datas:
			fwriter.write("<tr>")
			fwriter.write("<td>%s</td>" % data['url'].encode("utf-8"))
			fwriter.write("<td>%s</td>" % data['title'].encode("utf-8"))
			fwriter.write("<td>%s</td>" % data['summary'].encode("utf-8"))
			fwriter.write("</tr>")
		fwriter.write("</table>")
		fwriter.write("</body>")
		fwriter.write("</html>")
