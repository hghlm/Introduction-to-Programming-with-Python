info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'

split_info = info.split(':')

join_info = '+'.join(split_info)

print(join_info)
    