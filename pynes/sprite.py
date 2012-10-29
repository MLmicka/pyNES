# -*- coding: utf-8 -*-

palette = [
    0x788084, 0x0000fc, 0x0000c4, 0x4028c4,
    0x94008c, 0xac0028, 0xac1000, 0x8c1800,
    0x503000, 0x007800, 0x006800, 0x005800,
    0x004058, 0x000000, 0x000000, 0x000008,

    0xbcc0c4, 0x0078fc, 0x0088fc, 0x6848fc,
    0xdc00d4, 0xe40060, 0xfc3800, 0xe46918,
    0xac8000, 0x00b800, 0x00a800, 0x00a848,
    0x008894, 0x2c2c2c, 0x000000, 0x000000,

    0xfcf8fc, 0x38c0fc, 0x6888fc, 0x9c78fc,
    0xfc78fc, 0xfc589c, 0xfc7858, 0xfca048,
    0xfcb800, 0xbcf818, 0x58d858, 0x58f89c,
    0x00e8e4, 0x606060, 0x000000, 0x000000,

    0xfcf8fc, 0xa4e8fc, 0xbcb8fc, 0xdcb8fc,
    0xfcb8fc, 0xf4c0e0, 0xf4d0b4, 0xfce0b4,
    0xfcd884, 0xdcf878, 0xb8f878, 0xb0f0d8,
    0x00f8fc, 0xc8c0c0, 0x000000, 0x000000
]

def load_sprites(src):
    f = open(src, 'rb')
    content = f.read()
    bin = []
    for c in content:
        bin.append(ord(c))
    return bin

def decode_sprite(channelA, channelB):
    s = []
    y = 0
    for y in range(0,8):
        a = channelA[y]
        b = channelB[y]
        line = []
        for x in range(0,8):
            bit = pow(2,7-x)
            pixel = -1
            if (not (a & bit) and not (b & bit)):
                pixel = 0
            elif ((a & bit) and not (b & bit)):
                pixel = 1
            elif (not (a & bit) and (b & bit)):
                pixel = 2
            elif ((a & bit) and (b & bit)):
                pixel = 3
            line.append(pixel);
        s.append(line)
    return s;

def get_sprite(index, sprites):
    iA = index * 16;
    iB = iA + 8;
    iC = iB + 8;
    channelA = sprites[iA:iB]
    channelB = sprites[iB:iC]
    return decode_sprite(channelA, channelB)

def encode_sprite(sprite):
    pass