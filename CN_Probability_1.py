import random
import CN_Function
import time

def generate_random_input():
    input_bits = ""
    for _ in range(8):
        bit = random.choice(["0", "1"])
        input_bits += bit
    return input_bits

def introduce_errors(codeword, error_rate):
    num_errors = int(len(codeword) * error_rate)
    error_indices = random.sample(range(len(codeword)), num_errors)
    flipped_codeword = list(codeword)
    
    for index in error_indices:
        flipped_codeword[index] = '0' if codeword[index] == '1' else '1'
    
    return ''.join(flipped_codeword)

dataword=generate_random_input()
start_time = time.perf_counter()
k=10

# Single Error Correction
s=0
error_rate=0.05
codeword=CN_Function.codgen(dataword)
codeerror=introduce_errors(codeword,error_rate)
correct_code=CN_Function.codecor(codeerror)
dwtemp=str(correct_code[0])+str(correct_code[1])+str(correct_code[3])+str(correct_code[4])+str(correct_code[9])+str(correct_code[10])+str(correct_code[12])+str(correct_code[13])
if dataword==dwtemp:
    s=s+1
prob=s/k
#print("Single error correction probability:",prob*100)
end_time = time.perf_counter()
running_time = end_time - start_time
print(f"Single error correction running time: {running_time} seconds")

# Double Error Correction
start_time = time.perf_counter()
s=0
error_rate=0.1
codeword=CN_Function.codgen(dataword)
codeerror=introduce_errors(codeword,error_rate)
correct_code=CN_Function.codecor(codeerror)
dwtemp=str(correct_code[0])+str(correct_code[1])+str(correct_code[3])+str(correct_code[4])+str(correct_code[9])+str(correct_code[10])+str(correct_code[12])+str(correct_code[13])
if dataword==dwtemp:
    s=s+1
prob=s/k
#print("Double error correction probability:",prob*100)
end_time = time.perf_counter()
running_time = end_time - start_time
print(f"Double error correction running time: {running_time} seconds")

# Triple Error Correction
start_time = time.perf_counter()
s=0
error_rate=0.15
codeword=CN_Function.codgen(dataword)
codeerror=introduce_errors(codeword,error_rate)
correct_code=CN_Function.codecor(codeerror)
dwtemp=str(correct_code[0])+str(correct_code[1])+str(correct_code[3])+str(correct_code[4])+str(correct_code[9])+str(correct_code[10])+str(correct_code[12])+str(correct_code[13])
if dataword==dwtemp:
    s=s+1
prob=s/k
#print("Triple error correction probability:",prob*100)
end_time = time.perf_counter()
running_time = end_time - start_time
print(f"Triple error correction running time: {running_time} seconds")

# Quatruple Error Correction
start_time = time.perf_counter()
s=0
error_rate=0.20
codeword=CN_Function.codgen(dataword)
codeerror=introduce_errors(codeword,error_rate)
correct_code=CN_Function.codecor(codeerror)
dwtemp=str(correct_code[0])+str(correct_code[1])+str(correct_code[3])+str(correct_code[4])+str(correct_code[9])+str(correct_code[10])+str(correct_code[12])+str(correct_code[13])
if dataword==dwtemp:
    s=s+1
prob=s/k
#print("Quatruple error correction probability:",prob*100)
end_time = time.perf_counter()
running_time = end_time - start_time
print(f"Quatruple error correction running time: {running_time} seconds")

# Penta Error Correction
start_time = time.perf_counter()
error_rate=0.25
codeword=CN_Function.codgen(dataword)
codeerror=introduce_errors(codeword,error_rate)
correct_code=CN_Function.codecor(codeerror)
dwtemp=str(correct_code[0])+str(correct_code[1])+str(correct_code[3])+str(correct_code[4])+str(correct_code[9])+str(correct_code[10])+str(correct_code[12])+str(correct_code[13])
if dataword==dwtemp:
    s=s+1
prob=s/25
#print("Penta error correction probability:",prob*100)
s=0
end_time = time.perf_counter()
running_time = end_time - start_time
print(f"Penta error correction running time: {running_time} seconds")
