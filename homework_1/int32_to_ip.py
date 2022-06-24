def int32_to_ip(int32):
    ip_adress = []
    for _ in range(4):
        ip_adress.append(str(int32 % 256))
        int32 //= 256
    return ".".join(ip_adress[::-1])


if __name__ == "__main__":
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"
