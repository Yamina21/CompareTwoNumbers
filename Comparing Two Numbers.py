#!/usr/bin/env python
# coding: utf-8

# In[107]:


from qiskit import *
from qiskit.providers.aer import Aer
from qiskit.providers.aer.library import save_statevector
import numpy as np


# In[128]:


#This algorithm is valid for all kinds of integers, whether positive or negative,
#because it encodes the integers into binary strings and compares them 
#bit by bit using C-Not Gates. Therefore, the algorithm 
#works regardless of the sign of the integers, as long as they can be represented as binary strings of equal length.

#Also, in this Function, we apply a quantum circuit, If The measurement outcome is '1', 
#it means that the most significant bit 'MSB' of the larger number is a '1'.
#We can determine which of the two input numbers is larger by comparing their MSBs:
#if the MSB of number_1 is '1', then it must be larger than number_2 since the MSB of number_2 is '0'; 
#otherwise, number_2 is larger than number_1.


def find_the_largest_number(number_1, number_2):
    
    #Determine the length of the binary strings
    n = max(len(bin(number_1)), len(bin(number_2))) - 2  

    # Create the quantum circuit
    qr = QuantumRegister(2*n, 'q')
    cr = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(qr, cr)    

    # Apply the Hadamard gate to all qubits
    qc.h(qr)    

    # Apply the CNOT gates
    for i in range(n-1):
        for j in range(i+1):
            qc.cx(qr[n+i-j],qr[n+i+1-j])    

    # Measure the first qubit
    qc.measure(qr[0], cr)    


    # Execute the circuit on the simulator
    backend = Aer.get_backend('qasm_simulator') 
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
   
    
    # Determine which number is larger based on the measurement outcome of counts
    if '1' in counts: 

        if number_1 > number_2:
            return number_1
        else:
            return number_2
    else:
        if number_1 > number_2:
            return number_1 
        else:
            return number_2


# In[129]:


larger_number = find_the_largest_number(5, -6)
print(larger_number)

