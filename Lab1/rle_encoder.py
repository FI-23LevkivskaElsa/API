import sys
import os

def rle_encode(input_bytes: bytes):
    encoded = bytearray()
    i = 0
    n = len(input_bytes)

    while i < n:
        repeat_len = 1
        while (i + repeat_len < n and input_bytes[i] == input_bytes[i + repeat_len] and repeat_len < 129):
            repeat_len += 1

        if repeat_len >= 2:
            encoded.append(128 + repeat_len - 2)
            encoded.append(input_bytes[i])
            i += repeat_len
        else:
            start = i
            i += 1
            while (i < n and (i + 1 >= n or input_bytes[i] != input_bytes[i + 1]) and (i - start) < 128):
                i += 1
            length = i - start
            encoded.append(length - 1)
            encoded.extend(input_bytes[start:start + length])

    return bytes(encoded)

def main():
    if len(sys.argv) < 2:
        print("Використання: python rle_encoder.py <вхідний_файл>")
        sys.exit(1)

    input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = os.path.splitext(input_path)[0] + '.rle'

    with open(input_path, 'rb') as f_in:
        input_data = f_in.read()

    compressed = rle_encode(input_data)

    with open(output_path, 'wb') as f_out:
        f_out.write(compressed)

    print(f"Файл стиснуто: {input_path} → {output_path}")

if __name__ == "__main__":
    main()
