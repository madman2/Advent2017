"""Day 01: Inverse Captcha"""

def main():
    """Return the pathname of the KOS root directory."""
    with open('day01.txt', 'r') as captcha_file:
        captcha = captcha_file.readline()
        captcha = captcha.strip()
        first_star(captcha)
        second_star(captcha)

def compute_captcha(captcha, dist):
    """Computes the sum of numbers in a sequence that are equivalent
    to the number 'dist' ahead of it (wraps around)"""
    captcha_length = len(captcha)
    result = 0
    for i in range(0, captcha_length):
        num1 = int(captcha[i])
        num2 = int(captcha[(i + dist) % captcha_length])
        if num1 == num2:
            result += num1
    return result

def first_star(captcha):
    """Prints the solution for the first star"""
    captcha_value = compute_captcha(captcha, 1)
    print("Part #1: {}".format(captcha_value))

def second_star(captcha):
    """Prints the solution for the second star"""
    captcha_value = compute_captcha(captcha, int(len(captcha) / 2))
    print("Part #2: {}".format(captcha_value))

if __name__ == "__main__":
    main()
