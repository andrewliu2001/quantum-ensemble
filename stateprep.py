def stateprep(x_train, y_train, x_test, d):

  """
  State preparation circuit
  
  x_train: array of training features
  y_train: array of binary training labels
  x_test: array of test features
  d: number of control qubits. Generates 2^d transformations to training data
  """

  N = x_train.shape[0]

  stateprep = QuantumCircuit(d+ 2*N + 2)

  #create uniform superposition of control qubits
  for i in range(d):
    stateprep.h(i)


  #initialize training data
  for i in range(x_train.shape[0]):
    stateprep.initialize(x_train[i]/np.linalg.norm(x_train[i]), i+d)

  for i in range(y_train.shape[0]):
    if y_train[i] == 1:
      stateprep.initialize([0, 1], i+d+x_train.shape[0])
    else:
      stateprep.initialize([1, 0], i+d+x_train.shape[0])

  #initialize test data
  stateprep.initialize(x_test/np.linalg.norm(x_test), d+2*N)


  stateprep.barrier()

  return stateprep