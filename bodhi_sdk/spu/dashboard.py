# bodhi_sdk/spu/dashboard.py (Corrected)

import numpy as np

# The ONLY change is putting 'VirtualSPU' in quotes.
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
    # Handle both vector and matrix output gracefully
    output = vspu.OutputRegister
    if output.ndim == 1:
        print(f"  {output}")
    else:
        for i, row in enumerate(output):
            print(f"  {row}")
            
    print(border)