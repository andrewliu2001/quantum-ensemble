# quantum-ensemble

Quantum simulation/computation project based on https://arxiv.org/abs/2007.01028



Group members: Erinn, Andrew

**Summary of Quantum Ensemble Paper:**

General approach: Use 3 quantum registers: Data (encodes training set), control (d-qubits), test (encodes test set).

1. State preparation
    1. Use Hadamard gates to transform every qubit in control register to uniform superposition of |0> and |1>. 
    2. Encode training set (x,y) into data register using some mapping S(x,y)|0> = |x,y>. 
2. Sampling in superposition
    1. Entangles the data path with each of the d control qubits (uniform superpositions of |0> and |1>), generating 2^d different feature transformations to the data path (mathematically, you get 2^d different terms in superposition after this stage). These 2^d different transformations correspond to applying 2^d different base models.
3. Learning via interference
    1. Use a classifier F (e.g. cosine classifier, which measures similarities). F takes in the training data path, feature transformation S(x_test, 0) of test dataset, and a |0> qubit to write the prediction to.
4. Measurement
    1. Measuring the output of F gives either |0> or |1> (in the case of binary classification), with probability determined by relative amplitudes.

**Division of tasks + Tentative timeline:**

1. Understand theory of approach (Read section **Quantum Algorithm for Classification Ensemble**). (complete by April 2)
2. Understand where complexity advantage arises from (Read subsection 3.3 Computational Complexity + potentially consult other papers). 
3. Qiskit implementation part: (complete by April 9)
    1. Quantum cosine classifier module 
    2. State preparation circuit 
    3. Sampling in superposition circuit
    4. Learning via interference circuit
    5. Measurement circuit
    6. Implementation on actual quantum computer?
    7. Classical cosine ensemble classifier
    8. Compilation of results (comparing performance, creating graphs)
4. Project report (complete by April 16)
    1. Introduction and significance of ensemble methods, quantum ensembles.
    2. Methodology
    3. Results and discussion
    4. Conclusion
    5. Further research
    6. Acknowledgements
5. Project PPT (just summarize report) (complete by April 23)

Other specifications:

1. What dataset to use? 

External deadlines:

1. Presentation (5/3)
2. Report (5/8)
