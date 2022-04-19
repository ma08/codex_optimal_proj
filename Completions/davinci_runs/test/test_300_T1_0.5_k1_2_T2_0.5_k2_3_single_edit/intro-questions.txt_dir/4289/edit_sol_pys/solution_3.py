

# === import ======================================================================================================================================================
import sys

# === const =======================================================================================================================================================

# === functions ===================================================================================================================================================

class File:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __getitem__(self):
        pass

    def __setitem__(self):
        pass

    def __len__(self):
        pass

    def __contains__(self):
        pass

    def __eq__(self):
        pass

    def __lt__(self):
        pass

    def __le__(self):
        pass

    def __gt__(self):
        pass

    def __ge__(self):
        pass

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __truediv__(self):
        pass

    def __floordiv__(self):
        pass

    def __mod__(self):
        pass

    def __pow__(self):
        pass

    def __lshift__(self):
        pass

    def __rshift__(self):
        pass

    def __and__(self):
        pass

    def __or__(self):
        pass

    def __xor__(self):
        pass

    def __invert__(self):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __abs__(self):
        pass

    def __int__(self):
        pass

    def __float__(self):
        pass

    def __complex__(self):
        pass

    def __hex__(self):
        pass

    def __oct__(self):
        pass

    def __bin__(self):
        pass

    def __index__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __iadd__(self):
        pass

    def __isub__(self):
        pass

    def __imul__(self):
        pass

    def __itruediv__(self):
        pass

    def __ifloordiv__(self):
        pass

    def __imod__(self):
        pass

    def __ipow__(self):
        pass

    def __ilshift__(self):
        pass

    def __irshift__(self):
        pass

    def __iand__(self):
        pass

    def __ior__(self):
        pass

    def __ixor__(self):
        pass

    def __getattr__(self):
        pass

    def __setattr__(self):
        pass

    def __delattr__(self):
        pass

    def __getattribute__(self):
        pass

    def __get__(self):
        pass

    def __set__(self):
        pass

    def __delete__(self):
        pass

    def __init_subclass__(self):
        pass

    def __instancecheck__(self):
        pass

    def __subclasscheck__(self):
        pass

    def __call__(self):
        pass

    def __new__(self):
        pass

    def __prepare__(self):
        pass

    def __getnewargs_ex__(self):
        pass

    def __getnewargs__(self):
        pass

    def __reduce_ex__(self):
        pass

    def __reduce__(self):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self):
        pass

    def __sizeof__(self):
        pass

    def __dir__(self):
        pass

    def __reversed__(self):
        pass

    def __hash__(self):
        pass

    def __missing__(self):
        pass

    def __getinitargs__(self):
        pass

    def __getstate__(self):
        pass

    def __setstate__(self):
        pass

    def __getformat__(self):
        pass

    def __setformat__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __format__(self):
        pass

    def __bytes__(self):
        pass

    def __lt__(self):
        pass

    def __le__(self):
        pass

    def __eq__(self):
        pass

    def __ne__(self):
        pass

    def __gt__(self):
        pass

    def __ge__(self):
        pass

    def __bool__(self):
        pass

    def __getattribute__(self):
        pass

    def __getattr__(self):
        pass

    def __setattr__(self):
        pass

    def __delattr__(self):
        pass

    def __lt__(self):
        pass

    def __le__(self):
        pass

    def __eq__(self):
        pass

    def __ne__(self):
        pass

    def __gt__(self):
        pass

    def __ge__(self):
        pass

    def __init__(self):
        pass

    def __new__(self):
        pass

    def __del__(self):
        pass

    def __call__(self):
        pass

    def __len__(self):
        pass

    def __length_hint__(self):
        pass

    def __getitem__(self):
        pass

    def __missing__(self):
        pass

    def __setitem__(self):
        pass

    def __delitem__(self):
        pass

    def __iter__(self):
        pass

    def __reversed__(self):
        pass

    def __contains__(self):
        pass

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __matmul__(self):
        pass

    def __truediv__(self):
        pass

    def __floordiv__(self):
        pass

    def __mod__(self):
        pass

    def
# === classes =====================================================================================================================================================

# === main ========================================================================================================================================================
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    dif = [abs(t - h[i] * 0.006 - a) for i in range(n)]
    ans = dif.index(min(dif)) + 1
    print(ans)

# ==================================================================================
if __name__ == "__main__":
    main()
