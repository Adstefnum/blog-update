import os

with open('header.txt','r') as header,open('foot.txt','r') as footer:

	body = open('post.txt','r').read()
	
	num_list = []

	for r,d,files in os.walk('./posts'):
		for file in files:
			if file.endswith('.html'):
				num_list.append(file.split(".")[0])

	
	if num_list:
		last_num = max(num_list)
		num = int(last_num) +1

	else:
		num = 1

	name = str(num)+'.html'

	post = "\n<section>"+ body + "</section>\n"+"<a href=" +str(num-1)+".html"+ ">Previous</a> &nbsp&nbsp&nbsp&nbsp&nbsp <a href=" +str(num+1)+".html"+ ">Next</a>\n"
	post_page = header.read()+ post + footer.read()

	os.chdir('./posts')
	write_out = open(name,'w')
	write_out.write(post_page)
	write_out.close()