def music_styles(my_styles):
    print(my_styles)
    unique_styles = set()
    count = 0
    for style in my_styles:
        if style not in unique_styles:
            unique_styles.add(style)
            count += 1
    print(count)


my_music_styles = []
while True:
    my_style = input("Please input a music style: ")
    print(my_style)
    my_music_styles.append(my_style)
    if input("If you would like to enter another style, enter Y; else, enter N: ") == 'N':
        break
music_styles(my_music_styles)
