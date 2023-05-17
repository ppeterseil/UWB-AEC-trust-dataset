import struct
import base64
def extract_cir(cir_str):
    if type(cir_str) == str:
        return struct.unpack("=50H", base64.b64decode(cir_str))
    if type(cir_str) == list:
        return list(map(extract_cir, cir_str))
    
if __name__ == "__main__":
    cir1 = "FgAaAEEAJwA2AFAASABKACoAsAAABCwKaQzsBacDTwjGCO4IHweOAfEFAwSPBfEEJQMOAqcCXANrAo0CtAOTAysBLwH1AJoAYgE7AWgBMANfBJcDawMsA8IBbgDtAD4B/AFfAg=="
    cir2 = "RwAcAFAAPwA+AG8AUgBhABkATwBrAvUHQwwQCNgBFghYCBUIqAd1AlQFZgWNBH0GhQPiAg8DKwN4ArwBfwPRA2kBJgGOAYoAwwHyAW0BewIOBOoDSgNeA2MCuAAcAfQAzgFoAg=="
    
    print(extract_cir(cir1))
    print(extract_cir(cir2))
    
    cir = [cir1, cir2]
    print(extract_cir(cir))