import qiskit
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.art3d as art3d
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.visualization import plot_bloch_multivector

def superposition_sampler(x_train, y_train, x_test, d):

  """
  x_train: array of training features
  y_train: array of binary training labels
  x_test: array of test features
  d: number of control qubits. Generates 2^d transformations to training data
  """
  N = x_train.shape[0]

  control_reg = QuantumRegister(d, 'control')
  x_train_reg = QuantumRegister(N, 'x_train')
  y_train_reg = QuantumRegister(N, 'y_train')
  x_test_reg = QuantumRegister(1, 'x_test')
  prediction_reg = QuantumRegister(1, 'prediction')

  sampler = QuantumCircuit(control_reg, x_train_reg, y_train_reg, x_test_reg, prediction_reg)

  for i in range(d):
    if(i % 2 == 0):
      sampler.cswap(i, i+2, i+4)
      sampler.cswap(i, i+2+N, i+4+N)
      sampler.x(i)
      sampler.cswap(i, i+3, i+5)
      sampler.cswap(i, i+3+N, i+5+N)
      sampler.barrier()
    else:
      sampler.x(i)
      sampler.cswap(i, i+3, i+4)
      sampler.cswap(i, i+7, i+8)
      sampler.barrier()

  return sampler