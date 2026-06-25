def char_count_frame(data):
    length = len(data)
    return str(length)+"|"+data

def char_count_deframe(frame):
    length, data = frame.split("|")
    return data

frame = char_count_frame("Aditya")
print(frame)
deframe = char_count_deframe(frame)
print(deframe)

flag = '#'
esc = '\\'

def char_stuffing_frame(data):
    stuffed = ""
    for ch in data:
        if ch == flag or ch == esc:
            stuffed += esc
        stuffed += ch
    return flag + stuffed + flag

ans = char_stuffing_frame("A#dit\\a")
print(ans)

def char_stuffing_deframe(frame):
    data = ans[1:-1]
    res = ""
    i = 0
    while i < len(data):
        if data[i] == esc:
            i+=1
        res += data[i]
        i+=1
    return res

ans2 = char_stuffing_deframe(ans)
print(ans2)

def bit_stuffing_frame(data):
    cnt = 0
    stuffed = ""
    for bit in data:
        if bit == '1':
            cnt += 1
            stuffed += bit
            if cnt == 5:
                stuffed += '0'
                cnt = 0
        else:
            stuffed += bit
            cnt = 0
    return "01111110" + stuffed + "01111110"

def bit_stuffing_deframe(frame):
    data = frame[8:-8]
    cnt = 0
    res = ""
    i = 0
    while i < len(data):
        if data[i] == '1':
            cnt += 1
            res += data[i]
            if cnt == 5:
                i += 1
                cnt = 0
        else:
            res += data[i]
            cnt = 0
        i += 1
    return res

bitframe = bit_stuffing_frame("111111011111101")
print(bitframe)
print(bit_stuffing_deframe(bitframe))

        