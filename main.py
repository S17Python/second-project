# "from PiL import Image,ImageDraw,ImageFont"
# print("Генератор мемов запущен")
# top_text=input("Введите верхний текст мема:" )
# bottom_text=input("Введите нижний текст мема:" )
# print(top_text, bottom_text)
# print("Список картинок:")
# print("1.удивлённый кот")
# print("2.грустное лицо")
#
# image_number =int(input("Введите номер картинки:" ))
#
# if image_number==1:
#     image_file="кот.jpg"
# elif image_number==2:
#     image_file="грустное лицо.jpg"
# print(image_file)
#
# image=Image.open(image_file)
# width,height=image.size
# draw=ImageDraw.Draw(image)
#
# font=ImageFont.truetype("arial.ttf",size=70)
# text=draw.textbox(0,0,top_text,font)
# textwidth=text[2]
# draw.text(((width - textwidth) / 2, 10),top_text,font=font,fill="black")
#
# text=draw.textbox(0,0,bottom_text,font)
# textwidth=text[2]
# textheight=text[3]
# draw.text(((width-textwidth)/2,textheight-10),bottom_text,font=font,fill="black")
# image.save("new_meme.jpg")
