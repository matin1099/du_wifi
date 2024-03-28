""" 
source:
https://thepythoncode.com/article/hide-secret-data-in-images-using-steganography-python
"""
import cv2
import numpy as np
import os
from tqdm import tqdm

def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes):
        return ''.join([ format(i, "08b") for i in data ])
    elif isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")
    
def encode(image_name, secret_data):
    """encoding Data in flie

    Args:
        image_name (PNG): License
        secret_data (str): id and password

    Raises:
        ValueError: Data is larger than license

    Returns:
        png: License
    """
    # read the image
    image = cv2.imread(image_name)
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    if len(secret_data) > n_bytes:
        raise ValueError(" Insufficient bytes, need bigger image or less data.")
    # add stopping criteria
    secret_data += "====="
    data_index = 0
    # convert data to binary
    binary_secret_data = to_bin(secret_data)
    # size of data to hide
    data_len = len(binary_secret_data)
    for row in tqdm(image ,desc="encoding..."):
        for pixel in row:
            # convert RGB values to binary format
            r, g, b = to_bin(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    return image

def decode(image_name):
    """decoding Image to extract 'secret'

    Args:
        image_name (PNG file): Creator license file.

    Returns:
        str: secret message.
    """
  
    # read the image
    image = cv2.imread(image_name)
    binary_data = ""
    for row in tqdm(image,desc="Decoding..."):
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    # split by 8-bits
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]


def add_Password():
    """Adding Password to key.    
    """
    secret_data=input("Enter ID:\t")+"`"+input("Enter Password:\t")
    
    input_image = "CreatorPlusLICENSE.png"
    output_image = "CreatorPlusLICENSE.png"
    # encode the data into the image
    encoded_image = encode( "CreatorPlusLICENSE.png",secret_data=secret_data)
    # save the output image (encoded image)
    cv2.imwrite(output_image, encoded_image)
    # decode the secret data from the image
    return print("Password added.")

def clear_Password():
    """clearing License from any password!
    !!!!USE WITH COTIONS!!!!
    """
    input_image = "CreatorPlusLICENSE.png"
    output_image = "CreatorPlusLICENSE.png"
    # encode the data into the image
    encoded_image = encode( "CreatorPlusLICENSE.png",secret_data="" )
    # save the output image (encoded image)
    cv2.imwrite(output_image, encoded_image)
    # decode the secret data from the image
    return print("Clear!")





def get_Password():
    """get stored data

    Returns:
        tuples: id and password
        
        Especial Cases:
        
        NO License: No license found. SO NO PASSWORD


        key is clear: No data being stored
            """
    if os.path.isfile("CreatorPlusLICENSE.png"):
        decoded = decode("CreatorPlusLICENSE.png")
    
        id=decoded[ : decoded.find("`")]
        pw=decoded[decoded.find("`")+1 : ] 

        if (id != '' or pw != '' ):
            return id,pw   
        else:
            print("No Data found! Key is Clear.")
    else:
        print(" Licnese Doesnt exist. CALL t.me/MATIN1099")





### to BE ADD     P.S sari ke dard nemikone ro dasmal nemibandand!

"""def remove_Password(pfid):


    # add a regex to get find pfid in old_data and remove password whole sec then reEncode
    # return password remove


    pass

def read_Password():
    # add a regex to get find all pfid in old_data and then password
    # return a;ll pfid

    pass"""