# bodhi_sdk/spu/dashboard.py

import numpy as np

def display_spu_state(vspu: 'VirtualSPU', title: str, operation: str = ""):
    """Renders a text-based dashboard of the V-SPU's state."""
    np.set_printoptions(precision=2, suppress=True)
    
    border = "=" * 60
    print(f"\n{border}")
    print(f"| V-SPU DASHBOARD | {title:<35} |")
    if operation:
        print(f"| Operation: {operation:<43} |")
    print(f"{border}")
    
    print("\n[SVR - Spinor Vector Register (Input)]:")
    print(f"  {vspu.SVR}")
    
    print("\n[TMA - Transformation Matrix Array (Kernel)]:")
    for i, row in enumerate(vspu.TMA):
        print(f"  {row}")
        
    print("\n[Output Register (Result)]:")
    if vspu.OutputRegister.ndim == 1:
        print(f"  {vspu.OutputRegister}")
    else:
        for i, row in enumerate(vspu.OutputRegister):
            print(f"  {row}")
            
    print(border)