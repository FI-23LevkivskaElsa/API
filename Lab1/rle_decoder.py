import sys
import os

def rle_decode(encoded_bytes: bytes):
    decoded = bytearray()
    i = 0
    n = len(encoded_bytes)

    while i < n:
        control = encoded_bytes[i]
        i += 1
        if control >= 128:
            if i >= n:
                raise ValueError("Помилка: неочікуваний кінець файлу (повторюваний байт відсутній)")
            count = control - 128 + 2
            decoded.extend([encoded_bytes[i]] * count)
            i += 1
        else:
            count = control + 1
            if i + count > n:
                raise ValueError("Помилка: неочікуваний кінець файлу (відсутні унікальні байти)")
            decoded.extend(encoded_bytes[i:i+count])
            i += count

    return bytes(decoded)

def main():
    if len(sys.argv) < 2:
        print("Використання: python rle_decoder.py <вхідний_файл>")
        sys.exit(1)

    input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        if input_path.endswith('.rle'):
            output_path = input_path[:-4] + '_decoded.bin'
        else:
            output_path = input_path + '_decoded.bin'

    with open(input_path, 'rb') as f_in:
        encoded_data = f_in.read()

    try:
        decoded_data = rle_decode(encoded_data)
        with open(output_path, 'wb') as f_out:
            f_out.write(decoded_data)
        print(f"Файл розпаковано: {input_path} → {output_path}")
    except ValueError as e:
        print(f"Помилка при декодуванні: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()