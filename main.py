def app(event):
    with open("/tmp/test.html", "wb") as tst:
        tst.write(b"test")
    return "Hello, world!333"
