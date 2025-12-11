import torch
import torch.nn as nn

class VAE(nn.Module):
  def __init__(self):
    pass

if __name__ == "__main__":
  print(torch.version.cuda)       # Shows which CUDA version PyTorch was built with
  print(torch.cuda.is_available()) # True if GPU is usable
  print(torch.cuda.device_count()) # Number of GPUs detected