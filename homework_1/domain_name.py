import re


def domain_name(url):
    protocol_pattern = r"(?:https?://)?(?:w{3}\.)?"
    without_protocol = re.split(protocol_pattern, url)
    return "".join(without_protocol).split(".")[0]


if __name__ == "__main__":
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("xakep") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
